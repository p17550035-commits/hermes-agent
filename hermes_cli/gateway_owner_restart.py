# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

OWNER_RESTART_REASONS = None

_TRANSIENT_OWNER_STATES = None

_RESTART_CONTROL_REASONS = None

def owner_restarting(*args, **kwargs):
    return None

def restartable(*args, **kwargs):
    return None

def _transport_lost(*args, **kwargs):
    return None

class SuccessorWaitStopped:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def restart_wait_budget(*args, **kwargs):
    return None

def wait_for_successor(*args, **kwargs):
    return None

def _fresh_connection(*args, **kwargs):
    return None

def _announce(*args, **kwargs):
    return None

def through_owner_restart(*args, **kwargs):
    return None

def exit_on_stopped_wait(*args, **kwargs):
    return None
