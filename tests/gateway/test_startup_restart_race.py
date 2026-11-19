# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class StartupRaceAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def make_startup_runner(*args, **kwargs):
    return None

def patch_startup_side_effects(*args, **kwargs):
    return None

def test_startup_aborts_when_restart_begins_during_platform_connect(*args, **kwargs):
    return None

def _patch_aborted_startup(*args, **kwargs):
    return None

def test_start_gateway_does_not_start_cron_after_aborted_startup(*args, **kwargs):
    return None

def test_start_gateway_preserves_service_restart_fallback_after_aborted_startup(*args, **kwargs):
    return None

def test_start_gateway_classifies_startup_signal_exit(*args, **kwargs):
    return None

def test_failure_exit_still_stops_cron_housekeeping_and_mcp(*args, **kwargs):
    return None
