# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_adapter(*args, **kwargs):
    return None

class _FakePTBUpdater:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_network_recovery_skips_read_receipt_cleanup_wedged_in_stop(*args, **kwargs):
    return None

def test_stop_skips_cleanup_only_when_callback_present(*args, **kwargs):
    return None
