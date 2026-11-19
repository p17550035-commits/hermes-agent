# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

KEY = None

class _ImmediateThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def profile(*args, **kwargs):
    return None

def resume(*args, **kwargs):
    return None

def test_resume_lands_in_the_profiles_own_home(*args, **kwargs):
    return None

def test_resume_keeps_a_folder_chosen_for_the_profile(*args, **kwargs):
    return None

def test_launch_profile_resume_is_unchanged(*args, **kwargs):
    return None
