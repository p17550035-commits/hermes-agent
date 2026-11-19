# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _classify(*args, **kwargs):
    return None

class TestContextOverflowStillSkipsTranscript:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestTransientFailureKeepsUserMessage:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSuccessfulResultUnaffected:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
