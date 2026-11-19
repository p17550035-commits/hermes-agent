# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_TIER_FROM_RUNNER = None

def _resolve_policy_agent_runtime(*args, **kwargs):
    return None

def _recover_or_remember_model(*args, **kwargs):
    return None

def _managed_oauth_env_host(*args, **kwargs):
    return None

def _session_override_uses_managed_oauth(*args, **kwargs):
    return None

def _resolve_session_override_runtime(*args, **kwargs):
    return None

def _log_missing_session_override(*args, **kwargs):
    return None

def _session_override_snapshot(*args, **kwargs):
    return None

def _resolve_channel_runtime(*args, **kwargs):
    return None

class GatewayTurnPrepareMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
