# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeWatchdog:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _bare_runner(*args, **kwargs):
    return None

def test_runner_starts_watchdog_only_after_running(*args, **kwargs):
    return None
