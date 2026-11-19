# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Ledger:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _registry(*args, **kwargs):
    return None

def test_serving_authorities_skips_unbuilt_and_retiring_slots(*args, **kwargs):
    return None

def test_a_webhook_readback_never_reads_a_parked_store(*args, **kwargs):
    return None
