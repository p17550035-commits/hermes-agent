# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_PEER_GONE_ERRNOS = None

logger = None

_DISABLE_FLUSH = None

class Transport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def current_transport(*args, **kwargs):
    return None

def bind_transport(*args, **kwargs):
    return None

def reset_transport(*args, **kwargs):
    return None

def _raise_unless_peer_gone(*args, **kwargs):
    return None

def serialize_frame(*args, **kwargs):
    return None

class StdioTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FanoutPeer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FanoutTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TeeTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
