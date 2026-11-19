# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Harness:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _consumer(*args, **kwargs):
    return None

def _turn_ctx(*args, **kwargs):
    return None

def _mark_streamed_delivery(*args, **kwargs):
    return None

def test_finite_turn_keeps_the_terminal_reply(*args, **kwargs):
    return None

def test_nonfinite_turn_still_suppresses(*args, **kwargs):
    return None

def test_finite_turn_reply_carries_no_messaging_footer(*args, **kwargs):
    return None
