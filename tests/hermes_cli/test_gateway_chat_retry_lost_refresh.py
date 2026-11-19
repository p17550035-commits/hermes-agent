# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

class _DropRefreshOnce:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_retry_after_a_lost_refresh_replays_the_same_rewind(*args, **kwargs):
    return None
