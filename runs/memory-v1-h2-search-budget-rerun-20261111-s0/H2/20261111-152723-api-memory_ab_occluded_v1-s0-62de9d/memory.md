# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 99,
    "revision": 133,
    "active_plan_id": "plan-0033",
    "public_context": {
      "image_id": "frame-00051",
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
        "image_id": "frame-00051",
        "image_size": {
          "width": 640,
          "height": 360
        },
        "tracked_points": [
          {
            "point_id": "point-027",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "optical_flow_lost",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-028",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "inconsistent_flow",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-029",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "inconsistent_flow",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-030",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "inconsistent_flow",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-031",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "optical_flow_lost",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-032",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "inconsistent_flow",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-033",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "inconsistent_flow",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-034",
            "image_id": "frame-00051",
            "timestamp_s": 108.63999999992821,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "optical_flow_lost",
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
        "target_candidates": [],
        "source": "current_public_rgbd_and_tool_geometry"
      },
      "visual_candidates": []
    },
    "exploration": {
      "successful_turns_without_search_progress": 0,
      "turn_limit": 6,
      "stalled": false,
      "progress_basis": "successful_translation_tool_or_first_task_observation_not_motion_gt",
      "evidence_ids": [],
      "recovery": "change_viewpoint_with_translation; inspect_geometry_or_abort_if_motion_unsupported",
      "decisions_since_task_novelty": 99,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "review_due": true,
      "review_count": 8,
      "last_review_step": 96,
      "review_evidence_id": "e000592",
      "review_semantics": "advisory_strategy_review_not_failure_or_motion_prohibition"
    }
  },
  "pose": {
    "frame": "episode_start",
    "position_m": [
      0.79901707634295,
      6.180561223539937
    ],
    "yaw_rad": -1.9717433992014755,
    "source": "simulated_proprioception",
    "provenance": "existing_public_idealized_simulator_odometry"
  },
  "objects": [
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "object_id": "point-001",
      "visual_feature": {
        "image_id": "frame-00001",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 1,
      "evidence_ids": [
        "e000004"
      ],
      "candidate_pose": null
    },
    {
      "category": "task_target",
      "anchor_node": null,
      "source": "task_label_rgbd_tracking",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8852620242737823,
          0.735033009777705
        ]
      },
      "object_id": "task:B",
      "visual_feature": {
        "image_id": "frame-00016",
        "pixel_uv": [
          297.0,
          193.0
        ]
      },
      "confidence": 0.95,
      "state": "stale",
      "last_seen": 30,
      "evidence_ids": [
        "e000005",
        "e000023",
        "e000035",
        "e000052",
        "e000067",
        "e000084",
        "e000102",
        "e000117",
        "e000131",
        "e000147",
        "e000162",
        "e000176",
        "e000191",
        "e000205"
      ],
      "candidate_pose": null,
      "task_label": "B",
      "label_description": "绿方块",
      "camera_pose": {
        "frame": "current_camera_optical",
        "image_id": "frame-00016",
        "position_m": [
          -0.040307654497876245,
          0.02418459269872575,
          0.5585192441940308
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
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7393738185676924,
          0.382003556520252
        ]
      },
      "object_id": "point-002",
      "visual_feature": {
        "image_id": "frame-00003",
        "pixel_uv": [
          234.0,
          174.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 4,
      "evidence_ids": [
        "e000022"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7319796312697513,
          0.5556805700080226
        ]
      },
      "object_id": "point-003",
      "visual_feature": {
        "image_id": "frame-00004",
        "pixel_uv": [
          366.0,
          274.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 6,
      "evidence_ids": [
        "e000034"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7627708138852052,
          0.38095364208019017
        ]
      },
      "object_id": "point-004",
      "visual_feature": {
        "image_id": "frame-00007",
        "pixel_uv": [
          148.18,
          190.54
        ]
      },
      "confidence": 0.719,
      "state": "stale",
      "last_seen": 10,
      "evidence_ids": [
        "e000051",
        "e000059"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7344157565713676,
          0.3821539440126117
        ]
      },
      "object_id": "point-005",
      "visual_feature": {
        "image_id": "frame-00007",
        "pixel_uv": [
          146.0,
          301.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 11,
      "evidence_ids": [
        "e000066"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7335424367951235,
          0.640498243803566
        ]
      },
      "object_id": "point-006",
      "visual_feature": {
        "image_id": "frame-00008",
        "pixel_uv": [
          289.0,
          269.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 13,
      "evidence_ids": [
        "e000083"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          3.4004208923408856,
          1.5633539827284142
        ]
      },
      "object_id": "point-007",
      "visual_feature": {
        "image_id": "frame-00009",
        "pixel_uv": [
          266.0,
          221.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 16,
      "evidence_ids": [
        "e000101"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7337462727997779,
          0.38214475666172554
        ]
      },
      "object_id": "point-008",
      "visual_feature": {
        "image_id": "frame-00010",
        "pixel_uv": [
          127.0,
          327.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 18,
      "evidence_ids": [
        "e000116"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.8091086450660088,
          1.2889812071044175
        ]
      },
      "object_id": "point-009",
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          256.0,
          223.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 20,
      "evidence_ids": [
        "e000130"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8609319082677085,
          0.8144340891745419
        ]
      },
      "object_id": "point-010",
      "visual_feature": {
        "image_id": "frame-00012",
        "pixel_uv": [
          239.0,
          309.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 22,
      "evidence_ids": [
        "e000146"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288659069493864,
          0.3863726043865756
        ]
      },
      "object_id": "point-011",
      "visual_feature": {
        "image_id": "frame-00013",
        "pixel_uv": [
          179.0,
          340.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 24,
      "evidence_ids": [
        "e000161"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.0328796285414112,
          0.8984070403122474
        ]
      },
      "object_id": "point-012",
      "visual_feature": {
        "image_id": "frame-00014",
        "pixel_uv": [
          266.0,
          267.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 26,
      "evidence_ids": [
        "e000175"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.591430703572166,
          1.2175910688100848
        ]
      },
      "object_id": "point-013",
      "visual_feature": {
        "image_id": "frame-00015",
        "pixel_uv": [
          262.0,
          253.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 28,
      "evidence_ids": [
        "e000190"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8852620242737823,
          0.735033009777705
        ]
      },
      "object_id": "point-014",
      "visual_feature": {
        "image_id": "frame-00016",
        "pixel_uv": [
          297.0,
          193.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 30,
      "evidence_ids": [
        "e000204"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7021418598500693,
          1.7074169171205484
        ]
      },
      "object_id": "point-015",
      "visual_feature": {
        "image_id": "frame-00021",
        "pixel_uv": [
          231.0,
          343.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 39,
      "evidence_ids": [
        "e000252"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7900307378316307,
          1.9560474331728126
        ]
      },
      "object_id": "point-016",
      "visual_feature": {
        "image_id": "frame-00022",
        "pixel_uv": [
          214.0,
          350.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 41,
      "evidence_ids": [
        "e000266"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.964122003468572,
          2.3696275537602127
        ]
      },
      "object_id": "point-017",
      "visual_feature": {
        "image_id": "frame-00023",
        "pixel_uv": [
          217.0,
          342.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 43,
      "evidence_ids": [
        "e000278"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.3017593415189768,
          2.531611723225905
        ]
      },
      "object_id": "point-018",
      "visual_feature": {
        "image_id": "frame-00024",
        "pixel_uv": [
          313.0,
          344.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 45,
      "evidence_ids": [
        "e000290"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.393442221970812,
          3.0267669022717953
        ]
      },
      "object_id": "point-019",
      "visual_feature": {
        "image_id": "frame-00026",
        "pixel_uv": [
          246.0,
          320.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 49,
      "evidence_ids": [
        "e000311"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.7219852294274296,
          3.0318281341556013
        ]
      },
      "object_id": "point-020",
      "visual_feature": {
        "image_id": "frame-00028",
        "pixel_uv": [
          343.0,
          357.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 53,
      "evidence_ids": [
        "e000333"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.893684700315791,
          3.362242866347792
        ]
      },
      "object_id": "point-021",
      "visual_feature": {
        "image_id": "frame-00030",
        "pixel_uv": [
          329.0,
          348.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 56,
      "evidence_ids": [
        "e000351"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.6548728100217973,
          3.953194612255616
        ]
      },
      "object_id": "point-022",
      "visual_feature": {
        "image_id": "frame-00032",
        "pixel_uv": [
          362.0,
          334.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 60,
      "evidence_ids": [
        "e000373"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.4970705305555323,
          4.202008702340932
        ]
      },
      "object_id": "point-023",
      "visual_feature": {
        "image_id": "frame-00033",
        "pixel_uv": [
          301.0,
          344.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 64,
      "evidence_ids": [
        "e000395"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.5873445442816903,
          4.5271353457599695
        ]
      },
      "object_id": "point-024",
      "visual_feature": {
        "image_id": "frame-00035",
        "pixel_uv": [
          336.0,
          347.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 67,
      "evidence_ids": [
        "e000412"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.5866073728757826,
          4.786048793146852
        ]
      },
      "object_id": "point-025",
      "visual_feature": {
        "image_id": "frame-00036",
        "pixel_uv": [
          344.0,
          357.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 70,
      "evidence_ids": [
        "e000428"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.0933546780199532,
          4.877363071356823
        ]
      },
      "object_id": "point-026",
      "visual_feature": {
        "image_id": "frame-00037",
        "pixel_uv": [
          394.0,
          328.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 72,
      "evidence_ids": [
        "e000441"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.5211947919903206,
          5.389915109109923
        ]
      },
      "object_id": "point-027",
      "visual_feature": {
        "image_id": "frame-00040",
        "pixel_uv": [
          328.93,
          354.75
        ]
      },
      "confidence": 0.748,
      "state": "stale",
      "last_seen": 77,
      "evidence_ids": [
        "e000459",
        "e000467",
        "e000474"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.2753451247079461,
          5.961051220558526
        ]
      },
      "object_id": "point-028",
      "visual_feature": {
        "image_id": "frame-00041",
        "pixel_uv": [
          359.0,
          304.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 79,
      "evidence_ids": [
        "e000487"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.9424846738286271,
          5.96760303227536
        ]
      },
      "object_id": "point-029",
      "visual_feature": {
        "image_id": "frame-00042",
        "pixel_uv": [
          287.0,
          320.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 84,
      "evidence_ids": [
        "e000513"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.44421999308692367,
          5.980061528032222
        ]
      },
      "object_id": "point-030",
      "visual_feature": {
        "image_id": "frame-00043",
        "pixel_uv": [
          151.0,
          320.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 86,
      "evidence_ids": [
        "e000526"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.27552046513072087,
          5.9852318754380605
        ]
      },
      "object_id": "point-031",
      "visual_feature": {
        "image_id": "frame-00045",
        "pixel_uv": [
          86.0,
          344.0
        ]
      },
      "confidence": 1.0,
      "state": "stale",
      "last_seen": 89,
      "evidence_ids": [
        "e000543"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.19116123428988596,
          5.986632457342582
        ]
      },
      "object_id": "point-032",
      "visual_feature": {
        "image_id": "frame-00047",
        "pixel_uv": [
          251.0,
          334.0
        ]
      },
      "confidence": 1.0,
      "state": "unknown",
      "last_seen": 93,
      "evidence_ids": [
        "e000567"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.024575548622372434,
          5.990335401341222
        ]
      },
      "object_id": "point-033",
      "visual_feature": {
        "image_id": "frame-00049",
        "pixel_uv": [
          226.0,
          347.0
        ]
      },
      "confidence": 1.0,
      "state": "unknown",
      "last_seen": 96,
      "evidence_ids": [
        "e000584"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "anchor_node": null,
      "source": "rgbd_optical_flow",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.30605287547588134,
          5.997360022194634
        ]
      },
      "object_id": "point-034",
      "visual_feature": {
        "image_id": "frame-00050",
        "pixel_uv": [
          198.0,
          322.0
        ]
      },
      "confidence": 1.0,
      "state": "unknown",
      "last_seen": 98,
      "evidence_ids": [
        "e000598"
      ],
      "candidate_pose": null
    }
  ],
  "active_beliefs": [],
  "invalidated": [],
  "events": [
    {
      "event_id": "event-1",
      "kind": "replan_required",
      "step": 3,
      "evidence_ids": [
        "e000021"
      ],
      "plan_id": "plan-0001"
    },
    {
      "event_id": "event-2",
      "kind": "target_state_changed",
      "step": 6,
      "evidence_ids": [
        "e000035"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-3",
      "kind": "target_state_changed",
      "step": 9,
      "evidence_ids": [
        "e000052"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-4",
      "kind": "target_state_changed",
      "step": 11,
      "evidence_ids": [
        "e000067"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-5",
      "kind": "target_state_changed",
      "step": 11,
      "evidence_ids": [
        "e000068"
      ],
      "object_id": "point-001",
      "state": "stale"
    },
    {
      "event_id": "event-6",
      "kind": "replan_required",
      "step": 11,
      "evidence_ids": [
        "e000068"
      ],
      "object_id": "point-001",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-7",
      "kind": "search_review_due",
      "step": 12,
      "evidence_ids": [
        "e000082"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-8",
      "kind": "target_state_changed",
      "step": 14,
      "evidence_ids": [
        "e000092"
      ],
      "object_id": "point-002",
      "state": "stale"
    },
    {
      "event_id": "event-9",
      "kind": "replan_required",
      "step": 14,
      "evidence_ids": [
        "e000092"
      ],
      "object_id": "point-002",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-10",
      "kind": "target_state_changed",
      "step": 16,
      "evidence_ids": [
        "e000102",
        "e000103"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-11",
      "kind": "replan_required",
      "step": 16,
      "evidence_ids": [
        "e000102"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-12",
      "kind": "target_state_changed",
      "step": 16,
      "evidence_ids": [
        "e000104"
      ],
      "object_id": "point-003",
      "state": "stale"
    },
    {
      "event_id": "event-13",
      "kind": "replan_required",
      "step": 16,
      "evidence_ids": [
        "e000104"
      ],
      "object_id": "point-003",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-14",
      "kind": "target_state_changed",
      "step": 18,
      "evidence_ids": [
        "e000117"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-15",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000131",
        "e000132"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-16",
      "kind": "replan_required",
      "step": 20,
      "evidence_ids": [
        "e000131"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-17",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000133"
      ],
      "object_id": "point-004",
      "state": "stale"
    },
    {
      "event_id": "event-18",
      "kind": "replan_required",
      "step": 20,
      "evidence_ids": [
        "e000133"
      ],
      "object_id": "point-004",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-19",
      "kind": "target_state_changed",
      "step": 21,
      "evidence_ids": [
        "e000141"
      ],
      "object_id": "point-005",
      "state": "stale"
    },
    {
      "event_id": "event-20",
      "kind": "replan_required",
      "step": 21,
      "evidence_ids": [
        "e000141"
      ],
      "object_id": "point-005",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-21",
      "kind": "target_state_changed",
      "step": 22,
      "evidence_ids": [
        "e000147"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-22",
      "kind": "target_state_changed",
      "step": 23,
      "evidence_ids": [
        "e000156"
      ],
      "object_id": "point-006",
      "state": "stale"
    },
    {
      "event_id": "event-23",
      "kind": "replan_required",
      "step": 23,
      "evidence_ids": [
        "e000156"
      ],
      "object_id": "point-006",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-24",
      "kind": "target_state_changed",
      "step": 24,
      "evidence_ids": [
        "e000162"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-25",
      "kind": "search_review_due",
      "step": 24,
      "evidence_ids": [
        "e000169"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-26",
      "kind": "replan_required",
      "step": 25,
      "evidence_ids": [
        "e000174"
      ],
      "plan_id": "plan-0008"
    },
    {
      "event_id": "event-27",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000176",
        "e000177"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-28",
      "kind": "replan_required",
      "step": 26,
      "evidence_ids": [
        "e000176"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-29",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000178"
      ],
      "object_id": "point-007",
      "state": "stale"
    },
    {
      "event_id": "event-30",
      "kind": "replan_required",
      "step": 26,
      "evidence_ids": [
        "e000178"
      ],
      "object_id": "point-007",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-31",
      "kind": "target_state_changed",
      "step": 28,
      "evidence_ids": [
        "e000191",
        "e000192"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-32",
      "kind": "replan_required",
      "step": 28,
      "evidence_ids": [
        "e000191"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-33",
      "kind": "target_state_changed",
      "step": 28,
      "evidence_ids": [
        "e000193"
      ],
      "object_id": "point-008",
      "state": "stale"
    },
    {
      "event_id": "event-34",
      "kind": "replan_required",
      "step": 28,
      "evidence_ids": [
        "e000193"
      ],
      "object_id": "point-008",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-35",
      "kind": "target_state_changed",
      "step": 30,
      "evidence_ids": [
        "e000205"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-36",
      "kind": "target_state_changed",
      "step": 30,
      "evidence_ids": [
        "e000207"
      ],
      "object_id": "point-009",
      "state": "stale"
    },
    {
      "event_id": "event-37",
      "kind": "replan_required",
      "step": 30,
      "evidence_ids": [
        "e000207"
      ],
      "object_id": "point-009",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-38",
      "kind": "target_state_changed",
      "step": 32,
      "evidence_ids": [
        "e000219"
      ],
      "object_id": "point-010",
      "state": "stale"
    },
    {
      "event_id": "event-39",
      "kind": "replan_required",
      "step": 32,
      "evidence_ids": [
        "e000219"
      ],
      "object_id": "point-010",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-40",
      "kind": "target_state_changed",
      "step": 34,
      "evidence_ids": [
        "e000228"
      ],
      "object_id": "point-011",
      "state": "stale"
    },
    {
      "event_id": "event-41",
      "kind": "replan_required",
      "step": 34,
      "evidence_ids": [
        "e000228"
      ],
      "object_id": "point-011",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-42",
      "kind": "target_state_changed",
      "step": 36,
      "evidence_ids": [
        "e000237"
      ],
      "object_id": "point-012",
      "state": "stale"
    },
    {
      "event_id": "event-43",
      "kind": "replan_required",
      "step": 36,
      "evidence_ids": [
        "e000237"
      ],
      "object_id": "point-012",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-44",
      "kind": "search_review_due",
      "step": 36,
      "evidence_ids": [
        "e000242"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-45",
      "kind": "target_state_changed",
      "step": 38,
      "evidence_ids": [
        "e000247"
      ],
      "object_id": "point-013",
      "state": "stale"
    },
    {
      "event_id": "event-46",
      "kind": "replan_required",
      "step": 38,
      "evidence_ids": [
        "e000247"
      ],
      "object_id": "point-013",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-47",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000260"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-48",
      "kind": "replan_required",
      "step": 40,
      "evidence_ids": [
        "e000260"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-49",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000261"
      ],
      "object_id": "point-014",
      "state": "stale"
    },
    {
      "event_id": "event-50",
      "kind": "replan_required",
      "step": 40,
      "evidence_ids": [
        "e000261"
      ],
      "object_id": "point-014",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-51",
      "kind": "search_review_due",
      "step": 48,
      "evidence_ids": [
        "e000310"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-52",
      "kind": "target_state_changed",
      "step": 49,
      "evidence_ids": [
        "e000312"
      ],
      "object_id": "point-015",
      "state": "stale"
    },
    {
      "event_id": "event-53",
      "kind": "replan_required",
      "step": 49,
      "evidence_ids": [
        "e000312"
      ],
      "object_id": "point-015",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-54",
      "kind": "target_state_changed",
      "step": 51,
      "evidence_ids": [
        "e000324"
      ],
      "object_id": "point-016",
      "state": "stale"
    },
    {
      "event_id": "event-55",
      "kind": "replan_required",
      "step": 51,
      "evidence_ids": [
        "e000324"
      ],
      "object_id": "point-016",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-56",
      "kind": "target_state_changed",
      "step": 53,
      "evidence_ids": [
        "e000334"
      ],
      "object_id": "point-017",
      "state": "stale"
    },
    {
      "event_id": "event-57",
      "kind": "replan_required",
      "step": 53,
      "evidence_ids": [
        "e000334"
      ],
      "object_id": "point-017",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-58",
      "kind": "target_state_changed",
      "step": 55,
      "evidence_ids": [
        "e000346"
      ],
      "object_id": "point-018",
      "state": "stale"
    },
    {
      "event_id": "event-59",
      "kind": "replan_required",
      "step": 55,
      "evidence_ids": [
        "e000346"
      ],
      "object_id": "point-018",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-60",
      "kind": "target_state_changed",
      "step": 59,
      "evidence_ids": [
        "e000368"
      ],
      "object_id": "point-019",
      "state": "stale"
    },
    {
      "event_id": "event-61",
      "kind": "replan_required",
      "step": 59,
      "evidence_ids": [
        "e000368"
      ],
      "object_id": "point-019",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-62",
      "kind": "search_review_due",
      "step": 60,
      "evidence_ids": [
        "e000380"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-63",
      "kind": "target_state_changed",
      "step": 63,
      "evidence_ids": [
        "e000390"
      ],
      "object_id": "point-020",
      "state": "stale"
    },
    {
      "event_id": "event-64",
      "kind": "replan_required",
      "step": 63,
      "evidence_ids": [
        "e000390"
      ],
      "object_id": "point-020",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-65",
      "kind": "target_state_changed",
      "step": 66,
      "evidence_ids": [
        "e000407"
      ],
      "object_id": "point-021",
      "state": "stale"
    },
    {
      "event_id": "event-66",
      "kind": "replan_required",
      "step": 66,
      "evidence_ids": [
        "e000407"
      ],
      "object_id": "point-021",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-67",
      "kind": "target_state_changed",
      "step": 70,
      "evidence_ids": [
        "e000429"
      ],
      "object_id": "point-022",
      "state": "stale"
    },
    {
      "event_id": "event-68",
      "kind": "replan_required",
      "step": 70,
      "evidence_ids": [
        "e000429"
      ],
      "object_id": "point-022",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-69",
      "kind": "search_review_due",
      "step": 72,
      "evidence_ids": [
        "e000448"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-70",
      "kind": "target_state_changed",
      "step": 74,
      "evidence_ids": [
        "e000454"
      ],
      "object_id": "point-023",
      "state": "stale"
    },
    {
      "event_id": "event-71",
      "kind": "replan_required",
      "step": 74,
      "evidence_ids": [
        "e000454"
      ],
      "object_id": "point-023",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-72",
      "kind": "target_state_changed",
      "step": 76,
      "evidence_ids": [
        "e000467"
      ],
      "object_id": "point-027",
      "state": "confirmed"
    },
    {
      "event_id": "event-73",
      "kind": "target_state_changed",
      "step": 77,
      "evidence_ids": [
        "e000474"
      ],
      "object_id": "point-027",
      "state": "unknown"
    },
    {
      "event_id": "event-74",
      "kind": "target_state_changed",
      "step": 77,
      "evidence_ids": [
        "e000475"
      ],
      "object_id": "point-024",
      "state": "stale"
    },
    {
      "event_id": "event-75",
      "kind": "replan_required",
      "step": 77,
      "evidence_ids": [
        "e000475"
      ],
      "object_id": "point-024",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-76",
      "kind": "target_state_changed",
      "step": 80,
      "evidence_ids": [
        "e000495"
      ],
      "object_id": "point-025",
      "state": "stale"
    },
    {
      "event_id": "event-77",
      "kind": "replan_required",
      "step": 80,
      "evidence_ids": [
        "e000495"
      ],
      "object_id": "point-025",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-78",
      "kind": "target_state_changed",
      "step": 82,
      "evidence_ids": [
        "e000504"
      ],
      "object_id": "point-026",
      "state": "stale"
    },
    {
      "event_id": "event-79",
      "kind": "replan_required",
      "step": 82,
      "evidence_ids": [
        "e000504"
      ],
      "object_id": "point-026",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-80",
      "kind": "search_review_due",
      "step": 84,
      "evidence_ids": [
        "e000520"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-81",
      "kind": "target_state_changed",
      "step": 87,
      "evidence_ids": [
        "e000534"
      ],
      "object_id": "point-027",
      "state": "stale"
    },
    {
      "event_id": "event-82",
      "kind": "replan_required",
      "step": 87,
      "evidence_ids": [
        "e000534"
      ],
      "object_id": "point-027",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-83",
      "kind": "target_state_changed",
      "step": 89,
      "evidence_ids": [
        "e000544"
      ],
      "object_id": "point-028",
      "state": "stale"
    },
    {
      "event_id": "event-84",
      "kind": "replan_required",
      "step": 89,
      "evidence_ids": [
        "e000544"
      ],
      "object_id": "point-028",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-85",
      "kind": "target_state_changed",
      "step": 94,
      "evidence_ids": [
        "e000575"
      ],
      "object_id": "point-029",
      "state": "stale"
    },
    {
      "event_id": "event-86",
      "kind": "replan_required",
      "step": 94,
      "evidence_ids": [
        "e000575"
      ],
      "object_id": "point-029",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-87",
      "kind": "target_state_changed",
      "step": 96,
      "evidence_ids": [
        "e000585"
      ],
      "object_id": "point-030",
      "state": "stale"
    },
    {
      "event_id": "event-88",
      "kind": "replan_required",
      "step": 96,
      "evidence_ids": [
        "e000585"
      ],
      "object_id": "point-030",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-89",
      "kind": "search_review_due",
      "step": 96,
      "evidence_ids": [
        "e000592"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-90",
      "kind": "target_state_changed",
      "step": 99,
      "evidence_ids": [
        "e000606"
      ],
      "object_id": "point-031",
      "state": "stale"
    },
    {
      "event_id": "event-91",
      "kind": "replan_required",
      "step": 99,
      "evidence_ids": [
        "e000606"
      ],
      "object_id": "point-031",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-92",
      "kind": "skill_stuck",
      "step": 99,
      "evidence_ids": [
        "e000610"
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
      "value": 0.79901707634295,
      "source": "simulated_proprioception",
      "step": 99,
      "evidence_ids": [
        "e000607"
      ]
    },
    "pose.y_m": {
      "value": 6.180561223539937,
      "source": "simulated_proprioception",
      "step": 99,
      "evidence_ids": [
        "e000608"
      ]
    },
    "pose.yaw_rad": {
      "value": -1.9717433992014755,
      "source": "simulated_proprioception",
      "step": 99,
      "evidence_ids": [
        "e000609"
      ]
    },
    "point-001.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 1,
      "evidence_ids": [
        "e000009"
      ]
    },
    "point-001.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 1,
      "evidence_ids": [
        "e000010"
      ]
    },
    "point-002.range_m": {
      "value": 1.7714,
      "source": "rgbd_optical_flow",
      "step": 4,
      "evidence_ids": [
        "e000027"
      ]
    },
    "point-002.bearing_rad": {
      "value": 0.2203,
      "source": "rgbd_optical_flow",
      "step": 4,
      "evidence_ids": [
        "e000028"
      ]
    },
    "point-003.range_m": {
      "value": 1.7972,
      "source": "rgbd_optical_flow",
      "step": 6,
      "evidence_ids": [
        "e000039"
      ]
    },
    "point-003.bearing_rad": {
      "value": -0.1246,
      "source": "rgbd_optical_flow",
      "step": 6,
      "evidence_ids": [
        "e000040"
      ]
    },
    "point-004.range_m": {
      "value": 1.5905,
      "source": "rgbd_optical_flow",
      "step": 11,
      "evidence_ids": [
        "e000074"
      ]
    },
    "point-004.bearing_rad": {
      "value": 0.4053,
      "source": "rgbd_optical_flow",
      "step": 11,
      "evidence_ids": [
        "e000075"
      ]
    },
    "point-005.range_m": {
      "value": 1.5627,
      "source": "rgbd_optical_flow",
      "step": 11,
      "evidence_ids": [
        "e000072"
      ]
    },
    "point-005.bearing_rad": {
      "value": 0.4093,
      "source": "rgbd_optical_flow",
      "step": 11,
      "evidence_ids": [
        "e000073"
      ]
    },
    "point-006.range_m": {
      "value": 1.6208,
      "source": "rgbd_optical_flow",
      "step": 13,
      "evidence_ids": [
        "e000088"
      ]
    },
    "point-006.bearing_rad": {
      "value": 0.0762,
      "source": "rgbd_optical_flow",
      "step": 13,
      "evidence_ids": [
        "e000089"
      ]
    },
    "point-007.range_m": {
      "value": 3.2821,
      "source": "rgbd_optical_flow",
      "step": 16,
      "evidence_ids": [
        "e000108"
      ]
    },
    "point-007.bearing_rad": {
      "value": 0.1525,
      "source": "rgbd_optical_flow",
      "step": 16,
      "evidence_ids": [
        "e000109"
      ]
    },
    "point-008.range_m": {
      "value": 1.3134,
      "source": "rgbd_optical_flow",
      "step": 18,
      "evidence_ids": [
        "e000122"
      ]
    },
    "point-008.bearing_rad": {
      "value": 0.4264,
      "source": "rgbd_optical_flow",
      "step": 18,
      "evidence_ids": [
        "e000123"
      ]
    },
    "point-009.range_m": {
      "value": 2.6327,
      "source": "rgbd_optical_flow",
      "step": 20,
      "evidence_ids": [
        "e000137"
      ]
    },
    "point-009.bearing_rad": {
      "value": 0.1746,
      "source": "rgbd_optical_flow",
      "step": 20,
      "evidence_ids": [
        "e000138"
      ]
    },
    "point-010.range_m": {
      "value": 1.3501,
      "source": "rgbd_optical_flow",
      "step": 22,
      "evidence_ids": [
        "e000152"
      ]
    },
    "point-010.bearing_rad": {
      "value": 0.1916,
      "source": "rgbd_optical_flow",
      "step": 22,
      "evidence_ids": [
        "e000153"
      ]
    },
    "point-011.range_m": {
      "value": 1.0928,
      "source": "rgbd_optical_flow",
      "step": 24,
      "evidence_ids": [
        "e000166"
      ]
    },
    "point-011.bearing_rad": {
      "value": 0.3051,
      "source": "rgbd_optical_flow",
      "step": 24,
      "evidence_ids": [
        "e000167"
      ]
    },
    "point-012.range_m": {
      "value": 1.5483,
      "source": "rgbd_optical_flow",
      "step": 26,
      "evidence_ids": [
        "e000182"
      ]
    },
    "point-012.bearing_rad": {
      "value": 0.133,
      "source": "rgbd_optical_flow",
      "step": 26,
      "evidence_ids": [
        "e000183"
      ]
    },
    "point-013.range_m": {
      "value": 1.9672,
      "source": "rgbd_optical_flow",
      "step": 28,
      "evidence_ids": [
        "e000197"
      ]
    },
    "point-013.bearing_rad": {
      "value": 0.1502,
      "source": "rgbd_optical_flow",
      "step": 28,
      "evidence_ids": [
        "e000198"
      ]
    },
    "point-014.range_m": {
      "value": 0.8804,
      "source": "rgbd_optical_flow",
      "step": 30,
      "evidence_ids": [
        "e000211"
      ]
    },
    "point-014.bearing_rad": {
      "value": 0.047,
      "source": "rgbd_optical_flow",
      "step": 30,
      "evidence_ids": [
        "e000212"
      ]
    },
    "point-015.range_m": {
      "value": 1.1471,
      "source": "rgbd_optical_flow",
      "step": 39,
      "evidence_ids": [
        "e000256"
      ]
    },
    "point-015.bearing_rad": {
      "value": 0.1964,
      "source": "rgbd_optical_flow",
      "step": 39,
      "evidence_ids": [
        "e000257"
      ]
    },
    "point-016.range_m": {
      "value": 1.1179,
      "source": "rgbd_optical_flow",
      "step": 41,
      "evidence_ids": [
        "e000270"
      ]
    },
    "point-016.bearing_rad": {
      "value": 0.2303,
      "source": "rgbd_optical_flow",
      "step": 41,
      "evidence_ids": [
        "e000271"
      ]
    },
    "point-017.range_m": {
      "value": 1.167,
      "source": "rgbd_optical_flow",
      "step": 43,
      "evidence_ids": [
        "e000282"
      ]
    },
    "point-017.bearing_rad": {
      "value": 0.2286,
      "source": "rgbd_optical_flow",
      "step": 43,
      "evidence_ids": [
        "e000283"
      ]
    },
    "point-018.range_m": {
      "value": 1.1365,
      "source": "rgbd_optical_flow",
      "step": 45,
      "evidence_ids": [
        "e000294"
      ]
    },
    "point-018.bearing_rad": {
      "value": 0.0085,
      "source": "rgbd_optical_flow",
      "step": 45,
      "evidence_ids": [
        "e000295"
      ]
    },
    "point-019.range_m": {
      "value": 1.2723,
      "source": "rgbd_optical_flow",
      "step": 49,
      "evidence_ids": [
        "e000316"
      ]
    },
    "point-019.bearing_rad": {
      "value": 0.1697,
      "source": "rgbd_optical_flow",
      "step": 49,
      "evidence_ids": [
        "e000317"
      ]
    },
    "point-020.range_m": {
      "value": 1.0729,
      "source": "rgbd_optical_flow",
      "step": 53,
      "evidence_ids": [
        "e000338"
      ]
    },
    "point-020.bearing_rad": {
      "value": -0.0601,
      "source": "rgbd_optical_flow",
      "step": 53,
      "evidence_ids": [
        "e000339"
      ]
    },
    "point-021.range_m": {
      "value": 1.1036,
      "source": "rgbd_optical_flow",
      "step": 56,
      "evidence_ids": [
        "e000355"
      ]
    },
    "point-021.bearing_rad": {
      "value": -0.0285,
      "source": "rgbd_optical_flow",
      "step": 56,
      "evidence_ids": [
        "e000356"
      ]
    },
    "point-022.range_m": {
      "value": 1.166,
      "source": "rgbd_optical_flow",
      "step": 60,
      "evidence_ids": [
        "e000377"
      ]
    },
    "point-022.bearing_rad": {
      "value": -0.0986,
      "source": "rgbd_optical_flow",
      "step": 60,
      "evidence_ids": [
        "e000378"
      ]
    },
    "point-023.range_m": {
      "value": 1.1123,
      "source": "rgbd_optical_flow",
      "step": 64,
      "evidence_ids": [
        "e000399"
      ]
    },
    "point-023.bearing_rad": {
      "value": 0.0359,
      "source": "rgbd_optical_flow",
      "step": 64,
      "evidence_ids": [
        "e000400"
      ]
    },
    "point-024.range_m": {
      "value": 1.1054,
      "source": "rgbd_optical_flow",
      "step": 67,
      "evidence_ids": [
        "e000416"
      ]
    },
    "point-024.bearing_rad": {
      "value": -0.0445,
      "source": "rgbd_optical_flow",
      "step": 67,
      "evidence_ids": [
        "e000417"
      ]
    },
    "point-025.range_m": {
      "value": 1.0755,
      "source": "rgbd_optical_flow",
      "step": 70,
      "evidence_ids": [
        "e000433"
      ]
    },
    "point-025.bearing_rad": {
      "value": -0.0581,
      "source": "rgbd_optical_flow",
      "step": 70,
      "evidence_ids": [
        "e000434"
      ]
    },
    "point-026.range_m": {
      "value": 1.2169,
      "source": "rgbd_optical_flow",
      "step": 72,
      "evidence_ids": [
        "e000445"
      ]
    },
    "point-026.bearing_rad": {
      "value": -0.1766,
      "source": "rgbd_optical_flow",
      "step": 72,
      "evidence_ids": [
        "e000446"
      ]
    },
    "point-027.range_m": {
      "value": 1.0696,
      "source": "rgbd_optical_flow",
      "step": 77,
      "evidence_ids": [
        "e000479"
      ]
    },
    "point-027.bearing_rad": {
      "value": -0.0278,
      "source": "rgbd_optical_flow",
      "step": 77,
      "evidence_ids": [
        "e000480"
      ]
    },
    "point-028.range_m": {
      "value": 1.3966,
      "source": "rgbd_optical_flow",
      "step": 79,
      "evidence_ids": [
        "e000491"
      ]
    },
    "point-028.bearing_rad": {
      "value": -0.1001,
      "source": "rgbd_optical_flow",
      "step": 79,
      "evidence_ids": [
        "e000492"
      ]
    },
    "point-029.range_m": {
      "value": 1.296,
      "source": "rgbd_optical_flow",
      "step": 84,
      "evidence_ids": [
        "e000517"
      ]
    },
    "point-029.bearing_rad": {
      "value": 0.0786,
      "source": "rgbd_optical_flow",
      "step": 84,
      "evidence_ids": [
        "e000518"
      ]
    },
    "point-030.range_m": {
      "value": 1.3346,
      "source": "rgbd_optical_flow",
      "step": 86,
      "evidence_ids": [
        "e000530"
      ]
    },
    "point-030.bearing_rad": {
      "value": 0.3779,
      "source": "rgbd_optical_flow",
      "step": 86,
      "evidence_ids": [
        "e000531"
      ]
    },
    "point-031.range_m": {
      "value": 1.2624,
      "source": "rgbd_optical_flow",
      "step": 90,
      "evidence_ids": [
        "e000554"
      ]
    },
    "point-031.bearing_rad": {
      "value": 0.4889,
      "source": "rgbd_optical_flow",
      "step": 90,
      "evidence_ids": [
        "e000555"
      ]
    },
    "point-032.range_m": {
      "value": 1.1505,
      "source": "rgbd_optical_flow",
      "step": 93,
      "evidence_ids": [
        "e000571"
      ]
    },
    "point-032.bearing_rad": {
      "value": 0.1533,
      "source": "rgbd_optical_flow",
      "step": 93,
      "evidence_ids": [
        "e000572"
      ]
    },
    "point-033.range_m": {
      "value": 1.1292,
      "source": "rgbd_optical_flow",
      "step": 96,
      "evidence_ids": [
        "e000589"
      ]
    },
    "point-033.bearing_rad": {
      "value": 0.2075,
      "source": "rgbd_optical_flow",
      "step": 96,
      "evidence_ids": [
        "e000590"
      ]
    },
    "point-034.range_m": {
      "value": 1.2687,
      "source": "rgbd_optical_flow",
      "step": 98,
      "evidence_ids": [
        "e000602"
      ]
    },
    "point-034.bearing_rad": {
      "value": 0.278,
      "source": "rgbd_optical_flow",
      "step": 98,
      "evidence_ids": [
        "e000603"
      ]
    }
  },
  "plans": [
    {
      "subgoals": [
        {
          "subgoal_id": "scan_right",
          "description": "Turn right 0.6 rad from initial yaw 0.0 to sweep the right hemisphere for blue ball A; reference is current heading, endpoint yaw <= -0.5 rad.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "le",
              "value": -0.5
            }
          ],
          "active": false,
          "status": "已失效",
          "evidence_ids": [
            "e000021"
          ]
        },
        {
          "subgoal_id": "scan_left_back",
          "description": "Sweep back left through original heading to the opposite side, ending yaw >= 0.5 rad, to look for A where the right sweep did not cover.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 0.5
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000020"
          ]
        },
        {
          "subgoal_id": "viewpoint_move",
          "description": "Short forward translation of 0.25 m toward the observed open floor ahead-left of tracked green candidate to gain a new viewpoint; endpoint measured forward pose.x_m >= 0.15 m.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 0.15
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000042"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "viewpoint_move"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "viewpoint_move"
        }
      ],
      "recovery": "Stop, re-inspect fresh geometry (tracked point-001 range/bearing and pose), then either resume the opposite sweep or take a different short viewpoint move; abort if geometry shows no safe direction.",
      "plan_id": "plan-0001",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "sweep_right_for_A",
          "description": "Sweep right hemisphere for blue ball A: turn right from current yaw 0.465 rad by 0.6 rad, committing to a rightward scan; endpoint yaw <= -0.1 rad.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "le",
              "value": -0.1
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000062"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "sweep_right_for_A"
        }
      ],
      "recovery": "Re-observe fresh geometry; if A still not visible, take a short supported translation or sweep the opposite direction; abort if no safe option.",
      "plan_id": "plan-0002",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "sweep_left_for_A",
          "description": "Turn left 0.55 rad from yaw ~-0.23 to yaw >= 0.30, committing to a leftward scan for blue ball A while keeping confirmed green block B as the observed reference on the left-front.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 0.3
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000081"
          ]
        },
        {
          "subgoal_id": "explore_viewpoint_forward",
          "description": "If A still unseen, take a short 0.25 m forward viewpoint change toward the open floor in front of the tracked B ray (point-005 at ~1.56 m), endpoint when point-005.range_m <= 1.35 m.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-005.range_m",
              "op": "le",
              "value": 1.35
            }
          ],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_viewpoint_forward"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_viewpoint_forward"
        }
      ],
      "recovery": "Re-observe fresh geometry; if A is still not visible and forward clearance is unsupported, sweep the opposite side or abort with a reason rather than looping turns.",
      "plan_id": "plan-0003",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_viewpoint_for_A",
          "description": "Move 0.3 m forward along the clear visible ray toward confirmed green block B (point-006 at 1.62 m, bearing 0.076 rad left of heading) to change viewpoint and search for the unseen blue ball A; endpoint when point-006.range_m <= 1.42.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-006.range_m",
              "op": "le",
              "value": 1.42
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000096"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_viewpoint_for_A"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_viewpoint_for_A"
        }
      ],
      "recovery": "Stop, re-observe fresh geometry, then scan the unexamined right side (negative yaw) for A, or abort with a reason if no geometry supports motion.",
      "plan_id": "plan-0004",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_right_for_A",
          "description": "Rotate right 0.6 rad (yaw 0.29 -> about -0.31) to survey the not-yet-examined right side for blue ball A, keeping the visible green candidate B (point-007, bearing 0.15 rad, range 3.28 m) as a stable geometric reference. No translation, so no collision exposure during the scan.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "le",
              "value": -0.25
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000114"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "scan_right_for_A"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_right_for_A"
        }
      ],
      "recovery": "Stop and re-observe fresh geometry; if A is visible, track its pixel and inspect geometry before approaching; if not, switch branch to a short forward translation along the evidenced clear ray to point-007 (B candidate) and inspect the new view.",
      "plan_id": "plan-0005",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_for_A",
          "description": "Rotate left 0.6 rad to survey the previously unexamined left sector for blue ball A, using the tracked green candidate point-008 (bearing 0.43 rad, range 1.31 m ahead-left) as a stable reference; endpoint is yaw near +0.34 rad. No translation, so no collision exposure.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 0.2
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000128"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "scan_left_for_A"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_left_for_A"
        }
      ],
      "recovery": "Stop and re-observe fresh geometry; if blue A becomes visible, track its pixel and inspect geometry before approaching; if not, change branch to a short translation along an evidenced direction with point-008 kept as reference, then inspect the new view.",
      "plan_id": "plan-0006",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_viewpoint_forward",
          "description": "Translate forward 0.3 m along the only evidenced clear ray (tracked green candidate point-009, bearing 0.175 rad, range 2.63 m ahead) to change viewpoint and survey for blue ball A; endpoint when point-009 range drops to <=2.35 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-009.range_m",
              "op": "le",
              "value": 2.35
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000145"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_viewpoint_forward"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_viewpoint_forward"
        }
      ],
      "recovery": "Stop, observe fresh geometry; if blue A becomes visible track its pixel and inspect geometry, otherwise pick another evidenced viewpoint change or abort with reason",
      "plan_id": "plan-0007",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_right_for_A",
          "description": "Rotate right 0.5 rad in place from current yaw 0.271 rad to sweep the unexplored right side of the view (away from green candidate point-010 at bearing +0.19 rad) looking for blue ball A; endpoint when pose.yaw_rad <= -0.15 rad",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "le",
              "value": -0.15
            }
          ],
          "active": false,
          "status": "已失效",
          "evidence_ids": [
            "e000174"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_right_for_A"
        }
      ],
      "recovery": "Stop and observe fresh frame; if blue A is visible, track its pixel and inspect geometry; if still no A after this sweep, choose a short translation to a new viewpoint with evidenced clearance or abort with reason",
      "plan_id": "plan-0008",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_viewpoint",
          "description": "Commit to a forward search leg along tracked reference point-012 (range ~1.55 m, bearing +0.13 rad ahead-left); translate forward 0.3 m to a new viewpoint to reveal occluded scene; endpoint pose.x_m >= 0.85",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 0.85
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000200"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_viewpoint"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_viewpoint"
        }
      ],
      "recovery": "Stop, observe a fresh frame; if blue A is visible track its pixel and inspect geometry; otherwise re-evaluate with another short evidenced translation or abort with reason",
      "plan_id": "plan-0009",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_for_A",
          "description": "Turn left 0.6 rad away from the already-seen green B toward unexplored sector, sweeping for blue ball A; endpoint heading pose.yaw_rad >= 0.93 (from 0.345)",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 0.93
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000218"
          ]
        },
        {
          "subgoal_id": "advance_viewpoint",
          "description": "After the left turn, translate ~0.3 m forward-left from the new heading (yaw~0.94) to a fresh viewpoint that reveals cabinet-occluded areas; endpoint pose.y_m >= 0.65",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.y_m",
              "op": "ge",
              "value": 0.65
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000225"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_viewpoint"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_viewpoint"
        }
      ],
      "recovery": "Stop and observe a fresh frame; if blue A is visible track its pixel and inspect get_geometry; if geometry is insufficient abort with a reason; otherwise pick one evidenced short translation and inspect again.",
      "plan_id": "plan-0010",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_left",
          "description": "Commit to one short forward-left leg from current yaw 0.89 rad along the bearing of tracked floor point-015 (1.13 m ahead, 0.22 m left, clear floor); endpoint pose.y_m >= 0.90",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.y_m",
              "op": "ge",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000263"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_left"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_left"
        }
      ],
      "recovery": "Stop and observe a fresh frame; re-read get_geometry for point-015 and any fresh visual candidates; if blue A becomes visible track its pixel, else abort with reason if no motion is supported",
      "plan_id": "plan-0011",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_F",
          "description": "Commit to one short forward-left leg along the bearing of tracked floor point-016 (1.09 m ahead, 0.26 m left) from current yaw 0.90 rad; endpoint when point-016 range closes from 1.12 m to <= 0.78 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-016.range_m",
              "op": "le",
              "value": 0.78
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000277"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_F"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_F"
        }
      ],
      "recovery": "Stop and observe a fresh frame; re-read get_geometry for point-016 and any fresh visual candidates; if the floor reference is lost, re-select a floor point and change viewing direction; abort with reason if no safe motion is supported",
      "plan_id": "plan-0012",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_floor",
          "description": "Commit to one forward-left leg along the bearing of the fresh tracked floor point-017 (1.167 m ahead, 0.229 rad left of camera forward) from current yaw 0.92 rad; endpoint when point-017 range closes from 1.167 m to <= 0.90 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-017.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000289"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_floor"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_floor"
        }
      ],
      "recovery": "Stop and observe a fresh frame; re-read get_geometry for point-017 and any fresh visual candidates; if the floor reference is lost, re-select another floor point or change viewing direction with a short turn; abort with reason if no safe motion is supported",
      "plan_id": "plan-0013",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_new_ref",
          "description": "Review due: switch reference from lost point-017 to fresh tracked floor point-018 (1.136 m ahead, bearing 0.009 rad) and commit to a short forward leg from current yaw 0.92 rad; endpoint when point-018 range closes to <= 0.80 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-018.range_m",
              "op": "le",
              "value": 0.8
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000301"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_new_ref"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_new_ref"
        }
      ],
      "recovery": "Stop and observe a fresh frame; re-read get_geometry for point-018 and any fresh visual candidates; if the floor reference is lost, re-select another floor point or change viewing direction with a short turn; abort with reason if no safe motion is supported",
      "plan_id": "plan-0014",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_ref019",
          "description": "Commit to forward motion along current heading (yaw ~0.93 rad) referenced by the fresh tracked floor point-019 (1.27 m ahead, bearing 0.17 rad); endpoint when point-019 range closes to <=0.85 m, then re-scan new view for blue A / green B",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-019.range_m",
              "op": "le",
              "value": 0.85
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000323"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_ref019"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_ref019"
        }
      ],
      "recovery": "Stop and observe a fresh frame; re-read get_geometry for point-019 and visual_candidates; if the floor reference is lost, reselect another point or switch scan direction with a short turn; abort if no safe motion is supported",
      "plan_id": "plan-0015",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_ref020",
          "description": "Commit to forward motion along current heading (yaw ~0.94 rad) referenced by fresh tracked floor point-020 at 1.07 m, bearing -0.06 rad; endpoint when point-020 range closes to <=0.70 m, then re-scan the new view for blue A / green B before any further leg",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-020.range_m",
              "op": "le",
              "value": 0.7
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000345"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_ref020"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_ref020"
        }
      ],
      "recovery": "Stop and observe a fresh frame; re-read get_geometry for point-020 and visual_candidates; if the reference is lost or geometry unknown, reselect another tracked point or switch scan direction with a short turn; abort if no safe motion is supported",
      "plan_id": "plan-0016",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_ref021",
          "description": "Commit to forward motion along current heading (yaw ~0.95 rad) referenced by fresh tracked floor point-021 at 1.10 m, bearing -0.03 rad (essentially straight ahead); endpoint when point-021 range closes to <=0.70 m, then observe the new view and scan for blue A / green B before any further leg",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-021.range_m",
              "op": "le",
              "value": 0.7
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000362"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_ref021"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_ref021"
        }
      ],
      "recovery": "Stop and observe a fresh frame; re-read get_geometry for point-021 and visual_candidates; if the reference is lost or geometry unknown, reselect another tracked point and change scan direction with a short turn; abort if no safe motion is supported",
      "plan_id": "plan-0017",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_branch",
          "description": "Change search branch due to review: rotate in place ~0.6 rad left from heading yaw~0.95 to ~1.55 because the forward leg lost its tracked reference and produced no blue-A or green-B evidence; then take a fresh frame to look for targets",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 1.45
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000371"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_left_branch"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "scan_left_branch"
        }
      ],
      "recovery": "Stop and observe a fresh frame; if still no target visible, track a fresh floor feature at mid-image and commit to a short forward translation (not another scan-only turn); abort only if geometry is unusable",
      "plan_id": "plan-0018",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "translate_forward",
          "description": "Commit forward along current heading toward the fresh tracked floor feature point-022 (bearing -0.10 rad, range 1.17 m); advance ~0.35 m and stop when its range drops to <=0.90 m so the new view can be searched for blue A / green B",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-022.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000385"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "translate_forward"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-track a clear floor feature before another short move; abort if geometry is unusable",
      "plan_id": "plan-0019",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward",
          "description": "Commit to a sustained forward leg along current heading (yaw 1.50 rad) using fresh tracked floor feature point-023 (bearing 0.036 rad, range 1.11 m) as observed reference; advance ~0.4 m to reach a new viewpoint and search for blue A / green B, with local endpoint when point-023 range drops to 0.75 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-023.range_m",
              "op": "le",
              "value": 0.75
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000406"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward"
        }
      ],
      "recovery": "stop, observe a fresh frame, inspect geometry; if point-023 is lost or floor geometry is unusable, re-track a clear floor feature for another short move or abort with a reason",
      "plan_id": "plan-0020",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward",
          "description": "Commit to a sustained forward leg along current heading (yaw 1.50 rad) using the fresh tracked floor feature point-024 (bearing -0.04 rad, range 1.11 m) as observed reference; advance ~0.35 m to a new viewpoint to search for blue A / green B behind obstacle blockages",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-024.range_m",
              "op": "le",
              "value": 0.8
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000423"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward"
        }
      ],
      "recovery": "stop, observe a fresh frame and inspect geometry; if point-024 is lost or floor geometry is unusable, re-track a clear floor feature for another short leg or abort with a reason",
      "plan_id": "plan-0021",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "search_new_sector",
          "description": "Strategy review (70 decisions, no A/B novelty, active leg endpoint point-024 went stale): abandon the previous forward leg along yaw~1.50 and rotate left 0.6 rad to face a new search sector; reference is current tracked floor feature point-025 (bearing -0.058 rad, range 1.08 m); local endpoint is that reference sweeping to bearing >= 0.45 rad, after which a new forward leg will be committed",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-025.bearing_rad",
              "op": "ge",
              "value": 0.45
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000440"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "search_new_sector"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "search_new_sector"
        }
      ],
      "recovery": "stop, observe a fresh frame and re-read point-025 geometry; if the point is lost or the view is unusable, re-track a clear floor/edge feature in the new view, then choose another sector or abort with a reason instead of repeating scan-only turns",
      "plan_id": "plan-0022",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_open_floor",
          "description": "Sustained translation branch: advance 0.35 m straight ahead (yaw ~2.08 body-frame forward) over the floor region evidenced by tracked point-026 at 1.22 m, bearing -0.18 rad, to leave the initial/sector-scan loop; endpoint is point-026 closing to <=0.90 m. Then stop and inspect the new view for A/B candidates.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-026.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000453"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "advance_open_floor"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_open_floor"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-read point-026 geometry and any new target_candidate; if the tracked point is lost or the view is unusable, re-track a clear floor/edge feature before choosing another short translation, or abort with a reason instead of repeating scan-only turns",
      "plan_id": "plan-0023",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_open_floor",
          "description": "Commit to a straight-ahead translation over the floor region evidenced by tracked floor feature point-027 at 1.19 m range, bearing -0.08 rad; advance 0.35 m toward it to exit the scan loop and open new viewpoints, endpoint is point-027 closing to <=0.90 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-027.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000473"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_open_floor"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_open_floor"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-read point-027 geometry and any new target_candidate; if the tracked point is lost or the view is unusable, re-track a clear floor feature before choosing another short translation, or abort with a reason",
      "plan_id": "plan-0024",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_open_floor",
          "description": "Continue committed straight-ahead exploration leg over floor evidenced by tracked floor feature point-027 (currently 1.07 m, bearing -0.03 rad, straight ahead); advance 0.35 m toward it to open new viewpoints for spotting blue A or green B, endpoint is point-027 closing to <=0.80 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-027.range_m",
              "op": "le",
              "value": 0.8
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000486"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_open_floor"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_open_floor"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-read point-027 geometry and any new target_candidate; if the point is lost or the view is unusable, re-track a clear floor feature before choosing another short move, else abort with a reason",
      "plan_id": "plan-0025",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_floor",
          "description": "Commit to a short straight-ahead leg over floor evidenced by tracked floor feature point-028 (range 1.40 m, bearing -0.10 rad, nearly straight ahead); advance 0.35 m to open a new viewpoint for spotting blue A or green B; endpoint is point-028 range <= 1.05 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-028.range_m",
              "op": "le",
              "value": 1.05
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000499"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_floor"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_floor"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-read point-028 geometry and any new target_candidate; if the point is lost or the view is unusable, re-track a clear floor feature before choosing another short move, else abort with a reason",
      "plan_id": "plan-0026",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_floor2",
          "description": "Advance 0.4 m straight ahead over floor evidenced by tracked feature point-029 (range 1.296 m, bearing 0.079 rad, nearly centered); commit to this forward leg to open a new viewpoint for spotting blue A then green B; endpoint point-029 range <= 0.95 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-029.range_m",
              "op": "le",
              "value": 0.95
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000525"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_floor2"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_floor2"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-read point-029 geometry and any new target_candidate; if the point is lost or the view is unusable, re-track a clear floor feature before choosing another short move, else abort with a reason",
      "plan_id": "plan-0027",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_floor3",
          "description": "Advance 0.3 m straight ahead over floor evidenced by freshly tracked feature point-030 (range 1.335 m, bearing 0.378 rad left); sustained forward leg toward the open area to reveal blue A then green B; endpoint point-030 range <= 1.05 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-030.range_m",
              "op": "le",
              "value": 1.05
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000538"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_floor3"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_floor3"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-track a clear floor feature; if geometry unusable and no new candidate appears, switch search branch or abort with a reason",
      "plan_id": "plan-0028",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_leg4",
          "description": "Sustained forward leg along the open floor evidenced by freshly tracked floor feature point-031 (range 1.262 m, bearing 0.489 rad left); commit straight ahead 0.3 m to reveal blue A (then green B) beyond the cabinet-side area; endpoint point-031 range <= 1.05 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-031.range_m",
              "op": "le",
              "value": 1.05
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000561"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_leg4"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_leg4"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-track a clear floor feature or new color candidate; if geometry unusable and no candidate appears, change search branch direction or abort with a reason",
      "plan_id": "plan-0029",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_new_arc",
          "description": "Rotate left 0.5 rad from current yaw 2.19 rad to sweep a new sector for blue A / green B; commit to this direction, endpoint pose.yaw_rad >= 2.60",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 2.6
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000565"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_new_arc"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "scan_new_arc"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-track a visible floor feature or color candidate; if nothing appears, translate to a new viewpoint instead of scanning again",
      "plan_id": "plan-0030",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_translate",
          "description": "Translate forward 0.25 m toward the tracked floor feature point-032 (range 1.15 m, bearing 0.15 rad ahead) to change viewpoint and reveal sectors hidden by cabinets; endpoint is point-032 range <= 0.95 m, well inside the observed free ray",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-032.range_m",
              "op": "le",
              "value": 0.95
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000579"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_translate"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_translate"
        }
      ],
      "recovery": "stop, observe a fresh frame, re-track a visible floor feature; if still no target appears, choose a new sustained direction with fresh geometry or abort",
      "plan_id": "plan-0031",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_translate",
          "description": "Commit forward 0.25 m along the visible floor ray to tracked point-033 (range 1.13 m, bearing 0.21 rad left), changing viewpoint to reveal cabinet-occluded sectors; endpoint is point-033 range at most 0.90 m.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-033.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000597"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_translate"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_translate"
        }
      ],
      "recovery": "Stop, observe a fresh frame, re-track a visible floor feature, and either continue with fresh geometry or choose a new safe direction; abort if motion remains unsupported.",
      "plan_id": "plan-0032",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward",
          "description": "Commit forward 0.3 m along the visible floor ray toward tracked point-034 (range 1.27 m, bearing 0.28 rad left) to change viewpoint and reveal cabinet-occluded sectors; local endpoint point-034 range at most 0.98 m.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-034.range_m",
              "op": "le",
              "value": 0.98
            }
          ],
          "active": true,
          "status": "进行中",
          "evidence_ids": [
            "e000610"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward"
        }
      ],
      "recovery": "Stop, observe a fresh frame, re-track a visible floor feature, then either continue with fresh geometry or pick a new safe direction; abort if motion remains unsupported.",
      "plan_id": "plan-0033",
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
        "call_id": "call_838238f6083141f489e27000",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000012",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 1,
      "plan_id": "plan-0001"
    },
    {
      "evidence_id": "e000013",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.x_m",
      "value": 0.021733950672051968
    },
    {
      "evidence_id": "e000014",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.y_m",
      "value": 0.002238333631713014
    },
    {
      "evidence_id": "e000015",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.yaw_rad",
      "value": -0.5251498275953836
    },
    {
      "evidence_id": "e000016",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 2,
      "action": {
        "call_id": "call_9b524b3b236f46978499e4ec",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_right",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.021733950672051968,
            0.002238333631713014
          ],
          "yaw_delta_rad": -0.5251498275953836,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000017",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.x_m",
      "value": 0.016467470766759758
    },
    {
      "evidence_id": "e000018",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.y_m",
      "value": -0.029697896850089854
    },
    {
      "evidence_id": "e000019",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.yaw_rad",
      "value": 0.01425524642322581
    },
    {
      "evidence_id": "e000020",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 3,
      "action": {
        "call_id": "call_db437f0395484e3798e69a78",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_left_back",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011454178761525591,
            -0.030273097246213465
          ],
          "yaw_delta_rad": 0.5394050740186094,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000021",
      "kind": "completion_invalidated",
      "source": "memory_verifier",
      "step": 3,
      "plan_id": "plan-0001",
      "subgoal_id": "scan_right"
    },
    {
      "evidence_id": "e000022",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 4,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7393738185676924,
            0.382003556520252
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
            234.0,
            174.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000023",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 4,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7393738185676924,
            0.382003556520252
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
            234.0,
            174.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00003",
          "position_m": [
            -0.38559178412228773,
            -0.024804149855819677,
            1.4060306549072266
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
      "evidence_id": "e000024",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.x_m",
      "value": 0.016467470766759758
    },
    {
      "evidence_id": "e000025",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.y_m",
      "value": -0.029697896850089854
    },
    {
      "evidence_id": "e000026",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.yaw_rad",
      "value": 0.01425524642322581
    },
    {
      "evidence_id": "e000027",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 4,
      "name": "point-002.range_m",
      "value": 1.7714
    },
    {
      "evidence_id": "e000028",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 4,
      "name": "point-002.bearing_rad",
      "value": 0.2203
    },
    {
      "evidence_id": "e000029",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 4,
      "action": {
        "call_id": "call_101ac25c3ff841e1b06ff5f7",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000030",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.x_m",
      "value": 0.029762223854601623
    },
    {
      "evidence_id": "e000031",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.y_m",
      "value": -0.020966937480605186
    },
    {
      "evidence_id": "e000032",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.yaw_rad",
      "value": 0.4512530133002123
    },
    {
      "evidence_id": "e000033",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 5,
      "action": {
        "call_id": "call_a7d1cf43963d414ab879cdfb",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_left_back",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01341786004570229,
            0.008540558703751125
          ],
          "yaw_delta_rad": 0.43699776687698666,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000034",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 6,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7319796312697513,
            0.5556805700080226
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
            366.0,
            274.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000035",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 6,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7319796312697513,
            0.5556805700080226
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
            366.0,
            274.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00004",
          "position_m": [
            0.21822786348900253,
            0.44349533547765035,
            1.4631551504135132
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
      "evidence_id": "e000036",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.x_m",
      "value": 0.029762223854601623
    },
    {
      "evidence_id": "e000037",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.y_m",
      "value": -0.020966937480605186
    },
    {
      "evidence_id": "e000038",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.yaw_rad",
      "value": 0.4512530133002123
    },
    {
      "evidence_id": "e000039",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-003.range_m",
      "value": 1.7972
    },
    {
      "evidence_id": "e000040",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-003.bearing_rad",
      "value": -0.1246
    },
    {
      "evidence_id": "e000041",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 6,
      "action": {
        "call_id": "call_aa1f487b1408402aa7b2d7ae",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000042",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.x_m",
      "value": 0.1919877470340414
    },
    {
      "evidence_id": "e000043",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.y_m",
      "value": 0.07718275158575467
    },
    {
      "evidence_id": "e000044",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.yaw_rad",
      "value": 0.46505038158026224
    },
    {
      "evidence_id": "e000045",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 7,
      "action": {
        "call_id": "call_dd2de1f1d8cc416eb43bfaf8",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "viewpoint_move",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.18878940981003628,
            0.01757955000118737
          ],
          "yaw_delta_rad": 0.013797368280049849,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000046",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 7,
      "plan_id": "plan-0002"
    },
    {
      "evidence_id": "e000047",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.x_m",
      "value": 0.19442977978924192
    },
    {
      "evidence_id": "e000048",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.y_m",
      "value": 0.09255765827241197
    },
    {
      "evidence_id": "e000049",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.yaw_rad",
      "value": -0.08690670533813329
    },
    {
      "evidence_id": "e000050",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 8,
      "action": {
        "call_id": "call_54786015124248129ecb4c6a",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "sweep_right_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.009077837451374459,
            0.012646902656671111
          ],
          "yaw_delta_rad": -0.5519570869183954,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000051",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 9,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.750506672934072,
            0.3817858599069216
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
            210.0,
            186.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000052",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 9,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.750506672934072,
            0.3817858599069216
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
            210.0,
            186.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00006",
          "position_m": [
            -0.4230655640823598,
            0.02511348097292547,
            1.2045551538467407
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
      "evidence_id": "e000053",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.x_m",
      "value": 0.19442977978924192
    },
    {
      "evidence_id": "e000054",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.y_m",
      "value": 0.09255765827241197
    },
    {
      "evidence_id": "e000055",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.yaw_rad",
      "value": -0.08690670533813329
    },
    {
      "evidence_id": "e000056",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-004.range_m",
      "value": 1.5828
    },
    {
      "evidence_id": "e000057",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-004.bearing_rad",
      "value": 0.2707
    },
    {
      "evidence_id": "e000058",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 9,
      "action": {
        "call_id": "call_9b5337f2b5244d5da7704634",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000059",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 10,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7627708138852052,
            0.38095364208019017
          ]
        },
        "pose_covariance": null,
        "confidence": 0.719,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00007",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00007",
          "pixel_uv": [
            148.18,
            190.54
          ]
        }
      }
    },
    {
      "evidence_id": "e000060",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.x_m",
      "value": 0.1976554625536557
    },
    {
      "evidence_id": "e000061",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.y_m",
      "value": 0.09821187469107491
    },
    {
      "evidence_id": "e000062",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.yaw_rad",
      "value": -0.2265715828488311
    },
    {
      "evidence_id": "e000063",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-004.range_m",
      "value": 1.5905
    },
    {
      "evidence_id": "e000064",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-004.bearing_rad",
      "value": 0.4053
    },
    {
      "evidence_id": "e000065",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 10,
      "action": {
        "call_id": "call_eb06913f8f264e4b97ef6eac",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "sweep_right_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00272273800578139,
            0.005912858053224947
          ],
          "yaw_delta_rad": -0.13966487751069767,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000066",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 11,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7344157565713676,
            0.3821539440126117
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
            146.0,
            301.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000067",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 11,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7344157565713676,
            0.3821539440126117
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
            146.0,
            301.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00007",
          "position_m": [
            -0.6205762756188328,
            0.4345822333584333,
            1.1151385307312012
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
      "evidence_id": "e000068",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 11,
      "object_id": "point-001",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000069",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.x_m",
      "value": 0.1976554625536557
    },
    {
      "evidence_id": "e000070",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.y_m",
      "value": 0.09821187469107491
    },
    {
      "evidence_id": "e000071",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.yaw_rad",
      "value": -0.2265715828488311
    },
    {
      "evidence_id": "e000072",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-005.range_m",
      "value": 1.5627
    },
    {
      "evidence_id": "e000073",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-005.bearing_rad",
      "value": 0.4093
    },
    {
      "evidence_id": "e000074",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-004.range_m",
      "value": 1.5905
    },
    {
      "evidence_id": "e000075",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-004.bearing_rad",
      "value": 0.4053
    },
    {
      "evidence_id": "e000076",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 11,
      "action": {
        "call_id": "call_a7db0fb4a31948dfb43a9226",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000077",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 11,
      "plan_id": "plan-0003"
    },
    {
      "evidence_id": "e000078",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.x_m",
      "value": 0.21157361216356943
    },
    {
      "evidence_id": "e000079",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.y_m",
      "value": 0.08314525255865861
    },
    {
      "evidence_id": "e000080",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.yaw_rad",
      "value": 0.27476770843684845
    },
    {
      "evidence_id": "e000081",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 12,
      "action": {
        "call_id": "call_c251462dafd147dab6337e68",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "sweep_left_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.016946970047107306,
            -0.011555007454234108
          ],
          "yaw_delta_rad": 0.5013392912856798,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000082",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 12,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 12,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 1,
      "recent_action_evidence_ids": [
        "e000081"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000083",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 13,
      "observation": {
        "object_id": "point-006",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7335424367951235,
            0.640498243803566
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
            289.0,
            269.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000084",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 13,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7335424367951235,
            0.640498243803566
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
            289.0,
            269.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00008",
          "position_m": [
            -0.12810647926344904,
            0.37591901292061275,
            1.3094966411590576
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
      "evidence_id": "e000085",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.x_m",
      "value": 0.21157361216356943
    },
    {
      "evidence_id": "e000086",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.y_m",
      "value": 0.08314525255865861
    },
    {
      "evidence_id": "e000087",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.yaw_rad",
      "value": 0.27476770843684845
    },
    {
      "evidence_id": "e000088",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-006.range_m",
      "value": 1.6208
    },
    {
      "evidence_id": "e000089",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 13,
      "name": "point-006.bearing_rad",
      "value": 0.0762
    },
    {
      "evidence_id": "e000090",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 13,
      "action": {
        "call_id": "call_baf1e51b8baf44cebf7c8ba7",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000091",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 13,
      "plan_id": "plan-0004"
    },
    {
      "evidence_id": "e000092",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 14,
      "object_id": "point-002",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000093",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.x_m",
      "value": 0.4337747765271018
    },
    {
      "evidence_id": "e000094",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.y_m",
      "value": 0.15941343073663167
    },
    {
      "evidence_id": "e000095",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.yaw_rad",
      "value": 0.28953712421814376
    },
    {
      "evidence_id": "e000096",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 14,
      "action": {
        "call_id": "call_584363a6356a408db0ba0167",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "advance_viewpoint_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23455934862572236,
            0.013118857395879091
          ],
          "yaw_delta_rad": 0.014769415781295425,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000097",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.x_m",
      "value": 0.4337747765271018
    },
    {
      "evidence_id": "e000098",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.y_m",
      "value": 0.15941343073663167
    },
    {
      "evidence_id": "e000099",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.yaw_rad",
      "value": 0.28953712421814376
    },
    {
      "evidence_id": "e000100",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 15,
      "action": {
        "call_id": "call_5c8c0359bf3e46f2aacfc5db",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000101",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 16,
      "observation": {
        "object_id": "point-007",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.4004208923408856,
            1.5633539827284142
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
            266.0,
            221.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000102",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 16,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.4004208923408856,
            1.5633539827284142
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
            266.0,
            221.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00009",
          "position_m": [
            -0.5026004767114702,
            0.3898676595051591,
            2.928884506225586
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
      "evidence_id": "e000103",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 16,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7335424367951235,
          0.640498243803566
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          3.4004208923408856,
          1.5633539827284142
        ]
      },
      "evidence_ids": [
        "e000102"
      ]
    },
    {
      "evidence_id": "e000104",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 16,
      "object_id": "point-003",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000105",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.x_m",
      "value": 0.4337747765271018
    },
    {
      "evidence_id": "e000106",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.y_m",
      "value": 0.15941343073663167
    },
    {
      "evidence_id": "e000107",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.yaw_rad",
      "value": 0.28953712421814376
    },
    {
      "evidence_id": "e000108",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-007.range_m",
      "value": 3.2821
    },
    {
      "evidence_id": "e000109",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-007.bearing_rad",
      "value": 0.1525
    },
    {
      "evidence_id": "e000110",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 16,
      "action": {
        "call_id": "call_3cf2a5b6a85e4ca29d9cf8bb",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000111",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 16,
      "plan_id": "plan-0005"
    },
    {
      "evidence_id": "e000112",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.x_m",
      "value": 0.4376884344108239
    },
    {
      "evidence_id": "e000113",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.y_m",
      "value": 0.1694525857890024
    },
    {
      "evidence_id": "e000114",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.yaw_rad",
      "value": -0.2637308773178636
    },
    {
      "evidence_id": "e000115",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 17,
      "action": {
        "call_id": "call_5c018bff87fe4e69bd63f986",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0005",
        "subgoal_id": "scan_right_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.006617021881377873,
            0.008503903434172318
          ],
          "yaw_delta_rad": -0.5532680015360074,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000116",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 18,
      "observation": {
        "object_id": "point-008",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7337462727997779,
            0.38214475666172554
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
            127.0,
            327.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000117",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 18,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7337462727997779,
            0.38214475666172554
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
            127.0,
            327.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00010",
          "position_m": [
            -0.5446513886958788,
            0.41733028484489415,
            0.8821064829826355
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
      "evidence_id": "e000118",
      "kind": "relocation_candidate_rejected",
      "source": "memory_rules",
      "step": 18,
      "object_id": "task:B",
      "rejected_pose": {
        "frame": "episode_start",
        "position_m": [
          3.4004208923408856,
          1.5633539827284142
        ]
      },
      "supporting_observation": "e000117"
    },
    {
      "evidence_id": "e000119",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.x_m",
      "value": 0.4376884344108239
    },
    {
      "evidence_id": "e000120",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.y_m",
      "value": 0.1694525857890024
    },
    {
      "evidence_id": "e000121",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.yaw_rad",
      "value": -0.2637308773178636
    },
    {
      "evidence_id": "e000122",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-008.range_m",
      "value": 1.3134
    },
    {
      "evidence_id": "e000123",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 18,
      "name": "point-008.bearing_rad",
      "value": 0.4264
    },
    {
      "evidence_id": "e000124",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 18,
      "action": {
        "call_id": "call_b1dddc135fad4f21b3fbfdc9",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000125",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 18,
      "plan_id": "plan-0006"
    },
    {
      "evidence_id": "e000126",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.x_m",
      "value": 0.43589035377335006
    },
    {
      "evidence_id": "e000127",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.y_m",
      "value": 0.1494091550278705
    },
    {
      "evidence_id": "e000128",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.yaw_rad",
      "value": 0.2730380994823521
    },
    {
      "evidence_id": "e000129",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 19,
      "action": {
        "call_id": "call_39ad150529284e8692dba048",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_left_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00348909603568517,
            -0.019819142754138295
          ],
          "yaw_delta_rad": 0.5367689768002157,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000130",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 20,
      "observation": {
        "object_id": "point-009",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.8091086450660088,
            1.2889812071044175
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
            256.0,
            223.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000131",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 20,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.8091086450660088,
            1.2889812071044175
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
            256.0,
            223.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00011",
          "position_m": [
            -0.4656624966975113,
            0.31899714340695656,
            2.2862865924835205
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
      "evidence_id": "e000132",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 20,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7337462727997779,
          0.38214475666172554
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          2.8091086450660088,
          1.2889812071044175
        ]
      },
      "evidence_ids": [
        "e000131"
      ]
    },
    {
      "evidence_id": "e000133",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 20,
      "object_id": "point-004",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000134",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.x_m",
      "value": 0.43589035377335006
    },
    {
      "evidence_id": "e000135",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.y_m",
      "value": 0.1494091550278705
    },
    {
      "evidence_id": "e000136",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.yaw_rad",
      "value": 0.2730380994823521
    },
    {
      "evidence_id": "e000137",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-009.range_m",
      "value": 2.6327
    },
    {
      "evidence_id": "e000138",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-009.bearing_rad",
      "value": 0.1746
    },
    {
      "evidence_id": "e000139",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 20,
      "action": {
        "call_id": "call_17054437ca4141b68dbf14e8",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000140",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 20,
      "plan_id": "plan-0007"
    },
    {
      "evidence_id": "e000141",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 21,
      "object_id": "point-005",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000142",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.x_m",
      "value": 0.6524644283602137
    },
    {
      "evidence_id": "e000143",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.y_m",
      "value": 0.21244412247573696
    },
    {
      "evidence_id": "e000144",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.yaw_rad",
      "value": 0.2705614782455228
    },
    {
      "evidence_id": "e000145",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 21,
      "action": {
        "call_id": "call_758278c15eee4cd9a5e2bf40",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "explore_viewpoint_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.22554922268569189,
            0.002298923702544961
          ],
          "yaw_delta_rad": -0.002476621236829235,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000146",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 22,
      "observation": {
        "object_id": "point-010",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8609319082677085,
            0.8144340891745419
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00012",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00012",
          "pixel_uv": [
            239.0,
            309.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000147",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 22,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8609319082677085,
            0.8144340891745419
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00012",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00012",
          "pixel_uv": [
            239.0,
            309.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00012",
          "position_m": [
            -0.26095030421105764,
            0.41978961981778834,
            1.0106366872787476
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
      "evidence_id": "e000148",
      "kind": "relocation_candidate_rejected",
      "source": "memory_rules",
      "step": 22,
      "object_id": "task:B",
      "rejected_pose": {
        "frame": "episode_start",
        "position_m": [
          2.8091086450660088,
          1.2889812071044175
        ]
      },
      "supporting_observation": "e000147"
    },
    {
      "evidence_id": "e000149",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.x_m",
      "value": 0.6524644283602137
    },
    {
      "evidence_id": "e000150",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.y_m",
      "value": 0.21244412247573696
    },
    {
      "evidence_id": "e000151",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.yaw_rad",
      "value": 0.2705614782455228
    },
    {
      "evidence_id": "e000152",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-010.range_m",
      "value": 1.3501
    },
    {
      "evidence_id": "e000153",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-010.bearing_rad",
      "value": 0.1916
    },
    {
      "evidence_id": "e000154",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 22,
      "action": {
        "call_id": "call_421aeea5f5d1436ba0eb029e",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000155",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 22,
      "plan_id": "plan-0008"
    },
    {
      "evidence_id": "e000156",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 23,
      "object_id": "point-006",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000157",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.x_m",
      "value": 0.6460874792345567
    },
    {
      "evidence_id": "e000158",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.y_m",
      "value": 0.23885631214940753
    },
    {
      "evidence_id": "e000159",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.yaw_rad",
      "value": -0.16973441427468342
    },
    {
      "evidence_id": "e000160",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 23,
      "action": {
        "call_id": "call_acf45328411e4167a63879da",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0008",
        "subgoal_id": "scan_right_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0009142908141151693,
            0.027155723444909286
          ],
          "yaw_delta_rad": -0.44029589252020607,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000161",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 24,
      "observation": {
        "object_id": "point-011",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288659069493864,
            0.3863726043865756
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00013",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00013",
          "pixel_uv": [
            179.0,
            340.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000162",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 24,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288659069493864,
            0.3863726043865756
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00013",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00013",
          "pixel_uv": [
            179.0,
            340.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00013",
          "position_m": [
            -0.3319946496634426,
            0.3792536745265661,
            0.7366952896118164
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
      "evidence_id": "e000163",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.x_m",
      "value": 0.6460874792345567
    },
    {
      "evidence_id": "e000164",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.y_m",
      "value": 0.23885631214940753
    },
    {
      "evidence_id": "e000165",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.yaw_rad",
      "value": -0.16973441427468342
    },
    {
      "evidence_id": "e000166",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-011.range_m",
      "value": 1.0928
    },
    {
      "evidence_id": "e000167",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-011.bearing_rad",
      "value": 0.3051
    },
    {
      "evidence_id": "e000168",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 24,
      "action": {
        "call_id": "call_8badbb60b5284365b9726e5c",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000169",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 24,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 24,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 2,
      "recent_action_evidence_ids": [
        "e000168"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000170",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.x_m",
      "value": 0.6387128257515572
    },
    {
      "evidence_id": "e000171",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.y_m",
      "value": 0.22499390857310747
    },
    {
      "evidence_id": "e000172",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.yaw_rad",
      "value": 0.316917964044659
    },
    {
      "evidence_id": "e000173",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 25,
      "action": {
        "call_id": "call_fff828f7d8c442a8a6fff7bd",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0008",
        "subgoal_id": "scan_right_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.004927031905231152,
            -0.014908926973842516
          ],
          "yaw_delta_rad": 0.4866523783193424,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000174",
      "kind": "completion_invalidated",
      "source": "memory_verifier",
      "step": 25,
      "plan_id": "plan-0008",
      "subgoal_id": "scan_right_for_A"
    },
    {
      "evidence_id": "e000175",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 26,
      "observation": {
        "object_id": "point-012",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0328796285414112,
            0.8984070403122474
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00014",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00014",
          "pixel_uv": [
            266.0,
            267.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000176",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 26,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0328796285414112,
            0.8984070403122474
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00014",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00014",
          "pixel_uv": [
            266.0,
            267.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00014",
          "position_m": [
            -0.21150924878123165,
            0.3459263414646312,
            1.2325618267059326
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
      "evidence_id": "e000177",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 26,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288659069493864,
          0.3863726043865756
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          2.0328796285414112,
          0.8984070403122474
        ]
      },
      "evidence_ids": [
        "e000176"
      ]
    },
    {
      "evidence_id": "e000178",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 26,
      "object_id": "point-007",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000179",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.x_m",
      "value": 0.6387128257515572
    },
    {
      "evidence_id": "e000180",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.y_m",
      "value": 0.22499390857310747
    },
    {
      "evidence_id": "e000181",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.yaw_rad",
      "value": 0.316917964044659
    },
    {
      "evidence_id": "e000182",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-012.range_m",
      "value": 1.5483
    },
    {
      "evidence_id": "e000183",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 26,
      "name": "point-012.bearing_rad",
      "value": 0.133
    },
    {
      "evidence_id": "e000184",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 26,
      "action": {
        "call_id": "call_9a76afabf06f46ee8c4504d5",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000185",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 26,
      "plan_id": "plan-0009"
    },
    {
      "evidence_id": "e000186",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.x_m",
      "value": 0.8454015624367144
    },
    {
      "evidence_id": "e000187",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.y_m",
      "value": 0.3114571944262847
    },
    {
      "evidence_id": "e000188",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.yaw_rad",
      "value": 0.3284847199832414
    },
    {
      "evidence_id": "e000189",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 27,
      "action": {
        "call_id": "call_9b8ce38fed8e450d971c843b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0009",
        "subgoal_id": "advance_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2233410977042753,
            0.017745076761846362
          ],
          "yaw_delta_rad": 0.011566755938582585,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000190",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 28,
      "observation": {
        "object_id": "point-013",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.591430703572166,
            1.2175910688100848
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00015",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00015",
          "pixel_uv": [
            262.0,
            253.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000191",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 28,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.591430703572166,
            1.2175910688100848
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00015",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00015",
          "pixel_uv": [
            262.0,
            253.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00015",
          "position_m": [
            -0.30138181117982776,
            0.3852445760298668,
            1.6341139078140259
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
      "evidence_id": "e000192",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 28,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288659069493864,
          0.3863726043865756
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          2.591430703572166,
          1.2175910688100848
        ]
      },
      "evidence_ids": [
        "e000191"
      ]
    },
    {
      "evidence_id": "e000193",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 28,
      "object_id": "point-008",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000194",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.x_m",
      "value": 0.8454015624367144
    },
    {
      "evidence_id": "e000195",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.y_m",
      "value": 0.3114571944262847
    },
    {
      "evidence_id": "e000196",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.yaw_rad",
      "value": 0.3284847199832414
    },
    {
      "evidence_id": "e000197",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-013.range_m",
      "value": 1.9672
    },
    {
      "evidence_id": "e000198",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-013.bearing_rad",
      "value": 0.1502
    },
    {
      "evidence_id": "e000199",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 28,
      "action": {
        "call_id": "call_a08a2980eb26416587039359",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000200",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.x_m",
      "value": 1.0715213692141219
    },
    {
      "evidence_id": "e000201",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.y_m",
      "value": 0.39905017345555804
    },
    {
      "evidence_id": "e000202",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.yaw_rad",
      "value": 0.34452333268668983
    },
    {
      "evidence_id": "e000203",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 29,
      "action": {
        "call_id": "call_44b8920652a04837a902ebdd",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0009",
        "subgoal_id": "advance_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.24228799016714425,
            0.00996126563447633
          ],
          "yaw_delta_rad": 0.01603861270344842,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000204",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 30,
      "observation": {
        "object_id": "point-014",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8852620242737823,
            0.735033009777705
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00016",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00016",
          "pixel_uv": [
            297.0,
            193.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000205",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 30,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8852620242737823,
            0.735033009777705
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00016",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00016",
          "pixel_uv": [
            297.0,
            193.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00016",
          "position_m": [
            -0.040307654497876245,
            0.02418459269872575,
            0.5585192441940308
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
      "evidence_id": "e000206",
      "kind": "relocation_candidate_rejected",
      "source": "memory_rules",
      "step": 30,
      "object_id": "task:B",
      "rejected_pose": {
        "frame": "episode_start",
        "position_m": [
          2.591430703572166,
          1.2175910688100848
        ]
      },
      "supporting_observation": "e000205"
    },
    {
      "evidence_id": "e000207",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 30,
      "object_id": "point-009",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000208",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.x_m",
      "value": 1.0715213692141219
    },
    {
      "evidence_id": "e000209",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.y_m",
      "value": 0.39905017345555804
    },
    {
      "evidence_id": "e000210",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.yaw_rad",
      "value": 0.34452333268668983
    },
    {
      "evidence_id": "e000211",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-014.range_m",
      "value": 0.8804
    },
    {
      "evidence_id": "e000212",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-014.bearing_rad",
      "value": 0.047
    },
    {
      "evidence_id": "e000213",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 30,
      "action": {
        "call_id": "call_6e2ae475c3cd488f83436c82",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000214",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 30,
      "plan_id": "plan-0010"
    },
    {
      "evidence_id": "e000215",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.x_m",
      "value": 1.07449960901934
    },
    {
      "evidence_id": "e000216",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.y_m",
      "value": 0.39504216992299274
    },
    {
      "evidence_id": "e000217",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.yaw_rad",
      "value": 0.8860068464282879
    },
    {
      "evidence_id": "e000218",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 31,
      "action": {
        "call_id": "call_00ae29cff22546fab8c53e41",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_left_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0014495327549089358,
            -0.004778374142622809
          ],
          "yaw_delta_rad": 0.5414835137415981,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000219",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 32,
      "object_id": "point-010",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000220",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.x_m",
      "value": 1.1189296442977494
    },
    {
      "evidence_id": "e000221",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.y_m",
      "value": 0.6164879802000954
    },
    {
      "evidence_id": "e000222",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.yaw_rad",
      "value": 0.8787685548589893
    },
    {
      "evidence_id": "e000223",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 32,
      "action": {
        "call_id": "call_b791ae4d88c749678b6c405e",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "advance_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.19962378411593867,
            0.10565329970879436
          ],
          "yaw_delta_rad": -0.0072382915692985605,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000224",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.x_m",
      "value": 1.1705887955030383
    },
    {
      "evidence_id": "e000225",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.y_m",
      "value": 0.6908600865482085
    },
    {
      "evidence_id": "e000226",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.yaw_rad",
      "value": 0.8926477772846361
    },
    {
      "evidence_id": "e000227",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 33,
      "action": {
        "call_id": "call_0db4373814224d9c89ccedef",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "advance_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.09022677002474816,
            0.007681671485238316
          ],
          "yaw_delta_rad": 0.013879222425646986,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000228",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 34,
      "object_id": "point-011",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000229",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.x_m",
      "value": 1.1705887955030383
    },
    {
      "evidence_id": "e000230",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.y_m",
      "value": 0.6908600865482085
    },
    {
      "evidence_id": "e000231",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.yaw_rad",
      "value": 0.8926477772846361
    },
    {
      "evidence_id": "e000232",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 34,
      "action": {
        "call_id": "call_6a69551f9b904676ab5c017c",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000233",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.x_m",
      "value": 1.1705887955030383
    },
    {
      "evidence_id": "e000234",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.y_m",
      "value": 0.6908600865482085
    },
    {
      "evidence_id": "e000235",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.yaw_rad",
      "value": 0.8926477772846361
    },
    {
      "evidence_id": "e000236",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 35,
      "action": {
        "call_id": "call_841f9720b6bd4ecf9094dd0c",
        "tool": "track_point",
        "status": "failed",
        "error_code": "PERCEPTION_ERROR"
      }
    },
    {
      "evidence_id": "e000237",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 36,
      "object_id": "point-012",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000238",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.x_m",
      "value": 1.1705887955030383
    },
    {
      "evidence_id": "e000239",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.y_m",
      "value": 0.6908600865482085
    },
    {
      "evidence_id": "e000240",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.yaw_rad",
      "value": 0.8926477772846361
    },
    {
      "evidence_id": "e000241",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 36,
      "action": {
        "call_id": "call_a24501e15ce648409889f93b",
        "tool": "track_point",
        "status": "failed",
        "error_code": "PERCEPTION_ERROR"
      }
    },
    {
      "evidence_id": "e000242",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 36,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 36,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 3,
      "recent_action_evidence_ids": [
        "e000241"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000243",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.x_m",
      "value": 1.1705887955030383
    },
    {
      "evidence_id": "e000244",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.y_m",
      "value": 0.6908600865482085
    },
    {
      "evidence_id": "e000245",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.yaw_rad",
      "value": 0.8926477772846361
    },
    {
      "evidence_id": "e000246",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 37,
      "action": {
        "call_id": "call_be17e98b607c4647aad1cfe1",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000247",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 38,
      "object_id": "point-013",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000248",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.x_m",
      "value": 1.1705887955030383
    },
    {
      "evidence_id": "e000249",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.y_m",
      "value": 0.6908600865482085
    },
    {
      "evidence_id": "e000250",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.yaw_rad",
      "value": 0.8926477772846361
    },
    {
      "evidence_id": "e000251",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 38,
      "action": {
        "call_id": "call_9c92e95753c44b59a16047c8",
        "tool": "track_point",
        "status": "failed",
        "error_code": "PERCEPTION_ERROR"
      }
    },
    {
      "evidence_id": "e000252",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 39,
      "observation": {
        "object_id": "point-015",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7021418598500693,
            1.7074169171205484
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00021",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00021",
          "pixel_uv": [
            231.0,
            343.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000253",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.x_m",
      "value": 1.1705887955030383
    },
    {
      "evidence_id": "e000254",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.y_m",
      "value": 0.6908600865482085
    },
    {
      "evidence_id": "e000255",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.yaw_rad",
      "value": 0.8926477772846361
    },
    {
      "evidence_id": "e000256",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-015.range_m",
      "value": 1.1471
    },
    {
      "evidence_id": "e000257",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-015.bearing_rad",
      "value": 0.1964
    },
    {
      "evidence_id": "e000258",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 39,
      "action": {
        "call_id": "call_74b482c831a84dd99a3607bc",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000259",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 39,
      "plan_id": "plan-0011"
    },
    {
      "evidence_id": "e000260",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "task:B",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000261",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-014",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000262",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.x_m",
      "value": 1.3135780321830293
    },
    {
      "evidence_id": "e000263",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.y_m",
      "value": 0.9447693362676501
    },
    {
      "evidence_id": "e000264",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.yaw_rad",
      "value": 0.9002777747851531
    },
    {
      "evidence_id": "e000265",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 40,
      "action": {
        "call_id": "call_f3cc23c092ea4a6c8cd1385f",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0011",
        "subgoal_id": "explore_forward_left",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.28743279081879736,
            0.04793975032823879
          ],
          "yaw_delta_rad": 0.007629997500516961,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000266",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 41,
      "observation": {
        "object_id": "point-016",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7900307378316307,
            1.9560474331728126
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00022",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00022",
          "pixel_uv": [
            214.0,
            350.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000267",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.x_m",
      "value": 1.3135780321830293
    },
    {
      "evidence_id": "e000268",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.y_m",
      "value": 0.9447693362676501
    },
    {
      "evidence_id": "e000269",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.yaw_rad",
      "value": 0.9002777747851531
    },
    {
      "evidence_id": "e000270",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-016.range_m",
      "value": 1.1179
    },
    {
      "evidence_id": "e000271",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-016.bearing_rad",
      "value": 0.2303
    },
    {
      "evidence_id": "e000272",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 41,
      "action": {
        "call_id": "call_deba2e9e67e54cd0825bcad1",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000273",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 41,
      "plan_id": "plan-0012"
    },
    {
      "evidence_id": "e000274",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.x_m",
      "value": 1.4839162872684566
    },
    {
      "evidence_id": "e000275",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.y_m",
      "value": 1.3060382156561046
    },
    {
      "evidence_id": "e000276",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.yaw_rad",
      "value": 0.9180572861125892
    },
    {
      "evidence_id": "e000277",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 42,
      "action": {
        "call_id": "call_9360c17bf2ce4bdb8837e177",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0012",
        "subgoal_id": "explore_forward_F",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3889008929541335,
            0.09102977435770848
          ],
          "yaw_delta_rad": 0.017779511327435937,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000278",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 43,
      "observation": {
        "object_id": "point-017",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.964122003468572,
            2.3696275537602127
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00023",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00023",
          "pixel_uv": [
            217.0,
            342.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000279",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.x_m",
      "value": 1.4839162872684566
    },
    {
      "evidence_id": "e000280",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.y_m",
      "value": 1.3060382156561046
    },
    {
      "evidence_id": "e000281",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.yaw_rad",
      "value": 0.9180572861125892
    },
    {
      "evidence_id": "e000282",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-017.range_m",
      "value": 1.167
    },
    {
      "evidence_id": "e000283",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-017.bearing_rad",
      "value": 0.2286
    },
    {
      "evidence_id": "e000284",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 43,
      "action": {
        "call_id": "call_0f88aafea19b407584165457",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000285",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 43,
      "plan_id": "plan-0013"
    },
    {
      "evidence_id": "e000286",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.x_m",
      "value": 1.623149794605124
    },
    {
      "evidence_id": "e000287",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.y_m",
      "value": 1.6199015593923678
    },
    {
      "evidence_id": "e000288",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.yaw_rad",
      "value": 0.9224017333662929
    },
    {
      "evidence_id": "e000289",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 44,
      "action": {
        "call_id": "call_bfa56ca6cacf45608b43c43e",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "explore_forward_floor",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3339058258190139,
            0.08001917014503339
          ],
          "yaw_delta_rad": 0.004344447253703976,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000290",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 45,
      "observation": {
        "object_id": "point-018",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.3017593415189768,
            2.531611723225905
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00024",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00024",
          "pixel_uv": [
            313.0,
            344.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000291",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.x_m",
      "value": 1.623149794605124
    },
    {
      "evidence_id": "e000292",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.y_m",
      "value": 1.6199015593923678
    },
    {
      "evidence_id": "e000293",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.yaw_rad",
      "value": 0.9224017333662929
    },
    {
      "evidence_id": "e000294",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 45,
      "name": "point-018.range_m",
      "value": 1.1365
    },
    {
      "evidence_id": "e000295",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 45,
      "name": "point-018.bearing_rad",
      "value": 0.0085
    },
    {
      "evidence_id": "e000296",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 45,
      "action": {
        "call_id": "call_f98894a188a14d7f98da9f07",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000297",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 45,
      "plan_id": "plan-0014"
    },
    {
      "evidence_id": "e000298",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.x_m",
      "value": 1.818930484383606
    },
    {
      "evidence_id": "e000299",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.y_m",
      "value": 1.8915866199489695
    },
    {
      "evidence_id": "e000300",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.yaw_rad",
      "value": 0.932559801637812
    },
    {
      "evidence_id": "e000301",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 46,
      "action": {
        "call_id": "call_98e599b0bdd14d05a293c51b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0014",
        "subgoal_id": "explore_forward_new_ref",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3347812014916447,
            0.00802482072033811
          ],
          "yaw_delta_rad": 0.010158068271519216,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000302",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.x_m",
      "value": 1.818930484383606
    },
    {
      "evidence_id": "e000303",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.y_m",
      "value": 1.8915866199489695
    },
    {
      "evidence_id": "e000304",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.yaw_rad",
      "value": 0.932559801637812
    },
    {
      "evidence_id": "e000305",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 47,
      "action": {
        "call_id": "call_a2bf72220d8747df9705dd5b",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000306",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.x_m",
      "value": 1.818930484383606
    },
    {
      "evidence_id": "e000307",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.y_m",
      "value": 1.8915866199489695
    },
    {
      "evidence_id": "e000308",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.yaw_rad",
      "value": 0.932559801637812
    },
    {
      "evidence_id": "e000309",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 48,
      "action": {
        "call_id": "call_4f2f719b77694c1487eaa2f8",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000310",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 48,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 48,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 4,
      "recent_action_evidence_ids": [
        "e000309"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000311",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 49,
      "observation": {
        "object_id": "point-019",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.393442221970812,
            3.0267669022717953
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00026",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00026",
          "pixel_uv": [
            246.0,
            320.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000312",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 49,
      "object_id": "point-015",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000313",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.x_m",
      "value": 1.818930484383606
    },
    {
      "evidence_id": "e000314",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.y_m",
      "value": 1.8915866199489695
    },
    {
      "evidence_id": "e000315",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.yaw_rad",
      "value": 0.932559801637812
    },
    {
      "evidence_id": "e000316",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 49,
      "name": "point-019.range_m",
      "value": 1.2723
    },
    {
      "evidence_id": "e000317",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 49,
      "name": "point-019.bearing_rad",
      "value": 0.1697
    },
    {
      "evidence_id": "e000318",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 49,
      "action": {
        "call_id": "call_c2e0944cc9ed4af3ba2d62c7",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000319",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 49,
      "plan_id": "plan-0015"
    },
    {
      "evidence_id": "e000320",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.x_m",
      "value": 2.037913824330921
    },
    {
      "evidence_id": "e000321",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.y_m",
      "value": 2.2052402303430134
    },
    {
      "evidence_id": "e000322",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.yaw_rad",
      "value": 0.939611800179775
    },
    {
      "evidence_id": "e000323",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 50,
      "action": {
        "call_id": "call_fa7578cb4bcf43c6b5d803fe",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0015",
        "subgoal_id": "explore_forward_ref019",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3823760624303026,
            0.010992605150611068
          ],
          "yaw_delta_rad": 0.00705199854196259,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000324",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 51,
      "object_id": "point-016",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000325",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.x_m",
      "value": 2.037913824330921
    },
    {
      "evidence_id": "e000326",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.y_m",
      "value": 2.2052402303430134
    },
    {
      "evidence_id": "e000327",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.yaw_rad",
      "value": 0.939611800179775
    },
    {
      "evidence_id": "e000328",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 51,
      "action": {
        "call_id": "call_d529253ab3d64ab482a4b032",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000329",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.x_m",
      "value": 2.037913824330921
    },
    {
      "evidence_id": "e000330",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.y_m",
      "value": 2.2052402303430134
    },
    {
      "evidence_id": "e000331",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.yaw_rad",
      "value": 0.939611800179775
    },
    {
      "evidence_id": "e000332",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 52,
      "action": {
        "call_id": "call_1593682acbe44fc683ca9640",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000333",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 53,
      "observation": {
        "object_id": "point-020",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.7219852294274296,
            3.0318281341556013
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00028",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00028",
          "pixel_uv": [
            343.0,
            357.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000334",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 53,
      "object_id": "point-017",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000335",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.x_m",
      "value": 2.037913824330921
    },
    {
      "evidence_id": "e000336",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.y_m",
      "value": 2.2052402303430134
    },
    {
      "evidence_id": "e000337",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.yaw_rad",
      "value": 0.939611800179775
    },
    {
      "evidence_id": "e000338",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 53,
      "name": "point-020.range_m",
      "value": 1.0729
    },
    {
      "evidence_id": "e000339",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 53,
      "name": "point-020.bearing_rad",
      "value": -0.0601
    },
    {
      "evidence_id": "e000340",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 53,
      "action": {
        "call_id": "call_afc1c40106114d2aa0bedb6d",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000341",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 53,
      "plan_id": "plan-0016"
    },
    {
      "evidence_id": "e000342",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.x_m",
      "value": 2.2235368756375133
    },
    {
      "evidence_id": "e000343",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.y_m",
      "value": 2.485477525404748
    },
    {
      "evidence_id": "e000344",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.yaw_rad",
      "value": 0.9466374369081593
    },
    {
      "evidence_id": "e000345",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 54,
      "action": {
        "call_id": "call_f048bbbb23ba40419c1c1181",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0016",
        "subgoal_id": "explore_forward_ref020",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.33578015498841157,
            0.015509553051130054
          ],
          "yaw_delta_rad": 0.007025636728384299,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000346",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 55,
      "object_id": "point-018",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000347",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.x_m",
      "value": 2.2235368756375133
    },
    {
      "evidence_id": "e000348",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.y_m",
      "value": 2.485477525404748
    },
    {
      "evidence_id": "e000349",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.yaw_rad",
      "value": 0.9466374369081593
    },
    {
      "evidence_id": "e000350",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 55,
      "action": {
        "call_id": "call_a71b8d748d004a82be4a7db3",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000351",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 56,
      "observation": {
        "object_id": "point-021",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.893684700315791,
            3.362242866347792
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00030",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00030",
          "pixel_uv": [
            329.0,
            348.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000352",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.x_m",
      "value": 2.2235368756375133
    },
    {
      "evidence_id": "e000353",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.y_m",
      "value": 2.485477525404748
    },
    {
      "evidence_id": "e000354",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.yaw_rad",
      "value": 0.9466374369081593
    },
    {
      "evidence_id": "e000355",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 56,
      "name": "point-021.range_m",
      "value": 1.1036
    },
    {
      "evidence_id": "e000356",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 56,
      "name": "point-021.bearing_rad",
      "value": -0.0285
    },
    {
      "evidence_id": "e000357",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 56,
      "action": {
        "call_id": "call_22762f9a3d2e46229cc9937c",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000358",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 56,
      "plan_id": "plan-0017"
    },
    {
      "evidence_id": "e000359",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.x_m",
      "value": 2.4378547802993906
    },
    {
      "evidence_id": "e000360",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.y_m",
      "value": 2.802308139258474
    },
    {
      "evidence_id": "e000361",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.yaw_rad",
      "value": 0.952268653616667
    },
    {
      "evidence_id": "e000362",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 57,
      "action": {
        "call_id": "call_91e14afb6b8a4ee99a4c8b30",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0017",
        "subgoal_id": "explore_forward_ref021",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3823443632888358,
            0.011251221926587729
          ],
          "yaw_delta_rad": 0.005631216708507747,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000363",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.x_m",
      "value": 2.4378547802993906
    },
    {
      "evidence_id": "e000364",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.y_m",
      "value": 2.802308139258474
    },
    {
      "evidence_id": "e000365",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.yaw_rad",
      "value": 0.952268653616667
    },
    {
      "evidence_id": "e000366",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 58,
      "action": {
        "call_id": "call_eba76f47e2a74232a71ade2a",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000367",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 58,
      "plan_id": "plan-0018"
    },
    {
      "evidence_id": "e000368",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 59,
      "object_id": "point-019",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000369",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.x_m",
      "value": 2.4504290440575818
    },
    {
      "evidence_id": "e000370",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.y_m",
      "value": 2.805293102300006
    },
    {
      "evidence_id": "e000371",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.yaw_rad",
      "value": 1.4931612191975148
    },
    {
      "evidence_id": "e000372",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 59,
      "action": {
        "call_id": "call_f44339e922994a9b9eec3a30",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0018",
        "subgoal_id": "scan_left_branch",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00972296180612471,
            -0.008513878501394732
          ],
          "yaw_delta_rad": 0.5408925655808479,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000373",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 60,
      "observation": {
        "object_id": "point-022",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.6548728100217973,
            3.953194612255616
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00032",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00032",
          "pixel_uv": [
            362.0,
            334.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000374",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.x_m",
      "value": 2.4504290440575818
    },
    {
      "evidence_id": "e000375",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.y_m",
      "value": 2.805293102300006
    },
    {
      "evidence_id": "e000376",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.yaw_rad",
      "value": 1.4931612191975148
    },
    {
      "evidence_id": "e000377",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 60,
      "name": "point-022.range_m",
      "value": 1.166
    },
    {
      "evidence_id": "e000378",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 60,
      "name": "point-022.bearing_rad",
      "value": -0.0986
    },
    {
      "evidence_id": "e000379",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 60,
      "action": {
        "call_id": "call_7044f4ab19f347ac8cb7cc7e",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000380",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 60,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 60,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 5,
      "recent_action_evidence_ids": [
        "e000379"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000381",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 60,
      "plan_id": "plan-0019"
    },
    {
      "evidence_id": "e000382",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.x_m",
      "value": 2.4594385658863387
    },
    {
      "evidence_id": "e000383",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.y_m",
      "value": 3.0903296096009747
    },
    {
      "evidence_id": "e000384",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.yaw_rad",
      "value": 1.5010789812323269
    },
    {
      "evidence_id": "e000385",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 61,
      "action": {
        "call_id": "call_f14addea92c84cbc99c82f03",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0019",
        "subgoal_id": "translate_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.28487670400299203,
            0.01312423309415225
          ],
          "yaw_delta_rad": 0.007917762034812093,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000386",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.x_m",
      "value": 2.4594385658863387
    },
    {
      "evidence_id": "e000387",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.y_m",
      "value": 3.0903296096009747
    },
    {
      "evidence_id": "e000388",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.yaw_rad",
      "value": 1.5010789812323269
    },
    {
      "evidence_id": "e000389",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 62,
      "action": {
        "call_id": "call_6f682e0ac5ae4740aeba48b5",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000390",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 63,
      "object_id": "point-020",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000391",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.x_m",
      "value": 2.4594385658863387
    },
    {
      "evidence_id": "e000392",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.y_m",
      "value": 3.0903296096009747
    },
    {
      "evidence_id": "e000393",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.yaw_rad",
      "value": 1.5010789812323269
    },
    {
      "evidence_id": "e000394",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 63,
      "action": {
        "call_id": "call_b406cd1c805544c5ba851995",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000395",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 64,
      "observation": {
        "object_id": "point-023",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.4970705305555323,
            4.202008702340932
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00033",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00033",
          "pixel_uv": [
            301.0,
            344.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000396",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.x_m",
      "value": 2.4594385658863387
    },
    {
      "evidence_id": "e000397",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.y_m",
      "value": 3.0903296096009747
    },
    {
      "evidence_id": "e000398",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.yaw_rad",
      "value": 1.5010789812323269
    },
    {
      "evidence_id": "e000399",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 64,
      "name": "point-023.range_m",
      "value": 1.1123
    },
    {
      "evidence_id": "e000400",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 64,
      "name": "point-023.bearing_rad",
      "value": 0.0359
    },
    {
      "evidence_id": "e000401",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 64,
      "action": {
        "call_id": "call_6974e7bcebc04ffcb9135c67",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000402",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 64,
      "plan_id": "plan-0020"
    },
    {
      "evidence_id": "e000403",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.x_m",
      "value": 2.4694766219957245
    },
    {
      "evidence_id": "e000404",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.y_m",
      "value": 3.428041954415999
    },
    {
      "evidence_id": "e000405",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.yaw_rad",
      "value": 1.5084872496818698
    },
    {
      "evidence_id": "e000406",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 65,
      "action": {
        "call_id": "call_5b424cb580d240548f5228bb",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0020",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.33759121021294486,
            0.013511668952295292
          ],
          "yaw_delta_rad": 0.0074082684495428985,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000407",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 66,
      "object_id": "point-021",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000408",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.x_m",
      "value": 2.4694766219957245
    },
    {
      "evidence_id": "e000409",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.y_m",
      "value": 3.428041954415999
    },
    {
      "evidence_id": "e000410",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.yaw_rad",
      "value": 1.5084872496818698
    },
    {
      "evidence_id": "e000411",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 66,
      "action": {
        "call_id": "call_40bf83cee0514bffa49c23ba",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000412",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 67,
      "observation": {
        "object_id": "point-024",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.5873445442816903,
            4.5271353457599695
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00035",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00035",
          "pixel_uv": [
            336.0,
            347.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000413",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.x_m",
      "value": 2.4694766219957245
    },
    {
      "evidence_id": "e000414",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.y_m",
      "value": 3.428041954415999
    },
    {
      "evidence_id": "e000415",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.yaw_rad",
      "value": 1.5084872496818698
    },
    {
      "evidence_id": "e000416",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 67,
      "name": "point-024.range_m",
      "value": 1.1054
    },
    {
      "evidence_id": "e000417",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 67,
      "name": "point-024.bearing_rad",
      "value": -0.0445
    },
    {
      "evidence_id": "e000418",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 67,
      "action": {
        "call_id": "call_0d74356988cf45f49e1a076a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000419",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 67,
      "plan_id": "plan-0021"
    },
    {
      "evidence_id": "e000420",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.x_m",
      "value": 2.4810001593864035
    },
    {
      "evidence_id": "e000421",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.y_m",
      "value": 3.7158290369944025
    },
    {
      "evidence_id": "e000422",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.yaw_rad",
      "value": 1.5305864116686816
    },
    {
      "evidence_id": "e000423",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 68,
      "action": {
        "call_id": "call_ade1a3df42ca48b9bb12f313",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0021",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2879461644402076,
            0.006418971658785842
          ],
          "yaw_delta_rad": 0.022099161986811833,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000424",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.x_m",
      "value": 2.4810001593864035
    },
    {
      "evidence_id": "e000425",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.y_m",
      "value": 3.7158290369944025
    },
    {
      "evidence_id": "e000426",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.yaw_rad",
      "value": 1.5305864116686816
    },
    {
      "evidence_id": "e000427",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 69,
      "action": {
        "call_id": "call_6004039ba6414f4a8b45ae9d",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000428",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 70,
      "observation": {
        "object_id": "point-025",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.5866073728757826,
            4.786048793146852
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00036",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00036",
          "pixel_uv": [
            344.0,
            357.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000429",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 70,
      "object_id": "point-022",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000430",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.x_m",
      "value": 2.4810001593864035
    },
    {
      "evidence_id": "e000431",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.y_m",
      "value": 3.7158290369944025
    },
    {
      "evidence_id": "e000432",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.yaw_rad",
      "value": 1.5305864116686816
    },
    {
      "evidence_id": "e000433",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 70,
      "name": "point-025.range_m",
      "value": 1.0755
    },
    {
      "evidence_id": "e000434",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 70,
      "name": "point-025.bearing_rad",
      "value": -0.0581
    },
    {
      "evidence_id": "e000435",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 70,
      "action": {
        "call_id": "call_3356805776ad40efa993c6f3",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000436",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 70,
      "plan_id": "plan-0022"
    },
    {
      "evidence_id": "e000437",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.x_m",
      "value": 2.490385933615639
    },
    {
      "evidence_id": "e000438",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.y_m",
      "value": 3.727042302144985
    },
    {
      "evidence_id": "e000439",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.yaw_rad",
      "value": 2.0796663475118726
    },
    {
      "evidence_id": "e000440",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 71,
      "action": {
        "call_id": "call_42231a34b7624889a7ace0cd",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0022",
        "subgoal_id": "search_new_sector",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011581500853360465,
            -0.008927424668012456
          ],
          "yaw_delta_rad": 0.5490799358431908,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000441",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 72,
      "observation": {
        "object_id": "point-026",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.0933546780199532,
            4.877363071356823
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00037",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00037",
          "pixel_uv": [
            394.0,
            328.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000442",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.x_m",
      "value": 2.490385933615639
    },
    {
      "evidence_id": "e000443",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.y_m",
      "value": 3.727042302144985
    },
    {
      "evidence_id": "e000444",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.yaw_rad",
      "value": 2.0796663475118726
    },
    {
      "evidence_id": "e000445",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 72,
      "name": "point-026.range_m",
      "value": 1.2169
    },
    {
      "evidence_id": "e000446",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 72,
      "name": "point-026.bearing_rad",
      "value": -0.1766
    },
    {
      "evidence_id": "e000447",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 72,
      "action": {
        "call_id": "call_efe8035b86ae472f8222369d",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000448",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 72,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 72,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 6,
      "recent_action_evidence_ids": [
        "e000447"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000449",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 72,
      "plan_id": "plan-0023"
    },
    {
      "evidence_id": "e000450",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.x_m",
      "value": 2.34398295802056
    },
    {
      "evidence_id": "e000451",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.y_m",
      "value": 3.9708177740055195
    },
    {
      "evidence_id": "e000452",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.yaw_rad",
      "value": 2.0805922990329098
    },
    {
      "evidence_id": "e000453",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 73,
      "action": {
        "call_id": "call_b83d0adeccd34b14969f6435",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0023",
        "subgoal_id": "advance_open_floor",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2842142180217156,
            0.00908791605507031
          ],
          "yaw_delta_rad": 0.0009259515210371383,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000454",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 74,
      "object_id": "point-023",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000455",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.x_m",
      "value": 2.34398295802056
    },
    {
      "evidence_id": "e000456",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.y_m",
      "value": 3.9708177740055195
    },
    {
      "evidence_id": "e000457",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.yaw_rad",
      "value": 2.0805922990329098
    },
    {
      "evidence_id": "e000458",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 74,
      "action": {
        "call_id": "call_1da28f69e1364a19bbde491d",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000459",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 75,
      "observation": {
        "object_id": "point-027",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.846940331505338,
            5.0491817327072415
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00038",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00038",
          "pixel_uv": [
            350.0,
            334.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000460",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.x_m",
      "value": 2.34398295802056
    },
    {
      "evidence_id": "e000461",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.y_m",
      "value": 3.9708177740055195
    },
    {
      "evidence_id": "e000462",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.yaw_rad",
      "value": 2.0805922990329098
    },
    {
      "evidence_id": "e000463",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 75,
      "name": "point-027.range_m",
      "value": 1.1874
    },
    {
      "evidence_id": "e000464",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 75,
      "name": "point-027.bearing_rad",
      "value": -0.0779
    },
    {
      "evidence_id": "e000465",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 75,
      "action": {
        "call_id": "call_9a9e7ecdb3464ca69589fdcd",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000466",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 75,
      "plan_id": "plan-0024"
    },
    {
      "evidence_id": "e000467",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 76,
      "observation": {
        "object_id": "point-027",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.6832093423709305,
            5.221487565585877
          ]
        },
        "pose_covariance": null,
        "confidence": 0.836,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00039",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00039",
          "pixel_uv": [
            344.0,
            346.05
          ]
        }
      }
    },
    {
      "evidence_id": "e000468",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.x_m",
      "value": 2.192476282797208
    },
    {
      "evidence_id": "e000469",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.y_m",
      "value": 4.210634656707014
    },
    {
      "evidence_id": "e000470",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.yaw_rad",
      "value": 2.0967948392497324
    },
    {
      "evidence_id": "e000471",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 76,
      "name": "point-027.range_m",
      "value": 1.1319
    },
    {
      "evidence_id": "e000472",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 76,
      "name": "point-027.bearing_rad",
      "value": -0.0593
    },
    {
      "evidence_id": "e000473",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 76,
      "action": {
        "call_id": "call_b565ada24291466fbba49d38",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0024",
        "subgoal_id": "advance_open_floor",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2832578811884896,
            0.01521126590735701
          ],
          "yaw_delta_rad": 0.01620254021682266,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000474",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 77,
      "observation": {
        "object_id": "point-027",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.5211947919903206,
            5.389915109109923
          ]
        },
        "pose_covariance": null,
        "confidence": 0.748,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00040",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00040",
          "pixel_uv": [
            328.93,
            354.75
          ]
        }
      }
    },
    {
      "evidence_id": "e000475",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 77,
      "object_id": "point-024",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000476",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.x_m",
      "value": 2.0358810576371273
    },
    {
      "evidence_id": "e000477",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.y_m",
      "value": 4.452275104654831
    },
    {
      "evidence_id": "e000478",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.yaw_rad",
      "value": 2.1005780926836857
    },
    {
      "evidence_id": "e000479",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 77,
      "name": "point-027.range_m",
      "value": 1.0696
    },
    {
      "evidence_id": "e000480",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 77,
      "name": "point-027.bearing_rad",
      "value": -0.0278
    },
    {
      "evidence_id": "e000481",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 77,
      "action": {
        "call_id": "call_3c4784ec16114d768713ddb1",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0024",
        "subgoal_id": "advance_open_floor",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.28759905567984645,
            0.014105098348412129
          ],
          "yaw_delta_rad": 0.0037832534339532486,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000482",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 77,
      "plan_id": "plan-0025"
    },
    {
      "evidence_id": "e000483",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.x_m",
      "value": 1.8819714620568757
    },
    {
      "evidence_id": "e000484",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.y_m",
      "value": 4.703095379984374
    },
    {
      "evidence_id": "e000485",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.yaw_rad",
      "value": 2.120182012973807
    },
    {
      "evidence_id": "e000486",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 78,
      "action": {
        "call_id": "call_c53af1f0cb7349038c1c11bd",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0025",
        "subgoal_id": "advance_open_floor",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.29421462348194316,
            0.006060483268114397
          ],
          "yaw_delta_rad": 0.01960392029012148,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000487",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 79,
      "observation": {
        "object_id": "point-028",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.2753451247079461,
            5.961051220558526
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00041",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00041",
          "pixel_uv": [
            359.0,
            304.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000488",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.x_m",
      "value": 1.8819714620568757
    },
    {
      "evidence_id": "e000489",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.y_m",
      "value": 4.703095379984374
    },
    {
      "evidence_id": "e000490",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.yaw_rad",
      "value": 2.120182012973807
    },
    {
      "evidence_id": "e000491",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 79,
      "name": "point-028.range_m",
      "value": 1.3966
    },
    {
      "evidence_id": "e000492",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 79,
      "name": "point-028.bearing_rad",
      "value": -0.1001
    },
    {
      "evidence_id": "e000493",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 79,
      "action": {
        "call_id": "call_fc4194834307445390f424a6",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000494",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 79,
      "plan_id": "plan-0026"
    },
    {
      "evidence_id": "e000495",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 80,
      "object_id": "point-025",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000496",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.x_m",
      "value": 1.7261845597009833
    },
    {
      "evidence_id": "e000497",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.y_m",
      "value": 4.935410521702038
    },
    {
      "evidence_id": "e000498",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.yaw_rad",
      "value": 2.1416427474937314
    },
    {
      "evidence_id": "e000499",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 80,
      "action": {
        "call_id": "call_68ccb6c9c1af4bc9b9448cf3",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0026",
        "subgoal_id": "advance_floor",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.27947513337429375,
            0.011555684417783527
          ],
          "yaw_delta_rad": 0.02146073451992425,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000500",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.x_m",
      "value": 1.7261845597009833
    },
    {
      "evidence_id": "e000501",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.y_m",
      "value": 4.935410521702038
    },
    {
      "evidence_id": "e000502",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.yaw_rad",
      "value": 2.1416427474937314
    },
    {
      "evidence_id": "e000503",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 81,
      "action": {
        "call_id": "call_cdcfe42f7be24594af5c6ae1",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000504",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 82,
      "object_id": "point-026",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000505",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.x_m",
      "value": 1.7261845597009833
    },
    {
      "evidence_id": "e000506",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.y_m",
      "value": 4.935410521702038
    },
    {
      "evidence_id": "e000507",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.yaw_rad",
      "value": 2.1416427474937314
    },
    {
      "evidence_id": "e000508",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 82,
      "action": {
        "call_id": "call_d6034f2c64d14ad18d83782e",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000509",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.x_m",
      "value": 1.7261845597009833
    },
    {
      "evidence_id": "e000510",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.y_m",
      "value": 4.935410521702038
    },
    {
      "evidence_id": "e000511",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.yaw_rad",
      "value": 2.1416427474937314
    },
    {
      "evidence_id": "e000512",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 83,
      "action": {
        "call_id": "call_1664b172a16d47c1b2e037b1",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000513",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 84,
      "observation": {
        "object_id": "point-029",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.9424846738286271,
            5.96760303227536
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00042",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00042",
          "pixel_uv": [
            287.0,
            320.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000514",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.x_m",
      "value": 1.7261845597009833
    },
    {
      "evidence_id": "e000515",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.y_m",
      "value": 4.935410521702038
    },
    {
      "evidence_id": "e000516",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.yaw_rad",
      "value": 2.1416427474937314
    },
    {
      "evidence_id": "e000517",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 84,
      "name": "point-029.range_m",
      "value": 1.296
    },
    {
      "evidence_id": "e000518",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 84,
      "name": "point-029.bearing_rad",
      "value": 0.0786
    },
    {
      "evidence_id": "e000519",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 84,
      "action": {
        "call_id": "call_8e748b92704347adacbfcb9f",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000520",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 84,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 84,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 7,
      "recent_action_evidence_ids": [
        "e000519"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000521",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 84,
      "plan_id": "plan-0027"
    },
    {
      "evidence_id": "e000522",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.x_m",
      "value": 1.5339712240182732
    },
    {
      "evidence_id": "e000523",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.y_m",
      "value": 5.209613175004189
    },
    {
      "evidence_id": "e000524",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.yaw_rad",
      "value": 2.1482275459666766
    },
    {
      "evidence_id": "e000525",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 85,
      "action": {
        "call_id": "call_96eb76e3670c4cbaa7883187",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0027",
        "subgoal_id": "advance_floor2",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.33458756553633656,
            0.01357285823549731
          ],
          "yaw_delta_rad": 0.006584798472945241,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000526",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 86,
      "observation": {
        "object_id": "point-030",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.44421999308692367,
            5.980061528032222
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00043",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00043",
          "pixel_uv": [
            151.0,
            320.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000527",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.x_m",
      "value": 1.5339712240182732
    },
    {
      "evidence_id": "e000528",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.y_m",
      "value": 5.209613175004189
    },
    {
      "evidence_id": "e000529",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.yaw_rad",
      "value": 2.1482275459666766
    },
    {
      "evidence_id": "e000530",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 86,
      "name": "point-030.range_m",
      "value": 1.3346
    },
    {
      "evidence_id": "e000531",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 86,
      "name": "point-030.bearing_rad",
      "value": 0.3779
    },
    {
      "evidence_id": "e000532",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 86,
      "action": {
        "call_id": "call_7c73f48b1a0c4896b905ee0a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000533",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 86,
      "plan_id": "plan-0028"
    },
    {
      "evidence_id": "e000534",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 87,
      "object_id": "point-027",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000535",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.x_m",
      "value": 1.3941295424804654
    },
    {
      "evidence_id": "e000536",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.y_m",
      "value": 5.400121294376024
    },
    {
      "evidence_id": "e000537",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.yaw_rad",
      "value": 2.17075112769498
    },
    {
      "evidence_id": "e000538",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 87,
      "action": {
        "call_id": "call_9b6129c152a649cf90bf4198",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0028",
        "subgoal_id": "advance_floor3",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2359564487716313,
            0.013175497144169837
          ],
          "yaw_delta_rad": 0.022523581728303377,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000539",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.x_m",
      "value": 1.3941295424804654
    },
    {
      "evidence_id": "e000540",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.y_m",
      "value": 5.400121294376024
    },
    {
      "evidence_id": "e000541",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.yaw_rad",
      "value": 2.17075112769498
    },
    {
      "evidence_id": "e000542",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 88,
      "action": {
        "call_id": "call_6c9593526c264b1e98251cce",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000543",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 89,
      "observation": {
        "object_id": "point-031",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.27552046513072087,
            5.9852318754380605
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00045",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00045",
          "pixel_uv": [
            86.0,
            344.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000544",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 89,
      "object_id": "point-028",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000545",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.x_m",
      "value": 1.3941295424804654
    },
    {
      "evidence_id": "e000546",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.y_m",
      "value": 5.400121294376024
    },
    {
      "evidence_id": "e000547",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.yaw_rad",
      "value": 2.17075112769498
    },
    {
      "evidence_id": "e000548",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 89,
      "name": "point-031.range_m",
      "value": 1.2624
    },
    {
      "evidence_id": "e000549",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 89,
      "name": "point-031.bearing_rad",
      "value": 0.4889
    },
    {
      "evidence_id": "e000550",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 89,
      "action": {
        "call_id": "call_b0bd109ea78a4e5288209799",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000551",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.x_m",
      "value": 1.3941295424804654
    },
    {
      "evidence_id": "e000552",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.y_m",
      "value": 5.400121294376024
    },
    {
      "evidence_id": "e000553",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.yaw_rad",
      "value": 2.17075112769498
    },
    {
      "evidence_id": "e000554",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 90,
      "name": "point-031.range_m",
      "value": 1.2624
    },
    {
      "evidence_id": "e000555",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 90,
      "name": "point-031.bearing_rad",
      "value": 0.4889
    },
    {
      "evidence_id": "e000556",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 90,
      "action": {
        "call_id": "call_d4190a6d773e4cc185cbe6cf",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000557",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 90,
      "plan_id": "plan-0029"
    },
    {
      "evidence_id": "e000558",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.x_m",
      "value": 1.2538122715272635
    },
    {
      "evidence_id": "e000559",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.y_m",
      "value": 5.590815409689876
    },
    {
      "evidence_id": "e000560",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.yaw_rad",
      "value": 2.1893345724686477
    },
    {
      "evidence_id": "e000561",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 91,
      "action": {
        "call_id": "call_7ea8ba3072604a6787204f91",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0029",
        "subgoal_id": "advance_leg4",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2366153679239394,
            0.008145538981891062
          ],
          "yaw_delta_rad": 0.01858344477366769,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000562",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 91,
      "plan_id": "plan-0030"
    },
    {
      "evidence_id": "e000563",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.x_m",
      "value": 1.2702920627316596
    },
    {
      "evidence_id": "e000564",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.y_m",
      "value": 5.5877388059684705
    },
    {
      "evidence_id": "e000565",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.yaw_rad",
      "value": 2.6342096091891505
    },
    {
      "evidence_id": "e000566",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 92,
      "action": {
        "call_id": "call_eed8f1ccce7b41ccabed7632",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0030",
        "subgoal_id": "scan_new_arc",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.012062313922783568,
            -0.011642576666154359
          ],
          "yaw_delta_rad": 0.44487503672050277,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000567",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 93,
      "observation": {
        "object_id": "point-032",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.19116123428988596,
            5.986632457342582
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00047",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00047",
          "pixel_uv": [
            251.0,
            334.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000568",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.x_m",
      "value": 1.2702920627316596
    },
    {
      "evidence_id": "e000569",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.y_m",
      "value": 5.5877388059684705
    },
    {
      "evidence_id": "e000570",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.yaw_rad",
      "value": 2.6342096091891505
    },
    {
      "evidence_id": "e000571",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 93,
      "name": "point-032.range_m",
      "value": 1.1505
    },
    {
      "evidence_id": "e000572",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 93,
      "name": "point-032.bearing_rad",
      "value": 0.1533
    },
    {
      "evidence_id": "e000573",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 93,
      "action": {
        "call_id": "call_4e842aa8a12840ca9feeb875",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000574",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 93,
      "plan_id": "plan-0031"
    },
    {
      "evidence_id": "e000575",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 94,
      "object_id": "point-029",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000576",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.x_m",
      "value": 1.1096019308976475
    },
    {
      "evidence_id": "e000577",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.y_m",
      "value": 5.677458365164662
    },
    {
      "evidence_id": "e000578",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.yaw_rad",
      "value": 2.6532941494042026
    },
    {
      "evidence_id": "e000579",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 94,
      "action": {
        "call_id": "call_99bf0844f15c4a0090b0e376",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0031",
        "subgoal_id": "explore_translate",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.18404022145462529,
            -0.00033861205469024047
          ],
          "yaw_delta_rad": 0.019084540215052126,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000580",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.x_m",
      "value": 1.1096019308976475
    },
    {
      "evidence_id": "e000581",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.y_m",
      "value": 5.677458365164662
    },
    {
      "evidence_id": "e000582",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.yaw_rad",
      "value": 2.6532941494042026
    },
    {
      "evidence_id": "e000583",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 95,
      "action": {
        "call_id": "call_f427e087d3ed49288ab6e97c",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000584",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 96,
      "observation": {
        "object_id": "point-033",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.024575548622372434,
            5.990335401341222
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00049",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00049",
          "pixel_uv": [
            226.0,
            347.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000585",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 96,
      "object_id": "point-030",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000586",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.x_m",
      "value": 1.1096019308976475
    },
    {
      "evidence_id": "e000587",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.y_m",
      "value": 5.677458365164662
    },
    {
      "evidence_id": "e000588",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.yaw_rad",
      "value": 2.6532941494042026
    },
    {
      "evidence_id": "e000589",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 96,
      "name": "point-033.range_m",
      "value": 1.1292
    },
    {
      "evidence_id": "e000590",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 96,
      "name": "point-033.bearing_rad",
      "value": 0.2075
    },
    {
      "evidence_id": "e000591",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 96,
      "action": {
        "call_id": "call_b38bf35a1c1343f3b25c031f",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000592",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 96,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 96,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 8,
      "recent_action_evidence_ids": [
        "e000591"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000593",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 96,
      "plan_id": "plan-0032"
    },
    {
      "evidence_id": "e000594",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.x_m",
      "value": 0.9402823533583216
    },
    {
      "evidence_id": "e000595",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.y_m",
      "value": 5.760101223902989
    },
    {
      "evidence_id": "e000596",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.yaw_rad",
      "value": 2.6754601349965212
    },
    {
      "evidence_id": "e000597",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 97,
      "action": {
        "call_id": "call_14219cbc946a4e9f80a93b15",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0032",
        "subgoal_id": "explore_translate",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.1883013382566532,
            0.006447282318335842
          ],
          "yaw_delta_rad": 0.022165985592318638,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000598",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 98,
      "observation": {
        "object_id": "point-034",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.30605287547588134,
            5.997360022194634
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00050",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00050",
          "pixel_uv": [
            198.0,
            322.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000599",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.x_m",
      "value": 0.9402823533583216
    },
    {
      "evidence_id": "e000600",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.y_m",
      "value": 5.760101223902989
    },
    {
      "evidence_id": "e000601",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.yaw_rad",
      "value": 2.6754601349965212
    },
    {
      "evidence_id": "e000602",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 98,
      "name": "point-034.range_m",
      "value": 1.2687
    },
    {
      "evidence_id": "e000603",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 98,
      "name": "point-034.bearing_rad",
      "value": 0.278
    },
    {
      "evidence_id": "e000604",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 98,
      "action": {
        "call_id": "call_35915fc4cf4b44e782cbb07b",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000605",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 98,
      "plan_id": "plan-0033"
    },
    {
      "evidence_id": "e000606",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 99,
      "object_id": "point-031",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000607",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.x_m",
      "value": 0.79901707634295
    },
    {
      "evidence_id": "e000608",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.y_m",
      "value": 6.180561223539937
    },
    {
      "evidence_id": "e000609",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.yaw_rad",
      "value": -1.9717433992014755
    },
    {
      "evidence_id": "e000610",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 99,
      "action": {
        "call_id": "call_4144348b73af42db94ac540d",
        "tool": "move_relative",
        "status": "failed",
        "error_code": "ROBOT_FELL",
        "plan_id": "plan-0033",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3151634777194149,
            -0.31211291561986876
          ],
          "yaw_delta_rad": 1.63598177298159,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    }
  ]
}
```

## 操作经验

## 程序工具
