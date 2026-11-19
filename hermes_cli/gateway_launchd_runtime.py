# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

LABEL_PREFIX = None

_POLL_INTERVAL_S = None

def _budget(*args, **kwargs):
    return None

def _launchctl(*args, **kwargs):
    return None

class GatewayJob:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _remove_finished_jobs(*args, **kwargs):
    return None

def start_gateway_job(*args, **kwargs):
    return None
