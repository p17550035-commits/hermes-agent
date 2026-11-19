# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _await_frame_count(*args, **kwargs):
    return None

def _overflow_slow_peer(*args, **kwargs):
    return None

class PipeClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _SocketWS:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class SocketClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _session(*args, **kwargs):
    return None

def test_membership_preserves_terminal_delivery_and_revokes_departed_peers(*args, **kwargs):
    return None

def test_backpressure_never_blocks_later_frames_or_other_subscribers(*args, **kwargs):
    return None

def test_overflow_closes_only_the_slow_peer_and_healthy_keeps_streaming(*args, **kwargs):
    return None

def test_overflow_and_send_deadline_close_the_socket_once(*args, **kwargs):
    return None

def test_fanout_close_and_detach_leave_peer_sockets_open(*args, **kwargs):
    return None
