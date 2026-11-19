# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _reset_async_delegation_records(*args, **kwargs):
    return None

def _cleanup_async_delegations(*args, **kwargs):
    return None

class TestDrainWaitsForBackgroundDelegations:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestManagedWorkerDelegationDrain:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
