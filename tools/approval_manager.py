import json
from pathlib import Path
from datetime import datetime, timezone

from tools.audit_log import log_action

APPROVAL_FILE = Path("data/approvals.json")


def _load():
    if not APPROVAL_FILE.exists():
        return []

    try:
        return json.loads(
            APPROVAL_FILE.read_text(encoding="utf-8")
        )
    except (json.JSONDecodeError, OSError):
        return []


def _save(data):
    APPROVAL_FILE.parent.mkdir(parents=True, exist_ok=True)

    APPROVAL_FILE.write_text(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


def request_approval(action: str, details=None):
    approvals = _load()

    approval = {
        "id": f"APPROVAL-{len(approvals) + 1:04d}",
        "action": action,
        "details": details or {},
        "status": "PENDING",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    approvals.append(approval)
    _save(approvals)

    log_action(
        "APPROVAL_REQUESTED",
        "PENDING",
        {
            "approval_id": approval["id"],
            "action": action
        }
    )

    return approval


def list_approvals(status=None):
    approvals = _load()

    if status:
        approvals = [
            item
            for item in approvals
            if item["status"].upper() == status.upper()
        ]

    return approvals


def approve_action(approval_id: str):
    approvals = _load()

    for approval in approvals:
        if approval["id"] == approval_id:
            approval["status"] = "APPROVED"
            approval["approved_at"] = (
                datetime.now(timezone.utc).isoformat()
            )

            _save(approvals)

            log_action(
                "APPROVAL_GRANTED",
                "SUCCESS",
                {
                    "approval_id": approval_id,
                    "action": approval["action"]
                }
            )

            return approval

    log_action(
        "APPROVAL_GRANT_FAILED",
        "FAILED",
        {
            "approval_id": approval_id
        }
    )

    return {
        "error": f"Approval {approval_id} not found"
    }


def consume_approval(approval_id: str, action: str):
    approvals = _load()

    for approval in approvals:
        if approval["id"] == approval_id:

            if approval["action"] != action:
                return {
                    "consumed": False,
                    "approval_id": approval_id,
                    "reason": (
                        "Approval action does not match "
                        "requested action."
                    )
                }

            if approval["status"] != "APPROVED":
                return {
                    "consumed": False,
                    "approval_id": approval_id,
                    "status": approval["status"],
                    "reason": (
                        "Only an APPROVED approval "
                        "can be consumed."
                    )
                }

            approval["status"] = "CONSUMED"
            approval["consumed_at"] = (
                datetime.now(timezone.utc).isoformat()
            )

            _save(approvals)

            log_action(
                "APPROVAL_CONSUMED",
                "SUCCESS",
                {
                    "approval_id": approval_id,
                    "action": action
                }
            )

            return {
                "consumed": True,
                "approval_id": approval_id,
                "action": action,
                "status": "CONSUMED"
            }

    return {
        "consumed": False,
        "approval_id": approval_id,
        "reason": "Approval record not found."
    }


def reject_action(approval_id: str):
    approvals = _load()

    for approval in approvals:
        if approval["id"] == approval_id:
            approval["status"] = "REJECTED"
            approval["rejected_at"] = (
                datetime.now(timezone.utc).isoformat()
            )

            _save(approvals)

            log_action(
                "APPROVAL_REJECTED",
                "SUCCESS",
                {
                    "approval_id": approval_id,
                    "action": approval["action"]
                }
            )

            return approval

    log_action(
        "APPROVAL_REJECTION_FAILED",
        "FAILED",
        {
            "approval_id": approval_id
        }
    )

    return {
        "error": f"Approval {approval_id} not found"
    }