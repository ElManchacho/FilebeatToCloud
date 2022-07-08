# delete git config ?



# unzip
Add-Type -AssemblyName System.IO.Compression
function Unzip
{
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}
$location = Get-Location

Unzip $location"\filebeat-8.3.1-windows-x86_64.zip" $location -Wait

# installer python
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe" -OutFile $location"\python-3.10.5-amd64.exe"

Start-Process -Wait -FilePath $location"\python-3.10.5-amd64.exe"  -Argument "/silent" -PassThru

# script python pour demander des paramètres pour config le .yaml + lien vers cloud et/ou kibana

py "./py-scripts/main.py" -Wait

# remplacer le .yaml

# script d'instanciation du service filebeat blablabla.ps1

# start service

# générer des logs basiques pour faire un tests de création d'index

# renvoyer vers le cloud ou kibana

# delete python installer
#Remove-Item "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\filebeat-8.3.1-windows-x86_64.zip" -Wait
#Remove-Item "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\python-3.10.5-amd64.exe"