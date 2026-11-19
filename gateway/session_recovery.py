# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

def _origin_json(*args, **kwargs):
    return None

class SessionRecoveryMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
