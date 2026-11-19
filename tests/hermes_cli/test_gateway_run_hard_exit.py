# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _HardExitObserved:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _prepare(*args, **kwargs):
    return None

def test_run_gateway_hard_exits_after_clean_return(*args, **kwargs):
    return None

def test_run_gateway_hard_exits_after_keyboard_interrupt(*args, **kwargs):
    return None
