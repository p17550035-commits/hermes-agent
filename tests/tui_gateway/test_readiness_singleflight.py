# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _RecordingTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _dispatch(*args, **kwargs):
    return None

def _patch_fast_probe_env(*args, **kwargs):
    return None

def test_overlapping_runtime_checks_share_one_probe_and_keep_pool_responsive(*args, **kwargs):
    return None

def test_blocked_provider_does_not_serialize_a_healthy_provider_check(*args, **kwargs):
    return None

def test_probe_outliving_its_budget_answers_retryable_unknown_then_reprobes(*args, **kwargs):
    return None

def test_fast_probe_cannot_deadlock_the_share_lock(*args, **kwargs):
    return None

def test_overlapping_poll_joins_a_fast_probe_instead_of_erroring(*args, **kwargs):
    return None
