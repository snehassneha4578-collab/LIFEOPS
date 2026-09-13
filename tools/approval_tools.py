from strands import tool

from tools.approval_manager import (
    request_approval,
    list_approvals,
    approve_action,
    reject_action,
    consume_approval
)


@tool
def lifeops_request_approval(
    action: str,
    details: dict = None
) -> dict:
    return request_approval(action, details)


@tool
def lifeops_list_approvals(
    status: str = None
) -> list:
    return list_approvals(status)


@tool
def lifeops_approve_action(
    approval_id: str
) -> dict:
    return approve_action(approval_id)


@tool
def lifeops_reject_action(
    approval_id: str
) -> dict:
    return reject_action(approval_id)


@tool
def lifeops_consume_approval(
    approval_id: str,
    action: str
) -> dict:
    return consume_approval(
        approval_id,
        action
    )


@tool
def lifeops_require_approval(
    approval_id: str,
    action: str
) -> dict:
    approvals = list_approvals()

    for approval in approvals:
        if approval["id"] != approval_id:
            continue

        if approval["action"] != action:
            return {
                "authorized": False,
                "approval_id": approval_id,
                "reason": (
                    "Approval action does not match "
                    "requested action."
                )
            }

        if approval["status"] != "APPROVED":
            return {
                "authorized": False,
                "approval_id": approval_id,
                "status": approval["status"],
                "reason": (
                    "Sensitive action requires "
                    "an APPROVED approval."
                )
            }

        return {
            "authorized": True,
            "approval_id": approval_id,
            "status": "APPROVED",
            "action": action
        }

    return {
        "authorized": False,
        "approval_id": approval_id,
        "reason": "Approval record not found."
    }