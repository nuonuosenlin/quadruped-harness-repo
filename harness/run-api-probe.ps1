$ErrorActionPreference = 'Stop'
. "$PSScriptRoot\..\scripts\env.ps1"
if (-not $env:DASHSCOPE_API_KEY) {
    $env:DASHSCOPE_API_KEY = [Environment]::GetEnvironmentVariable('DASHSCOPE_API_KEY', 'User')
}
Assert-SimSpace
& 'D:\RoboHarnessSim\envs\libero\python.exe' -B "$PSScriptRoot\api_probe.py"
if ($LASTEXITCODE -ne 0) { throw 'API preflight failed. Stop here; inspect the result.json path above.' }
