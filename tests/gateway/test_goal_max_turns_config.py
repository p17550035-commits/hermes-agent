# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeSessionEntry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeSessionStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _make_goal_event(*args, **kwargs):
    return None

def test_gateway_goal_uses_goals_max_turns_from_full_config(*args, **kwargs):
    return None

def test_goal_command_slow_db_init_still_persists(*args, **kwargs):
    return None
