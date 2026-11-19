# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PROJECT_ROOT = None

logger = None

_CAPTURE_TEXT = None

class GatewayRuntimeSnapshot:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ProfileGatewayProcess:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class WindowsGatewayService:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _get_service_pids(*args, **kwargs):
    return None

def _get_parent_pid(*args, **kwargs):
    return None

def _is_pid_ancestor_of_current_process(*args, **kwargs):
    return None

def _request_gateway_self_restart(*args, **kwargs):
    return None

def _graceful_restart_via_sigusr1(*args, **kwargs):
    return None

def _wait_for_pid_exit(*args, **kwargs):
    return None

GATEWAY_LOOP_ALIVE = None

GATEWAY_LOOP_WEDGED = None

GATEWAY_LOOP_UNKNOWN = None

DEFAULT_LOOP_LIVENESS_STALE_AFTER_S = None

_LOOP_TICK_ABSENT = None

def _probe_loop_tick_socket(*args, **kwargs):
    return None

def _ping_loop_tick_witness(*args, **kwargs):
    return None

def _probe_loop_tick_tcp(*args, **kwargs):
    return None

def _probe_loop_tick_socket_sustained(*args, **kwargs):
    return None

def probe_gateway_loop_liveness(*args, **kwargs):
    return None

def _escalate_wedged_gateway(*args, **kwargs):
    return None

def _get_ancestor_pids(*args, **kwargs):
    return None

def _append_unique_pid(*args, **kwargs):
    return None

def _iter_proc_cmdlines(*args, **kwargs):
    return None

def _scan_gateway_pids(*args, **kwargs):
    return None

def _parse_ps_line(*args, **kwargs):
    return None

def _iter_windows_list_processes(*args, **kwargs):
    return None

def _windows_process_listing(*args, **kwargs):
    return None

def _filter_venv_launcher_stubs(*args, **kwargs):
    return None

def find_gateway_pids(*args, **kwargs):
    return None

def find_profile_gateway_processes(*args, **kwargs):
    return None

def _scm_service_field(*args, **kwargs):
    return None

def find_windows_gateway_services(*args, **kwargs):
    return None

def _gateway_run_args_for_profile(*args, **kwargs):
    return None

def _capture_gateway_argv(*args, **kwargs):
    return None

def _prepare_profile_gateway_update_restart(*args, **kwargs):
    return None

def launch_detached_gateway_restart_by_cmdline(*args, **kwargs):
    return None

def launch_detached_profile_gateway_restart(*args, **kwargs):
    return None

GATEWAY_RESTART_WATCHER_TIMEOUT_S = None

def _restart_argv_is_host_gateway(*args, **kwargs):
    return None

def _spawn_gateway_restart_watcher(*args, **kwargs):
    return None

def _systemd_unit_is_active(*args, **kwargs):
    return None

def _probe_systemd_service_running(*args, **kwargs):
    return None

def _parse_kv_pairs(*args, **kwargs):
    return None

def _systemctl_show(*args, **kwargs):
    return None

def _unit_environment_value(*args, **kwargs):
    return None

def _hermes_home_pinned_by_unit(*args, **kwargs):
    return None

def _hermes_home_from_systemd_unit_file(*args, **kwargs):
    return None

def _sync_hermes_home_from_systemd_unit(*args, **kwargs):
    return None

def _read_systemd_unit_properties(*args, **kwargs):
    return None

def _positive_pid(*args, **kwargs):
    return None

def _systemd_main_pid_from_props(*args, **kwargs):
    return None

def _runtime_state_pid(*args, **kwargs):
    return None

def _systemd_main_pid(*args, **kwargs):
    return None

def _read_gateway_runtime_status(*args, **kwargs):
    return None

def _systemd_cli_bits(*args, **kwargs):
    return None

def _wait_for_systemd_service_restart(*args, **kwargs):
    return None

def _systemd_restart_wait_timeout(*args, **kwargs):
    return None

def _systemd_unit_is_start_limited(*args, **kwargs):
    return None

def _systemd_error_indicates_start_limit(*args, **kwargs):
    return None

def _systemd_service_is_start_limited(*args, **kwargs):
    return None

def _print_systemd_start_limit_wait(*args, **kwargs):
    return None

def _recover_pending_systemd_restart(*args, **kwargs):
    return None

def _parse_launchd_pid_from_list_output(*args, **kwargs):
    return None

def _parse_launchd_pid_from_print_output(*args, **kwargs):
    return None

