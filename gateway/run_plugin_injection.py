# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_PLUGIN_PRODUCER = None

def _plugin_admission(*args, **kwargs):
    return None

def admission_turn_scope(*args, **kwargs):
    return None

def _waiting_turn(*args, **kwargs):
    return None

def wake_background_wait(*args, **kwargs):
    return None

def _wake_if_person_queued(*args, **kwargs):
    return None

def _log_wake_failure(*args, **kwargs):
    return None

def person_input_joined_turn(*args, **kwargs):
    return None

def _wait_pending(*args, **kwargs):
    return None

def _wake_joined_turn(*args, **kwargs):
    return None

class GatewayPluginInjectionMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
