from pathlib import Path
from strands import tool


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    "dist",
    "build",
}


def _is_ignored(path: Path) -> bool:
    return any(
        part in IGNORED_DIRECTORIES
        for part in path.parts
    )


@tool
def lifeops_inspect_workspace(
    workspace_path: str = "."
) -> dict:
    """Safely inspect workspace structure without modifying files."""

    root = Path(workspace_path).resolve()

    if not root.exists():
        return {
            "success": False,
            "error": f"Workspace not found: {root}"
        }

    if not root.is_dir():
        return {
            "success": False,
            "error": f"Workspace is not a directory: {root}"
        }

    files = []
    directories = []
    extensions = {}

    for item in root.rglob("*"):
        try:
            relative = item.relative_to(root)

            if _is_ignored(relative):
                continue

            if item.is_dir():
                directories.append(str(relative))

            elif item.is_file():
                files.append(str(relative))

                extension = item.suffix.lower() or "[no_extension]"
                extensions[extension] = (
                    extensions.get(extension, 0) + 1
                )

        except OSError:
            continue

    return {
        "success": True,
        "workspace": str(root),
        "file_count": len(files),
        "directory_count": len(directories),
        "files": sorted(files),
        "directories": sorted(directories),
        "extensions": dict(
            sorted(
                extensions.items(),
                key=lambda item: (-item[1], item[0])
            )
        ),
        "ignored_directories": sorted(IGNORED_DIRECTORIES),
    }


@tool
def lifeops_find_workspace_artifacts(
    patterns: list[str],
    workspace_path: str = "."
) -> dict:
    """Find real workspace files matching explicitly supplied patterns."""

    root = Path(workspace_path).resolve()

    if not root.exists():
        return {
            "success": False,
            "error": f"Workspace not found: {root}"
        }

    if not root.is_dir():
        return {
            "success": False,
            "error": f"Workspace is not a directory: {root}"
        }

    if not patterns:
        return {
            "success": False,
            "error": "At least one search pattern is required."
        }

    matches = []

    for item in root.rglob("*"):
        try:
            relative = item.relative_to(root)

            if _is_ignored(relative) or not item.is_file():
                continue

            name = item.name.lower()

            for pattern in patterns:
                if pattern.lower() in name:
                    matches.append({
                        "pattern": pattern,
                        "path": str(relative)
                    })

        except OSError:
            continue

    return {
        "success": True,
        "patterns": patterns,
        "match_count": len(matches),
        "matches": matches
    }


@tool
def lifeops_read_workspace_artifact(
    artifact_path: str,
    workspace_path: str = ".",
    max_chars: int = 12000
) -> dict:
    """
    Safely read a bounded amount of text from a workspace artifact.

    Read-only. Does not modify the artifact.
    """

    root = Path(workspace_path).resolve()
    target = (root / artifact_path).resolve()

    try:
        target.relative_to(root)
    except ValueError:
        return {
            "success": False,
            "error": "Artifact path must remain inside the workspace."
        }

    if _is_ignored(target.relative_to(root)):
        return {
            "success": False,
            "error": "Artifact is inside an ignored directory."
        }

    if not target.exists():
        return {
            "success": False,
            "error": f"Artifact not found: {artifact_path}"
        }

    if not target.is_file():
        return {
            "success": False,
            "error": f"Artifact is not a file: {artifact_path}"
        }

    if max_chars <= 0:
        return {
            "success": False,
            "error": "max_chars must be greater than zero."
        }

    try:
        content = target.read_text(
            encoding="utf-8",
            errors="replace"
        )

        truncated = len(content) > max_chars

        return {
            "success": True,
            "path": str(target.relative_to(root)),
            "size_bytes": target.stat().st_size,
            "character_count": len(content),
            "truncated": truncated,
            "content": content[:max_chars]
        }

    except OSError as exc:
        return {
            "success": False,
            "error": str(exc)
        }