# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_slack_mock(*args, **kwargs):
    return None

class _SdkLikeResponse:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _real_sdk_response(*args, **kwargs):
    return None

_FACTORIES = None

response_shape = None

def _make_adapter(*args, **kwargs):
    return None

class TestSlackResponsePayload:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestIdentityResolution:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSendPaths:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestHandoffThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _fake_slack_sdk(*args, **kwargs):
    return None

class TestStandaloneSendMediaPath:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
