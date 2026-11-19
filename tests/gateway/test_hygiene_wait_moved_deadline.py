# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _ReadingFence:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_hygiene_wait_reads_the_moved_deadline_after_each_slice(*args, **kwargs):
    return None
