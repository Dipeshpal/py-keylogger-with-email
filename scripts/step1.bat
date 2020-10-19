ECHO OFF
ECHO Downloading required files
mkdir files
Powershell.exe -File download.ps1
ECHO Downloaded files
ECHO Done
PAUSE