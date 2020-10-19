$url = "https://gist.githubusercontent.com/MarkTiedemann/c42bc1d01138e33b2d37cce7b3aad45c/raw/6ae485562ae3a6dc14622f0d4fce33b1c43dec63/download.cmd"
$file = "file.txt"
$ProgressPreference = "SilentlyContinue";
Invoke-WebRequest -Uri $url -outfile $file