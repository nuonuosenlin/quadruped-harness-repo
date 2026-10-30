"""Simulation-only RGB/depth/mask/action interface probe based on LIBERO official Task example."""
import os,json,pathlib,time,sys,platform,importlib.metadata as md,shutil
import numpy as np
from PIL import Image
import imageio.v2 as imageio
from libero.libero import benchmark,get_libero_path
from libero.libero.envs import OffScreenRenderEnv
from robosuite.utils import camera_utils
ROOT=pathlib.Path(os.environ["SIM_ROOT"])
OUT=ROOT/"reports"/"libero_probe"
OUT.mkdir(exist_ok=True)
if shutil.disk_usage(str(ROOT)).free<10*1024**3:raise RuntimeError("D: reserve below 10GiB")
suite=benchmark.get_benchmark_dict()["libero_10"]()
task=suite.get_task(0)
env=None
def save_obs(obs,label):
    for camera in ("agentview","robot0_eye_in_hand"):
        rgb=obs[camera+"_image"]
        Image.fromarray(rgb[::-1]).save(OUT/(label+"_"+camera+"_rgb.png"))
        depth=obs[camera+"_depth"]
        metric=camera_utils.get_real_depth_map(env.sim,depth)
        np.save(OUT/(label+"_"+camera+"_depth_m.npy"),metric[::-1].copy())
        raw=np.squeeze(metric)
        valid=np.isfinite(raw)
        lo,hi=np.percentile(raw[valid],[2,98])
        preview=(np.clip((raw-lo)/max(hi-lo,1e-6),0,1)*255).astype(np.uint8)
        Image.fromarray(preview[::-1]).save(OUT/(label+"_"+camera+"_depth_preview.png"))
        seg_key=next((k for k in obs if k.startswith(camera+"_segmentation")),None)
        if seg_key:
            seg=np.squeeze(obs[seg_key]).astype(np.int32)
            np.save(OUT/(label+"_"+camera+"_instance_ids.npy"),seg[::-1].copy())
            colors=np.random.RandomState(0).randint(0,256,(1024,3),dtype=np.uint8)
            Image.fromarray(colors[seg[::-1]%1024]).save(OUT/(label+"_"+camera+"_mask_preview.png"))
    np.savez_compressed(OUT/(label+"_observations.npz"),**{k:v for k,v in obs.items() if isinstance(v,np.ndarray)})
start=time.perf_counter()
try:
    env=OffScreenRenderEnv(bddl_file_name=os.path.join(get_libero_path("bddl_files"),task.problem_folder,task.bddl_file),camera_heights=256,camera_widths=256,camera_depths=True,camera_segmentations="instance")
    env.seed(0)
    env.reset()
    obs=env.set_init_state(suite.get_task_init_states(0)[0])
    for _ in range(10):obs,_,_,_=env.step(np.zeros(7))
    save_obs(obs,"before")
    before=np.asarray(obs["robot0_eef_pos"]).copy()
    joint_before=np.asarray(obs["robot0_joint_pos"]).copy()
    frames=[];positions=[];actions=[]
    for i in range(60):
        action=np.zeros(7,dtype=np.float32)
        if i<20:action[0]=0.3
        elif i<40:action[2]=0.3
        else:action[0]=-0.3
        obs,reward,done,info=env.step(action)
        frames.append(np.ascontiguousarray(obs["agentview_image"][::-1]))
        positions.append(np.asarray(obs["robot0_eef_pos"]).tolist())
        actions.append(action.tolist())
    save_obs(obs,"after")
    imageio.mimwrite(str(OUT/"action_demo.mp4"),frames,fps=20,macro_block_size=1)
    after=np.asarray(obs["robot0_eef_pos"]).copy()
    displacement=np.linalg.norm(after-before)
    if displacement<1e-4:raise AssertionError("no measurable EEF displacement")
    if not np.isfinite(obs["agentview_depth"]).all():raise AssertionError("non-finite depth")
    if np.std(obs["agentview_image"])<1:raise AssertionError("blank image")
    cam_info={}
    for cam in ("agentview","robot0_eye_in_hand"):
        cam_info[cam]={"K":camera_utils.get_camera_intrinsic_matrix(env.sim,cam,256,256).tolist(),"T_camera_to_world":camera_utils.get_camera_extrinsic_matrix(env.sim,cam).tolist()}
    low,high=env.env.action_spec
    controller=env.robots[0].controller
    controller_info={name:np.asarray(getattr(controller,name)).tolist() for name in ("input_min","input_max","output_min","output_max","control_dim","use_delta","control_ori","uncouple_pos_ori") if hasattr(controller,name)}
    versions={p:md.version(p) for p in ("libero","robosuite","mujoco","numpy","torch","opencv-python","numba")}
    result={"status":"passed","task":task.name,"language":task.language,"task_completion_claimed":False,"control_steps":60,"control_freq_hz":env.env.control_freq,"eef_before_m":before.tolist(),"eef_after_m":after.tolist(),"eef_displacement_m":float(displacement),"joint_before_rad":joint_before.tolist(),"joint_after_rad":np.asarray(obs["robot0_joint_pos"]).tolist(),"observations":{k:{"shape":list(v.shape),"dtype":str(v.dtype)} for k,v in obs.items() if hasattr(v,"shape")},"action_low":np.asarray(low).tolist(),"action_high":np.asarray(high).tolist(),"controller":controller_info,"camera_calibration":cam_info,"segmentation_instances":env.env.model.instances_to_ids,"instance_mask_id_by_name":{name:i+1 for i,name in enumerate(env.env.model.instances_to_ids)},"export_convention":{"png_and_separate_npy":"aligned top-left origin; RGB/depth/mask","raw_observations_npz":"original OpenGL row order"},"versions":versions,"python":sys.version,"platform":platform.platform(),"elapsed_seconds":time.perf_counter()-start,"MUJOCO_GL":os.getenv("MUJOCO_GL"),"cwd":os.getcwd(),"paths":{"output":str(OUT),"config":os.getenv("LIBERO_CONFIG_PATH")}}
    (OUT/"result.json").write_text(json.dumps(result,indent=2,default=str),encoding="utf-8")
    (OUT/"actions_and_eef.json").write_text(json.dumps({"actions":actions,"eef_positions_world_m":positions},indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2,default=str))
finally:
    if env is not None:env.close()

