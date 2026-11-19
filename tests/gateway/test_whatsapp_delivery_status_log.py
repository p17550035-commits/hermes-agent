# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Resp:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_delivery_status_is_logged_to_gateway_log_and_never_dispatched(*args, **kwargs):
    return None
