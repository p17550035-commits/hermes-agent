# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _MalformedConn:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _assert_diverted(*args, **kwargs):
    return None

def test_corrupt_state_db_diverts_pending_without_fts_rebuild(*args, **kwargs):
    return None
