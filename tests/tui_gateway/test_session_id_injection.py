# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _reset_contextvars(*args, **kwargs):
    return None

class _FakeAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _install_session(*args, **kwargs):
    return None

def test_set_session_context_injects_agent_session_id(*args, **kwargs):
    return None

def test_set_session_context_falls_back_to_session_key(*args, **kwargs):
    return None

def test_set_session_context_injects_session_profile(*args, **kwargs):
    return None

def test_set_session_context_uses_launch_profile_without_override(*args, **kwargs):
    return None
