# Store filebeat version to use in variable

$filebeatVersion = "filebeat-8.8.2-windows-x86_64"

# Check privileges : if admin, laucnh app, if not, asks for admin rights

if(!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {

    # Launch py script with modal to ask for privileges in a powershell invocation

    try {
        Start-Process -FilePath PowerShell.exe -Wait -windowstyle hidden -Verb Runas -ArgumentList Exit

        py "./py-scripts/main.py" -p $filebeatVersion -Wait
        
    }
    catch{
        Exit
    }
}
else {
    py "./py-scripts/main.py" -p $filebeatVersion -Wait
}