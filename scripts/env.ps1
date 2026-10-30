$ErrorActionPreference = 'Stop'
$SimRoot = 'D:\RoboHarnessSim'
$env:SIM_ROOT = $SimRoot
$env:TEMP = "$SimRoot\tmp"
$env:TMP = "$SimRoot\tmp"
$env:USERPROFILE = "$SimRoot\home"
$env:APPDATA = "$SimRoot\home\AppData\Roaming"
$env:LOCALAPPDATA = "$SimRoot\cache\localappdata"
$env:XDG_CACHE_HOME = "$SimRoot\cache"
$env:XDG_CONFIG_HOME = "$SimRoot\home\.config"
$env:HF_HOME = "$SimRoot\cache\huggingface"
$env:HF_HUB_CACHE = "$SimRoot\cache\huggingface\hub"
$env:HF_DATASETS_CACHE = "$SimRoot\cache\huggingface\datasets"
$env:TORCH_HOME = "$SimRoot\cache\torch"
$env:PIP_CACHE_DIR = "$SimRoot\cache\pip"
$env:PIP_DISABLE_PIP_VERSION_CHECK = '1'
$env:PYTHONNOUSERSITE = '1'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:MPLCONFIGDIR = "$SimRoot\cache\matplotlib"
$env:NUMBA_CACHE_DIR = "$SimRoot\cache\numba"
$env:CUDA_CACHE_PATH = "$SimRoot\cache\cuda"
$env:MAMBA_ROOT_PREFIX = "$SimRoot\tools\mamba"
$env:CONDA_PKGS_DIRS = "$SimRoot\cache\conda-pkgs"
$env:CONDA_ENVS_PATH = "$SimRoot\envs"
$env:CONDARC = "$SimRoot\home\.condarc"
$env:LIBERO_CONFIG_PATH = "$SimRoot\home\.libero"
$env:WANDB_MODE = 'disabled'
$env:WANDB_DIR = "$SimRoot\cache\wandb"
$env:MUJOCO_GL = 'glfw'
$env:OMNI_USER_CONFIG_PATH = "$SimRoot\home\omniverse\config"
$env:OMNI_CACHE_ROOT = "$SimRoot\cache\omniverse"
$env:OMNI_DATA_PATH = "$SimRoot\assets\omniverse"
$env:OMNI_LOG_PATH = "$SimRoot\logs\omniverse"
@($env:TEMP,$env:APPDATA,$env:LOCALAPPDATA,$env:XDG_CONFIG_HOME,$env:HF_HOME,$env:TORCH_HOME,$env:PIP_CACHE_DIR,$env:MPLCONFIGDIR,$env:NUMBA_CACHE_DIR,$env:CUDA_CACHE_PATH,$env:MAMBA_ROOT_PREFIX,$env:CONDA_PKGS_DIRS,$env:LIBERO_CONFIG_PATH,$env:OMNI_USER_CONFIG_PATH,$env:OMNI_CACHE_ROOT,$env:OMNI_DATA_PATH,$env:OMNI_LOG_PATH) | ForEach-Object { [IO.Directory]::CreateDirectory($_) | Out-Null }
function Assert-SimSpace([double]$AdditionalGB = 0) {
  $free = (Get-PSDrive -Name D).Free
  if ($free -lt ((10 + $AdditionalGB) * 1GB)) { throw "D: space guard: must retain 10 GiB; free=$free additionalGB=$AdditionalGB" }
}
Assert-SimSpace

$env:OMNIGIBSON_DATA_PATH = "$SimRoot\assets\behavior"
$env:OMNIGIBSON_APPDATA_PATH = "$SimRoot\cache\omnigibson"
$env:__GL_SHADER_DISK_CACHE_PATH = "$SimRoot\cache\nvidia-gl"
$env:NLTK_DATA = "$SimRoot\cache\nltk"
$env:PIP_NO_COMPILE = "1"
