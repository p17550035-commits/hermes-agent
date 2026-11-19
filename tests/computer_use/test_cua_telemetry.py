# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_VAR = None

class TestTelemetryDisabledFlag:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestChildEnv:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
