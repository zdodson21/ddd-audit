# PowerShell Test File
Set-Location .\test-element;

Write-Host "Running tests" -f Blue;
py ../main.py;

Set-Location ..;