def _launchd_print_service_pid(*args, **kwargs):
    return None

def _launchd_service_registered(*args, **kwargs):
    return None

def _locate_launchd_gateway_service(*args, **kwargs):
    return None

def _probe_launchd_service_running(*args, **kwargs):
    return None

def _s6_gateway_snapshot(*args, **kwargs):
    return None

def get_gateway_runtime_snapshot(*args, **kwargs):
    return None

def _format_gateway_pids(*args, **kwargs):
    return None

def _print_gateway_process_mismatch(*args, **kwargs):
    return None

def _print_multiplex_standalone_reason(*args, **kwargs):
    return None

def _print_served_ingress_urls(*args, **kwargs):
    return None

def _print_unserved_shared_ingress(*args, **kwargs):
    return None

def _print_other_profiles_gateway_status(*args, **kwargs):
    return None

def _print_duplicate_credential_warnings(*args, **kwargs):
    return None

def _gateway_list(*args, **kwargs):
    return None

def kill_gateway_processes(*args, **kwargs):
    return None

_REAPER_SUPERVISOR_WALK_LIMIT = None

def _reaper_candidate_is_supervisor_owned(*args, **kwargs):
    return None

def _reap_unsupervised_gateway_orphans(*args, **kwargs):
    return None

def _reaper_exclusion_pids(*args, **kwargs):
    return None

_ORPHAN_EXIT_GRACE_SECONDS = None

_ORPHAN_EXIT_POLL_SECONDS = None

def _await_gateway_exit(*args, **kwargs):
    return None

def _force_kill_survivors(*args, **kwargs):
    return None

def stop_profile_gateway(*args, **kwargs):
    return None

def is_linux(*args, **kwargs):
    return None

def _wsl_systemd_operational(*args, **kwargs):
    return None

def _systemd_operational(*args, **kwargs):
    return None

def supports_systemd_services(*args, **kwargs):
    return None

def is_macos(*args, **kwargs):
    return None

def is_windows(*args, **kwargs):
    return None

def _gw_windows(*args, **kwargs):
    return None

_WINDOWS_TASK_SUPERVISOR_STATES = None

def _windows_scheduled_task_state(*args, **kwargs):
    return None

def _windows_scheduled_task_supervises(*args, **kwargs):
    return None

def _gateway_detached_env(*args, **kwargs):
    return None

def _stdin_is_tty(*args, **kwargs):
    return None

def _windows_gateway_should_absorb_console_controls(*args, **kwargs):
    return None

def _windows_console_window_attached(*args, **kwargs):
    return None

def _windows_gateway_breakaway_state(*args, **kwargs):
    return None

_SERVICE_BASE = None

SERVICE_DESCRIPTION = None

_SYSTEM_UNIT_DIR = None

def _profile_name_from_home(*args, **kwargs):
    return None

def _native_service_homes(*args, **kwargs):
    return None

def _bare_unit_pinned_home(*args, **kwargs):
    return None

def _home_owns_bare_service_name(*args, **kwargs):
    return None

def _profile_suffix(*args, **kwargs):
    return None

def _current_profile_name(*args, **kwargs):
    return None

def _profile_arg(*args, **kwargs):
    return None

def get_service_name(*args, **kwargs):
    return None

def user_systemd_unit_dir(*args, **kwargs):
    return None

def get_systemd_unit_path(*args, **kwargs):
    return None

class UserSystemdUnavailableError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class SystemScopeRequiresRootError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _user_runtime_dir(*args, **kwargs):
    return None

def _user_dbus_socket_path(*args, **kwargs):
    return None

def _user_systemd_private_socket_path(*args, **kwargs):
    return None

def _path_exists_safe(*args, **kwargs):
    return None

def _runtime_dir_is_ours(*args, **kwargs):
    return None

def _user_systemd_socket_ready(*args, **kwargs):
    return None

def _ensure_user_systemd_env(*args, **kwargs):
    return None

def _wait_for_user_dbus_socket(*args, **kwargs):
    return None

def _wait_for_target_user_bus(*args, **kwargs):
    return None

def _loginctl_enable_linger(*args, **kwargs):
    return None

def _completed_process_detail(*args, **kwargs):
    return None

def _preflight_user_systemd(*args, **kwargs):
    return None

def _raise_user_systemd_unavailable(*args, **kwargs):
    return None

def _systemctl_cmd(*args, **kwargs):
    return None

def _run_systemctl(*args, **kwargs):
    return None

