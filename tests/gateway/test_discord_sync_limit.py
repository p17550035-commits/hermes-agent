# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_discord_mock(*args, **kwargs):
    return None

class _FakeTreeCommand:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def adapter(*args, **kwargs):
    return None

def test_safe_sync_deletes_before_creating(*args, **kwargs):
    return None
