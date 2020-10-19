ECHO OFF
ECHO Deleting Not Required Files
del "files/ch.bat"
del "files/key.pyw"
del download.ps1
del step1.bat
del step2.bat
del step3.bat
rmdir files /Q /S
del step4.bat
ECHO Done
PAUSE