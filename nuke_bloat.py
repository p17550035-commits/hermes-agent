import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(".").resolve()
QUARANTINE = REPO_ROOT / "_purged_code"

# Directories and files to physically rip out of the codebase
PURGE_KEYWORDS = [
    "gateway",
    "telemetry",
    "updater",
    "self_update",
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

def purge_repo():
    if QUARANTINE.exists():
        shutil.rmtree(QUARANTINE)
    QUARANTINE.mkdir(parents=True)

    deleted_files = []
    stubbed_modules = set()

    # 1. Physically move matching files/folders out of the source tree into _purged_code
    for path in sorted(REPO_ROOT.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if any(skip in path.parts for skip in ["_purged_code", ".git", "venv", ".venv", "__pycache__"]):
            continue
        if path.is_file() and any(kw in path.name.lower() for kw in PURGE_KEYWORDS):
            rel = path.relative_to(REPO_ROOT)
            dest = QUARANTINE / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(dest))
            deleted_files.append(str(rel))
            if path.suffix == ".py":
                stubbed_modules.add(path.stem)

    # 2. Clean broken imports, strip hardcoded guardrail strings, and neutralize phone-home URLs
    leftover_urls = []
    for py_file in REPO_ROOT.rglob("*.py"):
        if any(skip in py_file.parts for skip in ["_purged_code", ".git", "venv", ".venv"]):
            continue

        content = py_file.read_text(encoding="utf-8", errors="ignore")
        orig = content

        # Neutralize imports pointing to physically deleted modules
        for mod in stubbed_modules:
            content = re.sub(
                rf"^(?:from\s+[\w.]*{re.escape(mod)}[\w.]*\s+import\s+.*|import\s+[\w.]*{re.escape(mod)}.*)$",
                f"# PURGED: {mod}",
                content,
                flags=re.MULTILINE,
            )

        # Strip guardrail / updater / telemetry function bodies
        for pat, rep in STRIP_BLOCKS:
            content = re.sub(pat, rep, content)

        # Kill any hardcoded Nous / telemetry domains
        content = re.sub(r"https?://[a-zA-Z0-9.-]*(?:nousresearch|hermes|atropos|posthog|sentry|segment)[a-zA-Z0-9./_-]*", "http://0.0.0", content)

        if content != orig:
            py_file.write_text(content, encoding="utf-8")

        # Audit any remaining URLs so nothing sneaks past
        for match in re.findall(r"https?://[^\s\"'<>]+", content):
            if "0.0.0.0" not in match and "127.0.0.1" not in match and "localhost" not in match:
                leftover_urls.append((str(py_file.relative_to(REPO_ROOT)), match))

    print(f"[+] Physically removed {len(deleted_files)} gateway/telemetry/updater files -> moved to _purged_code/")
    print("\n[!] AUDIT OF REMAINING EXTERNAL URLS IN CODEBASE:")
    for fpath, url in sorted(set(leftover_urls)):
        print(f"    {fpath}: {url}")

if __name__ == "__main__":
    purge_repo()
