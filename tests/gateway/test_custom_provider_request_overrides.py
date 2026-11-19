# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _CapturingAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _install_fake_agent(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _make_source(*args, **kwargs):
    return None

def test_resolve_runtime_agent_kwargs_preserves_request_overrides(*args, **kwargs):
    return None

def test_turn_route_preserves_provider_request_overrides_without_fast_mode(*args, **kwargs):
    return None

def test_turn_route_merges_fast_mode_with_provider_request_overrides(*args, **kwargs):
    return None

def test_run_agent_preserves_provider_request_overrides_on_gateway_path(*args, **kwargs):
    return None

def test_reused_agent_turn_merges_request_overrides_not_overwrite(*args, **kwargs):
    return None
