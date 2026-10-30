param([ValidateSet('official','probe','all')][string]$Mode='all')
. "$PSScriptRoot\env.ps1"
Set-Location "$env:SIM_ROOT\LIBERO"
$MambaExe = "$env:SIM_ROOT\tools\Library\bin\micromamba.exe"
$EnvPrefix = "$env:SIM_ROOT\envs\libero"
Assert-SimSpace
if ($Mode -in @('official','all')) {
    & $MambaExe run --prefix $EnvPrefix python "$PSScriptRoot\libero_official_demo.py" 2>&1 | Tee-Object -FilePath "$env:SIM_ROOT\logs\libero-official-demo.log"
    if ($LASTEXITCODE -ne 0) { throw "LIBERO official demo failed, exit=$LASTEXITCODE; see logs." }
}
if ($Mode -in @('probe','all')) {
    & $MambaExe run --prefix $EnvPrefix python "$PSScriptRoot\libero_interface_probe.py" 2>&1 | Tee-Object -FilePath "$env:SIM_ROOT\logs\libero-interface-probe.log"
    if ($LASTEXITCODE -ne 0) { throw "LIBERO interface probe failed, exit=$LASTEXITCODE; see logs." }
}

