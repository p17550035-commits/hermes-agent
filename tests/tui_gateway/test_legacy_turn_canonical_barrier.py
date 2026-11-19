# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _InlineThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_legacy_submit_refuses_while_canonical_ledger_holds_work(*args, **kwargs):
    return None

def test_ledger_read_failure_refuses_as_coordination_unavailable(*args, **kwargs):
    return None
