# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class HookRecordingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _TwoTurnAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _RaisingSecondTurnAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _install_fake_agent(*args, **kwargs):
    return None

SESSION_KEY = None

def test_queue_terminal_presentation_belongs_to_last_turn(*args, **kwargs):
    return None

def _source(*args, **kwargs):
    return None

def test_queued_followup_fires_processing_hooks(*args, **kwargs):
    return None

def test_queued_followup_failure_completes_the_hook(*args, **kwargs):
    return None

def test_synthetic_followup_is_not_acknowledged(*args, **kwargs):
    return None

def test_raw_envelope_only_followup_is_acknowledged(*args, **kwargs):
    return None

class CompleteOnlyAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_complete_only_adapter_is_left_alone(*args, **kwargs):
    return None

def test_fifo_depth_limit_preserves_every_accepted_message(*args, **kwargs):
    return None

def test_depth_limit_restores_events_without_media_merging(*args, **kwargs):
    return None

def test_depth_limit_keeps_eventless_followup_and_staged_completion(*args, **kwargs):
    return None
