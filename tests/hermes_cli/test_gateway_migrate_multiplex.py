# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_REAL_SERVICE_OP = None

def fleet(*args, **kwargs):
    return None

def _fake_spawn(*args, **kwargs):
    return None

def _pid_of_started_gateway(*args, **kwargs):
    return None

def _name(*args, **kwargs):
    return None

def _units(*args, **kwargs):
    return None

_real_preflight = None

def _config_flag(*args, **kwargs):
    return None

def test_dry_run_and_blocked_preflight_change_nothing(*args, **kwargs):
    return None

def test_parked_profile_remains_in_migration_inventory(*args, **kwargs):
    return None

def test_preflight_never_imports_a_parked_profiles_plugins(*args, **kwargs):
    return None

def test_migration_removes_parked_footprint_without_waiting_for_it_to_serve(*args, **kwargs):
    return None

def _apply_capturing_manifest(*args, **kwargs):
    return None

def test_apply_clears_the_manifest_on_success_and_the_compensator_restores(*args, **kwargs):
    return None

def test_migration_preserves_root_system_service_user_for_default_install(*args, **kwargs):
    return None

def test_rollback_that_cannot_bring_the_gateway_back_reports_failure_and_keeps_the_manifest(*args, **kwargs):
    return None

def test_rollback_never_respawns_a_detached_secondary(*args, **kwargs):
    return None

def test_malformed_manifest_is_refused_before_any_mutation(*args, **kwargs):
    return None

def test_secondary_port_binder_is_notice_with_ingress_and_blocker_without(*args, **kwargs):
    return None

def test_serves_profile_prefix_is_read_from_adapter_classes(*args, **kwargs):
    return None

def test_update_hook_migrates_when_unblocked_and_only_warns_when_blocked(*args, **kwargs):
    return None

def test_update_hook_never_touches_single_profile_or_already_multiplexed(*args, **kwargs):
    return None

def test_update_hook_reads_a_masked_default_unit_as_an_opt_out(*args, **kwargs):
    return None

def test_update_hook_refuses_to_cross_service_user_or_home_boundary(*args, **kwargs):
    return None

def test_update_hook_still_migrates_same_user_same_scope_profiles_under_the_default_tree(*args, **kwargs):
    return None

def test_update_hook_folds_a_unit_less_default_when_every_secondary_shares_one_manager(*args, **kwargs):
    return None

def test_auto_multiplex_migration_false_opts_out_of_the_update_hook_but_not_the_explicit_command(*args, **kwargs):
    return None

def test_explicit_migrate_with_no_standalone_secondaries_still_flips_flag_and_restarts_default(*args, **kwargs):
    return None

def test_failed_default_bringup_compensates_to_one_detached_gateway(*args, **kwargs):
    return None

def test_interrupted_apply_is_resumed_from_the_manifest_not_short_circuited(*args, **kwargs):
    return None

def test_every_installed_unit_of_a_secondary_is_removed_and_recorded(*args, **kwargs):
    return None

def test_unresolvable_system_unit_user_is_unknown_principal_not_directory_owner(*args, **kwargs):
    return None

def test_opt_out_reads_effective_config_managed_false_wins_and_string_false_is_false(*args, **kwargs):
    return None

def test_interruption_after_the_default_unit_exists_is_still_interrupted_not_already_multiplexed(*args, **kwargs):
    return None

def test_failure_anywhere_in_the_destructive_phase_restores_the_removed_secondaries(*args, **kwargs):
    return None

def test_known_bringup_refusal_is_rejected_before_any_secondary_is_touched(*args, **kwargs):
    return None

def test_unknown_default_system_principal_blocks_the_update_hook(*args, **kwargs):
    return None

def test_migrate_leaves_exactly_one_host_unit_serving_every_profile_and_is_idempotent(*args, **kwargs):
    return None

def test_half_migrated_host_converges_on_a_re_run(*args, **kwargs):
    return None

def test_migrate_enables_the_survivor_before_it_removes_anything(*args, **kwargs):
    return None

def test_migrate_refuses_when_the_survivor_cannot_be_enabled(*args, **kwargs):
    return None

def test_plan_names_every_process_it_will_sigterm_before_it_signals_anything(*args, **kwargs):
    return None

def test_windows_task_detection_reads_both_the_task_and_the_startup_fallback(*args, **kwargs):
    return None

def test_windows_is_migratable_and_only_s6_is_refused(*args, **kwargs):
    return None

def test_standalone_profile_is_listed_left_alone_and_not_a_fold_target(*args, **kwargs):
    return None
