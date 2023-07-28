if(!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
    
    Start-Process -FilePath PowerShell.exe -windowstyle hidden -Verb Runas -ArgumentList "-File `"$($MyInvocation.MyCommand.Path)`"  `"$($MyInvocation.MyCommand.UnboundArguments)`""
  
    $filebeatVersion = "filebeat-8.8.2-windows-x86_64"

    py "./py-scripts/main.py" -p $filebeatVersion -Wait
}