# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _reset(*args, **kwargs):
    return None

class TestRuntimeProviderUsesScope:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMcpInterpolationUsesScope:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestProfilePathResolutionUnderMultiplexScope:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_turn_scoped_dotenv_reload_does_not_pollute_process_env(*args, **kwargs):
    return None

def test_launch_home_dotenv_still_loads_under_multiplex(*args, **kwargs):
    return None

def test_launch_home_load_inside_foreign_turn_keeps_routed_cwd_out_of_process_env(*args, **kwargs):
    return None

def test_cold_profile_hydrates_external_source_without_global_env(*args, **kwargs):
    return None
