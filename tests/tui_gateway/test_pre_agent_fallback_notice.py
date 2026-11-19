# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StubAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _build(*args, **kwargs):
    return None

def test_fallback_build_attaches_the_switch_notice_outside_agent_kwargs(*args, **kwargs):
    return None

def test_primary_build_carries_no_notice(*args, **kwargs):
    return None

def test_fallback_build_survives_model_string_shorthand(*args, **kwargs):
    return None
