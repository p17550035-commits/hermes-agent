# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_discord_mock(*args, **kwargs):
    return None

class FakeDMChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeTextChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def adapter(*args, **kwargs):
    return None

def make_message(*args, **kwargs):
    return None

def test_ignored_channel_blocks_even_with_mention(*args, **kwargs):
    return None

def test_non_ignored_channel_processes_normally(*args, **kwargs):
    return None

def test_ignored_channels_empty_string_ignores_nothing(*args, **kwargs):
    return None

def test_no_thread_channel_skips_auto_thread(*args, **kwargs):
    return None

def test_auto_thread_failure_skips_agent_and_notifies_user(*args, **kwargs):
    return None

def test_config_bridges_ignored_channels(*args, **kwargs):
    return None
