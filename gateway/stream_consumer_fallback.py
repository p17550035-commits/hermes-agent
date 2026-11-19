# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

def _edit_skipped(*args, **kwargs):
    return None

class StreamFallbackMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
