# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 82,
    "revision": 89,
    "active_plan_id": "plan-0006",
    "public_context": {
      "image_id": "frame-00077",
      "image_size": {
        "width": 640,
        "height": 360
      },
      "completion_requirements": {
        "goal_kind": "ordered_standoff",
        "reference_body": "base",
        "stop_required": true,
        "collision_free_required": true,
        "max_stopped_speed_mps": 0.12,
        "max_stopped_yaw_rate_radps": 0.25,
        "standoff_m": 1.0,
        "distance_tolerance_m": 0.18,
        "heading_tolerance_rad": 0.25
      },
      "visual_candidates": [
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            139.0,
            17.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            521.0,
            190.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            525.0,
            21.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            136.0,
            183.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            247.0,
            58.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            412.0,
            46.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            410.0,
            106.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            247.0,
            116.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            246.0,
            163.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            236.0,
            176.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            235.0,
            261.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            408.0,
            178.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            245.0,
            233.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            245.0,
            248.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            297.0,
            326.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00077",
          "pixel_uv": [
            293.0,
            343.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        }
      ]
    }
  },
  "pose": {
    "frame": "episode_start",
    "position_m": [
      0.0,
      0.0
    ],
    "yaw_rad": 0.0,
    "source": "simulated_proprioception"
  },
  "objects": [],
  "active_beliefs": [],
  "invalidated": [],
  "events": [
    {
      "event_id": "event-1",
      "kind": "key_precondition_invalidated",
      "step": 17,
      "evidence_ids": [
        "e000073"
      ]
    },
    {
      "event_id": "event-2",
      "kind": "replan_required",
      "step": 17,
      "evidence_ids": [
        "e000073"
      ]
    },
    {
      "event_id": "event-3",
      "kind": "key_precondition_invalidated",
      "step": 33,
      "evidence_ids": [
        "e000138"
      ]
    },
    {
      "event_id": "event-4",
      "kind": "replan_required",
      "step": 33,
      "evidence_ids": [
        "e000138"
      ]
    },
    {
      "event_id": "event-5",
      "kind": "key_precondition_invalidated",
      "step": 40,
      "evidence_ids": [
        "e000167"
      ]
    },
    {
      "event_id": "event-6",
      "kind": "replan_required",
      "step": 40,
      "evidence_ids": [
        "e000167"
      ]
    },
    {
      "event_id": "event-7",
      "kind": "key_precondition_invalidated",
      "step": 72,
      "evidence_ids": [
        "e000296"
      ]
    },
    {
      "event_id": "event-8",
      "kind": "replan_required",
      "step": 72,
      "evidence_ids": [
        "e000296"
      ]
    },
    {
      "event_id": "event-9",
      "kind": "key_precondition_invalidated",
      "step": 78,
      "evidence_ids": [
        "e000321"
      ]
    },
    {
      "event_id": "event-10",
      "kind": "replan_required",
      "step": 78,
      "evidence_ids": [
        "e000321"
      ]
    }
  ],
  "topology": null,
  "confidence_thresholds": {
    "confirmed": 0.8,
    "predicted_after_steps": 3,
    "unknown_after_steps": 6,
    "stale_after_steps": 10,
    "relocation_distance_m": 0.5
  },
  "measurements": {
    "pose.x_m": {
      "value": 0.0,
      "source": "simulated_proprioception",
      "step": 82,
      "evidence_ids": [
        "e000335"
      ]
    },
    "pose.y_m": {
      "value": 0.0,
      "source": "simulated_proprioception",
      "step": 82,
      "evidence_ids": [
        "e000336"
      ]
    },
    "pose.yaw_rad": {
      "value": 0.0,
      "source": "simulated_proprioception",
      "step": 82,
      "evidence_ids": [
        "e000337"
      ]
    }
  },
  "plans": [
    {
      "subgoals": [
        {
          "subgoal_id": "inspect_scene",
          "description": "observe initial scene and locate candidate blue ball A and green block B",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000012"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_scene"
        }
      ],
      "recovery": "observe again and re-select tracked features",
      "plan_id": "plan-0001",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "inspect_scene",
          "description": "observe initial scene and locate candidate blue ball A and green block B",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000017"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_scene"
        }
      ],
      "recovery": "observe again and re-select tracked features",
      "plan_id": "plan-0002",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "inspect_scene",
          "description": "observe initial scene and locate candidate blue ball A and green block B",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000102"
          ]
        },
        {
          "subgoal_id": "approach_A",
          "description": "navigate to standoff 1.0m from blue ball A and face it, then stop",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_B",
          "description": "navigate to standoff 1.0m from green block B and face it, then stop and finish",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_scene"
        }
      ],
      "recovery": "observe again and re-select tracked features",
      "plan_id": "plan-0003",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "inspect_scene",
          "description": "observe scene, keep both targets in view before leaving initial area, confirm blue ball A and green block B identities and track reliable features",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000151"
          ]
        },
        {
          "subgoal_id": "approach_A",
          "description": "navigate around cabinet obstacles to 0.82-1.18 m from blue ball A center, face it within 0.25 rad, then call stop to confirm standstill",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_B",
          "description": "after A checkpoint verified, navigate around cabinet obstacles to 0.82-1.18 m from green block B center, face it within 0.25 rad, call stop, then finish",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_scene"
        },
        {
          "on": "target_occluded",
          "subgoal_id": "inspect_scene"
        },
        {
          "on": "collision_risk",
          "subgoal_id": "inspect_scene"
        }
      ],
      "recovery": "stop, observe again, re-select tracked features and re-plan a safe detour around cabinet obstacles",
      "plan_id": "plan-0004",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "inspect_scene",
          "description": "observe scene after replan event, re-identify blue ball A and green block B, track reliable static features, note cabinet obstacles",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000305"
          ]
        },
        {
          "subgoal_id": "approach_A",
          "description": "navigate safely around cabinets to 0.82-1.18 m from blue ball A center, face it within 0.25 rad, call stop",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_B",
          "description": "after A checkpoint verified, navigate safely to 0.82-1.18 m from green block B center, face it within 0.25 rad, call stop then finish",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_scene"
        },
        {
          "on": "target_occluded",
          "subgoal_id": "inspect_scene"
        },
        {
          "on": "collision_risk",
          "subgoal_id": "inspect_scene"
        }
      ],
      "recovery": "stop, observe again, re-select tracked features and re-plan a safe detour around cabinet obstacles",
      "plan_id": "plan-0005",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "inspect_scene",
          "description": "observe scene, re-identify blue ball A and green block B, track reliable static features, note cabinet obstacles",
          "preconditions": [],
          "completion": [],
          "active": true,
          "status": "进行中",
          "evidence_ids": [
            "e000326"
          ]
        },
        {
          "subgoal_id": "approach_A",
          "description": "navigate safely around cabinets to 0.82-1.18 m from blue ball A center, face it within 0.25 rad, call stop",
          "preconditions": [],
          "completion": [],
          "active": true,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_B",
          "description": "after A checkpoint verified, navigate safely to 0.82-1.18 m from green block B center, face it within 0.25 rad, call stop then finish",
          "preconditions": [],
          "completion": [],
          "active": true,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_scene"
        },
        {
          "on": "target_occluded",
          "subgoal_id": "inspect_scene"
        },
        {
          "on": "collision_risk",
          "subgoal_id": "inspect_scene"
        }
      ],
      "recovery": "stop, observe again, re-select tracked features and re-plan a safe detour around cabinet obstacles",
      "plan_id": "plan-0006",
      "active": true
    }
  ],
  "ledger": [
    {
      "evidence_id": "e000001",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 0,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000002",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 0,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000003",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 0,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000004",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 1,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000005",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 1,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000006",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 1,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000007",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 1,
      "action": {
        "call_id": "call_898223e9cf874430b5f9da40",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000008",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 1,
      "plan_id": "plan-0001"
    },
    {
      "evidence_id": "e000009",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000010",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000011",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000012",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 2,
      "action": {
        "call_id": "call_6bf62386eadc48c39f68363c",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0001",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000013",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 2,
      "plan_id": "plan-0002"
    },
    {
      "evidence_id": "e000014",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000015",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000016",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000017",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 3,
      "action": {
        "call_id": "call_d6858aefe52d46f18b5a6df6",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0002",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000018",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000019",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000020",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000021",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 4,
      "action": {
        "call_id": "call_1bd0fdb2f99c416c9ddcfe5e",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000022",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000023",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000024",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000025",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 5,
      "action": {
        "call_id": "call_e2ec551709834d7fb60bcaed",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000026",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000027",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000028",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000029",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 6,
      "action": {
        "call_id": "call_562bb14360af4056af689a8b",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0002",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000030",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000031",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000032",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000033",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 7,
      "action": {
        "call_id": "call_060f223dd08642b0b4a7630e",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0002",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000034",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000035",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000036",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000037",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 8,
      "action": {
        "call_id": "call_dd36b849b4e84a67b7d320c1",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000038",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000039",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000040",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000041",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 9,
      "action": {
        "call_id": "call_e8973361b53c4508a6a48ee1",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000042",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000043",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000044",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000045",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 10,
      "action": {
        "call_id": "call_67fbcc65e4854d41b5d875d7",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0002",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000046",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000047",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000048",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000049",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 11,
      "action": {
        "call_id": "call_78dea1f78d1a43fab599c022",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0002",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000050",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000051",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000052",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000053",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 12,
      "action": {
        "call_id": "call_cb8ab1be96fe4edab2684b2c",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000054",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000055",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000056",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000057",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 13,
      "action": {
        "call_id": "call_963a528436864f998cf9c856",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000058",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000059",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000060",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000061",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 14,
      "action": {
        "call_id": "call_acd9cf1705f243cca629a455",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000062",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000063",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000064",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000065",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 15,
      "action": {
        "call_id": "call_96c30eba587e4e06bebfde43",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000066",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000067",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000068",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000069",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 16,
      "action": {
        "call_id": "call_742e2083f63547a684260c02",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000070",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000071",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000072",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000073",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 17,
      "action": {
        "call_id": "call_320a428478a1429da7e08854",
        "tool": "observe",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000074",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000075",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000076",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000077",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 18,
      "action": {
        "call_id": "call_62005cdc80a44a9bb31ddee7",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000078",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000079",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000080",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000081",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 19,
      "action": {
        "call_id": "call_1f82a4139e0c4069b445a093",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000082",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000083",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000084",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000085",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 20,
      "action": {
        "call_id": "call_786e758bd5e24418a2fa41c0",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000086",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000087",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000088",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000089",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 21,
      "action": {
        "call_id": "call_95f45679b1f6494798ebf2de",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000090",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000091",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000092",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000093",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 22,
      "action": {
        "call_id": "call_221bb83d9621410a85d89217",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000094",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000095",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000096",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000097",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 23,
      "action": {
        "call_id": "call_f44ae875f4be43ab9d021fb3",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000098",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 23,
      "plan_id": "plan-0003"
    },
    {
      "evidence_id": "e000099",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000100",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000101",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000102",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 24,
      "action": {
        "call_id": "call_3869b4e974504beb9bb3bb18",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0003",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000103",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000104",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000105",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000106",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 25,
      "action": {
        "call_id": "call_d52719b4f57940cda485d5ff",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0003",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000107",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000108",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000109",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000110",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 26,
      "action": {
        "call_id": "call_8db1911e18f744ceb040e56e",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0003",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000111",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000112",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000113",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000114",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 27,
      "action": {
        "call_id": "call_c4ea436c632d44f6bedc6a11",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000115",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000116",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000117",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000118",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 28,
      "action": {
        "call_id": "call_a01656d1f57843fca4b997d2",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000119",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000120",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000121",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000122",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 29,
      "action": {
        "call_id": "call_2d8ea793189f4b059ab4b4fb",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0003",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000123",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000124",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000125",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000126",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 30,
      "action": {
        "call_id": "call_29e2fd6a86de4705823fd901",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000127",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000128",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000129",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000130",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 31,
      "action": {
        "call_id": "call_954580de334d4ebb95098d80",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000131",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000132",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000133",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000134",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 32,
      "action": {
        "call_id": "call_8c6cdf9479ed416eb5bd5cd5",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000135",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000136",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000137",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000138",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 33,
      "action": {
        "call_id": "call_2c960b3f556e4112a2865929",
        "tool": "observe",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000139",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000140",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000141",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000142",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 34,
      "action": {
        "call_id": "call_f03adf9012354902a0715d5e",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000143",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000144",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000145",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000146",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 35,
      "action": {
        "call_id": "call_b3b4659d472743d299045e9b",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000147",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 35,
      "plan_id": "plan-0004"
    },
    {
      "evidence_id": "e000148",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000149",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000150",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000151",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 36,
      "action": {
        "call_id": "call_a1c080f174d346ceb37bb16d",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000152",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000153",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000154",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000155",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 37,
      "action": {
        "call_id": "call_6930068a9151444893d8a7b3",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000156",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000157",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000158",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000159",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 38,
      "action": {
        "call_id": "call_179fa2dad87d4fdd95ab5a39",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000160",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000161",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000162",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000163",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 39,
      "action": {
        "call_id": "call_fd7f6e851b86426ea8e17880",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000164",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000165",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000166",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000167",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 40,
      "action": {
        "call_id": "call_2d354a1183ca42ec8ce2afb7",
        "tool": "observe",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000168",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000169",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000170",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000171",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 41,
      "action": {
        "call_id": "call_399f5ae1516f418992313ae9",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000172",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000173",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000174",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000175",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 42,
      "action": {
        "call_id": "call_cf655fb17bb3499a9e054c0c",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000176",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000177",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000178",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000179",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 43,
      "action": {
        "call_id": "call_76e104eea1834046909033fc",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000180",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000181",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000182",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000183",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 44,
      "action": {
        "call_id": "call_797dcc0cbedd49b4a634f9a0",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000184",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000185",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000186",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000187",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 45,
      "action": {
        "call_id": "call_4571afcfad0e42e1807e9834",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000188",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000189",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000190",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000191",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 46,
      "action": {
        "call_id": "call_108ae64aebfe4266b0ca8d93",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000192",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000193",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000194",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000195",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 47,
      "action": {
        "call_id": "call_72edecae1c2e4fcbab574ea2",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000196",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000197",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000198",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000199",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 48,
      "action": {
        "call_id": "call_9f3d6a241f4a473081f3653f",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000200",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000201",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000202",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000203",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 49,
      "action": {
        "call_id": "call_4a4f40c761f040cfa0f2e76b",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000204",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000205",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000206",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000207",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 50,
      "action": {
        "call_id": "call_351eb341ab2d4576b104ba37",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000208",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000209",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000210",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000211",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 51,
      "action": {
        "call_id": "call_31b5d1293a2d459ab88ecc36",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000212",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000213",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000214",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000215",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 52,
      "action": {
        "call_id": "call_251ccebc31ef48d6a094ed5e",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000216",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000217",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000218",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000219",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 53,
      "action": {
        "call_id": "call_b6284b8bd85f48e586ff1978",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000220",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000221",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000222",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000223",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 54,
      "action": {
        "call_id": "call_d5a132694aa34e55bd0a39ab",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000224",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000225",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000226",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000227",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 55,
      "action": {
        "call_id": "call_4406c931a2b4441fa9abade4",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000228",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000229",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000230",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000231",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 56,
      "action": {
        "call_id": "call_ce30db5cb8c042d3a0ea9c2a",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000232",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000233",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000234",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000235",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 57,
      "action": {
        "call_id": "call_4837f0be4a7b4395979d0ee6",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000236",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000237",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000238",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000239",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 58,
      "action": {
        "call_id": "call_1ebce0085be742059a54a287",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000240",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000241",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000242",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000243",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 59,
      "action": {
        "call_id": "call_7cd47232630449649d0f2c1a",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000244",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000245",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000246",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000247",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 60,
      "action": {
        "call_id": "call_cd8828a4221546a2aba0103c",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000248",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000249",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000250",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000251",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 61,
      "action": {
        "call_id": "call_9a3e74e72c184885a6c6451e",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000252",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000253",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000254",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000255",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 62,
      "action": {
        "call_id": "call_d92db170ff2b435bb83eaaf2",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000256",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000257",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000258",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000259",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 63,
      "action": {
        "call_id": "call_b5b296d1076a4816a3f55949",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000260",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000261",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000262",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000263",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 64,
      "action": {
        "call_id": "call_4b082fd0d28d45b3b2c4604d",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000264",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000265",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000266",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000267",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 65,
      "action": {
        "call_id": "call_ea255bd97e7c45b28e7ea616",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000268",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000269",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000270",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000271",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 66,
      "action": {
        "call_id": "call_d779c3f5785b4f0a8daab0f3",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000272",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000273",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000274",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000275",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 67,
      "action": {
        "call_id": "call_fc2de547c12e43c8b5e95dcf",
        "tool": "observe",
        "status": "failed",
        "error_code": "ONE_TOOL_PER_TURN"
      }
    },
    {
      "evidence_id": "e000276",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 67,
      "action": {
        "call_id": "call_a98c24694f7e458c8a7fa789",
        "tool": "observe",
        "status": "failed",
        "error_code": "ONE_TOOL_PER_TURN"
      }
    },
    {
      "evidence_id": "e000277",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000278",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000279",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000280",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 68,
      "action": {
        "call_id": "call_b347e42424324710931f05ea",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000281",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000282",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000283",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000284",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 69,
      "action": {
        "call_id": "call_b61b33eaa81e4c4681f1b715",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000285",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000286",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000287",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000288",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 70,
      "action": {
        "call_id": "call_f2f06c24476b4fa6b6c0aed1",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000289",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000290",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000291",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000292",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 71,
      "action": {
        "call_id": "call_f6d3c54c210d4c6f95586770",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0004",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000293",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000294",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000295",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000296",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 72,
      "action": {
        "call_id": "call_86eabf4723484e46b82cba04",
        "tool": "observe",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000297",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000298",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000299",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000300",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 73,
      "action": {
        "call_id": "call_e7a4488c2cfe42ac8cda9637",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000301",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 73,
      "plan_id": "plan-0005"
    },
    {
      "evidence_id": "e000302",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000303",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000304",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000305",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 74,
      "action": {
        "call_id": "call_cbc7fd27a18e4ae6ad7d1a33",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0005",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000306",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000307",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000308",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000309",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 75,
      "action": {
        "call_id": "call_f15a63fd13894ae7a4a0f1e1",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000310",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000311",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000312",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000313",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 76,
      "action": {
        "call_id": "call_c0ccad3e54584b4ab90d7fc3",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000314",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000315",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000316",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000317",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 77,
      "action": {
        "call_id": "call_52ca1c06ccc7450dac871db3",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0005",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000318",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000319",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000320",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000321",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 78,
      "action": {
        "call_id": "call_ba78d73286ab48838457648d",
        "tool": "observe",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000322",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 78,
      "plan_id": "plan-0006"
    },
    {
      "evidence_id": "e000323",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000324",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000325",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000326",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 79,
      "action": {
        "call_id": "call_8e94951790c24e2a92629845",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0006",
        "subgoal_id": "inspect_scene"
      }
    },
    {
      "evidence_id": "e000327",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000328",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000329",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000330",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 80,
      "action": {
        "call_id": "call_3397335294b745d3b2f58d0c",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000331",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000332",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000333",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000334",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 81,
      "action": {
        "call_id": "call_b110cd01d2054d3b9ee43d67",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000335",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000336",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000337",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000338",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 82,
      "action": {
        "call_id": "call_1e62ca927bef492ca3bb71e5",
        "tool": "observe",
        "status": "succeeded",
        "plan_id": "plan-0006",
        "subgoal_id": "inspect_scene"
      }
    }
  ]
}
```

## 操作经验

## 程序工具
