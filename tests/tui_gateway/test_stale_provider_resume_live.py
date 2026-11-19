# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

OLD_URL = None

NEW_URL = None

def live_home(*args, **kwargs):
    return None

def _seed_session_row(*args, **kwargs):
    return None

def _resume(*args, **kwargs):
    return None

def _teardown(*args, **kwargs):
    return None

class TestStaleProviderResumeLive:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
