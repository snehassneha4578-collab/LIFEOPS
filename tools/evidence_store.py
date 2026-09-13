import json
from pathlib import Path
from datetime import datetime, timezone

EVIDENCE_FILE = Path("data/research_evidence.json")


def save_evidence(url: str, domain: str, text: str, excerpt: str = "") -> dict:
    """Persist retrieved research evidence for later verification."""

    records = []

    if EVIDENCE_FILE.exists():
        try:
            records = json.loads(
                EVIDENCE_FILE.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, OSError):
            records = []

    evidence = {
        "id": f"EVIDENCE-{len(records) + 1:04d}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "url": url,
        "domain": domain,
        "text": text,
        "excerpt": excerpt
    }

    records.append(evidence)

    EVIDENCE_FILE.parent.mkdir(parents=True, exist_ok=True)
    EVIDENCE_FILE.write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return evidence


def list_evidence() -> list:
    """Return all persisted research evidence."""

    if not EVIDENCE_FILE.exists():
        return []

    try:
        return json.loads(
            EVIDENCE_FILE.read_text(encoding="utf-8")
        )
    except (json.JSONDecodeError, OSError):
        return []



