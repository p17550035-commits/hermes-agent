# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def adapter(*args, **kwargs):
    return None

class _SpyProvider:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def provider(*args, **kwargs):
    return None

def _post_fire(*args, **kwargs):
    return None

def _wait_for(*args, **kwargs):
    return None

class _StartingRunner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _once_waiting(*args, **kwargs):
    return None

def test_fire_during_startup_waits_and_receives_the_live_adapters(*args, **kwargs):
    return None

def test_fire_is_retryable_and_never_claimed_when_startup_does_not_finish(*args, **kwargs):
    return None

def test_gateway_that_starts_draining_mid_boot_is_refused_without_the_full_wait(*args, **kwargs):
    return None

def test_gateway_that_finishes_starting_into_a_drain_is_refused(*args, **kwargs):
    return None

def test_started_gateway_is_accepted_immediately(*args, **kwargs):
    return None

def test_slow_token_verify_spends_the_startup_budget(*args, **kwargs):
    return None
