from pathlib import Path
from datetime import datetime, timezone
import json

TASK_FILE = Path("data/tasks.json")
AUDIT_FILE = Path("data/audit_log.json")


def _load_json(path):
    if not path.exists():
        return []

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def _audit(action, status, details):
    log = _load_json(AUDIT_FILE)

    log.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "status": status,
        "details": details
    })

    _save_json(AUDIT_FILE, log)


def _load_tasks():
    return _load_json(TASK_FILE)


def create_task(title, priority="MEDIUM", deadline=None, category="GENERAL"):
    tasks = _load_tasks()

    task = {
        "id": f"TASK-{max([int(t["id"].split("-")[1]) for t in tasks if str(t.get("id", "")).startswith("TASK-") and t["id"].split("-")[1].isdigit()] or [0]) + 1:04d}",
        "title": title,
        "priority": priority.upper(),
        "deadline": deadline,
        "category": category,
        "status": "TODO",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    tasks.append(task)
    _save_json(TASK_FILE, tasks)

    _audit(
        "TASK_CREATED",
        "SUCCESS",
        {"task_id": task["id"], "title": title}
    )

    return task


def list_tasks(status=None):
    tasks = _load_tasks()

    if status:
        tasks = [
            task for task in tasks
            if task["status"].upper() == status.upper()
        ]

    return tasks


def complete_task(task_id):
    tasks = _load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "COMPLETED"
            task["completed_at"] = datetime.now(timezone.utc).isoformat()

            _save_json(TASK_FILE, tasks)

            _audit(
                "TASK_COMPLETED",
                "SUCCESS",
                {"task_id": task_id}
            )

            return task

    _audit(
        "TASK_COMPLETION_FAILED",
        "FAILED",
        {"task_id": task_id, "reason": "Task not found"}
    )

    return {
        "error": f"Task {task_id} not found"
    }
