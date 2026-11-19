# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _safe_int(*args, **kwargs):
    return None

class CompressionTelemetryMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
