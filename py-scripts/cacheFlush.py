import os, shutil

path = "C:/Users/paul.leroyducardonno/Desktop/Hot_Projects/FileBeat/"

def cacheFlush():
    if os.path.isdir(path+"FilebeatToCloud/py-scripts/__pycache__"):

        shutil.rmtree(path+"FilebeatToCloud/py-scripts/__pycache__")