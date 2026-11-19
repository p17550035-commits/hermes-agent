# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

CHAT_ID = None

REQ_ID = None

TURN_ID = None

BLOCK_TEXT = None

def _make_adapter(*args, **kwargs):
    return None

def _finalize_calls(*args, **kwargs):
    return None

class TestKeepaliveSuppressesClockDecline:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestIntermediateFrameFailureIsFireAndForget:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
