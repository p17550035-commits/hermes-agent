# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_event(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

class TestVerboseCommand:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
