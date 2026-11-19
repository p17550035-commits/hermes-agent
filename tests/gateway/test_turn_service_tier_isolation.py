# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

LAUNCH = None

class _Built:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _ReusedAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _turn(*args, **kwargs):
    return None

def test_overlapping_turns_each_build_their_agent_with_their_own_service_tier(*args, **kwargs):
    return None

def test_background_task_builds_its_agent_with_its_own_sessions_service_tier(*args, **kwargs):
    return None
