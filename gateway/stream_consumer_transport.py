# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_MAX_EDIT_BACKOFF_SECS = None

class StreamTransportMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
