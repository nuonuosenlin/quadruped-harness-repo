param([ValidateRange(0, 2147483647)][int]$InitialStateIndex = 0, [switch]$Grasp)

$ErrorActionPreference = 'Stop'
. 'D:\RoboHarnessSim\scripts\env.ps1'
if ($Grasp -and -not $env:DASHSCOPE_API_KEY) { throw 'DASHSCOPE_API_KEY is missing from the process environment' }
if (-not $env:DASHSCOPE_API_KEY) {
    $env:DASHSCOPE_API_KEY = [Environment]::GetEnvironmentVariable('DASHSCOPE_API_KEY', 'User')
}
Assert-SimSpace
Set-Location 'D:\RoboHarnessSim\LIBERO'
$graspArgs = @()
if ($Grasp) { $graspArgs += '--grasp' }
& 'D:\RoboHarnessSim\tools\Library\bin\micromamba.exe' run --prefix 'D:\RoboHarnessSim\envs\libero' python -B 'D:\RoboHarnessSim\harness\libero_loop.py' --initial-state-index $InitialStateIndex @graspArgs
if ($LASTEXITCODE -ne 0) { throw 'LIBERO loop stopped. Review the reported result.json; do not retry automatically.' }
