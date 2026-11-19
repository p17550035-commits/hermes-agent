# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_log = None

_DRAIN_STOP = None

_QUEUE_MAX = None

class WsPublisherTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
