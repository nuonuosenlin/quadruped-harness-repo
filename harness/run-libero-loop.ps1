$ErrorActionPreference = 'Stop'
. "$PSScriptRoot\..\scripts\env.ps1"
if (-not $env:DASHSCOPE_API_KEY) {
    $env:DASHSCOPE_API_KEY = [Environment]::GetEnvironmentVariable('DASHSCOPE_API_KEY', 'User')
}
Assert-SimSpace
Set-Location 'D:\RoboHarnessSim\LIBERO'
& 'D:\RoboHarnessSim\tools\Library\bin\micromamba.exe' run --prefix 'D:\RoboHarnessSim\envs\libero' python -B "$PSScriptRoot\libero_loop.py"
if ($LASTEXITCODE -ne 0) { throw 'LIBERO loop stopped. Review the reported result.json; do not retry automatically.' }
