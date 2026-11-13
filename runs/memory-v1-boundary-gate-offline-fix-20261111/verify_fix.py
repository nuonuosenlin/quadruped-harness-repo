"""Offline replay/source audit only: no model, simulator, credential, or network."""
from pathlib import Path
import ast
import difflib
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from go2_demo.experimental_boundary_gate import experimental_boundary_gate, EXPERIMENTAL_SUPPORT_MARGIN_M
from go2_demo.scenarios import get_scenario


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    episode = ROOT / "runs/memory-v1-h2-search-budget-rerun-20261111-s0/H2/20261111-152723-api-memory_ab_occluded_v1-s0-62de9d"
    rows = [json.loads(s) for s in (episode / "events.jsonl").read_text().splitlines()]
    trajectory = [json.loads(s) for s in (episode / "trajectory.jsonl").read_text().splitlines()]
    results = {r["turn"]: r for r in rows if r["event"] == "tool_results"}
    scene = get_scenario("memory_ab_occluded_v1")
    moves = []
    for row in rows:
        if row["event"] != "model_response":
            continue
        for call in row["calls"]:
            if call["name"] != "move_relative":
                continue
            turn = row["turn"]
            previous = results[turn - 1]
            sim_time = previous["next_observation"]["sim_time_s"]
            pose_row = min(trajectory, key=lambda r: abs(r["sim_time_s"] - sim_time))
            assert abs(pose_row["sim_time_s"] - sim_time) < 1e-7
            x, y, _ = pose_row["base_xyz_m"]
            yaw = pose_row["yaw_rad"]
            args = call["arguments"]
            feedback = experimental_boundary_gate(scene, [x, y, yaw], **args)
            f, l = args["forward_m"], args["lateral_m"]
            target = [x + math.cos(yaw)*f - math.sin(yaw)*l,
                      y + math.sin(yaw)*f + math.cos(yaw)*l]
            original = next(r for r in results[turn]["results"] if r["call_id"] == call["call_id"])
            moves.append({"decision": turn + 1, "sim_time_before_s": sim_time,
                          "pose_source": "recorded_simulator_ground_truth_control_trajectory",
                          "start_base_xy_yaw": [x,y,yaw], "arguments": args,
                          "nominal_center_endpoint_xy_m": target,
                          "original_status": original["status"], "original_error_code": original.get("error_code"),
                          "allowed_by_experimental_gate": feedback is None, "refusal": feedback})
    assert len(moves) == 28
    assert all(m["allowed_by_experimental_gate"] for m in moves[:10])
    fatal = next(m for m in moves if m["decision"] == 99)
    assert fatal["original_error_code"] == "ROBOT_FELL"
    assert fatal["refusal"]["error_code"] == "BOUNDARY_BLOCKED"
    assert fatal["refusal"]["constraint_feedback"]["blocked_directions"] == ["north"]
    assert fatal["nominal_center_endpoint_xy_m"][1] < scene.floor_half_size_m[1]
    replay = {"source_episode": str(episode), "source_files_sha256": {
        name: digest(episode/name) for name in ("metrics.json","events.jsonl","trajectory.jsonl")},
        "platform_half_size_from_scenario_m": list(scene.floor_half_size_m),
        "experimental_support_margin_m": EXPERIMENTAL_SUPPORT_MARGIN_M,
        "first_ten_move_decisions": [m["decision"] for m in moves[:10]],
        "first_ten_all_allowed": True, "fatal_move_99_blocked": True,
        "blocked_decisions_on_original_pose_trace": [m["decision"] for m in moves if not m["allowed_by_experimental_gate"]],
        "moves": moves,
        "interpretation": "Counterfactual command rejection at recorded GT poses only; no new physics or API. "
                          "Original later poses are not the route a gated run would follow. This proves rejection, "
                          "not that a future run succeeds or cannot fall."}
    (OUT/"replay.json").write_text(json.dumps(replay,ensure_ascii=False,indent=2)+"\n")
    before = json.loads((OUT/"before_hashes.json").read_text())
    after = {str(p.relative_to(ROOT)): digest(p) for folder in ("go2_demo","tests")
             for p in sorted((ROOT/folder).glob("*.py"))}
    changed = [k for k,v in before.items() if after.get(k)!=v]
    added = sorted(set(after)-set(before))
    assert sorted(changed) == ["go2_demo/harness.py", "go2_demo/runner.py"]
    assert added == ["go2_demo/experimental_boundary_gate.py", "tests/test_experimental_boundary_gate.py"]
    protected = ["go2_demo/"+name+".py" for name in (
        "scenarios","backend","ordered_evaluation","__main__","memory_perception","memory",
        "memory_planning","memory_context","memory_protocol","models","types")]
    assert all(before[k]==after[k] for k in protected)
    # The entire independent evaluation/cleanup block is byte-for-byte unchanged.
    old_runner=(OUT/"source_before/go2_demo/runner.py").read_text()
    new_runner=(ROOT/"go2_demo/runner.py").read_text()
    assert old_runner.split("    except KeyboardInterrupt:",1)[1] == new_runner.split("    except KeyboardInterrupt:",1)[1]
    # All Harness methods other than dispatch (including validation/observation)
    # and all runner functions other than run_episode have identical ASTs.
    def funcs(source, class_name=None):
        tree=ast.parse(source)
        if class_name:
            tree=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==class_name)
        return {n.name:ast.dump(n,include_attributes=False) for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
    for filename,class_name,exclude in (("harness.py","Harness","dispatch"),("runner.py",None,"run_episode")):
        left=funcs((OUT/"source_before/go2_demo"/filename).read_text(),class_name)
        right=funcs((ROOT/"go2_demo"/filename).read_text(),class_name)
        assert {k:v for k,v in left.items() if k!=exclude} == {k:v for k,v in right.items() if k!=exclude}
    patch=[]
    for name in changed:
        patch.extend(difflib.unified_diff((OUT/"source_before"/name).read_text().splitlines(True),
                     (ROOT/name).read_text().splitlines(True),fromfile="before/"+name,tofile="after/"+name))
    for name in added:
        patch.extend(difflib.unified_diff([], (ROOT/name).read_text().splitlines(True),fromfile="/dev/null",tofile="after/"+name))
    (OUT/"changes.patch").write_text("".join(patch))
    (OUT/"after_hashes.json").write_text(json.dumps(after,indent=2)+"\n")
    evidence={"changed_existing_files":changed,"added_files":added,"protected_hashes_unchanged":{k:True for k in protected},
              "harness_non_dispatch_ast_unchanged":True,"runner_non_episode_ast_unchanged":True,
              "runner_evaluation_cleanup_block_unchanged":True,"original_tests_hashes_unchanged":True,
              "before_hashes":before,"after_hashes":after,
              "first_ten_all_allowed":True,"fatal_move_99_blocked":True,
              "blocked_original_decisions":replay["blocked_decisions_on_original_pose_trace"],
              "truth_disclosure":"simulator GT base pose + scene-defined finite platform; safety interlock, not navigation measurement",
              "experimental":True,"pending_group_meeting_decision":True,
              "api_calls":0,"credentials_read":False,"new_simulation_episodes":0}
    (OUT/"evidence.json").write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"first_ten_allowed":replay["first_ten_move_decisions"],
          "blocked_original_decisions":replay["blocked_decisions_on_original_pose_trace"],
          "fatal_move":fatal,"changed":changed,"added":added,"protected_hashes_unchanged":True},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