def _service_scope_label(*args, **kwargs):
    return None

def get_installed_systemd_scopes(*args, **kwargs):
    return None

def has_conflicting_systemd_units(*args, **kwargs):
    return None

def _legacy_unit_search_paths(*args, **kwargs):
    return None

def _find_legacy_hermes_units(*args, **kwargs):
    return None

def has_legacy_hermes_units(*args, **kwargs):
    return None

def print_legacy_unit_warning(*args, **kwargs):
    return None

def remove_legacy_hermes_units(*args, **kwargs):
    return None

def print_systemd_scope_conflict_warning(*args, **kwargs):
    return None

def refuses_container_user_scope_install(*args, **kwargs):
    return None

def _require_root_for_system_service(*args, **kwargs):
    return None

def _system_service_identity(*args, **kwargs):
    return None

def _read_systemd_user_from_unit(*args, **kwargs):
    return None

def _default_system_service_user(*args, **kwargs):
    return None

def prompt_linux_gateway_install_scope(*args, **kwargs):
    return None

def install_linux_gateway_from_setup(*args, **kwargs):
    return None

def get_systemd_linger_status(*args, **kwargs):
    return None

def get_launchd_plist_path(*args, **kwargs):
    return None

def launchd_gateway_labels_for_install(*args, **kwargs):
    return None

def legacy_launchd_labels_for_install(*args, **kwargs):
    return None

def get_python_path(*args, **kwargs):
    return None

def _build_user_local_paths(*args, **kwargs):
    return None

def _build_wsl_interop_paths(*args, **kwargs):
    return None

def _remap_path_for_user(*args, **kwargs):
    return None

def _installed_unit_ld_library_path(*args, **kwargs):
    return None

def _ld_library_path_line(*args, **kwargs):
    return None

def _hermes_home_for_target_user(*args, **kwargs):
    return None

def _build_service_path_dirs(*args, **kwargs):
    return None

def _stable_service_working_dir(*args, **kwargs):
    return None

def _systemd_watchdog_seconds(*args, **kwargs):
    return None

def _pm_managed_node_dirs(*args, **kwargs):
    return None

def _append_node_dir_for_service(*args, **kwargs):
    return None

def _systemd_command(*args, **kwargs):
    return None

def _prepare_service_launcher(*args, **kwargs):
    return None

def generate_systemd_unit(*args, **kwargs):
    return None

def _normalize_service_definition(*args, **kwargs):
    return None

_SYSTEMD_OPTIONAL_DIRECTIVES = None

def _strip_optional_systemd_directives(*args, **kwargs):
    return None

def _normalize_launchd_plist_for_comparison(*args, **kwargs):
    return None

def systemd_unit_is_current(*args, **kwargs):
    return None

def _retire_hermes_replace_dropin(*args, **kwargs):
    return None

def refresh_systemd_unit_if_needed(*args, **kwargs):
    return None

def _print_linger_enable_warning(*args, **kwargs):
    return None

def _ensure_linger_enabled(*args, **kwargs):
    return None

def _ensure_system_service_linger(*args, **kwargs):
    return None

def _select_systemd_scope(*args, **kwargs):
    return None

def _system_scope_wizard_would_need_root(*args, **kwargs):
    return None

def _print_system_scope_remediation(*args, **kwargs):
    return None

def _get_restart_drain_timeout(*args, **kwargs):
    return None

def _agent_timeout_setting(*args, **kwargs):
    return None

def _get_cron_drain_timeout(*args, **kwargs):
    return None

def _get_restart_exit_wait_budget(*args, **kwargs):
    return None

def systemd_install(*args, **kwargs):
    return None

def _systemd_scope_preamble(*args, **kwargs):
    return None

def _systemd_unit_belongs_to_current_home(*args, **kwargs):
    return None

def systemd_uninstall(*args, **kwargs):
    return None

def _print_service_not_installed(*args, **kwargs):
    return None

def _require_service_installed(*args, **kwargs):
    return None

def systemd_start(*args, **kwargs):
    return None

def systemd_stop(*args, **kwargs):
    return None

def systemd_restart(*args, **kwargs):
    return None

def _systemd_graceful_restart_action(*args, **kwargs):
    return None

def _systemd_reset_and_run(*args, **kwargs):
    return None

def systemd_status(*args, **kwargs):
    return None

def _wait_for_gateway_exit(*args, **kwargs):
    return None

def _wait_for_tcp_port_free(*args, **kwargs):
    return None

