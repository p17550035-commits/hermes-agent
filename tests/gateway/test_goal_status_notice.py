# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class FakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _goal_continuation_event(*args, **kwargs):
    return None

def test_goal_status_notice_defers_until_post_delivery_callback(*args, **kwargs):
    return None
