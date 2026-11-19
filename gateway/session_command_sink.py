# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class CommandSink:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def active_sink(*args, **kwargs):
    return None

def capture(*args, **kwargs):
    return None
