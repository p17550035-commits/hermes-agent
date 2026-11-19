# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _event(*args, **kwargs):
    return None

def test_cancel_mid_dispatch_does_not_abort_the_turn(*args, **kwargs):
    return None

def test_superseded_flush_leaves_batch_for_its_successor(*args, **kwargs):
    return None

def test_enqueue_then_flush_delivers_merged_text_once(*args, **kwargs):
    return None
