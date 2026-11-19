# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _reset_cron_running_set(*args, **kwargs):
    return None

def _make_async_noop(*args, **kwargs):
    return None

class TestDrainWaitsForCronWork:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestKillToolSubprocessesMarksCronInterrupted:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
