# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PROXY_403_BODY = None

def proxy_403(*args, **kwargs):
    return None

def relay_refusal(*args, **kwargs):
    return None

def store_unavailable(*args, **kwargs):
    return None

OK = None

def json_proxy_403(*args, **kwargs):
    return None

def echoing(*args, **kwargs):
    return None

def _http_error(*args, **kwargs):
    return None

class _Resp:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeConnector:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
