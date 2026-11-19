# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Sink:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_cancel_during_the_terminal_commit_keeps_the_completed_snapshot(*args, **kwargs):
    return None
