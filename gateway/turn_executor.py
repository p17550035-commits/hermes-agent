# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_IDLE_TIMEOUT_S = None

class _Worker:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _UnboundedThreadExecutor:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
