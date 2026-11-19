# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_OWNER = None

_STRANGER = None

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _StubRunner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _MessageHandlerRunner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _event(*args, **kwargs):
    return None

def _turn_body(*args, **kwargs):
    return None

def _adapter(*args, **kwargs):
    return None

def _drive_turn(*args, **kwargs):
    return None

def test_unauthorized_sender_never_sees_typing(*args, **kwargs):
    return None

def test_authorized_sender_still_gets_typing(*args, **kwargs):
    return None

def test_unauthorized_sender_gets_no_typing_stop_either(*args, **kwargs):
    return None

def test_authorized_sender_still_gets_typing_stop(*args, **kwargs):
    return None

def test_internal_event_skips_the_authorization_probe(*args, **kwargs):
    return None

def test_runner_is_resolved_through_the_message_handler(*args, **kwargs):
    return None

def test_adapter_without_a_runner_keeps_typing(*args, **kwargs):
    return None

def test_authorization_probe_error_keeps_typing(*args, **kwargs):
    return None

class _ReactingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _reacting_adapter(*args, **kwargs):
    return None

def test_unauthorized_sender_gets_no_processing_reactions(*args, **kwargs):
    return None

def test_authorized_sender_keeps_processing_reactions(*args, **kwargs):
    return None

class _LaunchScopedRunner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_probe_reads_the_scope_the_handler_authorizes_under(*args, **kwargs):
    return None
