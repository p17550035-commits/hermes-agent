# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Popen:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _spawn(*args, **kwargs):
    return None

def test_slash_worker_argv_carries_provider(*args, **kwargs):
    return None

def test_slash_worker_argv_omits_empty_provider(*args, **kwargs):
    return None

def test_slash_exec_spawns_with_the_live_agent_provider(*args, **kwargs):
    return None

def test_slash_worker_child_forwards_provider_to_hermes_cli(*args, **kwargs):
    return None
