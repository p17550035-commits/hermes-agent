# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

class GatewayPluginRewireMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def reload_plugins_verb(*args, **kwargs):
    return None

_MCP_CONNECT_WAIT_S = None

def _reconcile_plugin_mcp_servers(*args, **kwargs):
    return None

def _count_adapters(*args, **kwargs):
    return None
