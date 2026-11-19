# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

CHAT_ID = None

REQ_ID = None

def _gateway_suppresses_normal_send(*args, **kwargs):
    return None

def _gateway_join_and_cancel(*args, **kwargs):
    return None

def _make_real_wecom_adapter(*args, **kwargs):
    return None

def _finalize_frames_on_wire(*args, **kwargs):
    return None

def _cleanup_adapter(*args, **kwargs):
    return None

class TestTimeoutInversionDoubleSend:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_manual_ack_adapter(*args, **kwargs):
    return None

class TestOrphanQueueAckRouting:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
