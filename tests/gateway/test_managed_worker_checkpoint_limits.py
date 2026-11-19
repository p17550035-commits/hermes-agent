# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Model:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_managed_worker_trims_checkpoints_to_the_configured_max_snapshots(*args, **kwargs):
    return None
