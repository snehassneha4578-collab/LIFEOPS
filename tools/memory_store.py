import json
import re
from pathlib import Path
from datetime import datetime, timezone

MEMORY_FILE = Path("data/lifeops_memory.json")

def _load():
    if not MEMORY_FILE.exists():
        return []
    try:
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

def save_memory(memory_type, content, source="workflow"):
    records = _load()
    record = {
        "id": f"MEMORY-{len(records) + 1:04d}",
        "type": memory_type,
        "content": content,
        "source": source,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    records.append(record)
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    MEMORY_FILE.write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    return record

def list_memories(memory_type=None):
    records = _load()
    if memory_type:
        records = [
            item for item in records
            if item.get("type", "").upper() == memory_type.upper()
        ]
    return records

def search_memories(query, limit=10):
    words = [
        word.lower()
        for word in re.findall(r"[A-Za-z0-9_-]+", query)
        if len(word) > 2
    ]

    if not words:
        return []

    scored = []

    for item in _load():
        searchable = json.dumps(item, ensure_ascii=False).lower()
        matched = [word for word in words if word in searchable]

        if matched:
            score = len(matched) / len(words)
            scored.append((score, item))

    scored.sort(key=lambda pair: (-pair[0], pair[1].get("created_at", "")))

    return [item for _, item in scored[:limit]]
