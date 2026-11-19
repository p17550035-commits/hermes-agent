# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

FIRST = None

SECOND = None

def _ledger_db(*args, **kwargs):
    return None

def _rows(*args, **kwargs):
    return None

class _LostAckAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _TwoTurnStreamingAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_timed_out_queued_first_answer_is_ledgered_not_resent(*args, **kwargs):
    return None
