# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 44,
    "revision": 45,
    "active_plan_id": null,
    "public_context": {
      "image_id": "frame-00011",
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
        "image_id": "frame-00011",
        "image_size": {
          "width": 640,
          "height": 360
        },
        "tracked_points": [
          {
            "point_id": "point-001",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-002",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-003",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-004",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-005",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-006",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-007",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-008",
            "image_id": "frame-00011",
            "timestamp_s": 1.0000000000000007,
            "valid": true,
            "pixel_uv": [
              156.0,
              248.0
            ],
            "relative_xy_m": [
              1.7354,
              0.7421
            ],
            "range_m": 1.8874,
            "bearing_rad": 0.4041,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          }
        ],
        "sensor_calibration": {
          "camera_frame": "front_rgbd_optical",
          "body_frame": "base",
          "optical_axes": "x right, y down, z forward",
          "body_axes": "x forward, y left, z up",
          "camera_position_in_body_m": [
            0.32,
            0.0,
            0.08
          ],
          "camera_optical_to_body_rotation": [
            [
              0.0,
              0.0,
              1.0
            ],
            [
              -1.0,
              0.0,
              0.0
            ],
            [
              0.0,
              -1.0,
              0.0
            ]
          ]
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
        "target_candidates": [
          {
            "object_id": "task:B",
            "task_label": "B",
            "description": "绿方块",
            "color": "green",
            "image_id": "frame-00011",
            "pixel_uv": [
              156,
              248
            ],
            "camera_xyz_m": [
              -0.746545465871329,
              0.31277287102254453,
              1.4235464334487915
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
      "visual_candidates": [
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            139.0,
            17.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            521.0,
            190.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            525.0,
            21.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            136.0,
            183.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            247.0,
            58.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            412.0,
            46.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            410.0,
            106.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            247.0,
            116.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            246.0,
            163.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            236.0,
            176.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            235.0,
            261.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            408.0,
            178.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            245.0,
            233.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            245.0,
            248.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
          "pixel_uv": [
            297.0,
            326.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00011",
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
    "source": "simulated_proprioception",
    "provenance": "existing_public_idealized_simulator_odometry"
  },
  "objects": [
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-001",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000004",
        "e000012",
        "e000040",
        "e000117",
        "e000158",
        "e000187",
        "e000216",
        "e000274",
        "e000318",
        "e000425",
        "e000469"
      ],
      "candidate_pose": null
    },
    {
      "confidence": 0.95,
      "source": "task_label_rgbd_tracking",
      "category": "task_target",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "task:B",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000005",
        "e000013",
        "e000041",
        "e000118",
        "e000159",
        "e000188",
        "e000217",
        "e000275",
        "e000319",
        "e000426",
        "e000470"
      ],
      "candidate_pose": null,
      "task_label": "B",
      "label_description": "绿方块",
      "camera_pose": {
        "frame": "current_camera_optical",
        "image_id": "frame-00011",
        "position_m": [
          -0.746545465871329,
          0.31277287102254453,
          1.4235464334487915
        ],
        "source": "rgbd_depth_intrinsics"
      },
      "measurement_provenance": {
        "identity": "task_given_label_plus_unique_current_color_component",
        "tracking": "rgbd_optical_flow",
        "reference_pose": "existing_public_idealized_simulator_odometry",
        "motion_delta_used": false
      }
    },
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-002",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000066",
        "e000119",
        "e000160",
        "e000189",
        "e000218",
        "e000276",
        "e000320",
        "e000427",
        "e000471"
      ],
      "candidate_pose": null
    },
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-003",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000083",
        "e000120",
        "e000161",
        "e000190",
        "e000219",
        "e000277",
        "e000321",
        "e000428",
        "e000472"
      ],
      "candidate_pose": null
    },
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-004",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000104",
        "e000121",
        "e000162",
        "e000191",
        "e000220",
        "e000278",
        "e000322",
        "e000429",
        "e000473"
      ],
      "candidate_pose": null
    },
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-005",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000303",
        "e000323",
        "e000430",
        "e000474"
      ],
      "candidate_pose": null
    },
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-006",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000338",
        "e000431",
        "e000475"
      ],
      "candidate_pose": null
    },
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-007",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 37,
      "evidence_ids": [
        "e000388",
        "e000432",
        "e000476"
      ],
      "candidate_pose": null
    },
    {
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "category": "unclassified_landmark",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "object_id": "point-008",
      "pose_covariance": null,
      "state": "unknown",
      "last_seen": 42,
      "evidence_ids": [
        "e000575"
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
      "step": 2,
      "evidence_ids": [
        "e000012"
      ],
      "object_id": "point-001",
      "state": "confirmed"
    },
    {
      "event_id": "event-2",
      "kind": "target_state_changed",
      "step": 2,
      "evidence_ids": [
        "e000013"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-3",
      "kind": "skill_stuck",
      "step": 3,
      "evidence_ids": [
        "e000025"
      ]
    },
    {
      "event_id": "event-4",
      "kind": "key_precondition_invalidated",
      "step": 3,
      "evidence_ids": [
        "e000025"
      ]
    },
    {
      "event_id": "event-5",
      "kind": "replan_required",
      "step": 3,
      "evidence_ids": [
        "e000025"
      ]
    },
    {
      "event_id": "event-6",
      "kind": "skill_stuck",
      "step": 4,
      "evidence_ids": [
        "e000031"
      ]
    },
    {
      "event_id": "event-7",
      "kind": "key_precondition_invalidated",
      "step": 4,
      "evidence_ids": [
        "e000031"
      ]
    },
    {
      "event_id": "event-8",
      "kind": "replan_required",
      "step": 4,
      "evidence_ids": [
        "e000031"
      ]
    },
    {
      "event_id": "event-9",
      "kind": "target_state_changed",
      "step": 5,
      "evidence_ids": [
        "e000032"
      ],
      "object_id": "point-001",
      "state": "predicted"
    },
    {
      "event_id": "event-10",
      "kind": "target_state_changed",
      "step": 5,
      "evidence_ids": [
        "e000033"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-11",
      "kind": "skill_stuck",
      "step": 5,
      "evidence_ids": [
        "e000039"
      ]
    },
    {
      "event_id": "event-12",
      "kind": "key_precondition_invalidated",
      "step": 5,
      "evidence_ids": [
        "e000039"
      ]
    },
    {
      "event_id": "event-13",
      "kind": "replan_required",
      "step": 5,
      "evidence_ids": [
        "e000039"
      ]
    },
    {
      "event_id": "event-14",
      "kind": "target_state_changed",
      "step": 6,
      "evidence_ids": [
        "e000040"
      ],
      "object_id": "point-001",
      "state": "unknown"
    },
    {
      "event_id": "event-15",
      "kind": "target_state_changed",
      "step": 6,
      "evidence_ids": [
        "e000041"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-16",
      "kind": "skill_stuck",
      "step": 7,
      "evidence_ids": [
        "e000053"
      ]
    },
    {
      "event_id": "event-17",
      "kind": "key_precondition_invalidated",
      "step": 7,
      "evidence_ids": [
        "e000053"
      ]
    },
    {
      "event_id": "event-18",
      "kind": "replan_required",
      "step": 7,
      "evidence_ids": [
        "e000053"
      ]
    },
    {
      "event_id": "event-19",
      "kind": "skill_stuck",
      "step": 8,
      "evidence_ids": [
        "e000059"
      ]
    },
    {
      "event_id": "event-20",
      "kind": "key_precondition_invalidated",
      "step": 8,
      "evidence_ids": [
        "e000059"
      ]
    },
    {
      "event_id": "event-21",
      "kind": "replan_required",
      "step": 8,
      "evidence_ids": [
        "e000059"
      ]
    },
    {
      "event_id": "event-22",
      "kind": "skill_stuck",
      "step": 9,
      "evidence_ids": [
        "e000065"
      ]
    },
    {
      "event_id": "event-23",
      "kind": "key_precondition_invalidated",
      "step": 9,
      "evidence_ids": [
        "e000065"
      ]
    },
    {
      "event_id": "event-24",
      "kind": "replan_required",
      "step": 9,
      "evidence_ids": [
        "e000065"
      ]
    },
    {
      "event_id": "event-25",
      "kind": "skill_stuck",
      "step": 11,
      "evidence_ids": [
        "e000082"
      ]
    },
    {
      "event_id": "event-26",
      "kind": "key_precondition_invalidated",
      "step": 11,
      "evidence_ids": [
        "e000082"
      ]
    },
    {
      "event_id": "event-27",
      "kind": "replan_required",
      "step": 11,
      "evidence_ids": [
        "e000082"
      ]
    },
    {
      "event_id": "event-28",
      "kind": "skill_stuck",
      "step": 13,
      "evidence_ids": [
        "e000103"
      ]
    },
    {
      "event_id": "event-29",
      "kind": "key_precondition_invalidated",
      "step": 13,
      "evidence_ids": [
        "e000103"
      ]
    },
    {
      "event_id": "event-30",
      "kind": "replan_required",
      "step": 13,
      "evidence_ids": [
        "e000103"
      ]
    },
    {
      "event_id": "event-31",
      "kind": "target_state_changed",
      "step": 15,
      "evidence_ids": [
        "e000121"
      ],
      "object_id": "point-004",
      "state": "confirmed"
    },
    {
      "event_id": "event-32",
      "kind": "skill_stuck",
      "step": 16,
      "evidence_ids": [
        "e000145"
      ]
    },
    {
      "event_id": "event-33",
      "kind": "key_precondition_invalidated",
      "step": 16,
      "evidence_ids": [
        "e000145"
      ]
    },
    {
      "event_id": "event-34",
      "kind": "replan_required",
      "step": 16,
      "evidence_ids": [
        "e000145"
      ]
    },
    {
      "event_id": "event-35",
      "kind": "skill_stuck",
      "step": 17,
      "evidence_ids": [
        "e000157"
      ]
    },
    {
      "event_id": "event-36",
      "kind": "key_precondition_invalidated",
      "step": 17,
      "evidence_ids": [
        "e000157"
      ]
    },
    {
      "event_id": "event-37",
      "kind": "replan_required",
      "step": 17,
      "evidence_ids": [
        "e000157"
      ]
    },
    {
      "event_id": "event-38",
      "kind": "target_state_changed",
      "step": 18,
      "evidence_ids": [
        "e000162"
      ],
      "object_id": "point-004",
      "state": "unknown"
    },
    {
      "event_id": "event-39",
      "kind": "skill_stuck",
      "step": 19,
      "evidence_ids": [
        "e000186"
      ]
    },
    {
      "event_id": "event-40",
      "kind": "key_precondition_invalidated",
      "step": 19,
      "evidence_ids": [
        "e000186"
      ]
    },
    {
      "event_id": "event-41",
      "kind": "replan_required",
      "step": 19,
      "evidence_ids": [
        "e000186"
      ]
    },
    {
      "event_id": "event-42",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000187"
      ],
      "object_id": "point-001",
      "state": "confirmed"
    },
    {
      "event_id": "event-43",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000188"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-44",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000189"
      ],
      "object_id": "point-002",
      "state": "confirmed"
    },
    {
      "event_id": "event-45",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000190"
      ],
      "object_id": "point-003",
      "state": "confirmed"
    },
    {
      "event_id": "event-46",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000191"
      ],
      "object_id": "point-004",
      "state": "confirmed"
    },
    {
      "event_id": "event-47",
      "kind": "skill_stuck",
      "step": 21,
      "evidence_ids": [
        "e000215"
      ]
    },
    {
      "event_id": "event-48",
      "kind": "key_precondition_invalidated",
      "step": 21,
      "evidence_ids": [
        "e000215"
      ]
    },
    {
      "event_id": "event-49",
      "kind": "replan_required",
      "step": 21,
      "evidence_ids": [
        "e000215"
      ]
    },
    {
      "event_id": "event-50",
      "kind": "skill_stuck",
      "step": 23,
      "evidence_ids": [
        "e000244"
      ]
    },
    {
      "event_id": "event-51",
      "kind": "key_precondition_invalidated",
      "step": 23,
      "evidence_ids": [
        "e000244"
      ]
    },
    {
      "event_id": "event-52",
      "kind": "replan_required",
      "step": 23,
      "evidence_ids": [
        "e000244"
      ]
    },
    {
      "event_id": "event-53",
      "kind": "skill_stuck",
      "step": 24,
      "evidence_ids": [
        "e000256"
      ]
    },
    {
      "event_id": "event-54",
      "kind": "key_precondition_invalidated",
      "step": 24,
      "evidence_ids": [
        "e000256"
      ]
    },
    {
      "event_id": "event-55",
      "kind": "replan_required",
      "step": 24,
      "evidence_ids": [
        "e000256"
      ]
    },
    {
      "event_id": "event-56",
      "kind": "target_state_changed",
      "step": 25,
      "evidence_ids": [
        "e000257"
      ],
      "object_id": "point-001",
      "state": "predicted"
    },
    {
      "event_id": "event-57",
      "kind": "target_state_changed",
      "step": 25,
      "evidence_ids": [
        "e000258"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-58",
      "kind": "target_state_changed",
      "step": 25,
      "evidence_ids": [
        "e000259"
      ],
      "object_id": "point-002",
      "state": "predicted"
    },
    {
      "event_id": "event-59",
      "kind": "target_state_changed",
      "step": 25,
      "evidence_ids": [
        "e000260"
      ],
      "object_id": "point-003",
      "state": "predicted"
    },
    {
      "event_id": "event-60",
      "kind": "target_state_changed",
      "step": 25,
      "evidence_ids": [
        "e000261"
      ],
      "object_id": "point-004",
      "state": "predicted"
    },
    {
      "event_id": "event-61",
      "kind": "skill_stuck",
      "step": 25,
      "evidence_ids": [
        "e000273"
      ]
    },
    {
      "event_id": "event-62",
      "kind": "key_precondition_invalidated",
      "step": 25,
      "evidence_ids": [
        "e000273"
      ]
    },
    {
      "event_id": "event-63",
      "kind": "replan_required",
      "step": 25,
      "evidence_ids": [
        "e000273"
      ]
    },
    {
      "event_id": "event-64",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000274"
      ],
      "object_id": "point-001",
      "state": "unknown"
    },
    {
      "event_id": "event-65",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000275"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-66",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000276"
      ],
      "object_id": "point-002",
      "state": "unknown"
    },
    {
      "event_id": "event-67",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000277"
      ],
      "object_id": "point-003",
      "state": "unknown"
    },
    {
      "event_id": "event-68",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000278"
      ],
      "object_id": "point-004",
      "state": "unknown"
    },
    {
      "event_id": "event-69",
      "kind": "skill_stuck",
      "step": 27,
      "evidence_ids": [
        "e000302"
      ]
    },
    {
      "event_id": "event-70",
      "kind": "key_precondition_invalidated",
      "step": 27,
      "evidence_ids": [
        "e000302"
      ]
    },
    {
      "event_id": "event-71",
      "kind": "replan_required",
      "step": 27,
      "evidence_ids": [
        "e000302"
      ]
    },
    {
      "event_id": "event-72",
      "kind": "target_state_changed",
      "step": 29,
      "evidence_ids": [
        "e000323"
      ],
      "object_id": "point-005",
      "state": "confirmed"
    },
    {
      "event_id": "event-73",
      "kind": "skill_stuck",
      "step": 31,
      "evidence_ids": [
        "e000370"
      ]
    },
    {
      "event_id": "event-74",
      "kind": "key_precondition_invalidated",
      "step": 31,
      "evidence_ids": [
        "e000370"
      ]
    },
    {
      "event_id": "event-75",
      "kind": "replan_required",
      "step": 31,
      "evidence_ids": [
        "e000370"
      ]
    },
    {
      "event_id": "event-76",
      "kind": "target_state_changed",
      "step": 32,
      "evidence_ids": [
        "e000371"
      ],
      "object_id": "point-005",
      "state": "predicted"
    },
    {
      "event_id": "event-77",
      "kind": "skill_stuck",
      "step": 32,
      "evidence_ids": [
        "e000387"
      ]
    },
    {
      "event_id": "event-78",
      "kind": "key_precondition_invalidated",
      "step": 32,
      "evidence_ids": [
        "e000387"
      ]
    },
    {
      "event_id": "event-79",
      "kind": "replan_required",
      "step": 32,
      "evidence_ids": [
        "e000387"
      ]
    },
    {
      "event_id": "event-80",
      "kind": "skill_stuck",
      "step": 34,
      "evidence_ids": [
        "e000424"
      ]
    },
    {
      "event_id": "event-81",
      "kind": "key_precondition_invalidated",
      "step": 34,
      "evidence_ids": [
        "e000424"
      ]
    },
    {
      "event_id": "event-82",
      "kind": "replan_required",
      "step": 34,
      "evidence_ids": [
        "e000424"
      ]
    },
    {
      "event_id": "event-83",
      "kind": "target_state_changed",
      "step": 35,
      "evidence_ids": [
        "e000430"
      ],
      "object_id": "point-005",
      "state": "unknown"
    },
    {
      "event_id": "event-84",
      "kind": "target_state_changed",
      "step": 35,
      "evidence_ids": [
        "e000432"
      ],
      "object_id": "point-007",
      "state": "confirmed"
    },
    {
      "event_id": "event-85",
      "kind": "skill_stuck",
      "step": 36,
      "evidence_ids": [
        "e000468"
      ]
    },
    {
      "event_id": "event-86",
      "kind": "key_precondition_invalidated",
      "step": 36,
      "evidence_ids": [
        "e000468"
      ]
    },
    {
      "event_id": "event-87",
      "kind": "replan_required",
      "step": 36,
      "evidence_ids": [
        "e000468"
      ]
    },
    {
      "event_id": "event-88",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000469"
      ],
      "object_id": "point-001",
      "state": "confirmed"
    },
    {
      "event_id": "event-89",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000470"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-90",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000471"
      ],
      "object_id": "point-002",
      "state": "confirmed"
    },
    {
      "event_id": "event-91",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000472"
      ],
      "object_id": "point-003",
      "state": "confirmed"
    },
    {
      "event_id": "event-92",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000473"
      ],
      "object_id": "point-004",
      "state": "confirmed"
    },
    {
      "event_id": "event-93",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000474"
      ],
      "object_id": "point-005",
      "state": "confirmed"
    },
    {
      "event_id": "event-94",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000475"
      ],
      "object_id": "point-006",
      "state": "confirmed"
    },
    {
      "event_id": "event-95",
      "kind": "skill_stuck",
      "step": 38,
      "evidence_ids": [
        "e000512"
      ]
    },
    {
      "event_id": "event-96",
      "kind": "key_precondition_invalidated",
      "step": 38,
      "evidence_ids": [
        "e000512"
      ]
    },
    {
      "event_id": "event-97",
      "kind": "replan_required",
      "step": 38,
      "evidence_ids": [
        "e000512"
      ]
    },
    {
      "event_id": "event-98",
      "kind": "skill_stuck",
      "step": 39,
      "evidence_ids": [
        "e000530"
      ]
    },
    {
      "event_id": "event-99",
      "kind": "key_precondition_invalidated",
      "step": 39,
      "evidence_ids": [
        "e000530"
      ]
    },
    {
      "event_id": "event-100",
      "kind": "replan_required",
      "step": 39,
      "evidence_ids": [
        "e000530"
      ]
    },
    {
      "event_id": "event-101",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000531"
      ],
      "object_id": "point-001",
      "state": "predicted"
    },
    {
      "event_id": "event-102",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000532"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-103",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000533"
      ],
      "object_id": "point-002",
      "state": "predicted"
    },
    {
      "event_id": "event-104",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000534"
      ],
      "object_id": "point-003",
      "state": "predicted"
    },
    {
      "event_id": "event-105",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000535"
      ],
      "object_id": "point-004",
      "state": "predicted"
    },
    {
      "event_id": "event-106",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000536"
      ],
      "object_id": "point-005",
      "state": "predicted"
    },
    {
      "event_id": "event-107",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000537"
      ],
      "object_id": "point-006",
      "state": "predicted"
    },
    {
      "event_id": "event-108",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000538"
      ],
      "object_id": "point-007",
      "state": "predicted"
    },
    {
      "event_id": "event-109",
      "kind": "skill_stuck",
      "step": 40,
      "evidence_ids": [
        "e000556"
      ]
    },
    {
      "event_id": "event-110",
      "kind": "key_precondition_invalidated",
      "step": 40,
      "evidence_ids": [
        "e000556"
      ]
    },
    {
      "event_id": "event-111",
      "kind": "replan_required",
      "step": 40,
      "evidence_ids": [
        "e000556"
      ]
    },
    {
      "event_id": "event-112",
      "kind": "skill_stuck",
      "step": 41,
      "evidence_ids": [
        "e000574"
      ]
    },
    {
      "event_id": "event-113",
      "kind": "key_precondition_invalidated",
      "step": 41,
      "evidence_ids": [
        "e000574"
      ]
    },
    {
      "event_id": "event-114",
      "kind": "replan_required",
      "step": 41,
      "evidence_ids": [
        "e000574"
      ]
    },
    {
      "event_id": "event-115",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000596"
      ],
      "object_id": "point-001",
      "state": "unknown"
    },
    {
      "event_id": "event-116",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000597"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-117",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000598"
      ],
      "object_id": "point-002",
      "state": "unknown"
    },
    {
      "event_id": "event-118",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000599"
      ],
      "object_id": "point-003",
      "state": "unknown"
    },
    {
      "event_id": "event-119",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000600"
      ],
      "object_id": "point-004",
      "state": "unknown"
    },
    {
      "event_id": "event-120",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000601"
      ],
      "object_id": "point-005",
      "state": "unknown"
    },
    {
      "event_id": "event-121",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000602"
      ],
      "object_id": "point-006",
      "state": "unknown"
    },
    {
      "event_id": "event-122",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000603"
      ],
      "object_id": "point-007",
      "state": "unknown"
    },
    {
      "event_id": "event-123",
      "kind": "skill_stuck",
      "step": 43,
      "evidence_ids": [
        "e000623"
      ]
    },
    {
      "event_id": "event-124",
      "kind": "key_precondition_invalidated",
      "step": 43,
      "evidence_ids": [
        "e000623"
      ]
    },
    {
      "event_id": "event-125",
      "kind": "replan_required",
      "step": 43,
      "evidence_ids": [
        "e000623"
      ]
    },
    {
      "event_id": "event-126",
      "kind": "skill_stuck",
      "step": 44,
      "evidence_ids": [
        "e000643"
      ]
    },
    {
      "event_id": "event-127",
      "kind": "key_precondition_invalidated",
      "step": 44,
      "evidence_ids": [
        "e000643"
      ]
    },
    {
      "event_id": "event-128",
      "kind": "replan_required",
      "step": 44,
      "evidence_ids": [
        "e000643"
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
      "step": 44,
      "evidence_ids": [
        "e000624"
      ]
    },
    "pose.y_m": {
      "value": 0.0,
      "source": "simulated_proprioception",
      "step": 44,
      "evidence_ids": [
        "e000625"
      ]
    },
    "pose.yaw_rad": {
      "value": 0.0,
      "source": "simulated_proprioception",
      "step": 44,
      "evidence_ids": [
        "e000626"
      ]
    },
    "point-001.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000627"
      ]
    },
    "point-001.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000628"
      ]
    },
    "point-002.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000629"
      ]
    },
    "point-002.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000630"
      ]
    },
    "point-003.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000631"
      ]
    },
    "point-003.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000632"
      ]
    },
    "point-004.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000633"
      ]
    },
    "point-004.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000634"
      ]
    },
    "point-005.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000635"
      ]
    },
    "point-005.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000636"
      ]
    },
    "point-006.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000637"
      ]
    },
    "point-006.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000638"
      ]
    },
    "point-007.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000639"
      ]
    },
    "point-007.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000640"
      ]
    },
    "point-008.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000641"
      ]
    },
    "point-008.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 44,
      "evidence_ids": [
        "e000642"
      ]
    }
  },
  "plans": [],
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
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 1,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00001",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00001",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000005",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 1,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00001",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00001",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00001",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000006",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 1,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000007",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 1,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000008",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 1,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000009",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 1,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000010",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 1,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000011",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 1,
      "action": {
        "call_id": "call_4996e2a14c3b4c0e9b44b693",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000012",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 2,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00002",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00002",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000013",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 2,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00002",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00002",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00002",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000014",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000015",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000016",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000017",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 2,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000018",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 2,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000019",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 2,
      "action": {
        "call_id": "call_66c575511db5448d8cac3a39",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000020",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000021",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000022",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000023",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 3,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000024",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 3,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000025",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 3,
      "action": {
        "call_id": "call_d7fe424ce06b4f5089684f3b",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000026",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000027",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000028",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000029",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 4,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000030",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 4,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000031",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 4,
      "action": {
        "call_id": "call_696e12b2bb7843f7923d0e87",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000032",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 5,
      "object_id": "point-001",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000033",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 5,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000034",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000035",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000036",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000037",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 5,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000038",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 5,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000039",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 5,
      "action": {
        "call_id": "call_2850df94a12b430188ba6897",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000040",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 6,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00003",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00003",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000041",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 6,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00003",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00003",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00003",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000042",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000043",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000044",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000045",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000046",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000047",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 6,
      "action": {
        "call_id": "call_c04e20e9c44541b5bd5086b4",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000048",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000049",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000050",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000051",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 7,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000052",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 7,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000053",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 7,
      "action": {
        "call_id": "call_36097fb1af024935a5bed45a",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000054",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000055",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000056",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000057",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 8,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000058",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 8,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000059",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 8,
      "action": {
        "call_id": "call_b64cb61dd9f343c68bef007f",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000060",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000061",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000062",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000063",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000064",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000065",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 9,
      "action": {
        "call_id": "call_c502e9b0719f4b919effed3d",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000066",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 10,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00003",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00003",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000067",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000068",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000069",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000070",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000071",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000072",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000073",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000074",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 10,
      "action": {
        "call_id": "call_29a1a53d66144f9fad97500a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000075",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000076",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000077",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000078",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000079",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000080",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000081",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000082",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 11,
      "action": {
        "call_id": "call_108832cb62f14dc6a1209973",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000083",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 12,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00003",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00003",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000084",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000085",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000086",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000087",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 12,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000088",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 12,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000089",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 12,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000090",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 12,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000091",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 12,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000092",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 12,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000093",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 12,
      "action": {
        "call_id": "call_bcc430a1da9846f89bfd7621",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000094",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000095",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000096",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000097",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000098",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000099",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000100",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000101",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000102",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000103",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 13,
      "action": {
        "call_id": "call_9ee5a4d2fce84682879b407e",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000104",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 14,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00003",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00003",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000105",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000106",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000107",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000108",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000109",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000110",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000111",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000112",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000113",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000114",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000115",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000116",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 14,
      "action": {
        "call_id": "call_c18f4cd8a96e43679772eecf",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000117",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 15,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00004",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00004",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000118",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 15,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00004",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00004",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00004",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000119",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 15,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00004",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00004",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000120",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 15,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00004",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00004",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000121",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 15,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00004",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00004",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000122",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000123",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000124",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000125",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000126",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000127",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000128",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000129",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000130",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000131",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000132",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000133",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 15,
      "action": {
        "call_id": "call_5f1381bcb243490faae0d17a",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000134",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000135",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000136",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000137",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000138",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000139",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000140",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000141",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000142",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000143",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000144",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000145",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 16,
      "action": {
        "call_id": "call_0eb54e00e1084b35980d16f5",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000146",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000147",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000148",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000149",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000150",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000151",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000152",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000153",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000154",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000155",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000156",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000157",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 17,
      "action": {
        "call_id": "call_5d8558d81cf1483d9e7e315e",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000158",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 18,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00005",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00005",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000159",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 18,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00005",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00005",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00005",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000160",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 18,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00005",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00005",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000161",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 18,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00005",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00005",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000162",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 18,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00005",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00005",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000163",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000164",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000165",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000166",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000167",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000168",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000169",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000170",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000171",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000172",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000173",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000174",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 18,
      "action": {
        "call_id": "call_5a244eefc9f5426aba4bdc63",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000175",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000176",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000177",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000178",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000179",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000180",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000181",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000182",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000183",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000184",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000185",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000186",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 19,
      "action": {
        "call_id": "call_a41a03d2bca24780bc2db058",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000187",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 20,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00006",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00006",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000188",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 20,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00006",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00006",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00006",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000189",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 20,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00006",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00006",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000190",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 20,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00006",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00006",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000191",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 20,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00006",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00006",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000192",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000193",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000194",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000195",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000196",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000197",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000198",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000199",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000200",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000201",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000202",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000203",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 20,
      "action": {
        "call_id": "call_08e648f1523746c3b2e45b02",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000204",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000205",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000206",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000207",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000208",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000209",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000210",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000211",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000212",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000213",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000214",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 21,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000215",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 21,
      "action": {
        "call_id": "call_a60c0a9e35ad41879ad6fbe7",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000216",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 22,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00007",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00007",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000217",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 22,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00007",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00007",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00007",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000218",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 22,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00007",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00007",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000219",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 22,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00007",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00007",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000220",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 22,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00007",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00007",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000221",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000222",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000223",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000224",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000225",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000226",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000227",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000228",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000229",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000230",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000231",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000232",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 22,
      "action": {
        "call_id": "call_96d382d28a514cdb919350e5",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000233",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000234",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000235",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000236",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000237",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000238",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000239",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000240",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000241",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000242",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000243",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000244",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 23,
      "action": {
        "call_id": "call_9b66df4a5374420384bb2a7d",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000245",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000246",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000247",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000248",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000249",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000250",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000251",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000252",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000253",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000254",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000255",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000256",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 24,
      "action": {
        "call_id": "call_e60ce0cbd98c448da8f20021",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000257",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 25,
      "object_id": "point-001",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000258",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 25,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000259",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 25,
      "object_id": "point-002",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000260",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 25,
      "object_id": "point-003",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000261",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 25,
      "object_id": "point-004",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000262",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000263",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000264",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000265",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000266",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000267",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000268",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000269",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000270",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000271",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000272",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000273",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 25,
      "action": {
        "call_id": "call_0b21ce9a8c2748e5b86456a8",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000274",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 26,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00008",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00008",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000275",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 26,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00008",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00008",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00008",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000276",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 26,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00008",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00008",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000277",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 26,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00008",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00008",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000278",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 26,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00008",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00008",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000279",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000280",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000281",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000282",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000283",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000284",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000285",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000286",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000287",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000288",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000289",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000290",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 26,
      "action": {
        "call_id": "call_ddd5d40d05bf4a28bed6fada",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000291",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000292",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000293",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000294",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000295",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000296",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000297",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000298",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000299",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000300",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000301",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000302",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 27,
      "action": {
        "call_id": "call_ef024b2b85b04ebdb6a6edfd",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000303",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 28,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00008",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00008",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000304",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000305",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000306",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000307",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000308",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000309",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000310",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000311",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000312",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000313",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000314",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000315",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000316",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000317",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 28,
      "action": {
        "call_id": "call_81495b74d060443ca1d7774c",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000318",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 29,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000319",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 29,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00009",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000320",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 29,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000321",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 29,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000322",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 29,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000323",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 29,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000324",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000325",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000326",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000327",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000328",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000329",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000330",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000331",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000332",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000333",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000334",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000335",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000336",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000337",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 29,
      "action": {
        "call_id": "call_15b7673ec1bd4df6899df24f",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000338",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 30,
      "observation": {
        "object_id": "point-006",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000339",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000340",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000341",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000342",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000343",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000344",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000345",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000346",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000347",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000348",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000349",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000350",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000351",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000352",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000353",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000354",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 30,
      "action": {
        "call_id": "call_c934f39618b4477c8a7ef6d5",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000355",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000356",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000357",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000358",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000359",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000360",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000361",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000362",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000363",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000364",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000365",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000366",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000367",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000368",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000369",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 31,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000370",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 31,
      "action": {
        "call_id": "call_ae3949e5a07d494298097aa8",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000371",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 32,
      "object_id": "point-005",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000372",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000373",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000374",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000375",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000376",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000377",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000378",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000379",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000380",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000381",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000382",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000383",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000384",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000385",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000386",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000387",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 32,
      "action": {
        "call_id": "call_43fa5ec71d6b4d83a879e3da",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000388",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 33,
      "observation": {
        "object_id": "point-007",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00009",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00009",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000389",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000390",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000391",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000392",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000393",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000394",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000395",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000396",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000397",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000398",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000399",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000400",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000401",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000402",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000403",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000404",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000405",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 33,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000406",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 33,
      "action": {
        "call_id": "call_b266ed65183945c5a1d36fef",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000407",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000408",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000409",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000410",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000411",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000412",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000413",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000414",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000415",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000416",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000417",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000418",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000419",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000420",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000421",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000422",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000423",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000424",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 34,
      "action": {
        "call_id": "call_6a43c813f1244ec0be79e48e",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000425",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 35,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000426",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 35,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00010",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000427",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 35,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000428",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 35,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000429",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 35,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000430",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 35,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000431",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 35,
      "observation": {
        "object_id": "point-006",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000432",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 35,
      "observation": {
        "object_id": "point-007",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00010",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00010",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000433",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000434",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000435",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000436",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000437",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000438",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000439",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000440",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000441",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000442",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000443",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000444",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000445",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000446",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000447",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000448",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000449",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 35,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000450",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 35,
      "action": {
        "call_id": "call_bd2b12f1c9274efbbf147823",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000451",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000452",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000453",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000454",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000455",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000456",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000457",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000458",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000459",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000460",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000461",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000462",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000463",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000464",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000465",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000466",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000467",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000468",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 36,
      "action": {
        "call_id": "call_eaf8edcd98ee4916896a0f4c",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000469",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 37,
      "observation": {
        "object_id": "point-001",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000470",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 37,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00011",
          "position_m": [
            -0.746545465871329,
            0.31277287102254453,
            1.4235464334487915
          ],
          "source": "rgbd_depth_intrinsics"
        },
        "measurement_provenance": {
          "identity": "task_given_label_plus_unique_current_color_component",
          "tracking": "rgbd_optical_flow",
          "reference_pose": "existing_public_idealized_simulator_odometry",
          "motion_delta_used": false
        }
      }
    },
    {
      "evidence_id": "e000471",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 37,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000472",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 37,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000473",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 37,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000474",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 37,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000475",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 37,
      "observation": {
        "object_id": "point-006",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000476",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 37,
      "observation": {
        "object_id": "point-007",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000477",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000478",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000479",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000480",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000481",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000482",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000483",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000484",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000485",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000486",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000487",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000488",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000489",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000490",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000491",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000492",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000493",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000494",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 37,
      "action": {
        "call_id": "call_20bf19af3f0f4658a18dde21",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000495",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000496",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000497",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000498",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000499",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000500",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000501",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000502",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000503",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000504",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000505",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000506",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000507",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000508",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000509",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000510",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000511",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000512",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 38,
      "action": {
        "call_id": "call_e6722900328845d0bdb35640",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000513",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000514",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000515",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000516",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000517",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000518",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000519",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000520",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000521",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000522",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000523",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000524",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000525",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000526",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000527",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000528",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000529",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000530",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 39,
      "action": {
        "call_id": "call_9e0b03c8c1d741fea76db218",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000531",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-001",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000532",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000533",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-002",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000534",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-003",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000535",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-004",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000536",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-005",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000537",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-006",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000538",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-007",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000539",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000540",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000541",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000542",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000543",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000544",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000545",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000546",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000547",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000548",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000549",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000550",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000551",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000552",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000553",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000554",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000555",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000556",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 40,
      "action": {
        "call_id": "call_647b21bd09cf4148a9af4c10",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000557",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000558",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000559",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000560",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000561",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000562",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000563",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000564",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000565",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000566",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000567",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000568",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000569",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000570",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000571",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000572",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000573",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000574",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 41,
      "action": {
        "call_id": "call_5183015e4abe40dda154381b",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000575",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 42,
      "observation": {
        "object_id": "point-008",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354,
            0.7421
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00011",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00011",
          "pixel_uv": [
            156.0,
            248.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000576",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000577",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000578",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000579",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-008.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000580",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-008.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000581",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000582",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000583",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000584",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000585",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000586",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000587",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000588",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000589",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000590",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000591",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000592",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000593",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000594",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000595",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 42,
      "action": {
        "call_id": "call_0302e67b47754a82904da456",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000596",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "point-001",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000597",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "task:B",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000598",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "point-002",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000599",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "point-003",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000600",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "point-004",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000601",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "point-005",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000602",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "point-006",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000603",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 43,
      "object_id": "point-007",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000604",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000605",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000606",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000607",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000608",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000609",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000610",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000611",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000612",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000613",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000614",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000615",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000616",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000617",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000618",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000619",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000620",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000621",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-008.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000622",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-008.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000623",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 43,
      "action": {
        "call_id": "call_35ef5b06367b47a1a0e0a4f7",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    },
    {
      "evidence_id": "e000624",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.x_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000625",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000626",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000627",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000628",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000629",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-002.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000630",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-002.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000631",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-003.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000632",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-003.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000633",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-004.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000634",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-004.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000635",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-005.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000636",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-005.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000637",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-006.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000638",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-006.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000639",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-007.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000640",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-007.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000641",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-008.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000642",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 44,
      "name": "point-008.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000643",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 44,
      "action": {
        "call_id": "call_48c1b44783624f26aa981f0d",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT"
      }
    }
  ]
}
```

## 操作经验

## 程序工具
