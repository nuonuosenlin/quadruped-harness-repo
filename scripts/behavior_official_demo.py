"""Run the unmodified official robot_control_example with its supported empty-scene option."""
import os,pathlib,json,traceback,time
ROOT=pathlib.Path(os.environ["SIM_ROOT"])
os.environ["OMNIGIBSON_DATA_PATH"]=str(ROOT/"assets"/"behavior")
os.environ["OMNIGIBSON_APPDATA_PATH"]=str(ROOT/"cache"/"omnigibson")
os.environ["OMNIGIBSON_HEADLESS"]="1"
os.environ["OMNI_KIT_ACCEPT_EULA"]="YES"
out=ROOT/"reports"/"behavior_official";out.mkdir(exist_ok=True)
import omnigibson as og
from omnigibson.macros import gm
gm.USE_GPU_DYNAMICS=False
gm.ENABLE_HQ_RENDERING=False
gm.ENABLE_OBJECT_STATES=False
gm.ENABLE_TRANSITION_RULES=False
from omnigibson.examples.robots import robot_control_example as demo
original=demo.choose_from_options
def choices(options,name,random_selection=False,**kwargs):
    if name=="scene":return "empty"
    if name=="robot":return "fetch"
    if name=="control mode":return "random"
    if name.endswith(" controller"):
        preferred={"base controller":"DifferentialDriveController","arm_0 controller":"InverseKinematicsController","gripper_0 controller":"MultiFingerGripperController","camera controller":"JointController","trunk controller":"JointController"}
        choice=preferred.get(name)
        if choice in options:return choice
        raise ValueError(f"Unsupported controller choices: {name} {options}")
    return original(options=options,name=name,random_selection=True,**kwargs)
demo.choose_from_options=choices
t=time.monotonic()
real_shutdown=og.shutdown
def observed_shutdown(*args,**kwargs):
    import inspect
    caller=inspect.currentframe().f_back
    if caller.f_code.co_filename==demo.__file__ and caller.f_locals.get("step")==100:
        result={"status":"passed","scene":"empty","robot":"fetch","steps":100,"source_file":demo.__file__,"source_modified":False,"selection":"Official empty/Fetch/random actions; deterministic default IK controllers.","elapsed_seconds":time.monotonic()-t,"evidence":"Reached official shutdown after 100 successful env.step calls; written before SimulationApp.close exits the process."}
        (out/"result.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
        print(json.dumps(result,indent=2),flush=True)
    return real_shutdown(*args,**kwargs)
og.shutdown=observed_shutdown
try:
    demo.main(random_selection=False,headless=True,short_exec=True,quickstart=False)
except BaseException as e:
    if isinstance(e,SystemExit) and e.code in (None,0):raise
    (out/"result.json").write_text(json.dumps({"status":"failed","error":repr(e),"traceback":traceback.format_exc()},indent=2))
    raise
