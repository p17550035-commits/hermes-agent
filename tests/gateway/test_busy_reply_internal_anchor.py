# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

WAKE_ID = None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _runner(*args, **kwargs):
    return None

def test_busy_reply_to_an_internal_wake_is_unanchored(*args, **kwargs):
    return None

def test_busy_reply_to_a_human_message_still_anchors(*args, **kwargs):
    return None
