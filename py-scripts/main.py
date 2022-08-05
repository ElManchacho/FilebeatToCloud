from cacheFlush import cacheFlush
from menuUi import menuUi
import atexit

if __name__ == "__main__":
    atexit.register(cacheFlush)
    
    # faire en sorte d'avoir plusieurs configurations/instances de services

    menuUi()