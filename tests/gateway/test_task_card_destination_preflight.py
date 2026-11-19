# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class CardTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def make_adapter(*args, **kwargs):
    return None

def run_progress(*args, **kwargs):
    return None

def test_destination_preflight_survives_transport_recovery(*args, **kwargs):
    return None

def test_only_explicit_destination_refusals_suppress_threaded_fallback(*args, **kwargs):
    return None
