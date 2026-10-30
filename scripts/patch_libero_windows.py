import pathlib,difflib
ROOT=pathlib.Path(r"D:\RoboHarnessSim")
base=ROOT/"envs"/"libero"/"Lib"/"site-packages"/"robosuite"
backup=ROOT/"scripts"/"vendor-originals"/"robosuite"
patch_file=ROOT/"reports"/"libero-windows-compat.patch"
def patch(rel,old,new):
    target=base/rel
    before=target.read_text(encoding="utf-8")
    if new in before:
        print("Already applied:",rel);return
    if before.count(old)!=1:raise RuntimeError("Expected exactly one replacement: "+rel)
    dest=backup/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists():dest.write_text(before,encoding="utf-8")
    after=before.replace(old,new)
    target.write_text(after,encoding="utf-8")
    diff="".join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile="original/robosuite/"+rel,tofile="local/robosuite/"+rel))
    with patch_file.open("a",encoding="utf-8") as f:f.write(diff)
    print("Applied:",rel)
patch("utils/binding_utils.py",'ctypes.WinDLL(os.path.join(os.path.dirname(__file__), "mujoco.dll"))','ctypes.WinDLL(os.path.join(os.path.dirname(mujoco.__file__), "mujoco.dll"))')
patch("utils/mjcf_utils.py",'if xml_path.startswith("/"):', 'if os.path.isabs(xml_path):')

