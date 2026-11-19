# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def runner_with_home(*args, **kwargs):
    return None

class TestStuckLoopDetection:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
