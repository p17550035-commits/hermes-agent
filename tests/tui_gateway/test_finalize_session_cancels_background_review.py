# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_session(*args, **kwargs):
    return None

def _agent_with_live_review_fork(*args, **kwargs):
    return None

class TestFinalizeSessionCancelsBackgroundReview:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
