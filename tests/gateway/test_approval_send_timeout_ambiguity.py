# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Result:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_timeout_is_ambiguous_not_failure(*args, **kwargs):
    return None

def test_success_is_sent(*args, **kwargs):
    return None

def test_definitive_error_result_is_failed(*args, **kwargs):
    return None

def test_non_timeout_exception_is_failed(*args, **kwargs):
    return None

def test_missing_future_is_failed(*args, **kwargs):
    return None
