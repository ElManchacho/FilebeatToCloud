# deployment folder location instanciation

$location = (Get-Location).Path

# unistall existing filebeat service

Invoke-Expression -Command $location"\filebeat-8.3.1-windows-x86_64\uninstall-service-filebeat.ps1"

# remove existing installation

Remove-Item -Recurse -Force $location"\filebeat-8.3.1-windows-x86_64"

# unzip function instanciation

Add-Type -AssemblyName System.IO.Compression

# unzip filbeat

Expand-Archive -Path $location"\filebeat-8.3.1-windows-x86_64.zip" -DestinationPath $location

# let time to unzip folder

Start-Sleep -s 10

# replace filebeat.yml from unzipped folder with almost ready filebeat file

Remove-Item $location"\filebeat-8.3.1-windows-x86_64\filebeat.yml"

Copy-Item -Path $location"\filebeat.yml" -Destination $location"\filebeat-8.3.1-windows-x86_64\filebeat.yml"

# download python 3.10.5 (last version on 08/07/2022)

Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe" -OutFile $location"\python-3.10.5-amd64.exe"

# install python

Start-Process -Wait -FilePath $location"\python-3.10.5-amd64.exe"  -Argument "/silent" -PassThru

# let time for python to install

Start-Sleep -s 15

# delete python installer

Remove-Item $location"\python-3.10.5-amd64.exe"

download pip python installer script

Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# install pip

py .\get-pip.py

# remove pip install script

Remove-Item $location"\get-pip.py"

# get pip path

$pipPath = ((Get-Command python).Source).Replace("python.exe","")+"Scripts"
$pipPath = ((Get-Command py).Source).Replace("py.exe","")+"Scripts"

"pipPath : " + $pipPath

# add pip path variable

$envVariables = [System.Environment]::GetEnvironmentVariable(
    'PATH',
    'Machine'
)

[System.Environment]::SetEnvironmentVariable(
    'PATH',
    $envVariables+$pipPath+";",
    'Machine'
)

$test = 'Jalon'

$test
"path : " + $envVariables
"pipPath : " + $pipPath

# let time for pip to install + add path variable

Start-Sleep -s 10

# install pip packages for python script purpose

pip install pyyaml

Start-Sleep -s 10

pip install python-dotenv

py "./py-scripts/main.py" -Wait

# renvoyer vers le cloud ou kibana
