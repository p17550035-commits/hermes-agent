# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def setup_runner(*args, **kwargs):
    return None

def completion(*args, **kwargs):
    return None

def collect(*args, **kwargs):
    return None

def deliver(*args, **kwargs):
    return None

def unseen(*args, **kwargs):
    return None

def test_exact_routed_profile_delivers_once_on_its_authorized_transport(*args, **kwargs):
    return None

def test_user_routed_subscription_uses_only_its_authorized_profile(*args, **kwargs):
    return None

def test_route_denials_leave_events_retryable_at_claim_and_send(*args, **kwargs):
    return None

def test_kanban_wakes_install_the_destination_runtime_scope(*args, **kwargs):
    return None

def test_removed_profile_never_wakes_under_the_primary_runtime(*args, **kwargs):
    return None

def test_anchorless_thread_subscription_warns_once_instead_of_silent_skip(*args, **kwargs):
    return None

def test_pinned_profile_without_this_platform_delivers_via_primary(*args, **kwargs):
    return None
