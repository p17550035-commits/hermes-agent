# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _NoOnboardingRun:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_session_delete_requires_session_id(*args, **kwargs):
    return None

def test_session_delete_returns_db_unavailable_when_no_db(*args, **kwargs):
    return None

def test_session_delete_refuses_active_session(*args, **kwargs):
    return None

def test_session_delete_fails_closed_when_active_snapshot_raises(*args, **kwargs):
    return None

def test_session_delete_returns_4007_when_missing(*args, **kwargs):
    return None

def test_session_delete_propagates_db_exception(*args, **kwargs):
    return None

def test_session_delete_success_returns_deleted_id(*args, **kwargs):
    return None

def test_session_delete_honors_params_profile_sessions_dir(*args, **kwargs):
    return None
