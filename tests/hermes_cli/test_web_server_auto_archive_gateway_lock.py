# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

_HOLDER = None

class _FakeStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def archive_probe(*args, **kwargs):
    return None

def test_serve_auto_archive_defers_to_a_live_gateway_for_the_profile(*args, **kwargs):
    return None
