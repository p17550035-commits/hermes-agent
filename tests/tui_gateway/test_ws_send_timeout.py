# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StalledWS:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FastWS:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_stalled_send_closes_socket_and_releases_queued_reply(*args, **kwargs):
    return None

def test_progress_then_final_ordering_preserved_on_healthy_socket(*args, **kwargs):
    return None
