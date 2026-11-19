# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _descriptor(*args, **kwargs):
    return None

class FakeTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeSource:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeEvent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _adapter(*args, **kwargs):
    return None

def _open_turn_draft(*args, **kwargs):
    return None

class TestPromptAckDoesNotSealDraft:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
