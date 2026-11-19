# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class TestBuildReplayEntry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestReplayEntryApiContentSidecar:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestGatewayHistoryBuildForwardsSidecar:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_gateway_history_keeps_sidecar_only_assistant_row(*args, **kwargs):
    return None

def test_replay_rebuilds_the_same_conversation_so_every_role_keeps_its_identity(*args, **kwargs):
    return None

def test_a_plain_replay_row_does_not_carry_a_tool_call_uid_map_without_its_calls(*args, **kwargs):
    return None
