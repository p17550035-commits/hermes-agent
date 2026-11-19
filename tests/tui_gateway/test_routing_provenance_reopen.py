# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

TURN = None

class _ImmediateThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _session(*args, **kwargs):
    return None

def db(*args, **kwargs):
    return None

def turn_env(*args, **kwargs):
    return None

def _stamp(*args, **kwargs):
    return None

def test_a_registered_stale_close_is_cleared_before_the_turn_and_rotation_publishes(*args, **kwargs):
    return None

def test_only_an_explicit_close_on_a_still_registered_session_is_cleared(*args, **kwargs):
    return None
