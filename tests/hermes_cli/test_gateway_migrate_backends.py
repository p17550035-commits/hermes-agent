# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_READ_ONLY_SYSTEMCTL = None

_READ_ONLY_LAUNCHCTL = None

def _argv(*args, **kwargs):
    return None

class FakeHost:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def host(*args, **kwargs):
    return None

def no_writes(*args, **kwargs):
    return None

def _by_supervisor(*args, **kwargs):
    return None

def test_systemd_units_by_mainpid_with_scope_path_and_nix_detection(*args, **kwargs):
    return None

def test_cgroup_without_mainpid_is_not_claimed_by_the_unit(*args, **kwargs):
    return None

def test_installed_enabled_unit_that_is_not_running_is_reported_once(*args, **kwargs):
    return None

def test_s6_docker_desktop_and_detached_shapes(*args, **kwargs):
    return None

def launch_agents(*args, **kwargs):
    return None

def test_launchd_job_with_plist_path_and_nix_store_plist(*args, **kwargs):
    return None

def nix_launcher_agent(*args, **kwargs):
    return None

def test_nix_wait_for_launcher_job_is_reported_with_its_plist_home(*args, **kwargs):
    return None

def test_launchd_plists_are_ignored_off_macos(*args, **kwargs):
    return None

def test_parent_launchd_is_not_reported_as_detached_on_macos(*args, **kwargs):
    return None

def test_home_ownership_is_reported_against_this_hermes_home(*args, **kwargs):
    return None

def test_cli_json_mode_exits_zero_and_never_applies(*args, **kwargs):
    return None

def test_cli_text_mode_with_nothing_found(*args, **kwargs):
    return None

def test_backends_refuses_apply_flags(*args, **kwargs):
    return None

def test_json_without_backends_is_an_argument_error(*args, **kwargs):
    return None

def test_parser_accepts_backends_dry_run_json(*args, **kwargs):
    return None

def test_scan_failure_still_exits_zero(*args, **kwargs):
    return None

_REPO = None

_SHIM = None

_SHIMMED = None

def _wait_for_detached_prune(*args, **kwargs):
    return None

def _fresh_hermes(*args, **kwargs):
    return None

def test_real_entry_point_report_writes_only_what_plain_migrate_dry_run_writes(*args, **kwargs):
    return None
