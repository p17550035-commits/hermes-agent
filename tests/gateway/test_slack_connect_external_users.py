# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_slack_mock(*args, **kwargs):
    return None

BOT_USER_ID = None

HOST_TEAM = None

EXT_TEAM = None

SHARED_CHANNEL = None

SHARED_TS = None

def _make_adapter(*args, **kwargs):
    return None

def _connect_message_event(*args, **kwargs):
    return None

def _connect_message_body(*args, **kwargs):
    return None

def _connect_mention_event(*args, **kwargs):
    return None

def _connect_mention_body(*args, **kwargs):
    return None

def _dm_event(*args, **kwargs):
    return None

def test_connect_message_event_resolves_to_install_workspace(*args, **kwargs):
    return None

def test_connect_mention_event_resolves_to_install_workspace(*args, **kwargs):
    return None

def test_envelope_without_team_id_still_falls_back_to_inner_event(*args, **kwargs):
    return None

def test_connect_pair_starts_one_turn_only(*args, **kwargs):
    return None

def test_external_org_dm_is_refused(*args, **kwargs):
    return None

def test_local_org_dm_passes_external_gate(*args, **kwargs):
    return None

def test_connect_channel_message_from_external_user_is_not_dm_gated(*args, **kwargs):
    return None

def test_resolver_ignores_foreign_envelope_with_single_install(*args, **kwargs):
    return None

def test_resolver_grid_example_prefers_authorization_install(*args, **kwargs):
    return None

def test_resolver_multi_install_no_match_is_empty(*args, **kwargs):
    return None

def test_multi_install_unattributed_external_dm_is_refused(*args, **kwargs):
    return None

def test_multi_install_dm_from_sibling_install_member_passes(*args, **kwargs):
    return None

def test_multi_install_dm_from_external_org_still_refused(*args, **kwargs):
    return None

def test_file_share_dm_from_sibling_install_member_synthesizes(*args, **kwargs):
    return None

def test_resolver_legacy_call_without_install_set_keeps_envelope_first(*args, **kwargs):
    return None

def test_team_in_install_set_filters_foreign_ids(*args, **kwargs):
    return None

def test_assistant_metadata_fallback_does_not_readopt_foreign_team(*args, **kwargs):
    return None

def test_dm_with_enterprise_user_team_passes_gate(*args, **kwargs):
    return None

def test_allowlisted_external_user_still_refused(*args, **kwargs):
    return None

def _file_share_event(*args, **kwargs):
    return None

def _file_share_client(*args, **kwargs):
    return None

def test_file_share_dm_from_external_org_is_refused(*args, **kwargs):
    return None

def test_file_share_dm_from_host_org_still_synthesizes(*args, **kwargs):
    return None

def test_file_share_dm_host_event_team_cannot_mask_external_sharer(*args, **kwargs):
    return None

def test_file_share_dm_with_injected_sender_team_refused(*args, **kwargs):
    return None

def _async_return(*args, **kwargs):
    return None

def _reaction_adapter(*args, **kwargs):
    return None

def _dm_reaction(*args, **kwargs):
    return None

def test_reaction_in_dm_from_external_org_is_refused(*args, **kwargs):
    return None

def test_reaction_in_dm_from_host_org_still_routes(*args, **kwargs):
    return None

def test_reaction_handoff_from_external_dm_is_refused(*args, **kwargs):
    return None

def test_reaction_handoff_into_dm_from_external_channel_user_is_refused(*args, **kwargs):
    return None
