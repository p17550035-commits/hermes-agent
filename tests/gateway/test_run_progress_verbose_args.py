# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

CODE = None

class _CodeBlockAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _ArgsAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _progress_text(*args, **kwargs):
    return None

def test_verbose_args_render_in_a_code_block_on_markdown_platforms(*args, **kwargs):
    return None

def test_streamed_verbose_args_share_the_code_block_and_skip_it_for_embedded_fences(*args, **kwargs):
    return None
