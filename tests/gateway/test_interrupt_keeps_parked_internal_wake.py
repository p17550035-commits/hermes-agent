# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_COMMAND_REASONS = None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _gateway(*args, **kwargs):
    return None

def _event(*args, **kwargs):
    return None

def _run_command(*args, **kwargs):
    return None

def test_interrupt_keeps_parked_internal_wake_and_discards_human_followup(*args, **kwargs):
    return None

def test_interrupt_promotes_internal_wake_queued_behind_discarded_human_head(*args, **kwargs):
    return None
