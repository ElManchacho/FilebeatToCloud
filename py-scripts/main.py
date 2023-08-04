from cacheFlush import cacheFlush
import atexit, sys, subprocess

if __name__ == "__main__":

    # Flush python cache

    atexit.register(cacheFlush)

    # check requirements

    pythonVersion = (subprocess.Popen(["powershell.exe", "python --version SilentlyContinue"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)).stdout.read().decode().strip()

    pipVersion = (subprocess.Popen(["powershell.exe", "pip --version SilentlyContinue"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)).stdout.read().decode().strip()

    pipPyyaml = (subprocess.Popen(["powershell.exe", "pip show pyyaml | findstr 'Version'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)).stdout.read().decode().strip()
        
    pipPythonDotenv = (subprocess.Popen(["powershell.exe", "pip show python-dotenv | findstr 'Version'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)).stdout.read().decode().strip()
        
    pipPsutil = (subprocess.Popen(["powershell.exe", "pip show psutil | findstr 'Version'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)).stdout.read().decode().strip()

    # Check if requirements are correctly installed to use the features, else will ony give acess to requirements list

    if (pythonVersion == '' or pipVersion == '' or pipPyyaml == '' or pipPythonDotenv == '' or pipPsutil == ''):
        from poorMenuUI import poorMenuUi
        poorMenuUi(pythonVersion, pipVersion, pipPyyaml, pipPythonDotenv, pipPsutil)
    else:# Start app's Menu, which takes one argument for filbeat version naming when calling the script
        from menuUI import menuUi
        menuUi(sys.argv[2], pythonVersion, pipVersion, pipPyyaml, pipPythonDotenv, pipPsutil)