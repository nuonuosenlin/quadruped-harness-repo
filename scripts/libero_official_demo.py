"""Official LIBERO README Task example, adding missing imports and a result record.
Source: https://github.com/Lifelong-Robot-Learning/LIBERO#task
No policy, model weights, or demonstration dataset are used.
"""
import json, os, pathlib, time
from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv
root=pathlib.Path(os.environ["SIM_ROOT"])
out=root/"reports"/"libero_official"
out.mkdir(exist_ok=True)
task_suite=benchmark.get_benchmark_dict()["libero_10"]()
task=task_suite.get_task(0)
bddl=os.path.join(get_libero_path("bddl_files"),task.problem_folder,task.bddl_file)
env=None
start=time.perf_counter()
try:
    env=OffScreenRenderEnv(bddl_file_name=bddl,camera_heights=128,camera_widths=128)
    env.seed(0)
    env.reset()
    states=task_suite.get_task_init_states(0)
    env.set_init_state(states[0])
    for step in range(10):
        obs,reward,done,info=env.step([0.]*7)
    result={"status":"passed","source":"LIBERO README Task example","task":task.name,"language":task.language,"steps":10,"observation_shapes":{k:list(v.shape) for k,v in obs.items() if hasattr(v,"shape")},"reward":float(reward),"done":bool(done),"elapsed_seconds":time.perf_counter()-start}
    (out/"result.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
finally:
    if env is not None:env.close()

