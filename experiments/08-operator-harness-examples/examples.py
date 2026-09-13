#!/usr/bin/env python3
"""Terminal client for the three retained examples. No AWS resource writes."""
from __future__ import annotations
import argparse
import json
import os
import uuid

NAMES = {key: 'lab1_demo_' + key for key in ('explainer', 'reader', 'approval')}
PROMPTS = {
    'explainer': 'Pasted finding: a demo security group allows inbound TCP 22 from 0.0.0.0/0. Explain the risk, a proposed fix, and what to verify, in under 120 words. Do not make changes.',
    'reader': 'Read the current lab setting once. Show its observed value, version, expected value and compliance status. No changes.',
    'approval': 'Start approval practice for DEMO_ONLY. Request my decision and wait. Do not execute any AWS change.',
}
ERRORS = {'validationException', 'internalServerException', 'runtimeClientError',
          'accessDeniedException', 'throttlingException', 'serviceUnavailableException'}


def consume(events):
    """Collect bounded typed events; model text is never an approval signal."""
    active, uses, results, text, seen = {}, [], [], [], set()
    stop, count, chars, usage = None, 0, 0, {'inputTokens': 0, 'outputTokens': 0}
    for event in events:
        count += 1
        chars += len(json.dumps(event, default=str))
        if count > 10000 or chars > 1000000:
            raise ValueError('stream exceeds evidence limits')
        if ERRORS.intersection(event) or any(k.lower().endswith('exception') for k in event):
            raise ValueError('Harness returned an error event')
        if 'messageStart' in event:
            if active:
                raise ValueError('unfinished tool block')
            stop = None
        if 'contentBlockStart' in event:
            block = event['contentBlockStart']; idx = block['contentBlockIndex']
            start = block.get('start', {})
            for kind in ('toolUse', 'toolResult'):
                if kind in start:
                    if idx in active:
                        raise ValueError('duplicate active block')
                    active[idx] = {'kind': kind, 'data': dict(start[kind]), 'parts': []}
        if 'contentBlockDelta' in event:
            block = event['contentBlockDelta']; idx = block['contentBlockIndex']
            delta = block.get('delta', {})
            if 'text' in delta:
                text.append(delta['text'])
            if 'toolUse' in delta or 'toolResult' in delta:
                if idx not in active:
                    raise ValueError('tool delta without start')
                item = active[idx]
                if item['kind'] == 'toolUse':
                    item['parts'].append(delta.get('toolUse', {}).get('input', ''))
                else:
                    parts = delta.get('toolResult', [])
                    if not isinstance(parts, list):
                        raise ValueError('invalid tool result delta')
                    item['parts'].extend(parts)
        if 'contentBlockStop' in event:
            idx = event['contentBlockStop']['contentBlockIndex']
            item = active.pop(idx, None)
            if item:
                data = item['data']; tid = data.get('toolUseId')
                if not isinstance(tid, str) or not tid:
                    raise ValueError('missing toolUseId')
                if item['kind'] == 'toolUse':
                    if tid in seen:
                        raise ValueError('duplicate toolUseId')
                    seen.add(tid)
                    data['input'] = json.loads(''.join(item['parts']) or '{}')
                    if not isinstance(data['input'], dict):
                        raise ValueError('tool input must be an object')
                    uses.append(data)
                else:
                    data['content'] = item['parts']; results.append(data)
        if 'messageStop' in event:
            stop = event['messageStop'].get('stopReason')
        if 'metadata' in event:
            for key in usage:
                usage[key] += event['metadata'].get('usage', {}).get(key, 0)
    if active or stop is None:
        raise ValueError('incomplete Harness stream')
    return {'text': ''.join(text), 'stop_reason': stop, 'tools': uses,
            'results': results, 'usage': usage}


def pending_approval(turn):
    if turn['stop_reason'] != 'tool_use' or len(turn['tools']) != 1 or turn['results']:
        raise ValueError('expected exactly one pending client approval')
    tool = turn['tools'][0]
    if (tool.get('name') != 'request_approval' or tool.get('input') != {'action': 'DEMO_ONLY'}
            or not isinstance(tool.get('toolUseId'), str) or not tool['toolUseId']):
        raise ValueError('unexpected approval tool or scope')
    return tool


