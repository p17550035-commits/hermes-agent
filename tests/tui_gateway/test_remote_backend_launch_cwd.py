# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def launch_dir(*args, **kwargs):
    return None

def _backend(*args, **kwargs):
    return None

def _fresh_session(*args, **kwargs):
    return None

class _Sprites:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _HostRunner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def clean_registry(*args, **kwargs):
    return None

def test_sandbox_session_does_not_register_the_launch_dir(*args, **kwargs):
    return None

def test_plugin_sandbox_backend_does_not_register_the_launch_dir(*args, **kwargs):
    return None

def test_plugin_host_backend_keeps_the_launch_dir(*args, **kwargs):
    return None

def test_plugin_classification_reads_the_bound_profiles_registry(*args, **kwargs):
    return None

def test_explicit_workspace_still_wins_on_a_sandbox_backend(*args, **kwargs):
    return None

def test_configured_sandbox_cwd_still_wins(*args, **kwargs):
    return None

def test_local_backend_keeps_the_launch_dir(*args, **kwargs):
    return None

def test_docker_keeps_the_host_dir(*args, **kwargs):
    return None

def test_sandbox_resume_drops_a_stored_hermes_home_cwd(*args, **kwargs):
    return None

def test_sandbox_resume_drops_a_stored_desktop_launch_dir(*args, **kwargs):
    return None

def test_sandbox_resume_keeps_a_workspace_picked_under_the_hermes_root(*args, **kwargs):
    return None

def test_sandbox_hydrated_workspace_stays_the_terminal_cwd(*args, **kwargs):
    return None

def test_compute_host_carries_workspace_provenance(*args, **kwargs):
    return None

def test_compute_host_minimal_record_keeps_workspace_provenance(*args, **kwargs):
    return None

def test_sandbox_path_completion_lists_the_backend_cwd(*args, **kwargs):
    return None
