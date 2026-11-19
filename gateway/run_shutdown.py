# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

def _exit_with_failure_verdict(*args, **kwargs):
    return None

def _resolve_gateway_exit_verdict(*args, **kwargs):
    return None

_WINDOWS_RESTART_WATCHER = None

def _log_suppressed(*args, **kwargs):
    return None

def _send_failed(*args, **kwargs):
    return None

def _send_error(*args, **kwargs):
    return None

def _notice_target_key(*args, **kwargs):
    return None

def _delivery_target_key(*args, **kwargs):
    return None

def _effective_watchdog_leash(*args, **kwargs):
    return None

def _active_async_delegation_count(*args, **kwargs):
    return None

class GatewayShutdownMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
