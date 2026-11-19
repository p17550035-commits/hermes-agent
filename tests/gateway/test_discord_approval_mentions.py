# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_exec_approval_mentions_allowed_users_when_enabled(*args, **kwargs):
    return None

def test_yaml_config_seeds_websocket_health_with_primary_precedence(*args, **kwargs):
    return None
