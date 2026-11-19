# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_GATEWAY_KIND = None

_RUNTIME_STATUS_FILE = None

_LOCKS_DIRNAME = None

_IS_WINDOWS = None

_UNSET = None

_GATEWAY_LOCK_FILENAME = None

_gateway_lock_handle = None

_WINDOWS_LOCK_OFFSET = None

_GATEWAY_RUNNING_PID_CACHE_TTL_SECONDS = None

_gateway_running_pid_cache_lock = None

logger = None

class _RuntimeStatusWriter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_runtime_status_state_lock = None

def _merge_over_on_disk(*args, **kwargs):
    return None

def _get_runtime_status_writer(*args, **kwargs):
    return None

def flush_runtime_status(*args, **kwargs):
    return None

def flush_runtime_status_async(*args, **kwargs):
    return None

class StormInfo:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def record_start_and_check_storm(*args, **kwargs):
    return None

def _get_process_hermes_home(*args, **kwargs):
    return None

def _canonical_hermes_home(*args, **kwargs):
    return None

def _same_hermes_home(*args, **kwargs):
    return None

def recorded_gateway_home_conflicts(*args, **kwargs):
    return None

_PROFILE_LABEL_RE = None

def _profile_label_for_home(*args, **kwargs):
    return None

def scoped_lock_owner_label(*args, **kwargs):
    return None

def _get_pid_path(*args, **kwargs):
    return None

def _get_gateway_lock_path(*args, **kwargs):
    return None

def _get_runtime_status_path(*args, **kwargs):
    return None

def _get_lock_dir(*args, **kwargs):
    return None

def _utc_now_iso(*args, **kwargs):
    return None

_EPOCH_MIN_PLAUSIBLE = None

def normalize_updated_at(*args, **kwargs):
    return None

WATCHDOG_EXIT_REASONS = None

def retained_gateway_state(*args, **kwargs):
    return None

def terminate_pid(*args, **kwargs):
    return None

def _start_times_agree(*args, **kwargs):
    return None

START_TIME_DRIFT_TOLERANCE = None

def start_time_fingerprints_match(*args, **kwargs):
    return None

def _scope_hash(*args, **kwargs):
    return None

def _get_scope_lock_path(*args, **kwargs):
    return None

def _get_process_start_time(*args, **kwargs):
    return None

def get_process_start_time(*args, **kwargs):
    return None

def _read_process_cmdline(*args, **kwargs):
    return None

def _gateway_command_subcommand(*args, **kwargs):
    return None

def gateway_spawn_intent_subcommand(*args, **kwargs):
    return None

def looks_like_gateway_command_line(*args, **kwargs):
    return None

def looks_like_gateway_runtime_command_line(*args, **kwargs):
    return None

def _looks_like_gateway_process(*args, **kwargs):
    return None

def _record_looks_like_gateway(*args, **kwargs):
    return None

def _profile_name_for_home(*args, **kwargs):
    return None

def profile_flag_value(*args, **kwargs):
    return None

_HERMES_HOME_ASSIGNMENT_RE = None

def hermes_home_assignments(*args, **kwargs):
    return None

def command_line_names_hermes_home(*args, **kwargs):
    return None

def _command_line_belongs_to_profile(*args, **kwargs):
    return None

def _host_gateway_serves_home(*args, **kwargs):
    return None

def _record_matches_live_gateway_pid(*args, **kwargs):
    return None

def _record_argv(*args, **kwargs):
    return None

def _build_pid_record(*args, **kwargs):
    return None

def _get_code_identity_fields(*args, **kwargs):
    return None

def _pid_record_belongs_to_current_profile(*args, **kwargs):
    return None

def _build_runtime_status_record(*args, **kwargs):
    return None

def _read_json_file(*args, **kwargs):
    return None

def _write_json_file(*args, **kwargs):
    return None

def _unlink_quietly(*args, **kwargs):
    return None

def _read_pid_record(*args, **kwargs):
    return None

def _read_gateway_lock_record(*args, **kwargs):
    return None

def _pid_from_record(*args, **kwargs):
    return None

def _start_times_conflict(*args, **kwargs):
    return None

def _live_pid_from_record(*args, **kwargs):
    return None

def _clear_running_pid_cache(*args, **kwargs):
    return None

def _file_cache_signature(*args, **kwargs):
    return None

def _cleanup_invalid_pid_path(*args, **kwargs):
    return None

def _try_acquire_file_lock(*args, **kwargs):
    return None

