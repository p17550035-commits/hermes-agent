import ast
import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(".").resolve()
QUARANTINE = REPO_ROOT / "_purged_code"

# Directories and files to physically rip out of the codebase (matched against full relative path)
PURGE_KEYWORDS = [
    "gateway",
    "telemetry",
    "otel",
    "observability",
    "trace_upload",
    "updater",
    "self_update",
    "update_cmd",
    "source_check",
    "model_catalog",
    "models_dev",
    "aa_quality_sync",
    "portal",
    "collective_wisdom",
    "honcho",
    "analytics",
    "atropos",
]

# Hardcoded prompt-injection / guardrail / phone-home strings to gut from remaining files
STRIP_BLOCKS = [
    # Rip out auto-update checks
    (r"def\s+check_for_updates\s*\([^)]*\):[\s\S]*?(?=\ndef\s|\nclass\s|\Z)", "def check_for_updates(*a, **kw):\n    return False\n"),
    # Rip out trajectory / telemetry exporters
    (r"def\s+(?:export_trajectory|send_telemetry|report_metrics|sync_portal)\s*\([^)]*\):[\s\S]*?(?=\ndef\s|\nclass\s|\Z)", "def disabled_hook(*a, **kw):\n    return None\n"),
    # Gut hardcoded safety/guardrail/commercial-restriction prompt blocks
    (r"(?:GUARDRAIL|SAFETY_PROMPT|SYSTEM_CONSTRAINTS|COLLECTIVE_WISDOM_PROMPT)\s*=\s*(?:\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\'|\"[^\"]*\"|\'[^\']*\')", 'GUARDRAIL_STRIPPED = ""'),
]

def build_silent_stub(py_path: Path) -> str:
    """Parse a purged .py file's AST and generate instant no-op stubs so callers never crash."""
    source = py_path.read_text(encoding="utf-8", errors="ignore")
    lines = ["# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub\n"]
    try:
        tree = ast.parse(source)
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                lines.append(f"def {node.name}(*args, **kwargs):\n    return None\n")
            elif isinstance(node, ast.ClassDef):
                lines.append(
                    f"class {node.name}:\n"
                    f"    def __init__(self, *args, **kwargs): pass\n"
                    f"    def __getattr__(self, name): return lambda *a, **kw: None\n"
                )
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and not target.id.startswith("__"):
                        lines.append(f"{target.id} = None\n")
    except SyntaxError:
        pass
    return "\n".join(lines)

def purge_repo():
    if QUARANTINE.exists():
        shutil.rmtree(QUARANTINE)
    QUARANTINE.mkdir(parents=True)

    deleted_files = []

    # 1. Physically move matching files out of the source tree into _purged_code
    #    and leave behind a silent, zero-latency local stub for .py modules
    for path in sorted(REPO_ROOT.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if any(skip in path.parts for skip in ["_purged_code", ".git", "venv", ".venv", "__pycache__"]):
            continue
        if path.name == "nuke_bloat.py":
            continue
        if path.is_file():
            rel = path.relative_to(REPO_ROOT)
            if any(kw in str(rel).lower() for kw in PURGE_KEYWORDS):
                dest = QUARANTINE / rel
                dest.parent.mkdir(parents=True, exist_ok=True)

                stub_code = build_silent_stub(path) if path.suffix == ".py" else None
                shutil.move(str(path), str(dest))
                deleted_files.append(str(rel))

                if stub_code is not None:
                    path.write_text(stub_code, encoding="utf-8")

    # 2. Strip hardcoded guardrail strings and neutralize phone-home URLs (without mangling multi-line imports)
    leftover_urls = []
    for py_file in REPO_ROOT.rglob("*.py"):
        if any(skip in py_file.parts for skip in ["_purged_code", ".git", "venv", ".venv"]):
            continue
        if py_file.name == "nuke_bloat.py":
            continue

        content = py_file.read_text(encoding="utf-8", errors="ignore")
        orig = content

        # Strip guardrail / updater / telemetry function bodies
        for pat, rep in STRIP_BLOCKS:
            content = re.sub(pat, rep, content)

        # Kill hardcoded Nous / telemetry / pastebin / catalog domains (sinkhole to 0.0.0.0)
        content = re.sub(
            r"https?://[a-zA-Z0-9.-]*(?:nousresearch|hermes|atropos|posthog|sentry|segment|dpaste\.com|paste\.rs|models\.dev|artificialanalysis\.ai)[a-zA-Z0-9./_-]*",
            "http://0.0.0.0",
            content,
        )

        if content != orig:
            py_file.write_text(content, encoding="utf-8")

        # Audit any remaining URLs outside tests/ so nothing sneaks past
        if "tests" not in py_file.parts:
            for match in re.findall(r"https?://[^\s\"'<>]+", content):
                if "0.0.0.0" not in match and "127.0.0.1" not in match and "localhost" not in match:
                    leftover_urls.append((str(py_file.relative_to(REPO_ROOT)), match))

    print(f"[+] Physically quarantined {len(deleted_files)} bloat/telemetry files -> _purged_code/ (replaced with 0ms no-op stubs)")
    print("\n[!] AUDIT OF REMAINING NON-TEST EXTERNAL URLS IN CODEBASE:")
    for fpath, url in sorted(set(leftover_urls)):
        print(f"    {fpath}: {url}")

if __name__ == "__main__":
    purge_repo()
