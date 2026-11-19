# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_HISTORICAL_UPDATE_FRAMES = None

def _is_historical_update_frame(*args, **kwargs):
    return None

def in_historical_update(*args, **kwargs):
    return None

def _historical_context(*args, **kwargs):
    return None

def _run_child(*args, **kwargs):
    return None

def _run_in_custody(*args, **kwargs):
    return None

def _checkout_custody(*args, **kwargs):
    return None

def stop_for_relaunch(*args, **kwargs):
    return None

class RetiredUpdaterHook:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def stop_historical_updater(*args, **kwargs):
    return None

def relaunch_stopped_serves(*args, **kwargs):
    return None
