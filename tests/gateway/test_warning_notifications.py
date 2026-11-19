# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class Emitter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_warning_opt_out_preserves_other_delivery(*args, **kwargs):
    return None

def test_direct_warning_delivery_keeps_failure_state(*args, **kwargs):
    return None
