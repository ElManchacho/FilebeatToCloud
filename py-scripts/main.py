from menuUI import *
from cacheFlush import cacheFlush
import atexit

if __name__ == "__main__":

    atexit.register(cacheFlush)
    
    menuUi()