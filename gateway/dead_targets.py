# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_DEAD_ERROR_KINDS = None

def _normalize(*args, **kwargs):
    return None

def classify_dead_error(*args, **kwargs):
    return None

class DeadTargetRegistry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
