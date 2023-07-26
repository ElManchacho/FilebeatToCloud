param([String]$serviceName="filebeat")

$serviceName = "filebeat"
$displayName = $serviceName.Replace($serviceName[0], $serviceName[0].ToString().ToUpper())

$alreadyExists = (Get-Service $displayName).Name = $serviceName

if ($alreadyExists)
{
  $serviceName = $serviceName+"_"+([guid]::NewGuid()).Guid
  $displayName = $serviceName.Replace($serviceName[0], $serviceName[0].ToString().ToUpper())
}

$serviceName
$displayName

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
  -binaryPathName "`"$workdir\filebeat.exe`" --environment=windows_service -c `"$workdir\filebeat.yml`" --path.home `"$workdir`" --path.data `"$env:PROGRAMDATA\filebeat`" --path.logs `"$env:PROGRAMDATA\filebeat\logs`" -E logging.files.redirect_stderr=true"

# Attempt to set the service to delayed start using sc config.
Try {
  Start-Process -FilePath sc.exe -ArgumentList 'config filebeat start= delayed-auto'
}
Catch { Write-Host -f red "An error occured setting the service to delayed start." }
