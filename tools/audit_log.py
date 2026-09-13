import json
from pathlib import Path
from datetime import datetime, timezone

AUDIT_FILE = Path("data/audit_log.json")


def _load_log():
    if not AUDIT_FILE.exists():
        return []

    try:
        return json.loads(AUDIT_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def log_action(action, status, details=None):
    entries = _load_log()

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "status": status,
        "details": details or {}
    }

    entries.append(entry)

    AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_FILE.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return entry


def get_audit_log():
    return _load_log()
