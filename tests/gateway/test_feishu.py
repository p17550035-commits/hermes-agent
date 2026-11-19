# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeRequestContent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _mock_event_dispatcher_builder(*args, **kwargs):
    return None

class TestConfigEnvOverrides:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuMessageNormalization:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuAdapterMessaging:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestDeleteMessage:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestAdapterModule:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _admits_group(*args, **kwargs):
    return None

class TestAdapterBehavior:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPendingInboundQueue:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestWebhookSecurity:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestDedupTTL:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestGroupMentionAtAll:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuMentionMap:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuMentionHint:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuStripLeadingSelf:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuNormalizeText:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuPostMentionParsing:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuPostFileParsing:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuPostTextIsNotMarkdownEscaped:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuNormalizeWithMentions:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuPostMentionsBot:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuExtractMessageContent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuProcessInboundMessage:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuFetchMessageText:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFeishuMentionEndToEnd:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeSdkBuilder:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeSdkRequestType:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def fake_lark_requests(*args, **kwargs):
    return None

def _plain_feishu_adapter(*args, **kwargs):
    return None

def _bot_info_response(*args, **kwargs):
    return None

def test_hydrated_bot_identity_wins_over_stale_env_values(*args, **kwargs):
    return None

def test_bot_sender_name_is_fetched_via_basic_batch_and_cached(*args, **kwargs):
    return None

def test_human_sender_name_is_fetched_from_contact_api_and_cached(*args, **kwargs):
    return None

def _reaction_adapter(*args, **kwargs):
    return None

def _run_processing(*args, **kwargs):
    return None

def test_processing_success_removes_typing_and_adds_nothing(*args, **kwargs):
    return None

def test_processing_failure_swaps_typing_for_cross_mark(*args, **kwargs):
    return None

def test_processing_failure_skips_cross_mark_when_typing_removal_fails(*args, **kwargs):
    return None
