import os, shutil

cacheDir = "__pycache__"

def cacheFlush():
    if os.path.isdir(cacheDir):

        shutil.rmtree(cacheDir)