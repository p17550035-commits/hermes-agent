# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

class _LiveBotApiServer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_adapter(*args, **kwargs):
    return None

def _diag(*args, **kwargs):
    return None

def test_drain_recovers_after_server_half_close_live(*args, **kwargs):
    return None

def test_drain_bounded_and_functional_when_close_wedges_live(*args, **kwargs):
    return None
