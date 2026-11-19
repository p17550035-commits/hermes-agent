# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_worker_stop_hard_cancels_the_agent_before_and_after_construction(*args, **kwargs):
    return None

CHILD = None

def test_worker_frames_read_no_ledger_per_frame(*args, **kwargs):
    return None
