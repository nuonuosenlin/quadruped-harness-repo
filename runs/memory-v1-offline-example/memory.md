# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 7,
    "revision": 9,
    "active_plan_id": "plan-0002"
  },
  "pose": null,
  "objects": [
    {
      "confidence": 0.95,
      "category": "marker",
      "visual_feature": {
        "description": "synthetic example marker"
      },
      "pose": {
        "frame": "task_local",
        "position_m": [
          4.0,
          0.0
        ]
      },
      "anchor_node": null,
      "object_id": "marker-1",
      "pose_covariance": [
        [
          0.01,
          0.0
        ],
        [
          0.0,
          0.01
        ]
      ],
      "source": "synthetic_offline_detector",
      "state": "confirmed",
      "last_seen": 7,
      "evidence_ids": [
        "e000001",
        "e000002",
        "e000006",
        "e000008",
        "e000010"
      ],
      "candidate_pose": null
    }
  ],
  "active_beliefs": [],
  "invalidated": [],
  "events": [
    {
      "event_id": "event-1",
      "kind": "target_state_changed",
      "step": 1,
      "evidence_ids": [
        "e000002"
      ],
      "object_id": "marker-1",
      "state": "confirmed"
    },
    {
      "event_id": "event-2",
      "kind": "dynamic_obstacle_blocked",
      "step": 2,
      "evidence_ids": [
        "e000004"
      ]
    },
    {
      "event_id": "event-3",
      "kind": "skill_stuck",
      "step": 2,
      "evidence_ids": [
        "e000004"
      ]
    },
    {
      "event_id": "event-4",
      "kind": "target_state_changed",
      "step": 4,
      "evidence_ids": [
        "e000005"
      ],
      "object_id": "marker-1",
      "state": "predicted"
    },
    {
      "event_id": "event-5",
      "kind": "target_state_changed",
      "step": 5,
      "evidence_ids": [
        "e000006",
        "e000007"
      ],
      "object_id": "marker-1"
    },
    {
      "event_id": "event-6",
      "kind": "key_precondition_invalidated",
      "step": 5,
      "evidence_ids": [
        "e000006"
      ],
      "plan_id": "plan-0001",
      "subgoal_id": "approach",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-7",
      "kind": "replan_required",
      "step": 5,
      "evidence_ids": [
        "e000006"
      ],
      "object_id": "marker-1",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-8",
      "kind": "target_state_changed",
      "step": 6,
      "evidence_ids": [
        "e000008"
      ],
      "object_id": "marker-1",
      "state": "confirmed"
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
    "marker-1.range_m": {
      "value": 1.05,
      "source": "synthetic_offline_range_sensor",
      "step": 7,
      "evidence_ids": [
        "e000011"
      ]
    }
  },
  "plans": [
    {
      "subgoals": [
        {
          "subgoal_id": "approach",
          "description": "接近标记",
          "preconditions": [
            {
              "object_id": "marker-1"
            }
          ],
          "completion": [
            {
              "measurement": "marker-1.range_m",
              "op": "le",
              "value": 1.1
            }
          ],
          "active": false,
          "status": "已失效",
          "evidence_ids": [
            "e000006"
          ]
        }
      ],
      "branches": [
        {
          "on": "target_state_changed",
          "subgoal_id": "approach"
        }
      ],
      "recovery": "重新观察目标，确认新位置后重新规划",
      "plan_id": "plan-0001",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "recover",
          "description": "新位置恢复接近",
          "preconditions": [
            {
              "object_id": "marker-1"
            }
          ],
          "completion": [
            {
              "measurement": "marker-1.range_m",
              "op": "le",
              "value": 1.1
            }
          ],
          "active": true,
          "status": "已完成",
          "evidence_ids": [
            "e000011"
          ]
        }
      ],
      "branches": [],
      "recovery": "若再次受阻则停止并重新观察",
      "plan_id": "plan-0002",
      "active": true
    }
  ],
  "ledger": [
    {
      "evidence_id": "e000001",
      "kind": "observation_confirmed",
      "source": "synthetic_offline_detector",
      "step": 0,
      "observation": {
        "object_id": "marker-1",
        "category": "marker",
        "pose": {
          "frame": "task_local",
          "position_m": [
            2.0,
            0.0
          ]
        },
        "pose_covariance": [
          [
            0.01,
            0.0
          ],
          [
            0.0,
            0.01
          ]
        ],
        "confidence": 0.95,
        "source": "synthetic_offline_detector",
        "frame_id": "f0",
        "anchor_node": null,
        "visual_feature": {
          "description": "synthetic example marker"
        }
      }
    },
    {
      "evidence_id": "e000002",
      "kind": "observation_confirmed",
      "source": "synthetic_offline_detector",
      "step": 1,
      "observation": {
        "object_id": "marker-1",
        "category": "marker",
        "pose": {
          "frame": "task_local",
          "position_m": [
            2.0,
            0.0
          ]
        },
        "pose_covariance": [
          [
            0.01,
            0.0
          ],
          [
            0.0,
            0.01
          ]
        ],
        "confidence": 0.95,
        "source": "synthetic_offline_detector",
        "frame_id": "f1",
        "anchor_node": null,
        "visual_feature": {
          "description": "synthetic example marker"
        }
      }
    },
    {
      "evidence_id": "e000003",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 1,
      "plan_id": "plan-0001"
    },
    {
      "evidence_id": "e000004",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 2,
      "action": {
        "tool": "move_relative",
        "status": "failed",
        "error_code": "DYNAMIC_OBSTACLE",
        "plan_id": "plan-0001",
        "subgoal_id": "approach"
      }
    },
    {
      "evidence_id": "e000005",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 4,
      "object_id": "marker-1",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000006",
      "kind": "observation_confirmed",
      "source": "synthetic_offline_detector",
      "step": 5,
      "observation": {
        "object_id": "marker-1",
        "category": "marker",
        "pose": {
          "frame": "task_local",
          "position_m": [
            4.0,
            0.0
          ]
        },
        "pose_covariance": [
          [
            0.01,
            0.0
          ],
          [
            0.0,
            0.01
          ]
        ],
        "confidence": 0.95,
        "source": "synthetic_offline_detector",
        "frame_id": "f5",
        "anchor_node": null,
        "visual_feature": {
          "description": "synthetic example marker"
        }
      }
    },
    {
      "evidence_id": "e000007",
      "kind": "target_relocated",
      "source": "synthetic_offline_detector",
      "step": 5,
      "object_id": "marker-1",
      "old_pose": {
        "frame": "task_local",
        "position_m": [
          2.0,
          0.0
        ]
      },
      "new_pose": {
        "frame": "task_local",
        "position_m": [
          4.0,
          0.0
        ]
      },
      "evidence_ids": [
        "e000006"
      ]
    },
    {
      "evidence_id": "e000008",
      "kind": "observation_confirmed",
      "source": "synthetic_offline_detector",
      "step": 6,
      "observation": {
        "object_id": "marker-1",
        "category": "marker",
        "pose": {
          "frame": "task_local",
          "position_m": [
            4.0,
            0.0
          ]
        },
        "pose_covariance": [
          [
            0.01,
            0.0
          ],
          [
            0.0,
            0.01
          ]
        ],
        "confidence": 0.95,
        "source": "synthetic_offline_detector",
        "frame_id": "f6",
        "anchor_node": null,
        "visual_feature": {
          "description": "synthetic example marker"
        }
      }
    },
    {
      "evidence_id": "e000009",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 6,
      "plan_id": "plan-0002"
    },
    {
      "evidence_id": "e000010",
      "kind": "observation_confirmed",
      "source": "synthetic_offline_detector",
      "step": 7,
      "observation": {
        "object_id": "marker-1",
        "category": "marker",
        "pose": {
          "frame": "task_local",
          "position_m": [
            4.0,
            0.0
          ]
        },
        "pose_covariance": [
          [
            0.01,
            0.0
          ],
          [
            0.0,
            0.01
          ]
        ],
        "confidence": 0.95,
        "source": "synthetic_offline_detector",
        "frame_id": "f7",
        "anchor_node": null,
        "visual_feature": {
          "description": "synthetic example marker"
        }
      }
    },
    {
      "evidence_id": "e000011",
      "kind": "measurement",
      "source": "synthetic_offline_range_sensor",
      "step": 7,
      "name": "marker-1.range_m",
      "value": 1.05
    },
    {
      "evidence_id": "e000012",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 7,
      "action": {
        "tool": "move_relative",
        "status": "succeeded",
        "plan_id": "plan-0002",
        "subgoal_id": "recover"
      }
    }
  ]
}
```

## 操作经验

## 程序工具
