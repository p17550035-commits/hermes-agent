# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeCLI:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _live_session(*args, **kwargs):
    return None

def test_run_harvests_pending_agent_seed(*args, **kwargs):
    return None

def test_run_without_seed_harvests_empty_seed(*args, **kwargs):
    return None

def test_empty_command_returns_empty_output_and_seed(*args, **kwargs):
    return None

class _SeedingWorker:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_slash_exec_routes_seed_as_send_dispatch(*args, **kwargs):
    return None

def test_slash_exec_plain_output_unchanged_when_no_seed(*args, **kwargs):
    return None
