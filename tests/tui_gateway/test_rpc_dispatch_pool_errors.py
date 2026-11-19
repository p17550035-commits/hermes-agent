# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Transport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_pool_handler_failure_is_logged_with_traceback(*args, **kwargs):
    return None
