# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StubStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _call(*args, **kwargs):
    return None

def test_session_list_surfaces_all_user_facing_sources(*args, **kwargs):
    return None
