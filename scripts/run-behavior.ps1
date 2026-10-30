param([ValidateSet('official','probe','all')][string]$Mode='all')
. "$PSScriptRoot\env.ps1"
Assert-SimSpace
$env:OMNI_KIT_ACCEPT_EULA = 'YES'
$env:OMNIGIBSON_HEADLESS = '1'
$env:HF_HUB_OFFLINE = '1'
$env:TRANSFORMERS_OFFLINE = '1'
Set-Location "$env:SIM_ROOT\BEHAVIOR-1K\OmniGibson"
$MambaExe = "$env:SIM_ROOT\tools\Library\bin\micromamba.exe"
$EnvPrefix = "$env:SIM_ROOT\envs\behavior"
if ($Mode -in @('official','all')) {
    & $MambaExe run --prefix $EnvPrefix python "$PSScriptRoot\behavior_official_demo.py" 2>&1 | Tee-Object -FilePath "$env:SIM_ROOT\logs\behavior-official-demo.log"
    if ($LASTEXITCODE -ne 0) { throw "BEHAVIOR official demo failed: $LASTEXITCODE. See D-drive logs." }
}
if ($Mode -in @('probe','all')) {
    & $MambaExe run --prefix $EnvPrefix python "$PSScriptRoot\behavior_interface_probe.py" 2>&1 | Tee-Object -FilePath "$env:SIM_ROOT\logs\behavior-interface-probe.log"
    if ($LASTEXITCODE -ne 0) { throw "BEHAVIOR interface probe failed: $LASTEXITCODE. See D-drive logs." }
}

