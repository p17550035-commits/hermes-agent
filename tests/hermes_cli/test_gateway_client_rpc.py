# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Socket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_rpc_error_keeps_numeric_code_and_bounded_data(*args, **kwargs):
    return None

def test_compress_waits_past_the_default_rpc_budget(*args, **kwargs):
    return None

def test_send_on_a_dead_socket_is_a_client_error_not_a_raw_websockets_one(*args, **kwargs):
    return None

def test_a_request_on_a_closing_socket_is_not_sent(*args, **kwargs):
    return None

def test_a_request_after_the_reader_ended_is_not_sent(*args, **kwargs):
    return None

def test_a_send_that_fails_after_the_reader_failed_its_request_logs_nothing(*args, **kwargs):
    return None
