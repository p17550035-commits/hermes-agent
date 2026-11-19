# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

RICH_CONTENT = None

CJK_RICH_CONTENT = None

ASTRAL_CJK_RICH_CONTENT = None

TABLE_ONLY_CONTENT = None

DANGEROUS_DETAILS_MATH = None

EndPointNotFound = None

InvalidToken = None

PTB_ENDPOINT_NOT_FOUND = None

PTB_INVALID_TOKEN_404 = None

def _make_adapter(*args, **kwargs):
    return None

def _rich_api_kwargs(*args, **kwargs):
    return None

def test_rich_delivery_keeps_literal_hash_references(*args, **kwargs):
    return None

def test_literal_hash_normalization_preserves_markdown_regions(*args, **kwargs):
    return None

def test_literal_hash_fences_close_like_commonmark(*args, **kwargs):
    return None

def test_rich_payload_is_linear_in_unclosed_backtick_runs(*args, **kwargs):
    return None

def test_details_without_math_still_uses_rich_send(*args, **kwargs):
    return None

def test_math_outside_details_still_uses_rich_send(*args, **kwargs):
    return None

def test_astral_cjk_rich_content_skips_rich_send_to_avoid_tdesktop_garble(*args, **kwargs):
    return None

def test_cjk_rich_content_can_be_opted_in(*args, **kwargs):
    return None

def test_plain_markdown_stays_on_legacy_path(*args, **kwargs):
    return None

def test_expect_edits_metadata_keeps_preview_on_legacy_path(*args, **kwargs):
    return None

def test_oversized_content_skips_rich_and_chunks(*args, **kwargs):
    return None

def test_permanent_rich_error_falls_back_to_legacy(*args, **kwargs):
    return None

def test_unknown_endpoint_error_falls_back_to_legacy(*args, **kwargs):
    return None

def test_capability_error_latches_rich_send_off(*args, **kwargs):
    return None

def test_real_ptb_endpoint_missing_falls_back_and_latches_off(*args, **kwargs):
    return None

def test_per_message_bad_request_does_not_latch_off(*args, **kwargs):
    return None

def test_transient_rich_error_does_not_legacy_resend(*args, **kwargs):
    return None

def test_rich_transport_error_redacts_bot_token_even_when_redaction_disabled(*args, **kwargs):
    return None

def test_legacy_send_error_redacts_bot_token_without_traceback(*args, **kwargs):
    return None

def test_routing_direct_messages_topic_id_drops_message_thread_id(*args, **kwargs):
    return None

def test_cjk_rich_content_skips_rich_draft_to_avoid_tdesktop_garble(*args, **kwargs):
    return None

def test_prefers_fresh_final_streaming_stays_disabled_when_rich_enabled(*args, **kwargs):
    return None

def test_prefers_fresh_final_streaming_for_dm_topic_tables(*args, **kwargs):
    return None

def test_legacy_draft_stream_finalizes_with_persistent_rich_message(*args, **kwargs):
    return None

def test_rich_table_uses_raw_plain_draft_before_persistent_rich_final(*args, **kwargs):
    return None

def test_dm_table_stream_persists_through_send_rich_message(*args, **kwargs):
    return None

TOPIC_METADATA = None

TOPIC_TABLE = None

def test_send_draft_routes_dm_topic_thread_id_as_int(*args, **kwargs):
    return None

def test_dm_topic_table_stream_uses_send_rich_message(*args, **kwargs):
    return None

def test_dm_topic_table_survives_when_drafts_degrade_to_edit(*args, **kwargs):
    return None

def test_supports_draft_streaming_enabled_when_rich_drafts_opt_in(*args, **kwargs):
    return None

def test_supports_draft_streaming_legacy_when_rich_messages_off(*args, **kwargs):
    return None

def test_streaming_overflow_limit_none_when_rich_latched_off(*args, **kwargs):
    return None

def _rich_edit_kwargs(*args, **kwargs):
    return None

def test_finalize_edit_uses_rich_for_table_content(*args, **kwargs):
    return None

def test_finalize_edit_dm_topic_omits_send_only_routing_fields(*args, **kwargs):
    return None

def test_finalize_edit_cjk_rich_content_can_be_opted_in(*args, **kwargs):
    return None

def test_legacy_edit_error_logs_redacted_bot_token_without_traceback(*args, **kwargs):
    return None

def _reply_message(*args, **kwargs):
    return None

def _reply_message_with_rich_blocks(*args, **kwargs):
    return None

def test_rich_reply_records_and_recovers_text(*args, **kwargs):
    return None

def test_rich_reply_and_inbound_blocks_share_one_flattener(*args, **kwargs):
    return None

def test_reply_to_deeply_nested_rich_message_still_reaches_the_agent(*args, **kwargs):
    return None

def test_rich_message_filter_leaves_media_messages_to_the_media_handler(*args, **kwargs):
    return None

def test_rich_message_text_keeps_tables_details_math_links_and_custom_emoji(*args, **kwargs):
    return None

def test_rich_send_degrades_unopenable_link_targets_but_keeps_urls_and_code(*args, **kwargs):
    return None
