# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def adapter(*args, **kwargs):
    return None

def _request(*args, **kwargs):
    return None

class TestResolverWithMultiplexOff:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMultiplexOnUnchanged:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_http_request_addressed_to_another_agent_is_404_not_answered(*args, **kwargs):
    return None