def resume_messages(tool, decision, simulated=False):
    if decision not in ('APPROVED', 'REJECTED'):
        raise ValueError('decision must be APPROVED or REJECTED')
    pending_approval({'stop_reason': 'tool_use', 'tools': [tool], 'results': []})
    result = {'decision': decision, 'simulation': True,
              'decision_source': 'automated-test-fixture' if simulated else 'terminal-operator',
              'action_executed': False}
    return [
        {'role': 'assistant', 'content': [{'toolUse': tool}]},
        {'role': 'user', 'content': [{'toolResult': {'toolUseId': tool['toolUseId'],
           'content': [{'text': json.dumps(result)}], 'status': 'success'}}]},
    ]


def discover(session, region):
    client = session.client('bedrock-agentcore-control', region_name=region)
    found, token, seen = {}, None, set()
    while True:
        value = client.list_harnesses(**({'nextToken': token} if token else {}))
        for item in value.get('harnesses', []):
            if item['harnessName'] in NAMES.values():
                if item['harnessName'] in found:
                    raise ValueError('ambiguous Harness name')
                details = client.get_harness(harnessId=item['harnessId'])
                details = details.get('harness', details)
                if details['status'] != 'READY':
                    raise ValueError('Harness not READY')
                found[item['harnessName']] = details
        token = value.get('nextToken')
        if not token:
            break
        if token in seen or len(seen) > 100:
            raise ValueError('unexpected pagination')
        seen.add(token)
    if set(found) != set(NAMES.values()):
        raise ValueError('three examples not found in selected account/region')
    return found


def run(client, arn, mode, prompt, decision=None, simulated=False):
    sid = 'lab-example-' + str(uuid.uuid4())
    first = consume(client.invoke_harness(harnessArn=arn, runtimeSessionId=sid,
        messages=[{'role': 'user', 'content': [{'text': prompt}]}])['stream'])
    if mode != 'approval':
        if first['stop_reason'] != 'end_turn':
            raise ValueError('example did not complete')
        return first
    tool = pending_approval(first)
    if decision is None:
        print('Paused: DEMO_ONLY. No AWS action will execute.')
        decision = input('Enter APPROVED or REJECTED: ').strip().upper()
    second = consume(client.invoke_harness(harnessArn=arn, runtimeSessionId=sid,
        messages=resume_messages(tool, decision, simulated))['stream'])
    if second['stop_reason'] != 'end_turn' or second['tools']:
        raise ValueError('approval continuation did not finish cleanly')
    return {'paused': True, 'decision': decision, 'simulation': True,
            'decision_source': 'automated-test-fixture' if simulated else 'terminal-operator',
            'first': first, 'second': second}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('example', choices=NAMES)
    p.add_argument('--region', default=os.environ.get('AWS_REGION', 'ap-southeast-1'))
    p.add_argument('--profile', default=None)
    p.add_argument('--prompt', default=None)
    p.add_argument('--decision', choices=['APPROVED', 'REJECTED'],
                   help='Automated simulation fixture; omit for a real terminal prompt')
    args = p.parse_args()
    import boto3
    from botocore.config import Config
    session = boto3.Session(profile_name=args.profile)
    found = discover(session, args.region)
    client = session.client('bedrock-agentcore', region_name=args.region,
        config=Config(read_timeout=120, connect_timeout=10, retries={'total_max_attempts': 1}))
    result = run(client, found[NAMES[args.example]]['arn'], args.example,
                 args.prompt or PROMPTS[args.example], args.decision, bool(args.decision))
    if args.example == 'approval':
        print(result['second']['text'])
        print('Typed pause/resume complete; simulation only. No AWS action executed.')
    else:
        print(result['text'])
        print('Completion: ' + result['stop_reason'])


if __name__ == '__main__':
    main()
