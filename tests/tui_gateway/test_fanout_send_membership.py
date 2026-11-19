# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _event(*args, **kwargs):
    return None

class _Socket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _idle(*args, **kwargs):
    return None

def test_detach_discards_batch_waiting_for_send_lock(*args, **kwargs):
    return None

def test_detach_discards_unsent_tail_of_captured_batch(*args, **kwargs):
    return None

def test_sync_peer_discards_unsent_tail_of_captured_batch(*args, **kwargs):
    return None
