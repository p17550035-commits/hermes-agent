# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RuntimeStartError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def remaining(*args, **kwargs):
    return None

def service_suffix(*args, **kwargs):
    return None

class ExistingService:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _run(*args, **kwargs):
    return None

def _verify_binding(*args, **kwargs):
    return None

def _unverified_detail(*args, **kwargs):
    return None

def _child_failure(*args, **kwargs):
    return None

def _exists(*args, **kwargs):
    return None

def _systemd(*args, **kwargs):
    return None

def _s6(*args, **kwargs):
    return None

def _launchd(*args, **kwargs):
    return None

def _windows_task_name(*args, **kwargs):
    return None

def refresh_ready_owner_launcher(*args, **kwargs):
    return None

def _windows(*args, **kwargs):
    return None

def _no_supervisor(*args, **kwargs):
    return None

def discover_existing_gateway_service(*args, **kwargs):
    return None

def start_existing_gateway_service(*args, **kwargs):
    return None
