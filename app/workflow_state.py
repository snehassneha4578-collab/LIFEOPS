from dataclasses import dataclass, field
from typing import Any

@dataclass
class WorkflowState:
    request: str
    plan: Any = None
    priorities: Any = None
    research: Any = None
    evidence: Any = None
    action: Any = None
    recovery: Any = None
    verification: Any = None
    report: Any = None
    approvals: list = field(default_factory=list)
    errors: list = field(default_factory=list)

    def to_dict(self):
        return {
            "request": self.request,
            "plan": self.plan,
            "priorities": self.priorities,
            "research": self.research,
            "evidence": self.evidence,
            "action": self.action,
            "recovery": self.recovery,
            "verification": self.verification,
            "report": self.report,
            "approvals": self.approvals,
            "errors": self.errors,
        }
