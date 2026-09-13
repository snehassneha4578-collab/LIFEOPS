import unittest

from tools.approval_manager import request_approval, approve_action
from tools.secure_actions import execute_sensitive_action
from tools.memory_evidence import get_memory_evidence
from tools.workflow_memory_agent import recall_workflow
from tools.task_manager import create_task, list_tasks
from agents.verification import verify_result
from agents.report import generate_report


class LIFEOPSRegressionTests(unittest.TestCase):

    def test_blocked_without_approval(self):
        result = execute_sensitive_action(
            "INVALID-APPROVAL",
            "TEST_REGRESSION_ACTION",
            lambda: {"executed": True}
        )
        self.assertEqual(result["status"], "BLOCKED")

    def test_approval_execution_and_replay(self):
        approval = request_approval("TEST_REGRESSION_ACTION")
        approve_action(approval["id"])

        first = execute_sensitive_action(
            approval["id"],
            "TEST_REGRESSION_ACTION",
            lambda: {"executed": True}
        )
        self.assertEqual(first["status"], "EXECUTED")

        replay = execute_sensitive_action(
            approval["id"],
            "TEST_REGRESSION_ACTION",
            lambda: {"executed": True}
        )
        self.assertEqual(replay["status"], "BLOCKED")

    def test_memory_evidence_integrity(self):
        evidence = get_memory_evidence()
        self.assertTrue(evidence["success"])
        self.assertGreaterEqual(evidence["count"], 1)
        self.assertEqual(len(evidence["sha256"]), 64)
        self.assertTrue(
            any(item["id"] == "MEMORY-0003" for item in evidence["records"])
        )

    def test_workflow_memory_retrieval(self):
        result = recall_workflow("secure file write approval consumed")
        self.assertGreaterEqual(result["count"], 1)
        self.assertTrue(
            any(item["id"] == "MEMORY-0003" for item in result["matches"])
        )


    def test_verification_memory_traceability(self):
        result = verify_result(
            "Verify whether persistent memory MEMORY-0003 exists. "
            "Use persistent memory evidence. Do not infer unsupported facts."
        )
        self.assertIn("MEMORY-0003", str(result))
        self.assertIn("VERIFIED:", str(result))

    def test_report_memory_traceability(self):
        result = generate_report(
            "Objective: Verify persistent memory. "
            "VERIFICATION: VERIFIED: MEMORY-0003 exists. "
            "EVIDENCE: Persistent memory evidence directly returned MEMORY-0003. "
            "EVIDENCE_IDS: MEMORY-0003."
        )
        self.assertIn("MEMORY-0003", str(result))
        self.assertIn("EVIDENCE_TRACE:", str(result))

    def test_task_creation_persistence(self):
        task = create_task(
            "LIFEOPS regression test task",
            priority="LOW",
            category="TEST"
        )
        tasks = list_tasks()
        self.assertTrue(
            any(item["id"] == task["id"] for item in tasks)
        )


if __name__ == "__main__":
    unittest.main()

