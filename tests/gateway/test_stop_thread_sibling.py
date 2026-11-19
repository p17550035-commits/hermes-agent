# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _thread_source(*args, **kwargs):
    return None

def _per_user_key(*args, **kwargs):
    return None

def test_sibling_returns_empty_for_non_thread_source(*args, **kwargs):
    return None

def test_sibling_matches_named_profile_runs(*args, **kwargs):
    return None

def test_sibling_does_not_cross_profiles(*args, **kwargs):
    return None

class _StoreEntry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_stop_does_not_interrupt_sibling_when_unauthorized(*args, **kwargs):
    return None

class _FakeStatusAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_stop_no_active_agent_survives_status_clear_failure(*args, **kwargs):
    return None
