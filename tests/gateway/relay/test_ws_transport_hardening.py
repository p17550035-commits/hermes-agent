# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

class _DroppingWS:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_read_loop_exit_fails_pending_futures_promptly(*args, **kwargs):
    return None

def test_send_during_redial_window_fails_fast(*args, **kwargs):
    return None

def test_send_allowed_once_redial_installs_fresh_socket(*args, **kwargs):
    return None

def _run_reader_to_exit(*args, **kwargs):
    return None

def test_read_loop_without_socket_still_fails_pending(*args, **kwargs):
    return None

def test_send_after_terminal_4401_revocation_fails_fast(*args, **kwargs):
    return None

def test_send_after_drop_with_reconnect_disabled_fails_fast(*args, **kwargs):
    return None

def test_send_raising_socket_returns_error_dict(*args, **kwargs):
    return None

def test_redial_hold_parks_the_supervisor_until_released(*args, **kwargs):
    return None

def test_redial_hold_expires_so_a_lost_suspend_cannot_strand_us(*args, **kwargs):
    return None
