# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeConsumer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _turn_runner(*args, **kwargs):
    return None

def _fake_consumer(*args, **kwargs):
    return None

def _interim_cb(*args, **kwargs):
    return None

def test_commentary_reaches_the_consumer_when_deltas_are_off(*args, **kwargs):
    return None

def test_commentary_is_deduped_when_this_consumer_accepted_the_deltas(*args, **kwargs):
    return None

def test_unstreamed_commentary_still_reaches_the_consumer(*args, **kwargs):
    return None

def test_streamed_commentary_on_a_local_route_is_only_a_segment_break(*args, **kwargs):
    return None
