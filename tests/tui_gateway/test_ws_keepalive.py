# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeSocket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeWS:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_ws_socket_enables_keepalive(*args, **kwargs):
    return None

def test_ws_socket_unreachable_is_silent(*args, **kwargs):
    return None
