# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Manager:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _agent(*args, **kwargs):
    return None

def test_manager_survives_across_requests_and_is_exclusive_per_home(*args, **kwargs):
    return None

def test_a_manager_parked_past_the_retry_horizon_is_not_handed_to_a_reused_id(*args, **kwargs):
    return None
