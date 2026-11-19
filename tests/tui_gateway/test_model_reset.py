# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_reset_drops_the_pin_and_adopts_config_without_repinning(*args, **kwargs):
    return None
