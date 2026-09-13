from datetime import datetime, timezone


def get_current_time():
    return datetime.now(timezone.utc).isoformat()


def days_until(deadline: str):
    deadline_date = datetime.fromisoformat(deadline).date()
    today = datetime.now(timezone.utc).date()

    return {
        "deadline": deadline,
        "today": today.isoformat(),
        "days_remaining": (deadline_date - today).days,
        "overdue": deadline_date < today
    }
