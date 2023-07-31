param([parameter(Mandatory=$false)][String]$serviceName = "filebeat")

$filebeatVersion = "filebeat-8.8.2-windows-x86_64"

$displayName = $serviceName.Replace($serviceName[0], $serviceName[0].ToString().ToUpper())

try {
  $alreadyExists = (Get-Service $displayName).Name = $serviceName
  if ($alreadyExists)
  {
    $serviceName = $serviceName+"_"+([guid]::NewGuid()).Guid
    $displayName = $serviceName.Replace($serviceName[0], $serviceName[0].ToString().ToUpper())
  }
}
catch {
 "No service create yet, creating one right now ..."
}



# Delete and stop the service if it already exists.
if (Get-Service $serviceName -ErrorAction SilentlyContinue) {
  Stop-Service $serviceName
  (Get-Service $serviceName).WaitForStatus('Stopped')
  Start-Sleep -s 1
  sc.exe delete $serviceName
}

$workdir = Split-Path $MyInvocation.MyCommand.Path

# Create the new service.
New-Service -name $serviceName `
  -displayName $displayName `
  -binaryPathName "`"$workdir\$filebeatVersion\filebeat.exe`" --environment=windows_service -c `"$workdir\$filebeatVersion\filebeat.yml`" --path.home `"$workdir\$filebeatVersion`" --path.data `"$env:PROGRAMDATA\filebeat`" --path.logs `"$env:PROGRAMDATA\filebeat\logs`" -E logging.files.redirect_stderr=true"

# Attempt to set the service to delayed start using sc config.
Try {
  Start-Process -FilePath sc.exe -ArgumentList 'config filebeat start= delayed-auto'
}
Catch { Write-Host -f red "An error occured setting the service to delayed start." }
