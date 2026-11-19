# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _captured_watcher_source(*args, **kwargs):
    return None

class TestWatcherRespawnTemplate:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
