# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _notify_socket(*args, **kwargs):
    return None

def notify(*args, **kwargs):
    return None

def extend_start_timeout(*args, **kwargs):
    return None

def watchdog_interval_seconds(*args, **kwargs):
    return None

class SystemdWatchdog:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
