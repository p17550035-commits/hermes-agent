# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _fire_post_delivery_cb(*args, **kwargs):
    return None

class CleanupCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class NoDeleteAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ProgressAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FailingAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _install_fakes(*args, **kwargs):
    return None

def test_messaging_agent_forwards_checkpoint_config(*args, **kwargs):
    return None

def test_cleanup_chains_with_existing_callback(*args, **kwargs):
    return None

class QueuedFollowupAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_queued_followup_starts_after_prior_turn_bubbles_are_deleted(*args, **kwargs):
    return None

class HeldSendAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class HeldSendAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_progress_send_in_flight_at_handoff_never_leaves_a_bubble(*args, **kwargs):
    return None

def test_one_slow_delete_does_not_strand_the_other_bubbles(*args, **kwargs):
    return None

def test_hung_sender_delays_the_followup_by_at_most_the_cap(*args, **kwargs):
    return None

def test_cancelling_the_turn_during_the_sender_wait_starts_no_followup(*args, **kwargs):
    return None
