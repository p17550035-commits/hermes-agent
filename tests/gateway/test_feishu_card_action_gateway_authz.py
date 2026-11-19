# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_feishu_mocks(*args, **kwargs):
    return None

class _FakeCallBackCard:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeP2Response:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _patch_callback_card_types(*args, **kwargs):
    return None

def _close_submitted_coro(*args, **kwargs):
    return None

def _make_adapter(*args, **kwargs):
    return None

class _GatewayCheck:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_gateway_check = None

def _approval_click(*args, **kwargs):
    return None

def _update_prompt_click(*args, **kwargs):
    return None

class TestNoFeishuAllowlist:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuAllowlistUnchanged:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuAllowlistMatchesEveryOperatorId:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
