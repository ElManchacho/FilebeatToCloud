from cacheFlush import cacheFlush
from menuUI import menuUi
import atexit
import sys

if __name__ == "__main__":

    # Flush python cache

    atexit.register(cacheFlush)
    
    # Start app's Menu, which takes one argument for filbeat version naming when calling the script
    
    menuUi(sys.argv[2])