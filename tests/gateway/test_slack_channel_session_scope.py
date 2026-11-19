# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def adapter(*args, **kwargs):
    return None

def _redirect_cache(*args, **kwargs):
    return None

def _channel_event(*args, **kwargs):
    return None

class TestChannelSessionScopeDefault:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestChannelSessionScopeShared:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestThreadReplyAlwaysScopesByThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
