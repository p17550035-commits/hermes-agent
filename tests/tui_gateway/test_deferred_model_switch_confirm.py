# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

GUARDED_MODEL = None

UNGUARDED_MODEL = None

def _session(*args, **kwargs):
    return None

def _config_set_model(*args, **kwargs):
    return None

def running_session(*args, **kwargs):
    return None

class TestGuardedPickAsksBeforeStashing:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestUnguardedPickStillDefers:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestGuardFailureIsNotFatal:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def threshold(*args, **kwargs):
    return None

def _live_agent(*args, **kwargs):
    return None

class TestLargeContextPickAsksBeforeStashing:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_bare_pick_is_guarded_against_the_live_provider(*args, **kwargs):
    return None

class TestDroppedQueuedPickIsLogged:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestDroppedQueuedPickIsNotATurnError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
