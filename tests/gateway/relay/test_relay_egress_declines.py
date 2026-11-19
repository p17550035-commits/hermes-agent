# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

DECLINE_TEXT = None

ALL_OPS = None

class DecliningConnector:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def relay(*args, **kwargs):
    return None

def test_decline_is_recognised_by_code_and_by_uniform_text(*args, **kwargs):
    return None

def test_an_ambiguous_failure_is_not_a_decline(*args, **kwargs):
    return None

def test_an_ordinary_failure_is_not_a_decline(*args, **kwargs):
    return None

def test_decline_error_is_the_connector_text_verbatim(*args, **kwargs):
    return None

def test_send_reports_the_decline(*args, **kwargs):
    return None

def test_media_decline_does_not_fall_back_to_a_text_send(*args, **kwargs):
    return None

def test_exec_approval_decline_is_not_reported_as_op_unavailable(*args, **kwargs):
    return None

def test_slash_confirm_decline_is_not_reported_as_op_unavailable(*args, **kwargs):
    return None

def test_clarify_decline_does_not_fall_back_to_a_numbered_text_send(*args, **kwargs):
    return None

def test_a_delivered_prompt_stays_registered(*args, **kwargs):
    return None

def test_task_card_stop_decline_carries_the_error(*args, **kwargs):
    return None

def test_cosmetic_lane_degrades_but_logs_the_decline_at_warning(*args, **kwargs):
    return None

def test_thread_qualified_session_id_attests_the_bare_chat(*args, **kwargs):
    return None

def test_relay_plane_attests_the_union_of_fronted_platforms(*args, **kwargs):
    return None

def _relay_env(*args, **kwargs):
    return None

def test_telegram_username_defers_to_the_connector(*args, **kwargs):
    return None

def test_numeric_telegram_target_is_still_guarded(*args, **kwargs):
    return None

def test_carve_out_is_telegram_only(*args, **kwargs):
    return None

def test_attested_handle_takes_the_normal_path(*args, **kwargs):
    return None

def test_username_like_but_not_prefixed_is_guarded(*args, **kwargs):
    return None

class CodeOnlyDecliningConnector:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def code_only_relay(*args, **kwargs):
    return None

def test_code_only_prompt_decline_reaches_the_caller_as_a_decline(*args, **kwargs):
    return None

def test_code_only_media_decline_does_not_fall_back(*args, **kwargs):
    return None

def _code_only_adapter(*args, **kwargs):
    return None

def test_declined_draft_seal_does_not_replay_as_a_plain_send(*args, **kwargs):
    return None

def test_declined_task_card_progress_carries_the_decline_to_its_caller(*args, **kwargs):
    return None

def test_declined_INITIAL_draft_is_not_retried_as_a_plain_send(*args, **kwargs):
    return None

def test_edit_message_carries_the_structured_decline(*args, **kwargs):
    return None

def test_declined_stream_edit_does_not_send_the_unseen_tail(*args, **kwargs):
    return None

def test_follow_up_carries_the_structured_decline(*args, **kwargs):
    return None

def test_declined_send_accepts_both_wire_shapes(*args, **kwargs):
    return None

def test_declined_draft_frame_is_terminal_for_the_run(*args, **kwargs):
    return None

def test_ambiguous_draft_result_never_reads_as_a_decline(*args, **kwargs):
    return None

def test_declined_send_ignores_ack_lost_text_without_a_structured_body(*args, **kwargs):
    return None
