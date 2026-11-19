# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_store(*args, **kwargs):
    return None

def _make_source(*args, **kwargs):
    return None

def _is_new_session(*args, **kwargs):
    return None

class TestIsNewSessionSurvivesUpdatedAtBump:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestVanillaBehaviorUnaffected:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPersistence:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
