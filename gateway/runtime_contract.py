# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

RuntimeState = None

class RuntimeObservation:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def next_start_action(*args, **kwargs):
    return None
