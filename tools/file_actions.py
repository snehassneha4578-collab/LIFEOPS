from pathlib import Path

from tools.secure_actions import execute_sensitive_action


def execute_file_write(
    approval_id: str,
    workspace_path: str,
    relative_path: str,
    content: str,
) -> dict:
    """Write a text file only after exact approval authorization."""

    root = Path(workspace_path).resolve()
    target = (root / relative_path).resolve()

    try:
        target.relative_to(root)
    except ValueError:
        return {
            "success": False,
            "status": "BLOCKED",
            "reason": "Target path must remain inside the workspace."
        }

    if target.name in {".env", ".gitignore"} or ".git" in target.parts:
        return {
            "success": False,
            "status": "BLOCKED",
            "reason": "Protected file or directory."
        }

    def writer():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return {
            "path": str(target.relative_to(root)),
            "bytes_written": len(content.encode("utf-8"))
        }

    return execute_sensitive_action(
        approval_id,
        f"WRITE_FILE:{target.relative_to(root).as_posix()}",
        writer
    )

