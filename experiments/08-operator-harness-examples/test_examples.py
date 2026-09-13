import unittest
from examples import consume, pending_approval, resume_messages


def tool_events(raw='{"action":"DEMO_ONLY"}', name='request_approval', tid='test-tool'):
    return [{'messageStart': {'role': 'assistant'}},
            {'contentBlockStart': {'contentBlockIndex': 0, 'start': {'toolUse': {'toolUseId': tid, 'name': name}}}},
            {'contentBlockDelta': {'contentBlockIndex': 0, 'delta': {'toolUse': {'input': raw}}}},
            {'contentBlockStop': {'contentBlockIndex': 0}},
            {'messageStop': {'stopReason': 'tool_use'}}]


class Tests(unittest.TestCase):
    def test_typed_pause(self):
        self.assertEqual(pending_approval(consume(tool_events()))['input'], {'action': 'DEMO_ONLY'})

    def test_fragmented_json(self):
        e = tool_events(); e[2]['contentBlockDelta']['delta']['toolUse']['input'] = '{"action":'
        e.insert(3, {'contentBlockDelta': {'contentBlockIndex': 0, 'delta': {'toolUse': {'input': '"DEMO_ONLY"}'}}}})
        pending_approval(consume(e))

    def test_resume_binding_both_decisions(self):
        tool = pending_approval(consume(tool_events()))
        for decision in ('APPROVED', 'REJECTED'):
            messages = resume_messages(tool, decision, True)
            self.assertEqual(messages[0]['content'][0]['toolUse']['toolUseId'],
                             messages[1]['content'][0]['toolResult']['toolUseId'])

    def test_invalid_decision(self):
        with self.assertRaises(ValueError):
            resume_messages(pending_approval(consume(tool_events())), 'yes')

    def test_wrong_tool_scope_or_id(self):
        for kwargs in ({'name': 'shell'}, {'raw': '{"action":"DELETE"}'},
                       {'raw': '{"action":"DEMO_ONLY","extra":1}'}, {'tid': ''}):
            with self.assertRaises(ValueError):
                pending_approval(consume(tool_events(**kwargs)))

    def test_malformed_json(self):
        with self.assertRaises(ValueError): consume(tool_events(raw='{bad'))

    def test_prose_is_not_approval(self):
        e = [{'contentBlockDelta': {'contentBlockIndex': 0, 'delta': {'text': 'I request approval'}}},
             {'messageStop': {'stopReason': 'end_turn'}}]
        with self.assertRaises(ValueError): pending_approval(consume(e))

    def test_incomplete(self):
        with self.assertRaises(ValueError): consume(tool_events()[:-1])

    def test_error_event(self):
        with self.assertRaises(ValueError): consume([{'runtimeClientError': {'message': 'bad'}}])

    def test_extra_tool(self):
        turn = consume(tool_events()); turn['tools'].append(dict(turn['tools'][0]))
        with self.assertRaises(ValueError): pending_approval(turn)

    def test_truncation_is_not_approval(self):
        e = tool_events(); e[-1]['messageStop']['stopReason'] = 'max_tokens'
        with self.assertRaises(ValueError): pending_approval(consume(e))

    def test_orphan_delta(self):
        with self.assertRaises(ValueError): consume(tool_events()[2:])


if __name__ == '__main__': unittest.main()
