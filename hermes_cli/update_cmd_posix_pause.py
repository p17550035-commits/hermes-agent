# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_STOP_TIMEOUT_S = None

_READY_TIMEOUT_S = None

class PauseRefused:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class StopUnsettled:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _empty_token(*args, **kwargs):
    return None

def arm_pause(*args, **kwargs):
    return None

def gateways_paused(*args, **kwargs):
    return None

def _unit_cgroup(*args, **kwargs):
    return None

def _pid_cgroup(*args, **kwargs):
    return None

def _inside(*args, **kwargs):
    return None

def _discover_systemd(*args, **kwargs):
    return None

def _discover_launchd(*args, **kwargs):
    return None

def _home_of(*args, **kwargs):
    return None

def _supervisor_markers(*args, **kwargs):
    return None

def _respawning_service(*args, **kwargs):
    return None

def _discover_bare(*args, **kwargs):
    return None

def _ppid(*args, **kwargs):
    return None

def _escape_cgroup(*args, **kwargs):
    return None

def _left_running(*args, **kwargs):
    return None

def _manage_cmd(*args, **kwargs):
    return None

def _scope_cmd(*args, **kwargs):
    return None

def _stop_unit(*args, **kwargs):
    return None

def unit_stop_pending(*args, **kwargs):
    return None

def _start_unit(*args, **kwargs):
    return None

def _stop_job(*args, **kwargs):
    return None

def _start_job(*args, **kwargs):
    return None

def _alive(*args, **kwargs):
    return None

def _wait_gone(*args, **kwargs):
    return None

def _ask_to_drain(*args, **kwargs):
    return None

def _stop_at_once(*args, **kwargs):
    return None

def _drain_budget(*args, **kwargs):
    return None

def _stop_gateways(*args, **kwargs):
    return None

def _leave_running(*args, **kwargs):
    return None

def _disarm(*args, **kwargs):
    return None

def _names(*args, **kwargs):
    return None

def _gateway_on_home(*args, **kwargs):
    return None

def _replay_env(*args, **kwargs):
    return None

def _bare_replay_env(*args, **kwargs):
    return None

def _relaunch_bare(*args, **kwargs):
    return None

def _describe(*args, **kwargs):
    return None

def pause_at_commit_point(*args, **kwargs):
    return None

def _pause(*args, **kwargs):
    return None

def _abort_unsettled(*args, **kwargs):
    return None

def resume_paused_set(*args, **kwargs):
    return None

def left_pending(*args, **kwargs):
    return None

def is_left_pending(*args, **kwargs):
    return None

def adopt_left_pending(*args, **kwargs):
    return None

def already_restarted(*args, **kwargs):
    return None
