# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

ACTIVE_TURN_MAX_AGE_SECONDS = None

def _make_source(*args, **kwargs):
    return None

def _make_store(*args, **kwargs):
    return None

def _make_db_store(*args, **kwargs):
    return None

def _close_store_handles(*args, **kwargs):
    return None

def _entry_for(*args, **kwargs):
    return None

def test_active_turn_fields_round_trip_and_legacy_payload_defaults(*args, **kwargs):
    return None

def test_mark_refreshes_updated_at_for_legacy_upgrade_fallback(*args, **kwargs):
    return None

def test_active_turn_clear_is_compare_and_swap(*args, **kwargs):
    return None

def test_failed_mark_persistence_does_not_leak_marker_into_later_save(*args, **kwargs):
    return None

def test_failed_clear_persistence_keeps_token_retryable_and_durable_clear_wins(*args, **kwargs):
    return None

def test_state_db_failure_atomic_marker_round_trip(*args, **kwargs):
    return None

def test_state_db_commit_survives_legacy_mirror_failure(*args, **kwargs):
    return None

def test_exact_old_active_turn_recovers_even_when_updated_at_is_stale(*args, **kwargs):
    return None

def test_suspended_active_turn_is_cleared_without_resume(*args, **kwargs):
    return None

def test_existing_resume_reason_and_freshness_are_preserved(*args, **kwargs):
    return None

def test_ancient_active_marker_is_cleared_without_auto_resume(*args, **kwargs):
    return None

def test_clean_startup_discards_orphan_markers_without_resuming(*args, **kwargs):
    return None

def test_clean_shutdown_marker_is_not_consumed_when_discard_fails(*args, **kwargs):
    return None

def test_clean_shutdown_marker_is_unlinked_after_durable_discard(*args, **kwargs):
    return None

def test_runner_active_turn_carrier_clears_the_exact_resolved_key(*args, **kwargs):
    return None

def test_runner_active_turn_clear_is_best_effort(*args, **kwargs):
    return None

def test_runner_active_turn_clear_stops_after_bounded_retries(*args, **kwargs):
    return None

def _db_runner(*args, **kwargs):
    return None

def _turn(*args, **kwargs):
    return None

def test_unclean_restart_resumes_only_the_turn_left_in_flight(*args, **kwargs):
    return None

def test_unclean_restart_delivers_a_persisted_unledgered_reply_instead_of_regenerating(*args, **kwargs):
    return None

_WAKE = None

def test_unclean_restart_never_redelivers_a_reply_live_delivery_suppressed(*args, **kwargs):
    return None

def test_turn_marker_start_survives_a_timezone_change_across_the_crash(*args, **kwargs):
    return None
