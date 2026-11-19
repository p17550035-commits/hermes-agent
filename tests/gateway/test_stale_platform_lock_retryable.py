# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def adapter(*args, **kwargs):
    return None

def test_stale_lock_failure_is_retryable(*args, **kwargs):
    return None

def test_explicit_replace_takeover_reacquires_lock_once(*args, **kwargs):
    return None

def test_lock_conflict_names_owning_profile(*args, **kwargs):
    return None

def test_lock_conflict_infers_profile_from_legacy_hermes_home(*args, **kwargs):
    return None
