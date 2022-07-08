# delete git config ?


# unzip function instanciation

Add-Type -AssemblyName System.IO.Compression
function Unzip
{
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}

# deployment folder location instanciation

$location = (Get-Location).Path

# unzip filbeat

Unzip $location"\filebeat-8.3.1-windows-x86_64.zip" $location

# let time to unzip folder

Start-Sleep -s 10

# remove filebeat zip folder

Remove-Item $location"\filebeat-8.3.1-windows-x86_64.zip"

# download python 3.10.5 (last version on 08/07/2022)

Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe" -OutFile $location"\python-3.10.5-amd64.exe"

# install python

Start-Process -Wait -FilePath $location"\python-3.10.5-amd64.exe"  -Argument "/silent" -PassThru

# let time for python to install

Start-Sleep -s 15

# download pip python installer script

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# install pip

py .\get-pip.py

# remove pip install script

Remove-Item $location"\get-pip.py"

# get pip path

$pipPath = ((Get-Command python).Source).Replace("python.exe","")+"Scripts"

# add pip path variable

$path = [System.Environment]::GetEnvironmentVariable(
    'PATH',
    'Machine'
)

[System.Environment]::SetEnvironmentVariable(
    'PATH',
    $path+$pipPath+";",
    'Machine'
)

# let time for pip to install + add path variable

Start-Sleep -s 10

# delete python installer

Remove-Item $location"\python-3.10.5-amd64.exe"

# install pip package for python script purpose

pip install pyyaml

py "./py-scripts/main.py" -Wait

# remplacer le .yaml

# script d'instanciation du service filebeat blablabla.ps1

# start service

# générer des logs basiques pour faire un tests de création d'index

# renvoyer vers le cloud ou kibana