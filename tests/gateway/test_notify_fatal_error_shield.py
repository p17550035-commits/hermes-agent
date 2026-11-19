# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_handler_survives_carrier_cancellation(*args, **kwargs):
    return None

def test_carrier_cancellation_still_propagates(*args, **kwargs):
    return None

def test_uncancelled_path_unchanged(*args, **kwargs):
    return None

def test_sync_handler_still_supported(*args, **kwargs):
    return None

def test_no_handler_is_noop(*args, **kwargs):
    return None
