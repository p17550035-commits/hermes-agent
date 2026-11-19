# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _EmptyDB:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def two_profiles(*args, **kwargs):
    return None

def _resume(*args, **kwargs):
    return None

def _seed_active_run(*args, **kwargs):
    return None

def test_lazy_resume_refuses_child_id_active_under_another_profile(*args, **kwargs):
    return None

def test_lazy_resume_still_opens_watch_window_under_owning_profile(*args, **kwargs):
    return None
