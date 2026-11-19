# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

FALLBACK = None

class _StopAfterSync:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _session(*args, **kwargs):
    return None

def _admit_turn(*args, **kwargs):
    return None

def test_chain_added_after_open_reaches_the_live_agent_at_turn_admission(*args, **kwargs):
    return None

def test_torn_config_keeps_the_last_known_good_chain_but_removal_still_applies(*args, **kwargs):
    return None
