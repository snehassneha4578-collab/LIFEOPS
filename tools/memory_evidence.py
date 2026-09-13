from pathlib import Path
import hashlib
import json

MEMORY_FILE = Path("data/lifeops_memory.json")

def get_memory_evidence():
    if not MEMORY_FILE.exists():
        return {
            "success": False,
            "reason": "Memory file not found."
        }

    raw = MEMORY_FILE.read_bytes()
    records = json.loads(raw)

    return {
        "success": True,
        "file": str(MEMORY_FILE),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "count": len(records),
        "records": records
    }
