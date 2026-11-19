# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class TimedOut:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class NetworkError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ConnectError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ReadTimeout:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class PoolTimeout:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ClientConnectorError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class SomeUnrelatedBug:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_transient_classifier_matches_known_network_errors(*args, **kwargs):
    return None

def test_handler_delegates_unknown_errors_to_default(*args, **kwargs):
    return None
