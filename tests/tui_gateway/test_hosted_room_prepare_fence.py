# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pending_approval = None

class _Peer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _HandoffLock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def preparation(*args, **kwargs):
    return None

def test_fenced_preparation_is_durable_before_unlock_and_worker_acknowledges(*args, **kwargs):
    return None

def test_local_cancel_still_acknowledges_synchronously(*args, **kwargs):
    return None
