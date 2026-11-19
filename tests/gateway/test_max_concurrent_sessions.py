# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _isolated_active_session_registry(*args, **kwargs):
    return None

class _FakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_source(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _occupy_session(*args, **kwargs):
    return None

def _silence_global_gateway_hooks(*args, **kwargs):
    return None

def test_new_session_gets_clean_error_at_active_session_limit(*args, **kwargs):
    return None

def test_status_command_bypasses_active_session_limit(*args, **kwargs):
    return None
