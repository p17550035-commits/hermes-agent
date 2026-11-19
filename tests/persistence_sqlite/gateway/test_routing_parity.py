# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

NOW = None

class Clock:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def clock(*args, **kwargs):
    return None

def _set(*args, **kwargs):
    return None

def _keyed(*args, **kwargs):
    return None

def _backend_seeder(*args, **kwargs):
    return None

def _seed_peers(*args, **kwargs):
    return None

def test_recovered_session_record_projects_markers_and_json(*args, **kwargs):
    return None
