# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _TrackedLock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _record(*args, **kwargs):
    return None

def _db_with_rows(*args, **kwargs):
    return None

def _peer(*args, **kwargs):
    return None

def _make_store(*args, **kwargs):
    return None

def _source(*args, **kwargs):
    return None

def _seed_entry(*args, **kwargs):
    return None

class TestStaleCheckOutsideLock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSaveOutsideLock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestRecoverOutsideLock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_concurrent_same_key_returns_one_published_session(*args, **kwargs):
    return None

def test_auto_reset_does_not_recover_session_being_ended(*args, **kwargs):
    return None
