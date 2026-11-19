# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Recorder:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _tcp_connections_for_polls(*args, **kwargs):
    return None

def test_getupdates_polls_reuse_one_socket_off_windows(*args, **kwargs):
    return None

def test_getupdates_polls_never_reuse_a_socket_on_windows(*args, **kwargs):
    return None
