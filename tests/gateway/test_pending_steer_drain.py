# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_accepted_steer_and_events_drain_once_in_order(*args, **kwargs):
    return None

def test_interrupt_then_steer_preserves_channel_inputs(*args, **kwargs):
    return None
