"""Minimal empty-scene interface probe based on the official v3.9.1 robot_control_example."""
import os,pathlib,json,traceback,time,sys,shutil
ROOT=pathlib.Path(os.environ["SIM_ROOT"]);OUT=ROOT/"reports"/"behavior_probe";OUT.mkdir(exist_ok=True)
os.environ["OMNIGIBSON_DATA_PATH"]=str(ROOT/"assets"/"behavior")
os.environ["OMNIGIBSON_APPDATA_PATH"]=str(ROOT/"cache"/"omnigibson")
os.environ["OMNIGIBSON_HEADLESS"]="1"
os.environ["OMNI_KIT_ACCEPT_EULA"]="YES"
started=time.monotonic();og=None
def arr(v):
    import numpy as np
    return v.detach().cpu().numpy() if hasattr(v,"detach") else np.asarray(v)
try:
    if shutil.disk_usage(str(ROOT)).free<10*1024**3:raise RuntimeError("D: reserve below 10GiB")
    import numpy as np
    import torch
    from PIL import Image
    import imageio.v2 as imageio
    import omnigibson as og
    from omnigibson.macros import gm
    gm.USE_GPU_DYNAMICS=False
    gm.ENABLE_HQ_RENDERING=False
    gm.ENABLE_OBJECT_STATES=False
    gm.ENABLE_TRANSITION_RULES=False
    # Minimal empty scene has a built-in ground plane but no household category folders.
    # Register only official structural names in the runtime category registry; no data assets are fabricated.
    from omnigibson.utils import constants as og_constants
    og_constants.OBJECT_CATEGORIES.update(og_constants.STRUCTURE_CATEGORIES)
    og_constants.semantic_class_name_to_id.cache_clear()
    og_constants.semantic_class_id_to_name.cache_clear()
    cfg={"scene":{"type":"Scene"},"robots":[{"model":"fetch","obs_modalities":["proprio"],"action_type":"continuous","action_normalize":True}],"env":{"action_frequency":20,"rendering_frequency":20,"physics_frequency":120,"external_sensors":[{"sensor_type":"VisionSensor","name":"probe_cam","modalities":["rgb","depth","depth_linear","seg_instance"],"sensor_kwargs":{"image_height":256,"image_width":256,"clipping_range":[0.01,20.0]},"position":[-0.201028,-2.72566,1.0654],"orientation":[0.68196617,-0.00155408,-0.00166678,0.73138017]}]},"render":{"viewer_width":256,"viewer_height":256}}
    env=og.Environment(configs=cfg);robot=env.robots[0]
    obs,info=env.reset()
    for _ in range(10):obs,_,_,_,info=env.step(torch.zeros(robot.action_dim))
    for _ in range(12):og.sim.render()
    obs,info=env.get_obs()
    print("SENSOR_STATS",{k:{"shape":list(arr(v).shape),"min":float(np.nanmin(arr(v))),"max":float(np.nanmax(arr(v)))} for k,v in obs["external"]["probe_cam"].items()},flush=True)
    camera=env.external_sensors["probe_cam"]
    depth_evidence={}
    before=arr(robot.get_position_orientation()[0]).copy()
    def save_obs(label,obs):
        camera=obs["external"]["probe_cam"]
        rgb=arr(camera["rgb"])[...,:3].astype(np.uint8)
        depth=arr(camera["depth_linear"]).copy()
        radial=arr(camera["depth"]).copy()
        np.save(OUT/(label+"_depth_linear_native_m.npy"),depth)
        np.save(OUT/(label+"_depth_radial_native_m.npy"),radial)
        source="native depth_linear"
        if not (np.isfinite(depth)&(depth>0)).any():
            sensor=env.external_sensors["probe_cam"]
            K=arr(sensor.intrinsic_matrix)
            yy,xx=np.indices(radial.shape,dtype=np.float32)
            depth=radial/np.sqrt(1+((xx-K[0,2])/K[0,0])**2+((yy-K[1,2])/K[1,1])**2)
            source="geometric conversion from native radial depth and actual camera K; native depth_linear is all zero"
        depth_evidence[label]={"source":source,"valid_positive_pixels":int((np.isfinite(depth)&(depth>0)).sum()),"native_radial_min_finite_m":float(np.min(radial[np.isfinite(radial)&(radial>0)]))}
        seg=arr(camera["seg_instance"]).astype(np.int32)
        Image.fromarray(rgb).save(OUT/(label+"_rgb.png"))
        np.save(OUT/(label+"_depth_imageplane_m.npy"),depth)
        np.save(OUT/(label+"_instance_ids.npy"),seg)
        valid=np.isfinite(depth)&(depth>0)
        if not valid.any():raise AssertionError("No valid finite depth")
        lo,hi=np.percentile(depth[valid],[2,98])
        Image.fromarray((np.clip((np.nan_to_num(depth,posinf=hi)-lo)/max(hi-lo,1e-6),0,1)*255).astype(np.uint8)).save(OUT/(label+"_depth_preview.png"))
        colors=np.random.RandomState(0).randint(0,256,(1024,3),dtype=np.uint8)
        Image.fromarray(colors[seg%1024]).save(OUT/(label+"_mask_preview.png"))
        if np.std(rgb)<1:raise AssertionError("RGB appears blank")
        return rgb
    save_obs("before",obs)
    idx=robot.controller_action_idx
    base_idx=arr(idx["base"]).astype(int)
    frames=[]
    for i in range(60):
        action=torch.zeros(robot.action_dim)
        action[int(base_idx[0])]=0.1
        obs,reward,terminated,truncated,info=env.step(action)
        frames.append(arr(obs["external"]["probe_cam"]["rgb"])[...,:3].astype(np.uint8))
    after=arr(robot.get_position_orientation()[0]).copy()
    save_obs("after",obs)
    displacement=float(np.linalg.norm((after-before)[:2]))
    if displacement<1e-4:raise AssertionError("No measurable base motion")
    imageio.mimwrite(str(OUT/"action_demo.mp4"),frames,fps=20,macro_block_size=1)
    camera=env.external_sensors["probe_cam"]
    result={"status":"passed","scene":"empty Scene (official demo option)","household_assets_installed":False,"task_completion_claimed":False,"source":"https://github.com/StanfordVL/BEHAVIOR-1K/blob/v3.9.1/OmniGibson/omnigibson/examples/robots/robot_control_example.py","model":"fetch","control_steps":60,"base_before_m":before.tolist(),"base_after_m":after.tolist(),"base_xy_displacement_m":displacement,"depth_evidence":depth_evidence,"camera_intrinsic_matrix":arr(camera.intrinsic_matrix).tolist(),"camera_position_world_m":arr(camera.get_position_orientation(frame="world")[0]).tolist(),"camera_orientation_world_xyzw":arr(camera.get_position_orientation(frame="world")[1]).tolist(),"export_convention":"Omniverse sensor output as returned; camera pose uses USD camera local axes (+X right,+Y up,-Z forward); convert to OpenCV optical axes with diag(1,-1,-1).", "action_dim":robot.action_dim,"controller_order":robot.controller_order,"controller_action_idx":{k:arr(v).tolist() for k,v in idx.items()},"mask_instance_ids_counts":{str(k):int(v) for k,v in zip(*np.unique(arr(obs["external"]["probe_cam"]["seg_instance"]),return_counts=True))},"observations":{k:{"shape":list(arr(v).shape),"dtype":str(arr(v).dtype)} for k,v in obs["external"]["probe_cam"].items()},"joint_positions_rad":arr(robot.get_joint_positions()).tolist(),"segmentation_info":info,"torch":torch.__version__,"cuda_available":torch.cuda.is_available(),"elapsed_seconds":time.monotonic()-started}
    (OUT/"result.json").write_text(json.dumps(result,indent=2,default=str),encoding="utf-8")
    print(json.dumps(result,indent=2,default=str),flush=True)
except BaseException as e:
    result={"status":"failed","error":repr(e),"traceback":traceback.format_exc(),"elapsed_seconds":time.monotonic()-started}
    (OUT/"result.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    traceback.print_exc()
    sys.exit(1)
finally:
    if og is not None:
        try:og.shutdown()
        except BaseException:pass


