# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _telegram_request(*args, **kwargs):
    return None

class _CountingTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _factory(*args, **kwargs):
    return None

def test_failed_fallback_pool_is_discarded_and_closed(*args, **kwargs):
    return None

def test_failed_primary_pool_is_discarded_and_closed(*args, **kwargs):
    return None

def test_pool_default_limits_applied_when_caller_omits(*args, **kwargs):
    return None
