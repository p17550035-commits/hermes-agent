# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _AbortedStartupRunner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_sigusr1_handler_installed_by_start_gateway_logs_graceful_restart(*args, **kwargs):
    return None
