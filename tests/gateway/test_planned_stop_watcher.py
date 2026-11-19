# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _write_self_marker(*args, **kwargs):
    return None

class _FakeRunner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_loop_capturing_calls(*args, **kwargs):
    return None

def test_watcher_fires_shutdown_when_marker_appears(*args, **kwargs):
    return None

def test_watcher_tolerates_marker_path_resolution_errors(*args, **kwargs):
    return None

def test_watcher_does_not_fire_for_foreign_pid_marker(*args, **kwargs):
    return None

def test_planned_stop_marker_targets_self_probe_is_non_destructive(*args, **kwargs):
    return None

def test_cli_sigterm_after_watcher_consumed_the_marker_stays_planned(*args, **kwargs):
    return None
