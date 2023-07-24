from cacheFlush import cacheFlush
from menuUI import menuUi
import atexit
import sys

if __name__ == "__main__":
    atexit.register(cacheFlush)
    
    # faire en sorte d'avoir plusieurs configurations/instances de services
    
    menuUi(sys.argv[2]) # takes one argument for filbeat version naming