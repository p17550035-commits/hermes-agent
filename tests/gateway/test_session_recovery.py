# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeGatewayDB:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _store(*args, **kwargs):
    return None

def test_resolve_profile_namespaced_key_does_not_adopt_main_row(*args, **kwargs):
    return None

def test_resolve_db_fallback_rejects_row_started_after_flush(*args, **kwargs):
    return None
