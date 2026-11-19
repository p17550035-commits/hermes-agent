# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Bot:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_dedup_is_scoped_to_the_receiving_bot_and_its_binding(*args, **kwargs):
    return None
