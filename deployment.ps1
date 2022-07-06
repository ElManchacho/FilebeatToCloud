# delete git config


# unzip
Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip
{
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}

#Unzip "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\filebeat-8.3.1-windows-x86_64.zip" "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\Filebeat"

# delete zipped folder

#Remove-Item "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\filebeat-8.3.1-windows-x86_64.zip"

# installer python
#Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe" -OutFile "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\python-3.10.5-amd64.exe"
#Invoke-Expression -Command "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\python-3.10.5-amd64.exe"

# script python pour demander des paramètres pour config le .yaml + lien vers cloud et/ou kibana

# remplacer le .yaml

# script d'instanciation du service filebeat blablabla.ps1

# start service

# générer des logs basiques pour faire un tests de création d'index

# renvoyer vers le cloud ou kibana

# delete python installer
#Remove-Item "C:\Users\paul.leroyducardonno\Desktop\Hot_Projects\FileBeat\FilebeatToCloud\filebeat-8.3.1-windows-x86_64.zip"