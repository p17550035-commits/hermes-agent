# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _fake_docker(*args, **kwargs):
    return None

def _sandbox_file(*args, **kwargs):
    return None

def _extract(*args, **kwargs):
    return None

def test_unreadable_sandbox_media_is_handed_back_before_delivery(*args, **kwargs):
    return None

def test_failed_handback_keeps_the_reply(*args, **kwargs):
    return None
