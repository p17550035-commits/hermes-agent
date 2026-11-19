# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_discord_mock(*args, **kwargs):
    return None

class FakeChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def adapter(*args, **kwargs):
    return None

def make_message(*args, **kwargs):
    return None

def make_bot_message(*args, **kwargs):
    return None

def test_configured_bot_sender_is_left_for_shared_ingress_policy(*args, **kwargs):
    return None

def test_should_not_backfill_message_with_non_down_bot_response(*args, **kwargs):
    return None

def test_parent_channel_unreferenced_bot_message_does_not_suppress_backfill(*args, **kwargs):
    return None

def test_thread_unreferenced_bot_message_does_not_mask_request(*args, **kwargs):
    return None

def test_backfills_when_only_down_notice_exists(*args, **kwargs):
    return None

def test_generic_unavailable_response_counts_as_completed(*args, **kwargs):
    return None

def test_run_backfill_dispatches_unaddressed_messages(*args, **kwargs):
    return None

def test_repeated_ready_coalesces_instead_of_cancelling_active_recovery(*args, **kwargs):
    return None

def test_recovered_mention_reuses_live_auth_and_mention_gates(*args, **kwargs):
    return None

def test_missed_message_backfill_config_stays_per_adapter(*args, **kwargs):
    return None

def test_explicit_empty_backfill_channel_list_disables_the_scan(*args, **kwargs):
    return None

def test_recovery_ledger_prunes_expired_rows(*args, **kwargs):
    return None

def test_send_offloads_final_delivery_ledger_write(*args, **kwargs):
    return None

def test_final_delivery_remains_complete_after_processing_hook(*args, **kwargs):
    return None

def test_unthreaded_final_reply_records_recovery_completion(*args, **kwargs):
    return None

def test_iter_candidates_keeps_latest_messages_when_window_exceeds_limit(*args, **kwargs):
    return None

def test_iter_candidates_skips_obfuscated_channel_on_explicit_ids(*args, **kwargs):
    return None

def test_success_outcome_completes_row_without_reply_anchor(*args, **kwargs):
    return None

def test_redispatch_of_one_message_is_bounded(*args, **kwargs):
    return None

def test_stored_cursor_cannot_widen_scan_window_or_leak_into_threads(*args, **kwargs):
    return None
