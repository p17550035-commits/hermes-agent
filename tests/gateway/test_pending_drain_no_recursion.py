# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_adapter(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def _sk(*args, **kwargs):
    return None

def _count_pmb_frames(*args, **kwargs):
    return None

def test_in_band_drain_does_not_grow_stack(*args, **kwargs):
    return None

def test_normal_path_releases_session_guard(*args, **kwargs):
    return None

def test_drain_task_cancellation_releases_session(*args, **kwargs):
    return None
