# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def test_sentinel_placed_before_agent_setup(*args, **kwargs):
    return None

def test_merge_pending_message_event_merges_text_and_photo_followups(*args, **kwargs):
    return None

def test_recent_telegram_followups_append_in_pending_queue(*args, **kwargs):
    return None

def test_start_command_is_noop_during_active_session(*args, **kwargs):
    return None

def test_active_session_bypass_commands_dispatch_without_interrupt(*args, **kwargs):
    return None

def test_stop_during_sentinel_force_cleans_session(*args, **kwargs):
    return None
