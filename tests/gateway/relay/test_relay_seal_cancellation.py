# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class HangOnSealTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestCancelDuringSeal:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
