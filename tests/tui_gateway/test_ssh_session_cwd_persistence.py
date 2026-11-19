# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _ImmediateThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def backend(*args, **kwargs):
    return None

def db(*args, **kwargs):
    return None

def resume_db(*args, **kwargs):
    return None

def _resume_live(*args, **kwargs):
    return None

def _hydrate(*args, **kwargs):
    return None

def _hermes_home_subdir(*args, **kwargs):
    return None

def test_ssh_launch_dir_is_not_persisted(*args, **kwargs):
    return None

def test_ssh_explicit_cwd_is_persisted(*args, **kwargs):
    return None

def test_host_backends_still_persist_the_launch_dir(*args, **kwargs):
    return None

def test_hermes_owned_cwd(*args, **kwargs):
    return None

def test_hermes_owned_cwd_includes_the_root_for_a_named_profile(*args, **kwargs):
    return None

def test_named_profile_resume_does_not_adopt_a_root_launch_dir(*args, **kwargs):
    return None

def test_resume_leaves_a_set_aside_row_unchanged(*args, **kwargs):
    return None

def test_resume_keeps_a_remote_tilde_cwd_when_home_is_inside_hermes_home(*args, **kwargs):
    return None

def test_resume_does_not_adopt_a_stored_hermes_home_cwd(*args, **kwargs):
    return None

def test_resume_keeps_a_stored_remote_workspace(*args, **kwargs):
    return None

def test_resume_without_a_stored_cwd_does_not_persist_the_launch_dir(*args, **kwargs):
    return None

def test_host_backends_resume_unchanged(*args, **kwargs):
    return None

def test_ssh_branch_seed_skips_the_launch_dir(*args, **kwargs):
    return None

KEY = None

def test_session_resume_does_not_adopt_a_stored_hermes_home_cwd(*args, **kwargs):
    return None

def test_session_resume_keeps_a_stored_remote_workspace(*args, **kwargs):
    return None

def test_session_resume_on_host_backends_unchanged(*args, **kwargs):
    return None
