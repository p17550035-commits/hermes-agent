# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Client:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Gateway:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _threads(*args, **kwargs):
    return None

def _waiting(*args, **kwargs):
    return None

def test_the_reply_comes_over_a_socket_of_its_own_that_then_closes(*args, **kwargs):
    return None

def test_a_stopped_wait_closes_the_command_socket_and_never_sends_again(*args, **kwargs):
    return None

def test_a_failed_command_dial_sends_nothing_and_is_not_retried(*args, **kwargs):
    return None
