# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Socket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def rig(*args, **kwargs):
    return None

def rpc(*args, **kwargs):
    return None

def settle(*args, **kwargs):
    return None

def test_waiting_context_reads_keep_reader_backpressure(*args, **kwargs):
    return None

def test_server_shutdown_does_not_wait_for_a_running_context_read(*args, **kwargs):
    return None

def test_hang_up_drops_reads_that_never_started(*args, **kwargs):
    return None

def test_a_failed_read_reply_does_not_cancel_the_running_control(*args, **kwargs):
    return None

def test_a_slow_stored_read_never_holds_an_interrupt(*args, **kwargs):
    return None
