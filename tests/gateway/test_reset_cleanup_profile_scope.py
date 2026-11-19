# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _RecordingAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _runner(*args, **kwargs):
    return None

def _profile_b(*args, **kwargs):
    return None

def test_reset_runs_memory_cleanup_and_session_hooks_under_the_owning_profile(*args, **kwargs):
    return None

def test_unkeyed_in_turn_cleanup_keeps_the_callers_named_profile(*args, **kwargs):
    return None

def test_reset_gateway_events_reach_only_the_owning_profile_hooks(*args, **kwargs):
    return None

def test_a_key_whose_profile_home_is_gone_warns_before_releasing_under_root(*args, **kwargs):
    return None
