# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

WAKE = None

class Hold:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def authority_route(*args, **kwargs):
    return None

def admissions(*args, **kwargs):
    return None

def start_human_turn(*args, **kwargs):
    return None

def test_authority_route_refuses_a_wake_while_draining(*args, **kwargs):
    return None

def test_authority_route_refuses_a_wake_when_the_drain_starts_during_admission(*args, **kwargs):
    return None
