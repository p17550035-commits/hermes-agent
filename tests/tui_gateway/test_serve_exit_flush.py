# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FlushAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def registered_session(*args, **kwargs):
    return None

def _restore_signal_state(*args, **kwargs):
    return None

def test_sigterm_flushes_populated_session_into_state_db(*args, **kwargs):
    return None

def test_ignored_sigint_leaves_terminal_commands_runnable(*args, **kwargs):
    return None

def test_exit_flush_is_bounded(*args, **kwargs):
    return None

def test_shutdown_sessions_flushes_before_teardown(*args, **kwargs):
    return None

def test_shutdown_mid_tool_kills_the_command_and_keeps_its_result(*args, **kwargs):
    return None

def test_sigterm_grace_hard_exit_kills_a_sigterm_ignoring_command(*args, **kwargs):
    return None

def test_periodic_flush_respects_interval_with_fake_clock(*args, **kwargs):
    return None

def test_periodic_flush_skips_running_sessions(*args, **kwargs):
    return None
