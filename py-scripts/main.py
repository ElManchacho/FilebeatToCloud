from menuUI import *
from cacheFlush import cacheFlush
import atexit

if __name__ == "__main__":

    atexit.register(cacheFlush)
    
    # faire en sorte d'avoir plusieurs configurations/instances de services

    menuUi()