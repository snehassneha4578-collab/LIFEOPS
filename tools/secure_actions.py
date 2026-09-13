from tools.approval_tools import (
    lifeops_require_approval,
    lifeops_consume_approval
)
from tools.audit_log import log_action


def execute_sensitive_action(
    approval_id: str,
    action: str,
    executor
) -> dict:
    """
    Execute a sensitive action only after exact approval authorization.

    A successfully executed approval is immediately consumed,
    preventing the same approval from being replayed.
    """

    authorization = lifeops_require_approval(
        approval_id,
        action
    )

    if not authorization.get("authorized"):
        log_action(
            "SENSITIVE_ACTION_BLOCKED",
            "BLOCKED",
            {
                "approval_id": approval_id,
                "action": action,
                "reason": authorization.get("reason")
            }
        )

        return {
            "success": False,
            "status": "BLOCKED",
            "approval_id": approval_id,
            "action": action,
            "reason": authorization.get("reason")
        }

    try:
        result = executor()

        consumption = lifeops_consume_approval(
            approval_id,
            action
        )

        if not consumption.get("consumed"):
            log_action(
                "SENSITIVE_ACTION_CONSUME_FAILED",
                "FAILED",
                {
                    "approval_id": approval_id,
                    "action": action,
                    "reason": consumption.get("reason")
                }
            )

            return {
                "success": False,
                "status": "FAILED",
                "approval_id": approval_id,
                "action": action,
                "result": result,
                "reason": (
                    "Action executed but approval "
                    "could not be consumed."
                )
            }

        log_action(
            "SENSITIVE_ACTION_EXECUTED",
            "SUCCESS",
            {
                "approval_id": approval_id,
                "action": action
            }
        )

        return {
            "success": True,
            "status": "EXECUTED",
            "approval_id": approval_id,
            "action": action,
            "result": result
        }

    except Exception as exc:
        log_action(
            "SENSITIVE_ACTION_FAILED",
            "FAILED",
            {
                "approval_id": approval_id,
                "action": action,
                "error": str(exc)
            }
        )

        return {
            "success": False,
            "status": "FAILED",
            "approval_id": approval_id,
            "action": action,
            "error": str(exc)
        }