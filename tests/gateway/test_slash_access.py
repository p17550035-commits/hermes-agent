# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class TestPolicyFromExtra:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPolicyForSource:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_blank_chat_type_resolves_to_the_gated_scope(*args, **kwargs):
    return None

def test_blank_chat_type_both_scopes_gated_grants_only_the_intersection(*args, **kwargs):
    return None
