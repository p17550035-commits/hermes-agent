# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_event(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

class _CapturingAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestReasoningCommand:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestLoadShowReasoningCoercion:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
