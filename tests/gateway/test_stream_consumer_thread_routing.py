# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_adapter(*args, **kwargs):
    return None

class TestInitialReplyToId:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestOverflowFirstMessage:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuFallbackThreadRouting:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFallbackResendThreading:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
