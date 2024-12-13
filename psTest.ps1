# PowerShell Test File. Not maintained for Linux or macOS.
Set-Location .\test-element;

Write-Host "Running tests" -f Blue;
py ../main.py;

Set-Location ..;