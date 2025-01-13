$ErrorActionPreference="Stop"

Write-Host "It's going to use:"
pip -V

Write-Host "Enter Anything To Confirm: " -NoNewline
[Console]::ReadLine()

New-Item -Force -Path "./dist" -ItemType Directory
New-Item -Force -Path "./statictorch.egg-info" -ItemType Directory
Remove-Item "./dist" -Recurse
Remove-Item "./statictorch.egg-info" -Recurse

python -m build "."

twine upload "./dist/*"
