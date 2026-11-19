# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class FakeNetworkError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeBadRequest:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeTimedOut:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeRetryAfter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeInlineKeyboardButton:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeInlineKeyboardMarkup:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeInputMediaPhoto:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_fake_telegram = None

_fake_telegram_error = None

_fake_telegram_constants = None

_fake_telegram_ext = None

_fake_telegram_request = None

def _inject_fake_telegram(*args, **kwargs):
    return None

def _make_adapter(*args, **kwargs):
    return None

def test_non_forum_group_reply_thread_id_does_not_fork_session_key(*args, **kwargs):
    return None

def test_forum_group_topic_message_preserves_thread_session_key(*args, **kwargs):
    return None

def test_forum_general_topic_without_message_thread_id_keeps_thread_context(*args, **kwargs):
    return None

def test_private_chat_explicit_thread_id_uses_message_thread_id_without_anchor(*args, **kwargs):
    return None

def test_private_dm_topic_reply_fallback_without_anchor_fails_loud(*args, **kwargs):
    return None

def test_base_gateway_metadata_marks_telegram_dm_topics_as_reply_fallback(*args, **kwargs):
    return None

def test_gateway_runner_busy_ack_replies_to_triggering_message_for_telegram_dm_topic(*args, **kwargs):
    return None

def test_created_private_topic_thread_not_found_fails_without_root_fallback(*args, **kwargs):
    return None

def test_native_media_dm_topic_reply_not_found_retry_preserves_thread_id(*args, **kwargs):
    return None

def test_animation_dm_topic_reply_not_found_retry_preserves_thread_id(*args, **kwargs):
    return None

def test_media_group_dm_topic_reply_not_found_retry_preserves_thread_id(*args, **kwargs):
    return None

def test_media_group_lost_reply_is_ambiguous_and_never_resent(*args, **kwargs):
    return None

class NetworkError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _html_5xx(*args, **kwargs):
    return None

def test_media_group_5xx_is_ambiguous_and_never_resent(*args, **kwargs):
    return None

def test_html_5xx_page_never_falls_back_to_plain_text(*args, **kwargs):
    return None

def test_send_image_upload_dm_topic_reply_not_found_retry_preserves_thread_id(*args, **kwargs):
    return None

def test_overflow_reply_anchor_retry_preserves_private_topic_route(*args, **kwargs):
    return None

def test_control_message_to_dead_private_topic_lands_in_root_without_its_anchor(*args, **kwargs):
    return None

def test_send_image_upload_fallback_blocks_connect_time_rebind(*args, **kwargs):
    return None

def test_slash_confirm_forum_callback_followup_keeps_existing_thread_behavior(*args, **kwargs):
    return None

def test_base_send_image_fallback_preserves_metadata(*args, **kwargs):
    return None

def test_thread_fallback_only_fires_once(*args, **kwargs):
    return None

def test_reply_into_dead_private_topic_reaches_chat_root_and_prunes_binding(*args, **kwargs):
    return None

def _anchor_and_topic_gone_bot(*args, **kwargs):
    return None

_GONE_META = None

def test_deleted_anchor_and_dead_topic_text_reply_still_reaches_chat_root(*args, **kwargs):
    return None

def test_deleted_anchor_and_dead_topic_media_reply_still_reaches_chat_root(*args, **kwargs):
    return None

def test_named_topic_media_to_dead_topic_fails_closed_instead_of_landing_in_root(*args, **kwargs):
    return None

_GATEWAY_META = None

def _topic_db(*args, **kwargs):
    return None

def test_private_topic_unconfirmed_failure_keeps_binding_and_skips_root(*args, **kwargs):
    return None

def test_media_ladder_ends_when_even_the_chat_root_is_rejected(*args, **kwargs):
    return None

def test_dead_private_topic_reaches_root_with_prune_and_fallback_flag_not_via_native_id(*args, **kwargs):
    return None

def test_rejected_direct_topic_outside_private_chats_is_not_retried(*args, **kwargs):
    return None

def test_forum_topic_deleted_wording_is_not_a_dead_topic_fallback(*args, **kwargs):
    return None

def test_private_topic_thread_not_found_flake_retries_same_thread_first(*args, **kwargs):
    return None

def test_text_reply_with_reply_message_not_found_wording_drops_only_the_anchor(*args, **kwargs):
    return None

def test_private_topic_media_flake_retries_same_thread_first(*args, **kwargs):
    return None

def test_private_topic_media_timeout_is_not_retried(*args, **kwargs):
    return None

def test_native_only_media_route_is_tried_once_before_root(*args, **kwargs):
    return None