def _pid_exists(*args, **kwargs):
    return None

def _release_file_lock(*args, **kwargs):
    return None

def acquire_gateway_runtime_lock(*args, **kwargs):
    return None

def release_gateway_runtime_lock(*args, **kwargs):
    return None

def owns_gateway_runtime_lock(*args, **kwargs):
    return None

def _probe_lock_file(*args, **kwargs):
    return None

def is_gateway_runtime_lock_active(*args, **kwargs):
    return None

def _strict_path_exists(*args, **kwargs):
    return None

def _is_gateway_runtime_lock_active_strict(*args, **kwargs):
    return None

def write_pid_file(*args, **kwargs):
    return None

def _write_json_excl(*args, **kwargs):
    return None

def _apply_set_fields(*args, **kwargs):
    return None

def _coerce_session_store(*args, **kwargs):
    return None

def _prepare_runtime_status_update(*args, **kwargs):
    return None

def _emit_runtime_status_transition(*args, **kwargs):
    return None

def write_runtime_status(*args, **kwargs):
    return None

def publish_runtime_status(*args, **kwargs):
    return None

def read_runtime_status(*args, **kwargs):
    return None

_RUNTIME_STATUS_STALE_TTL_S = None

def runtime_status_is_stale(*args, **kwargs):
    return None

def runtime_status_heartbeat_age_s(*args, **kwargs):
    return None

def runtime_status_pid_is_live(*args, **kwargs):
    return None

def parse_active_agents(*args, **kwargs):
    return None

_DRAINABLE_GATEWAY_STATES = None

def derive_gateway_busy(*args, **kwargs):
    return None

def derive_gateway_drainable(*args, **kwargs):
    return None

class GatewayLiveness:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def profile_name_for_home(*args, **kwargs):
    return None

def multiplexer_liveness_for_profile(*args, **kwargs):
    return None

def shared_listener_mirror_platforms(*args, **kwargs):
    return None

def profile_platforms_from_multiplexer(*args, **kwargs):
    return None

def resolve_gateway_liveness(*args, **kwargs):
    return None

def get_runtime_status_running_pid(*args, **kwargs):
    return None

def live_gateway_pid_for_home(*args, **kwargs):
    return None

def remove_pid_file(*args, **kwargs):
    return None

def _process_is_stopped(*args, **kwargs):
    return None

def acquire_scoped_lock(*args, **kwargs):
    return None

def _acquire_scoped_lock_at(*args, **kwargs):
    return None

_TAKEOVER_MARKER_FILENAME = None

_TAKEOVER_MARKER_TTL_S = None

_PLANNED_STOP_MARKER_FILENAME = None

_PLANNED_STOP_MARKER_TTL_S = None

def _get_takeover_marker_path(*args, **kwargs):
    return None

def _get_planned_stop_marker_path(*args, **kwargs):
    return None

def _marker_is_stale(*args, **kwargs):
    return None

def _read_live_pid_marker(*args, **kwargs):
    return None

def _pid_marker_names_self(*args, **kwargs):
    return None

def _consume_pid_marker_for_self(*args, **kwargs):
    return None

def write_takeover_marker(*args, **kwargs):
    return None

def _write_marker(*args, **kwargs):
    return None

def consume_takeover_marker_for_self(*args, **kwargs):
    return None

def clear_takeover_marker(*args, **kwargs):
    return None

def _validated_scoped_lock_gateway_owner(*args, **kwargs):
    return None

def _scoped_lock_owner_state(*args, **kwargs):
    return None

def _wait_for_scoped_lock_owner_exit(*args, **kwargs):
    return None

def _snapshot_gateway_children(*args, **kwargs):
    return None

def reap_gateway_children(*args, **kwargs):
    return None

def take_over_scoped_lock_holder(*args, **kwargs):
    return None

def _terminate_verified_owner(*args, **kwargs):
    return None

def write_planned_stop_marker(*args, **kwargs):
    return None

_PLANNED_STOP_MUTEX_WAIT_S = None

def _update_pause_on_disk(*args, **kwargs):
    return None

def _checkpoint_planned_stop(*args, **kwargs):
    return None

def consume_planned_stop_marker_for_self(*args, **kwargs):
    return None

def planned_stop_marker_targets_self(*args, **kwargs):
    return None

def get_running_pid(*args, **kwargs):
    return None

def get_running_pid_identity_strict(*args, **kwargs):
    return None

def get_running_pid_cached(*args, **kwargs):
    return None
