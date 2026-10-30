. "$PSScriptRoot\env.ps1"
Assert-SimSpace 8
$MambaExe = "$env:SIM_ROOT\tools\Library\bin\micromamba.exe"
$EnvPrefix = "$env:SIM_ROOT\envs\libero"
if (-not (Test-Path -LiteralPath "$EnvPrefix\python.exe")) {
    & $MambaExe create --prefix $EnvPrefix --override-channels -c conda-forge python=3.8.13 pip=24.3.1 -y
    if ($LASTEXITCODE -ne 0) { throw 'Python environment creation failed' }
}
& $MambaExe run --prefix $EnvPrefix python -m pip install --timeout 120 --retries 5 -r "$PSScriptRoot\libero-simulation-requirements.txt" -c "$PSScriptRoot\libero-constraints.txt" torch==1.11.0 torchvision==0.12.0 mujoco==2.3.7 imageio imageio-ffmpeg h5py
if ($LASTEXITCODE -ne 0) { throw 'LIBERO dependencies failed' }
& $MambaExe run --prefix $EnvPrefix python -m pip install -e "$env:SIM_ROOT\LIBERO" --no-deps
if ($LASTEXITCODE -ne 0) { throw 'LIBERO editable install failed' }
Copy-Item -LiteralPath "$PSScriptRoot\robosuite-macros-private.py" -Destination "$EnvPrefix\Lib\site-packages\robosuite\macros_private.py"
& $MambaExe run --prefix $EnvPrefix python "$PSScriptRoot\patch_libero_windows.py"
if ($LASTEXITCODE -ne 0) { throw 'Windows compatibility patch failed' }

