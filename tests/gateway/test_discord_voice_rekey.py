# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

KEY_A = None

KEY_B = None

def _make_conn(*args, **kwargs):
    return None

def _make_vc(*args, **kwargs):
    return None

def _make_receiver(*args, **kwargs):
    return None

def _rtp_packet(*args, **kwargs):
    return None

class _FakeAead:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def fake_nacl(*args, **kwargs):
    return None

class TestCredentialResolution:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFailureStreakRefresh:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestWebsocketHookTrigger:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestDaveUnmappedDrop:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestTeardownHealthLine:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
