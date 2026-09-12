import importlib.util
from pathlib import Path
import unittest

APP = Path(__file__).resolve().parents[1] / "app" / "main.py"
spec = importlib.util.spec_from_file_location("agentcore_runtime_main", APP)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PayloadTests(unittest.TestCase):
    def test_direct_prompt(self):
        self.assertEqual(
            module.response_for({"prompt": "hello"}),
            {"response": "AgentCore Runtime OK: hello", "status": "success"},
        )

    def test_wrapped_prompt(self):
        self.assertEqual(
            module.response_for({"input": {"prompt": "hello"}}),
            {"response": "AgentCore Runtime OK: hello", "status": "success"},
        )

    def test_empty_prompt_rejected(self):
        with self.assertRaises(ValueError):
            module.response_for({"prompt": "   "})


if __name__ == "__main__":
    unittest.main()
