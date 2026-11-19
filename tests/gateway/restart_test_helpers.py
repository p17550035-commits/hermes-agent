# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RestartTestAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def make_restart_source(*args, **kwargs):
    return None

def make_restart_runner(*args, **kwargs):
    return None
