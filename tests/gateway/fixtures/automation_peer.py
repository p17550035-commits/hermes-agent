# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Model:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _identify_until_ready(*args, **kwargs):
    return None

def probe(*args, **kwargs):
    return None
