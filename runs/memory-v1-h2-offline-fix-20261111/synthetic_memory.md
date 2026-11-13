# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 2,
    "revision": 3,
    "active_plan_id": null,
    "public_context": {
      "image_id": "synthetic-f2",
      "image_size": {
        "width": 100,
        "height": 80
      },
      "completion_requirements": {},
      "task_targets": [
        {
          "object_id": "task:A",
          "task_label": "A",
          "description": "蓝球",
          "color": "blue"
        },
        {
          "object_id": "task:B",
          "task_label": "B",
          "description": "绿方块",
          "color": "green"
        }
      ],
      "current_observation": {
        "image_id": "synthetic-f2",
        "image_size": {
          "width": 100,
          "height": 80
        },
        "tracked_points": [
          {
            "point_id": "synthetic-A",
            "image_id": "synthetic-f2",
            "pixel_uv": [
              31,
              37
            ],
            "relative_xy_m": [
              2.0,
              -0.3
            ],
            "confidence": 0.99,
            "source": "synthetic_rgbd_tracking",
            "valid": true
          },
          {
            "point_id": "synthetic-B",
            "image_id": "synthetic-f2",
            "pixel_uv": [
              85,
              45
            ],
            "relative_xy_m": [
              2.0,
              0.3
            ],
            "confidence": 0.99,
            "source": "synthetic_rgbd_tracking",
            "valid": true
          }
        ],
        "sensor_calibration": {},
        "completion_requirements": {},
        "target_candidates": [
          {
            "object_id": "task:A",
            "task_label": "A",
            "description": "蓝球",
            "color": "blue",
            "image_id": "synthetic-f2",
            "pixel_uv": [
              31,
              37
            ],
            "camera_xyz_m": [
              -0.38,
              -0.06,
              2.0
            ],
            "coordinate_frame": "current_camera_optical",
            "status": "candidate_not_confirmed",
            "identity_basis": "unique_visible_component_matching_task_given_color",
            "source": "task_label_color_rgbd_v1",
            "requires": "track_point_then_independent_frame"
          },
          {
            "object_id": "task:B",
            "task_label": "B",
            "description": "绿方块",
            "color": "green",
            "image_id": "synthetic-f2",
            "pixel_uv": [
              85,
              45
            ],
            "camera_xyz_m": [
              0.7,
              0.1,
              2.0
            ],
            "coordinate_frame": "current_camera_optical",
            "status": "candidate_not_confirmed",
            "identity_basis": "unique_visible_component_matching_task_given_color",
            "source": "task_label_color_rgbd_v1",
            "requires": "track_point_then_independent_frame"
          }
        ],
        "source": "current_public_rgbd_and_tool_geometry"
      },
      "visual_candidates": []
    }
  },
  "pose": {
    "frame": "episode_start",
    "position_m": [
      0.0,
      0.0
    ],
    "yaw_rad": 0.0,
    "source": "synthetic_public_odometry",
    "provenance": "existing_public_idealized_simulator_odometry"
  },
  "objects": [
    {
      "visual_feature": {
        "image_id": "synthetic-f2",
        "pixel_uv": [
          31,
          37
        ]
      },
      "object_id": "synthetic-A",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.0,
          -0.3
        ]
      },
      "confidence": 0.99,
      "source": "synthetic_rgbd_tracking",
      "anchor_node": null,
      "category": "unclassified_landmark",
      "state": "confirmed",
      "last_seen": 2,
      "evidence_ids": [
        "e000001",
        "e000013"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "synthetic-f2",
        "pixel_uv": [
          31,
          37
        ]
      },
      "object_id": "task:A",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.0,
          -0.3
        ]
      },
      "confidence": 0.95,
      "source": "task_label_rgbd_tracking",
      "anchor_node": null,
      "category": "task_target",
      "state": "confirmed",
      "last_seen": 2,
      "evidence_ids": [
        "e000002",
        "e000014"
      ],
      "candidate_pose": null,
      "task_label": "A",
      "label_description": "蓝球",
      "camera_pose": {
        "frame": "current_camera_optical",
        "image_id": "synthetic-f2",
        "position_m": [
          -0.38,
          -0.06,
          2.0
        ],
        "source": "rgbd_depth_intrinsics"
      },
      "measurement_provenance": {
        "identity": "task_given_label_plus_unique_current_color_component",
        "tracking": "synthetic_rgbd_tracking",
        "reference_pose": "existing_public_idealized_simulator_odometry",
        "motion_delta_used": false
      }
    },
    {
      "visual_feature": {
        "image_id": "synthetic-f2",
        "pixel_uv": [
          85,
          45
        ]
      },
      "object_id": "synthetic-B",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.0,
          0.3
        ]
      },
      "confidence": 0.99,
      "source": "synthetic_rgbd_tracking",
      "anchor_node": null,
      "category": "unclassified_landmark",
      "state": "confirmed",
      "last_seen": 2,
      "evidence_ids": [
        "e000003",
        "e000015"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "synthetic-f2",
        "pixel_uv": [
          85,
          45
        ]
      },
      "object_id": "task:B",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.0,
          0.3
        ]
      },
      "confidence": 0.95,
      "source": "task_label_rgbd_tracking",
      "anchor_node": null,
      "category": "task_target",
      "state": "confirmed",
      "last_seen": 2,
      "evidence_ids": [
        "e000004",
        "e000016"
      ],
      "candidate_pose": null,
      "task_label": "B",
      "label_description": "绿方块",
      "camera_pose": {
        "frame": "current_camera_optical",
        "image_id": "synthetic-f2",
        "position_m": [
          0.7,
          0.1,
          2.0
        ],
        "source": "rgbd_depth_intrinsics"
      },
      "measurement_provenance": {
        "identity": "task_given_label_plus_unique_current_color_component",
        "tracking": "synthetic_rgbd_tracking",
        "reference_pose": "existing_public_idealized_simulator_odometry",
        "motion_delta_used": false
      }
    }
  ],
  "active_beliefs": [],
  "invalidated": [],
  "events": [
    {
      "event_id": "event-1",
      "kind": "target_state_changed",
      "step": 2,
      "evidence_ids": [
        "e000013"
      ],
      "object_id": "synthetic-A",
      "state": "confirmed"
    },
    {
      "event_id": "event-2",
      "kind": "target_state_changed",
      "step": 2,
      "evidence_ids": [
        "e000014"
      ],
      "object_id": "task:A",
      "state": "confirmed"
    },
    {
      "event_id": "event-3",
      "kind": "target_state_changed",
      "step": 2,
      "evidence_ids": [
        "e000015"
      ],
      "object_id": "synthetic-B",
      "state": "confirmed"
    },
    {
      "event_id": "event-4",
      "kind": "target_state_changed",
      "step": 2,
      "evidence_ids": [
        "e000016"
      ],
      "object_id": "task:B",
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
    "pose.x_m": {
      "value": 0.0,
      "source": "synthetic_public_odometry",
      "step": 2,
      "evidence_ids": [
        "e000017"
      ]
    },
    "pose.y_m": {
      "value": 0.0,
      "source": "synthetic_public_odometry",
      "step": 2,
      "evidence_ids": [
        "e000018"
      ]
    },
    "pose.yaw_rad": {
      "value": 0.0,
      "source": "synthetic_public_odometry",
      "step": 2,
      "evidence_ids": [
        "e000019"
      ]
    }
  },
  "plans": [],
  "ledger": [
    {
      "evidence_id": "e000001",
      "kind": "observation_confirmed",
      "source": "synthetic_rgbd_tracking",
      "step": 0,
      "observation": {
        "object_id": "synthetic-A",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            -0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.99,
        "source": "synthetic_rgbd_tracking",
        "frame_id": "synthetic-f1",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f1",
          "pixel_uv": [
            31,
            37
          ]
        }
      }
    },
    {
      "evidence_id": "e000002",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 0,
      "observation": {
        "object_id": "task:A",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            -0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "synthetic-f1",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f1",
          "pixel_uv": [
            31,
            37
          ]
        },
        "task_label": "A",
        "label_description": "蓝球",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "synthetic-f1",
          "position_m": [
            -0.38,
            -0.06,
            2.0
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "synthetic_rgbd_tracking",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000003",
      "kind": "observation_confirmed",
      "source": "synthetic_rgbd_tracking",
      "step": 0,
      "observation": {
        "object_id": "synthetic-B",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.99,
        "source": "synthetic_rgbd_tracking",
        "frame_id": "synthetic-f1",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f1",
          "pixel_uv": [
            85,
            45
          ]
        }
      }
    },
    {
      "evidence_id": "e000004",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 0,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "synthetic-f1",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f1",
          "pixel_uv": [
            85,
            45
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "synthetic-f1",
          "position_m": [
            0.7,
            0.1,
            2.0
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "synthetic_rgbd_tracking",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000005",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 0,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000006",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 0,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000007",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 0,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000008",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 0,
      "action": {
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000009",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 1,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000010",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 1,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000011",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 1,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000012",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 1,
      "action": {
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000013",
      "kind": "observation_confirmed",
      "source": "synthetic_rgbd_tracking",
      "step": 2,
      "observation": {
        "object_id": "synthetic-A",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            -0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.99,
        "source": "synthetic_rgbd_tracking",
        "frame_id": "synthetic-f2",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f2",
          "pixel_uv": [
            31,
            37
          ]
        }
      }
    },
    {
      "evidence_id": "e000014",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 2,
      "observation": {
        "object_id": "task:A",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            -0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "synthetic-f2",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f2",
          "pixel_uv": [
            31,
            37
          ]
        },
        "task_label": "A",
        "label_description": "蓝球",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "synthetic-f2",
          "position_m": [
            -0.38,
            -0.06,
            2.0
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "synthetic_rgbd_tracking",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000015",
      "kind": "observation_confirmed",
      "source": "synthetic_rgbd_tracking",
      "step": 2,
      "observation": {
        "object_id": "synthetic-B",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.99,
        "source": "synthetic_rgbd_tracking",
        "frame_id": "synthetic-f2",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f2",
          "pixel_uv": [
            85,
            45
          ]
        }
      }
    },
    {
      "evidence_id": "e000016",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 2,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0,
            0.3
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "synthetic-f2",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "synthetic-f2",
          "pixel_uv": [
            85,
            45
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "synthetic-f2",
          "position_m": [
            0.7,
            0.1,
            2.0
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "synthetic_rgbd_tracking",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000017",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 2,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000018",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 2,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000019",
      "kind": "measurement",
      "source": "synthetic_public_odometry",
      "step": 2,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000020",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 2,
      "action": {
        "tool": "get_geometry",
        "status": "succeeded"
      }
    }
  ]
}
```

## 操作经验

## 程序工具