def _wait_for_api_server_port_free(*args, **kwargs):
    return None

def _truthy_env(*args, **kwargs):
    return None

def _is_official_docker_checkout(*args, **kwargs):
    return None

def _running_under_gateway_supervisor(*args, **kwargs):
    return None

def host_multiplexer_serving(*args, **kwargs):
    return None

def _served_by_another_host_gateway(*args, **kwargs):
    return None

def named_profile_served_by_running_multiplexer(*args, **kwargs):
    return None

def _served_profile_needs_no_service(*args, **kwargs):
    return None

def _named_profile_refused_under_multiplexer(*args, **kwargs):
    return None

def _guard_named_profile_under_multiplexer(*args, **kwargs):
    return None

def _host_decision_exit_code(*args, **kwargs):
    return None

def _attach_to_host_gateway_or_guard(*args, **kwargs):
    return None

def _guard_supervised_gateway_conflict(*args, **kwargs):
    return None

def _guard_existing_gateway_process_conflict(*args, **kwargs):
    return None

def _guard_official_docker_root_gateway(*args, **kwargs):
    return None

def _apply_startup_watchdog_config(*args, **kwargs):
    return None

def _absorb_windows_console_controls(*args, **kwargs):
    return None

def _make_exit_diag(*args, **kwargs):
    return None

def _respawn_storm_backoff(*args, **kwargs):
    return None

def run_gateway(*args, **kwargs):
    return None

_WATCHDOG_EXIT_REASONS = None

def _runtime_health_lines(*args, **kwargs):
    return None

def _print_info_lines(*args, **kwargs):
    return None

def _running_under_s6(*args, **kwargs):
    return None

def _systemd_unit_installed(*args, **kwargs):
    return None

def _is_service_installed(*args, **kwargs):
    return None

def _is_service_running(*args, **kwargs):
    return None

def _print_indented(*args, **kwargs):
    return None

def _service_backend(*args, **kwargs):
    return None

def _service_call(*args, **kwargs):
    return None

def _dispatch_via_service_manager_if_s6(*args, **kwargs):
    return None

def _dispatch_all_via_service_manager_if_s6(*args, **kwargs):
    return None

def gateway_command(*args, **kwargs):
    return None

def _maybe_redirect_run_to_s6_supervision(*args, **kwargs):
    return None

def _block_until_terminated(*args, **kwargs):
    return None

def _installed_service_kind_for(*args, **kwargs):
    return None

def _installed_service_kind(*args, **kwargs):
    return None

def _stop_installed_service(*args, **kwargs):
    return None

def _refuse_from_inside_gateway(*args, **kwargs):
    return None

def _print_lines(*args, **kwargs):
    return None

def _print_runtime_health(*args, **kwargs):
    return None

def _cmd_run(*args, **kwargs):
    return None

def _cmd_setup(*args, **kwargs):
    return None

_WSL_FOREGROUND_HINT = None

_NO_BACKEND_MESSAGES = None

def _no_backend_exit(*args, **kwargs):
    return None

def _is_apt_termux_install(*args, **kwargs):
    return None

def _service_mgmt_blocked(*args, **kwargs):
    return None

def _handle_no_backend(*args, **kwargs):
    return None

def _install_systemd_from_cli(*args, **kwargs):
    return None

def _cmd_install(*args, **kwargs):
    return None

def _cmd_uninstall(*args, **kwargs):
    return None

def _host_multiplexer_for_all_verb(*args, **kwargs):
    return None

def _host_multiplexer_is_ours(*args, **kwargs):
    return None

def _print_unfolded_gateway_note(*args, **kwargs):
    return None

def _cmd_start(*args, **kwargs):
    return None

def _cmd_stop(*args, **kwargs):
    return None

def _stop_host_multiplexer(*args, **kwargs):
    return None

def _restart_all(*args, **kwargs):
    return None

def _restart_all_as_host(*args, **kwargs):
    return None

def _cmd_restart(*args, **kwargs):
    return None

_STATUS_RUNNING_HINTS = None

_STATUS_STOPPED_HINTS = None

def _status_host_kind(*args, **kwargs):
    return None

def _cmd_status(*args, **kwargs):
    return None

def _cmd_list(*args, **kwargs):
    return None

def _cmd_migrate_legacy(*args, **kwargs):
    return None

def _cmd_migrate(*args, **kwargs):
    return None

_GATEWAY_SUBCOMMANDS = None

def _gateway_command_inner(*args, **kwargs):
    return None
