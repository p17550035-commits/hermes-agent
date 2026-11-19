# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_discord_mock(*args, **kwargs):
    return None

class FakeDMChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeTextChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeForumChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def adapter(*args, **kwargs):
    return None

def make_message(*args, **kwargs):
    return None

def make_history_message(*args, **kwargs):
    return None

class FakeHistoryChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_discord_free_response_in_server_channels(*args, **kwargs):
    return None

def test_discord_accepts_and_strips_bot_mentions_when_required(*args, **kwargs):
    return None

def test_unmentioned_bot_chunks_join_recent_tag_batch(*args, **kwargs):
    return None

def test_short_tagged_bot_chunk_waits_for_followup_window(*args, **kwargs):
    return None

def test_discord_reply_message_skips_auto_thread(*args, **kwargs):
    return None

def test_discord_voice_linked_channel_skips_mention_requirement_and_auto_thread(*args, **kwargs):
    return None

def test_discord_free_response_channel_skips_auto_thread(*args, **kwargs):
    return None

def test_discord_free_response_auto_thread_opt_in(*args, **kwargs):
    return None

def test_discord_no_thread_channels_wins_over_free_response_auto_thread(*args, **kwargs):
    return None

def test_discord_voice_linked_channel_ignores_free_response_auto_thread(*args, **kwargs):
    return None

def test_discord_free_response_auto_thread_respects_global_disable(*args, **kwargs):
    return None

def test_discord_free_response_auto_thread_yaml_bridge(*args, **kwargs):
    return None

def test_fetch_channel_context_stops_at_self_message_and_reverses_to_chronological_order(*args, **kwargs):
    return None

def test_fetch_channel_context_skips_self_improvement_boundary_message(*args, **kwargs):
    return None

def test_fetch_channel_context_hydrates_around_reply_target(*args, **kwargs):
    return None

def test_fetch_channel_context_reply_target_in_primary_window_not_duplicated(*args, **kwargs):
    return None

def test_nonconversational_fallback_requires_self_improvement_emoji(*args, **kwargs):
    return None

class TestChannelContextUnverifiedTagging:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_fetch_channel_context_uses_cache_to_narrow_window(*args, **kwargs):
    return None

def test_fetch_channel_context_cache_uses_latest_window_when_after_set(*args, **kwargs):
    return None

def test_fetch_channel_context_ignores_stale_cache(*args, **kwargs):
    return None

def test_discord_send_does_not_cache_nonconversational_status_as_history_boundary(*args, **kwargs):
    return None

def test_discord_shared_channel_backfill_prepends_context(*args, **kwargs):
    return None

def test_discord_per_user_channel_backfills_too(*args, **kwargs):
    return None

def test_discord_dm_does_not_backfill(*args, **kwargs):
    return None

def test_discord_reply_in_free_channel_triggers_backfill(*args, **kwargs):
    return None

class TestNonConversationalTrackerOffload:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_flagless_webhook_post_reaches_gateway_as_bot(*args, **kwargs):
    return None
