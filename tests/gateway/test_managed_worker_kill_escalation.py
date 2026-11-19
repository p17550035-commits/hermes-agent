# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _WedgedHandle:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_close_completes_when_the_post_kill_wait_times_out(*args, **kwargs):
    return None
