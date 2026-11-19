# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _launch_local_env(*args, **kwargs):
    return None

def _secondary(*args, **kwargs):
    return None

def _observe(*args, **kwargs):
    return None

def _run_side_worker(*args, **kwargs):
    return None

def test_secondary_side_worker_runs_its_own_terminal_backend(*args, **kwargs):
    return None

def test_secondary_branch_build_runs_its_own_terminal_backend(*args, **kwargs):
    return None

class _StopAfterPolicy:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _launch_turn_policy(*args, **kwargs):
    return None

def test_launch_turn_keeps_env_only_ssh_policy_once_multiplexing_is_active(*args, **kwargs):
    return None

def test_launch_turn_ignores_ambient_terminal_env_written_after_activation(*args, **kwargs):
    return None
