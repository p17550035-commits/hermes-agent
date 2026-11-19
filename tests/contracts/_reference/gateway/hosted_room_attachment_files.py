# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_FILES_KEY = None

class BlobFiles:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def blob_files(*args, **kwargs):
    return None

def _blob_name(*args, **kwargs):
    return None

def write_blob_file(*args, **kwargs):
    return None

def _open_blob(*args, **kwargs):
    return None

def read_verified_blob(*args, **kwargs):
    return None

def read_blob_slice(*args, **kwargs):
    return None

def unlink_blobs(*args, **kwargs):
    return None

def sweep_orphan_blobs(*args, **kwargs):
    return None
