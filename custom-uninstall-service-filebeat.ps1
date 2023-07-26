param([String]$serviceName="filebeat")

# Delete and stop the service if it already exists.
if (Get-Service $serviceName -ErrorAction SilentlyContinue) {
  Stop-Service $serviceName
  (Get-Service $serviceName).WaitForStatus('Stopped')
  Start-Sleep -s 1
  sc.exe delete $serviceName
}
