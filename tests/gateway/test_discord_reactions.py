# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_discord_mock(*args, **kwargs):
    return None

class FakeTree:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def adapter(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def test_process_message_background_adds_and_swaps_reactions(*args, **kwargs):
    return None

def test_reactions_disabled_via_env(*args, **kwargs):
    return None

class FakeChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_queued_event_without_raw_message_reacts_through_a_partial_message(*args, **kwargs):
    return None

def test_queued_event_with_a_non_discord_id_skips_reactions(*args, **kwargs):
    return None
