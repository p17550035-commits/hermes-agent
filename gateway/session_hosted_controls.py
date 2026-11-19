# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_GRANT_ERRORS = None

class HostedControls:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
