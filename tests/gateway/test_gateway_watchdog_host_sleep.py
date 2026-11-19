# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

TIMEOUT_S = None

SLEEP_S = None

class _Clock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def clock(*args, **kwargs):
    return None

class _ScriptedAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _resume_then_idle_steps(*args, **kwargs):
    return None

def test_turn_watchdog_thread_ignores_host_sleep(*args, **kwargs):
    return None

def test_turn_poll_loop_ignores_host_sleep(*args, **kwargs):
    return None

def test_stale_agent_eviction_ignores_host_sleep(*args, **kwargs):
    return None

def test_stale_agent_eviction_drops_sleep_credit_once_the_agent_was_active_again(*args, **kwargs):
    return None
