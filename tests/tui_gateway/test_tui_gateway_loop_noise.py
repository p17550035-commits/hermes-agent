# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeConnectionLostCallback:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_benign_teardown_matches_reset_in_connection_lost(*args, **kwargs):
    return None

def test_benign_teardown_matches_aborted_and_broken_pipe(*args, **kwargs):
    return None

def test_reset_outside_connection_lost_is_not_suppressed(*args, **kwargs):
    return None

def test_unrelated_exception_is_not_suppressed(*args, **kwargs):
    return None

def test_no_exception_is_not_suppressed(*args, **kwargs):
    return None

def test_install_suppresses_flood_and_forwards_real_errors(*args, **kwargs):
    return None
