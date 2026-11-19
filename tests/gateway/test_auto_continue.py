# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _simulate_auto_continue(*args, **kwargs):
    return None

class TestInterruptedReplayFiltering:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
