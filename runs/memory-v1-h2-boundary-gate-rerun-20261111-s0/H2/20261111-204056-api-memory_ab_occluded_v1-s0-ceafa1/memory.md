# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 120,
    "revision": 160,
    "active_plan_id": "plan-0039",
    "public_context": {
      "image_id": "frame-00062",
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
        "image_id": "frame-00062",
        "image_size": {
          "width": 640,
          "height": 360
        },
        "tracked_points": [
          {
            "point_id": "point-028",
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "geometry_jump",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-029",
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
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
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
            "valid": false,
            "pixel_uv": null,
            "relative_xy_m": null,
            "range_m": null,
            "bearing_rad": null,
            "confidence": 0.0,
            "loss_reason": "geometry_jump",
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-031",
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
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
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
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
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
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
            "point_id": "point-034",
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
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
            "point_id": "point-035",
            "image_id": "frame-00062",
            "timestamp_s": 125.85999999988807,
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
      "visual_candidates": [
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            336.0,
            353.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            408.0,
            350.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            373.0,
            344.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            444.0,
            357.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            351.0,
            325.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            302.0,
            348.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            291.0,
            327.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            328.0,
            319.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            277.0,
            341.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            410.0,
            334.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            476.0,
            343.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            314.0,
            333.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            442.0,
            338.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            380.0,
            329.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            361.0,
            312.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00062",
          "pixel_uv": [
            344.0,
            299.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        }
      ]
    },
    "exploration": {
      "successful_turns_without_search_progress": 1,
      "turn_limit": 6,
      "stalled": false,
      "progress_basis": "successful_translation_tool_or_first_task_observation_not_motion_gt",
      "evidence_ids": [
        "e000736"
      ],
      "recovery": "change_viewpoint_with_translation; inspect_geometry_or_abort_if_motion_unsupported",
      "decisions_since_task_novelty": 120,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "review_due": true,
      "review_count": 10,
      "last_review_step": 120,
      "review_evidence_id": "e000737",
      "review_semantics": "advisory_strategy_review_not_failure_or_motion_prohibition"
    }
  },
  "pose": {
    "frame": "episode_start",
    "position_m": [
      -3.1232582120948016,
      5.335256083791076
    ],
    "yaw_rad": -2.7871645064789115,
    "source": "simulated_proprioception",
    "provenance": "existing_public_idealized_simulator_odometry"
  },
  "objects": [
    {
      "visual_feature": {
        "image_id": "frame-00001",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-001",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "state": "stale",
      "last_seen": 1,
      "evidence_ids": [
        "e000004"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00012",
        "pixel_uv": [
          259.0,
          289.0
        ]
      },
      "category": "task_target",
      "confidence": 0.95,
      "source": "task_label_rgbd_tracking",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "task:B",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.2846073305590298,
          0.9118565825235814
        ]
      },
      "state": "stale",
      "last_seen": 22,
      "evidence_ids": [
        "e000005",
        "e000030",
        "e000042",
        "e000050",
        "e000058",
        "e000072",
        "e000098",
        "e000113",
        "e000128",
        "e000146"
      ],
      "candidate_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7353943796406988,
          0.7414044498890575
        ]
      },
      "task_label": "B",
      "label_description": "绿方块",
      "camera_pose": {
        "frame": "current_camera_optical",
        "image_id": "frame-00012",
        "position_m": [
          -0.21553650499005222,
          0.3901032610976978,
          1.1107046604156494
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
      "visual_feature": {
        "image_id": "frame-00003",
        "pixel_uv": [
          234.0,
          174.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-002",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7393738185676924,
          0.382003556520252
        ]
      },
      "state": "stale",
      "last_seen": 5,
      "evidence_ids": [
        "e000029"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00007",
        "pixel_uv": [
          471.95,
          189.64
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 0.998,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-003",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8591060019182373,
          0.534754314018822
        ]
      },
      "state": "stale",
      "last_seen": 11,
      "evidence_ids": [
        "e000041",
        "e000049",
        "e000057",
        "e000071"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00010",
        "pixel_uv": [
          562.0,
          277.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-004",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.489378930374773,
          0.24233612096510126
        ]
      },
      "state": "stale",
      "last_seen": 15,
      "evidence_ids": [
        "e000097"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00011",
        "pixel_uv": [
          493.0,
          198.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-005",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.879679245289256,
          0.6707707656217894
        ]
      },
      "state": "stale",
      "last_seen": 17,
      "evidence_ids": [
        "e000112"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00012",
        "pixel_uv": [
          259.0,
          289.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-006",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.2846073305590298,
          0.9118565825235814
        ]
      },
      "state": "stale",
      "last_seen": 19,
      "evidence_ids": [
        "e000127"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00014",
        "pixel_uv": [
          561.0,
          222.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-007",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7353943796406988,
          0.7414044498890575
        ]
      },
      "state": "stale",
      "last_seen": 22,
      "evidence_ids": [
        "e000145"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00016",
        "pixel_uv": [
          265.48,
          333.16
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 0.994,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-008",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.5334245961567703,
          1.8912895989407292
        ]
      },
      "state": "stale",
      "last_seen": 25,
      "evidence_ids": [
        "e000159",
        "e000167"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00018",
        "pixel_uv": [
          279.0,
          348.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-009",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.6195457040555363,
          2.054083182694093
        ]
      },
      "state": "stale",
      "last_seen": 29,
      "evidence_ids": [
        "e000184",
        "e000192"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00021",
        "pixel_uv": [
          275.0,
          340.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-010",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.5468313270989786,
          2.3787941282424954
        ]
      },
      "state": "stale",
      "last_seen": 34,
      "evidence_ids": [
        "e000222"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00022",
        "pixel_uv": [
          317.0,
          329.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-011",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7980792642809966,
          2.7178460870326777
        ]
      },
      "state": "stale",
      "last_seen": 36,
      "evidence_ids": [
        "e000235"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00023",
        "pixel_uv": [
          329.0,
          350.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-012",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8907049218691772,
          2.872567351780127
        ]
      },
      "state": "stale",
      "last_seen": 39,
      "evidence_ids": [
        "e000255"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00026",
        "pixel_uv": [
          294.61,
          351.03
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 0.994,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-013",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8998921326265916,
          3.2884268788203914
        ]
      },
      "state": "stale",
      "last_seen": 43,
      "evidence_ids": [
        "e000272",
        "e000280"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00029",
        "pixel_uv": [
          337.0,
          352.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-014",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.4896702362016716,
          3.722849345693233
        ]
      },
      "state": "stale",
      "last_seen": 49,
      "evidence_ids": [
        "e000312"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00032",
        "pixel_uv": [
          347.0,
          330.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-015",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.4075503718674622,
          4.127200481321564
        ]
      },
      "state": "stale",
      "last_seen": 53,
      "evidence_ids": [
        "e000330",
        "e000337"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00034",
        "pixel_uv": [
          325.0,
          356.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-016",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.816808425439323,
          3.726122944011987
        ]
      },
      "state": "stale",
      "last_seen": 57,
      "evidence_ids": [
        "e000359"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00035",
        "pixel_uv": [
          292.0,
          338.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-017",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.5767000658940684,
          3.820921225698166
        ]
      },
      "state": "stale",
      "last_seen": 59,
      "evidence_ids": [
        "e000371"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00036",
        "pixel_uv": [
          353.0,
          354.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-018",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.5767937515581019,
          3.9879103528947057
        ]
      },
      "state": "stale",
      "last_seen": 62,
      "evidence_ids": [
        "e000390"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00037",
        "pixel_uv": [
          226.0,
          342.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-019",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.07074629371457455,
          3.9911457094593774
        ]
      },
      "state": "stale",
      "last_seen": 64,
      "evidence_ids": [
        "e000403"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00041",
        "pixel_uv": [
          365.22,
          358.47
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 0.957,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-020",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.39229286487421955,
          4.726486778640571
        ]
      },
      "state": "stale",
      "last_seen": 69,
      "evidence_ids": [
        "e000415",
        "e000423",
        "e000431",
        "e000438"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00043",
        "pixel_uv": [
          296.0,
          329.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-021",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.7496732058632827,
          4.754992286629952
        ]
      },
      "state": "stale",
      "last_seen": 72,
      "evidence_ids": [
        "e000454"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00044",
        "pixel_uv": [
          308.0,
          323.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-022",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.9971585496445659,
          4.92639037988372
        ]
      },
      "state": "stale",
      "last_seen": 78,
      "evidence_ids": [
        "e000485"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00045",
        "pixel_uv": [
          282.0,
          337.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-023",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.162499357054927,
          4.930407586497242
        ]
      },
      "state": "stale",
      "last_seen": 80,
      "evidence_ids": [
        "e000498"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00046",
        "pixel_uv": [
          271.0,
          334.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-024",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.4006530436238418,
          5.024249511006157
        ]
      },
      "state": "stale",
      "last_seen": 82,
      "evidence_ids": [
        "e000510"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00047",
        "pixel_uv": [
          283.0,
          334.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-025",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.6600272791097146,
          5.189330537411828
        ]
      },
      "state": "stale",
      "last_seen": 87,
      "evidence_ids": [
        "e000536"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00049",
        "pixel_uv": [
          291.0,
          338.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-026",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.9053067197668578,
          5.359794911673753
        ]
      },
      "state": "stale",
      "last_seen": 92,
      "evidence_ids": [
        "e000562"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00050",
        "pixel_uv": [
          349.0,
          352.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-027",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.066289648867524,
          5.612945872842138
        ]
      },
      "state": "stale",
      "last_seen": 94,
      "evidence_ids": [
        "e000575"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00051",
        "pixel_uv": [
          368.0,
          310.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-028",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.5597188685698162,
          6.031478813534362
        ]
      },
      "state": "stale",
      "last_seen": 97,
      "evidence_ids": [
        "e000594"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00053",
        "pixel_uv": [
          503.56,
          337.07
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 0.344,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-029",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.8969703052549733,
          6.037607986794931
        ]
      },
      "state": "stale",
      "last_seen": 101,
      "evidence_ids": [
        "e000611",
        "e000619"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00055",
        "pixel_uv": [
          317.0,
          350.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-030",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -3.1503568569768223,
          5.5510287119806865
        ]
      },
      "state": "stale",
      "last_seen": 104,
      "evidence_ids": [
        "e000636"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00056",
        "pixel_uv": [
          353.0,
          351.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-031",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -3.3898595350664107,
          5.643223523803514
        ]
      },
      "state": "stale",
      "last_seen": 106,
      "evidence_ids": [
        "e000649"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00057",
        "pixel_uv": [
          482.0,
          324.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-032",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -3.7221938748146157,
          6.052613955205048
        ]
      },
      "state": "stale",
      "last_seen": 110,
      "evidence_ids": [
        "e000671"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00058",
        "pixel_uv": [
          369.0,
          260.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-033",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -4.728712237334042,
          6.0693363128197
        ]
      },
      "state": "unknown",
      "last_seen": 113,
      "evidence_ids": [
        "e000688"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00059",
        "pixel_uv": [
          343.0,
          324.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-034",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -3.8955193095079497,
          5.484098879076614
        ]
      },
      "state": "unknown",
      "last_seen": 116,
      "evidence_ids": [
        "e000707"
      ],
      "candidate_pose": null
    },
    {
      "visual_feature": {
        "image_id": "frame-00061",
        "pixel_uv": [
          340.0,
          350.0
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "pose_covariance": null,
      "object_id": "point-035",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -4.228937271063658,
          5.490336028557303
        ]
      },
      "state": "unknown",
      "last_seen": 119,
      "evidence_ids": [
        "e000724"
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
      "step": 1,
      "evidence_ids": [
        "e000012"
      ],
      "plan_id": "plan-0001"
    },
    {
      "event_id": "event-2",
      "kind": "skill_stuck",
      "step": 2,
      "evidence_ids": [
        "e000018"
      ]
    },
    {
      "event_id": "event-3",
      "kind": "key_precondition_invalidated",
      "step": 2,
      "evidence_ids": [
        "e000018"
      ]
    },
    {
      "event_id": "event-4",
      "kind": "replan_required",
      "step": 2,
      "evidence_ids": [
        "e000018"
      ]
    },
    {
      "event_id": "event-5",
      "kind": "replan_required",
      "step": 4,
      "evidence_ids": [
        "e000028"
      ],
      "plan_id": "plan-0002"
    },
    {
      "event_id": "event-6",
      "kind": "target_state_changed",
      "step": 7,
      "evidence_ids": [
        "e000042"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-7",
      "kind": "target_state_changed",
      "step": 8,
      "evidence_ids": [
        "e000049"
      ],
      "object_id": "point-003",
      "state": "confirmed"
    },
    {
      "event_id": "event-8",
      "kind": "target_state_changed",
      "step": 11,
      "evidence_ids": [
        "e000073"
      ],
      "object_id": "point-001",
      "state": "stale"
    },
    {
      "event_id": "event-9",
      "kind": "replan_required",
      "step": 11,
      "evidence_ids": [
        "e000073"
      ],
      "object_id": "point-001",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-10",
      "kind": "search_review_due",
      "step": 12,
      "evidence_ids": [
        "e000085"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-11",
      "kind": "target_state_changed",
      "step": 14,
      "evidence_ids": [
        "e000091"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-12",
      "kind": "target_state_changed",
      "step": 14,
      "evidence_ids": [
        "e000092"
      ],
      "object_id": "point-003",
      "state": "predicted"
    },
    {
      "event_id": "event-13",
      "kind": "target_state_changed",
      "step": 15,
      "evidence_ids": [
        "e000098",
        "e000099"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-14",
      "kind": "replan_required",
      "step": 15,
      "evidence_ids": [
        "e000098"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-15",
      "kind": "target_state_changed",
      "step": 15,
      "evidence_ids": [
        "e000100"
      ],
      "object_id": "point-002",
      "state": "stale"
    },
    {
      "event_id": "event-16",
      "kind": "replan_required",
      "step": 15,
      "evidence_ids": [
        "e000100"
      ],
      "object_id": "point-002",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-17",
      "kind": "target_state_changed",
      "step": 17,
      "evidence_ids": [
        "e000113"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-18",
      "kind": "target_state_changed",
      "step": 17,
      "evidence_ids": [
        "e000115"
      ],
      "object_id": "point-003",
      "state": "unknown"
    },
    {
      "event_id": "event-19",
      "kind": "target_state_changed",
      "step": 19,
      "evidence_ids": [
        "e000128"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-20",
      "kind": "target_state_changed",
      "step": 21,
      "evidence_ids": [
        "e000140"
      ],
      "object_id": "point-003",
      "state": "stale"
    },
    {
      "event_id": "event-21",
      "kind": "replan_required",
      "step": 21,
      "evidence_ids": [
        "e000140"
      ],
      "object_id": "point-003",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-22",
      "kind": "target_state_changed",
      "step": 22,
      "evidence_ids": [
        "e000146",
        "e000147"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-23",
      "kind": "replan_required",
      "step": 22,
      "evidence_ids": [
        "e000146"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-24",
      "kind": "search_review_due",
      "step": 24,
      "evidence_ids": [
        "e000166"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-25",
      "kind": "target_state_changed",
      "step": 25,
      "evidence_ids": [
        "e000167"
      ],
      "object_id": "point-008",
      "state": "confirmed"
    },
    {
      "event_id": "event-26",
      "kind": "target_state_changed",
      "step": 25,
      "evidence_ids": [
        "e000168"
      ],
      "object_id": "point-004",
      "state": "stale"
    },
    {
      "event_id": "event-27",
      "kind": "replan_required",
      "step": 25,
      "evidence_ids": [
        "e000168"
      ],
      "object_id": "point-004",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-28",
      "kind": "target_state_changed",
      "step": 27,
      "evidence_ids": [
        "e000179"
      ],
      "object_id": "point-005",
      "state": "stale"
    },
    {
      "event_id": "event-29",
      "kind": "replan_required",
      "step": 27,
      "evidence_ids": [
        "e000179"
      ],
      "object_id": "point-005",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-30",
      "kind": "target_state_changed",
      "step": 28,
      "evidence_ids": [
        "e000185"
      ],
      "object_id": "point-008",
      "state": "predicted"
    },
    {
      "event_id": "event-31",
      "kind": "target_state_changed",
      "step": 29,
      "evidence_ids": [
        "e000192"
      ],
      "object_id": "point-009",
      "state": "confirmed"
    },
    {
      "event_id": "event-32",
      "kind": "target_state_changed",
      "step": 29,
      "evidence_ids": [
        "e000193"
      ],
      "object_id": "point-006",
      "state": "stale"
    },
    {
      "event_id": "event-33",
      "kind": "replan_required",
      "step": 29,
      "evidence_ids": [
        "e000193"
      ],
      "object_id": "point-006",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-34",
      "kind": "target_state_changed",
      "step": 31,
      "evidence_ids": [
        "e000205"
      ],
      "object_id": "point-008",
      "state": "unknown"
    },
    {
      "event_id": "event-35",
      "kind": "target_state_changed",
      "step": 32,
      "evidence_ids": [
        "e000210"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-36",
      "kind": "replan_required",
      "step": 32,
      "evidence_ids": [
        "e000210"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-37",
      "kind": "target_state_changed",
      "step": 32,
      "evidence_ids": [
        "e000211"
      ],
      "object_id": "point-007",
      "state": "stale"
    },
    {
      "event_id": "event-38",
      "kind": "replan_required",
      "step": 32,
      "evidence_ids": [
        "e000211"
      ],
      "object_id": "point-007",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-39",
      "kind": "target_state_changed",
      "step": 32,
      "evidence_ids": [
        "e000212"
      ],
      "object_id": "point-009",
      "state": "predicted"
    },
    {
      "event_id": "event-40",
      "kind": "target_state_changed",
      "step": 35,
      "evidence_ids": [
        "e000229"
      ],
      "object_id": "point-008",
      "state": "stale"
    },
    {
      "event_id": "event-41",
      "kind": "replan_required",
      "step": 35,
      "evidence_ids": [
        "e000229"
      ],
      "object_id": "point-008",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-42",
      "kind": "target_state_changed",
      "step": 35,
      "evidence_ids": [
        "e000230"
      ],
      "object_id": "point-009",
      "state": "unknown"
    },
    {
      "event_id": "event-43",
      "kind": "search_review_due",
      "step": 36,
      "evidence_ids": [
        "e000242"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-44",
      "kind": "replan_required",
      "step": 36,
      "evidence_ids": [
        "e000243"
      ],
      "plan_id": "plan-0011"
    },
    {
      "event_id": "event-45",
      "kind": "skill_stuck",
      "step": 37,
      "evidence_ids": [
        "e000249"
      ]
    },
    {
      "event_id": "event-46",
      "kind": "key_precondition_invalidated",
      "step": 37,
      "evidence_ids": [
        "e000249"
      ]
    },
    {
      "event_id": "event-47",
      "kind": "replan_required",
      "step": 37,
      "evidence_ids": [
        "e000249"
      ]
    },
    {
      "event_id": "event-48",
      "kind": "target_state_changed",
      "step": 39,
      "evidence_ids": [
        "e000256"
      ],
      "object_id": "point-009",
      "state": "stale"
    },
    {
      "event_id": "event-49",
      "kind": "replan_required",
      "step": 39,
      "evidence_ids": [
        "e000256"
      ],
      "object_id": "point-009",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-50",
      "kind": "target_state_changed",
      "step": 43,
      "evidence_ids": [
        "e000280"
      ],
      "object_id": "point-013",
      "state": "confirmed"
    },
    {
      "event_id": "event-51",
      "kind": "target_state_changed",
      "step": 44,
      "evidence_ids": [
        "e000287"
      ],
      "object_id": "point-010",
      "state": "stale"
    },
    {
      "event_id": "event-52",
      "kind": "replan_required",
      "step": 44,
      "evidence_ids": [
        "e000287"
      ],
      "object_id": "point-010",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-53",
      "kind": "target_state_changed",
      "step": 46,
      "evidence_ids": [
        "e000296"
      ],
      "object_id": "point-011",
      "state": "stale"
    },
    {
      "event_id": "event-54",
      "kind": "replan_required",
      "step": 46,
      "evidence_ids": [
        "e000296"
      ],
      "object_id": "point-011",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-55",
      "kind": "target_state_changed",
      "step": 46,
      "evidence_ids": [
        "e000297"
      ],
      "object_id": "point-013",
      "state": "predicted"
    },
    {
      "event_id": "event-56",
      "kind": "search_review_due",
      "step": 48,
      "evidence_ids": [
        "e000311"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-57",
      "kind": "target_state_changed",
      "step": 49,
      "evidence_ids": [
        "e000313"
      ],
      "object_id": "point-012",
      "state": "stale"
    },
    {
      "event_id": "event-58",
      "kind": "replan_required",
      "step": 49,
      "evidence_ids": [
        "e000313"
      ],
      "object_id": "point-012",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-59",
      "kind": "target_state_changed",
      "step": 49,
      "evidence_ids": [
        "e000314"
      ],
      "object_id": "point-013",
      "state": "unknown"
    },
    {
      "event_id": "event-60",
      "kind": "target_state_changed",
      "step": 53,
      "evidence_ids": [
        "e000337"
      ],
      "object_id": "point-015",
      "state": "confirmed"
    },
    {
      "event_id": "event-61",
      "kind": "target_state_changed",
      "step": 53,
      "evidence_ids": [
        "e000338"
      ],
      "object_id": "point-013",
      "state": "stale"
    },
    {
      "event_id": "event-62",
      "kind": "replan_required",
      "step": 53,
      "evidence_ids": [
        "e000338"
      ],
      "object_id": "point-013",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-63",
      "kind": "target_state_changed",
      "step": 56,
      "evidence_ids": [
        "e000354"
      ],
      "object_id": "point-015",
      "state": "predicted"
    },
    {
      "event_id": "event-64",
      "kind": "target_state_changed",
      "step": 59,
      "evidence_ids": [
        "e000372"
      ],
      "object_id": "point-014",
      "state": "stale"
    },
    {
      "event_id": "event-65",
      "kind": "replan_required",
      "step": 59,
      "evidence_ids": [
        "e000372"
      ],
      "object_id": "point-014",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-66",
      "kind": "target_state_changed",
      "step": 59,
      "evidence_ids": [
        "e000373"
      ],
      "object_id": "point-015",
      "state": "unknown"
    },
    {
      "event_id": "event-67",
      "kind": "search_review_due",
      "step": 60,
      "evidence_ids": [
        "e000385"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-68",
      "kind": "target_state_changed",
      "step": 63,
      "evidence_ids": [
        "e000398"
      ],
      "object_id": "point-015",
      "state": "stale"
    },
    {
      "event_id": "event-69",
      "kind": "replan_required",
      "step": 63,
      "evidence_ids": [
        "e000398"
      ],
      "object_id": "point-015",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-70",
      "kind": "target_state_changed",
      "step": 67,
      "evidence_ids": [
        "e000423"
      ],
      "object_id": "point-020",
      "state": "confirmed"
    },
    {
      "event_id": "event-71",
      "kind": "target_state_changed",
      "step": 67,
      "evidence_ids": [
        "e000424"
      ],
      "object_id": "point-016",
      "state": "stale"
    },
    {
      "event_id": "event-72",
      "kind": "replan_required",
      "step": 67,
      "evidence_ids": [
        "e000424"
      ],
      "object_id": "point-016",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-73",
      "kind": "target_state_changed",
      "step": 68,
      "evidence_ids": [
        "e000431"
      ],
      "object_id": "point-020",
      "state": "unknown"
    },
    {
      "event_id": "event-74",
      "kind": "target_state_changed",
      "step": 69,
      "evidence_ids": [
        "e000439"
      ],
      "object_id": "point-017",
      "state": "stale"
    },
    {
      "event_id": "event-75",
      "kind": "replan_required",
      "step": 69,
      "evidence_ids": [
        "e000439"
      ],
      "object_id": "point-017",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-76",
      "kind": "target_state_changed",
      "step": 72,
      "evidence_ids": [
        "e000455"
      ],
      "object_id": "point-018",
      "state": "stale"
    },
    {
      "event_id": "event-77",
      "kind": "replan_required",
      "step": 72,
      "evidence_ids": [
        "e000455"
      ],
      "object_id": "point-018",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-78",
      "kind": "search_review_due",
      "step": 72,
      "evidence_ids": [
        "e000462"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-79",
      "kind": "target_state_changed",
      "step": 74,
      "evidence_ids": [
        "e000468"
      ],
      "object_id": "point-019",
      "state": "stale"
    },
    {
      "event_id": "event-80",
      "kind": "replan_required",
      "step": 74,
      "evidence_ids": [
        "e000468"
      ],
      "object_id": "point-019",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-81",
      "kind": "target_state_changed",
      "step": 79,
      "evidence_ids": [
        "e000493"
      ],
      "object_id": "point-020",
      "state": "stale"
    },
    {
      "event_id": "event-82",
      "kind": "replan_required",
      "step": 79,
      "evidence_ids": [
        "e000493"
      ],
      "object_id": "point-020",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-83",
      "kind": "target_state_changed",
      "step": 82,
      "evidence_ids": [
        "e000511"
      ],
      "object_id": "point-021",
      "state": "stale"
    },
    {
      "event_id": "event-84",
      "kind": "replan_required",
      "step": 82,
      "evidence_ids": [
        "e000511"
      ],
      "object_id": "point-021",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-85",
      "kind": "search_review_due",
      "step": 84,
      "evidence_ids": [
        "e000527"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-86",
      "kind": "target_state_changed",
      "step": 88,
      "evidence_ids": [
        "e000544"
      ],
      "object_id": "point-022",
      "state": "stale"
    },
    {
      "event_id": "event-87",
      "kind": "replan_required",
      "step": 88,
      "evidence_ids": [
        "e000544"
      ],
      "object_id": "point-022",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-88",
      "kind": "target_state_changed",
      "step": 90,
      "evidence_ids": [
        "e000553"
      ],
      "object_id": "point-023",
      "state": "stale"
    },
    {
      "event_id": "event-89",
      "kind": "replan_required",
      "step": 90,
      "evidence_ids": [
        "e000553"
      ],
      "object_id": "point-023",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-90",
      "kind": "target_state_changed",
      "step": 92,
      "evidence_ids": [
        "e000563"
      ],
      "object_id": "point-024",
      "state": "stale"
    },
    {
      "event_id": "event-91",
      "kind": "replan_required",
      "step": 92,
      "evidence_ids": [
        "e000563"
      ],
      "object_id": "point-024",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-92",
      "kind": "search_review_due",
      "step": 96,
      "evidence_ids": [
        "e000593"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-93",
      "kind": "target_state_changed",
      "step": 97,
      "evidence_ids": [
        "e000595"
      ],
      "object_id": "point-025",
      "state": "stale"
    },
    {
      "event_id": "event-94",
      "kind": "replan_required",
      "step": 97,
      "evidence_ids": [
        "e000595"
      ],
      "object_id": "point-025",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-95",
      "kind": "target_state_changed",
      "step": 102,
      "evidence_ids": [
        "e000627"
      ],
      "object_id": "point-026",
      "state": "stale"
    },
    {
      "event_id": "event-96",
      "kind": "replan_required",
      "step": 102,
      "evidence_ids": [
        "e000627"
      ],
      "object_id": "point-026",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-97",
      "kind": "target_state_changed",
      "step": 104,
      "evidence_ids": [
        "e000637"
      ],
      "object_id": "point-027",
      "state": "stale"
    },
    {
      "event_id": "event-98",
      "kind": "replan_required",
      "step": 104,
      "evidence_ids": [
        "e000637"
      ],
      "object_id": "point-027",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-99",
      "kind": "target_state_changed",
      "step": 107,
      "evidence_ids": [
        "e000657"
      ],
      "object_id": "point-028",
      "state": "stale"
    },
    {
      "event_id": "event-100",
      "kind": "replan_required",
      "step": 107,
      "evidence_ids": [
        "e000657"
      ],
      "object_id": "point-028",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-101",
      "kind": "search_review_due",
      "step": 108,
      "evidence_ids": [
        "e000666"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-102",
      "kind": "target_state_changed",
      "step": 111,
      "evidence_ids": [
        "e000679"
      ],
      "object_id": "point-029",
      "state": "stale"
    },
    {
      "event_id": "event-103",
      "kind": "replan_required",
      "step": 111,
      "evidence_ids": [
        "e000679"
      ],
      "object_id": "point-029",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-104",
      "kind": "target_state_changed",
      "step": 114,
      "evidence_ids": [
        "e000696"
      ],
      "object_id": "point-030",
      "state": "stale"
    },
    {
      "event_id": "event-105",
      "kind": "replan_required",
      "step": 114,
      "evidence_ids": [
        "e000696"
      ],
      "object_id": "point-030",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-106",
      "kind": "target_state_changed",
      "step": 116,
      "evidence_ids": [
        "e000708"
      ],
      "object_id": "point-031",
      "state": "stale"
    },
    {
      "event_id": "event-107",
      "kind": "replan_required",
      "step": 116,
      "evidence_ids": [
        "e000708"
      ],
      "object_id": "point-031",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-108",
      "kind": "target_state_changed",
      "step": 120,
      "evidence_ids": [
        "e000732"
      ],
      "object_id": "point-032",
      "state": "stale"
    },
    {
      "event_id": "event-109",
      "kind": "replan_required",
      "step": 120,
      "evidence_ids": [
        "e000732"
      ],
      "object_id": "point-032",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-110",
      "kind": "search_review_due",
      "step": 120,
      "evidence_ids": [
        "e000737"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
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
      "value": -3.1232582120948016,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000733"
      ]
    },
    "pose.y_m": {
      "value": 5.335256083791076,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000734"
      ]
    },
    "pose.yaw_rad": {
      "value": -2.7871645064789115,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000735"
      ]
    },
    "point-001.range_m": {
      "value": 1.8874,
      "source": "rgbd_optical_flow",
      "step": 2,
      "evidence_ids": [
        "e000016"
      ]
    },
    "point-001.bearing_rad": {
      "value": 0.4041,
      "source": "rgbd_optical_flow",
      "step": 2,
      "evidence_ids": [
        "e000017"
      ]
    },
    "point-002.range_m": {
      "value": 1.7714,
      "source": "rgbd_optical_flow",
      "step": 5,
      "evidence_ids": [
        "e000034"
      ]
    },
    "point-002.bearing_rad": {
      "value": 0.2203,
      "source": "rgbd_optical_flow",
      "step": 5,
      "evidence_ids": [
        "e000035"
      ]
    },
    "point-003.range_m": {
      "value": 1.4625,
      "source": "rgbd_optical_flow",
      "step": 11,
      "evidence_ids": [
        "e000077"
      ]
    },
    "point-003.bearing_rad": {
      "value": -0.358,
      "source": "rgbd_optical_flow",
      "step": 11,
      "evidence_ids": [
        "e000078"
      ]
    },
    "point-004.range_m": {
      "value": 1.8406,
      "source": "rgbd_optical_flow",
      "step": 15,
      "evidence_ids": [
        "e000104"
      ]
    },
    "point-004.bearing_rad": {
      "value": -0.5605,
      "source": "rgbd_optical_flow",
      "step": 15,
      "evidence_ids": [
        "e000105"
      ]
    },
    "point-005.range_m": {
      "value": 0.9923,
      "source": "rgbd_optical_flow",
      "step": 17,
      "evidence_ids": [
        "e000119"
      ]
    },
    "point-005.bearing_rad": {
      "value": -0.3497,
      "source": "rgbd_optical_flow",
      "step": 17,
      "evidence_ids": [
        "e000120"
      ]
    },
    "point-006.range_m": {
      "value": 1.4345,
      "source": "rgbd_optical_flow",
      "step": 19,
      "evidence_ids": [
        "e000132"
      ]
    },
    "point-006.bearing_rad": {
      "value": 0.1483,
      "source": "rgbd_optical_flow",
      "step": 19,
      "evidence_ids": [
        "e000133"
      ]
    },
    "point-007.range_m": {
      "value": 0.6642,
      "source": "rgbd_optical_flow",
      "step": 22,
      "evidence_ids": [
        "e000151"
      ]
    },
    "point-007.bearing_rad": {
      "value": -0.3595,
      "source": "rgbd_optical_flow",
      "step": 22,
      "evidence_ids": [
        "e000152"
      ]
    },
    "point-008.range_m": {
      "value": 1.1603,
      "source": "rgbd_optical_flow",
      "step": 25,
      "evidence_ids": [
        "e000172"
      ]
    },
    "point-008.bearing_rad": {
      "value": 0.1198,
      "source": "rgbd_optical_flow",
      "step": 25,
      "evidence_ids": [
        "e000173"
      ]
    },
    "point-009.range_m": {
      "value": 1.1026,
      "source": "rgbd_optical_flow",
      "step": 29,
      "evidence_ids": [
        "e000197"
      ]
    },
    "point-009.bearing_rad": {
      "value": 0.0866,
      "source": "rgbd_optical_flow",
      "step": 29,
      "evidence_ids": [
        "e000198"
      ]
    },
    "point-010.range_m": {
      "value": 1.1791,
      "source": "rgbd_optical_flow",
      "step": 34,
      "evidence_ids": [
        "e000226"
      ]
    },
    "point-010.bearing_rad": {
      "value": 0.1046,
      "source": "rgbd_optical_flow",
      "step": 34,
      "evidence_ids": [
        "e000227"
      ]
    },
    "point-011.range_m": {
      "value": 1.2576,
      "source": "rgbd_optical_flow",
      "step": 37,
      "evidence_ids": [
        "e000247"
      ]
    },
    "point-011.bearing_rad": {
      "value": 0.0089,
      "source": "rgbd_optical_flow",
      "step": 37,
      "evidence_ids": [
        "e000248"
      ]
    },
    "point-012.range_m": {
      "value": 1.1055,
      "source": "rgbd_optical_flow",
      "step": 39,
      "evidence_ids": [
        "e000260"
      ]
    },
    "point-012.bearing_rad": {
      "value": -0.0275,
      "source": "rgbd_optical_flow",
      "step": 39,
      "evidence_ids": [
        "e000261"
      ]
    },
    "point-013.range_m": {
      "value": 1.0737,
      "source": "rgbd_optical_flow",
      "step": 43,
      "evidence_ids": [
        "e000284"
      ]
    },
    "point-013.bearing_rad": {
      "value": 0.0509,
      "source": "rgbd_optical_flow",
      "step": 43,
      "evidence_ids": [
        "e000285"
      ]
    },
    "point-014.range_m": {
      "value": 1.0864,
      "source": "rgbd_optical_flow",
      "step": 49,
      "evidence_ids": [
        "e000318"
      ]
    },
    "point-014.bearing_rad": {
      "value": -0.0414,
      "source": "rgbd_optical_flow",
      "step": 49,
      "evidence_ids": [
        "e000319"
      ]
    },
    "point-015.range_m": {
      "value": 1.211,
      "source": "rgbd_optical_flow",
      "step": 53,
      "evidence_ids": [
        "e000342"
      ]
    },
    "point-015.bearing_rad": {
      "value": -0.0679,
      "source": "rgbd_optical_flow",
      "step": 53,
      "evidence_ids": [
        "e000343"
      ]
    },
    "point-016.range_m": {
      "value": 1.1044,
      "source": "rgbd_optical_flow",
      "step": 57,
      "evidence_ids": [
        "e000363"
      ]
    },
    "point-016.bearing_rad": {
      "value": -0.0124,
      "source": "rgbd_optical_flow",
      "step": 57,
      "evidence_ids": [
        "e000364"
      ]
    },
    "point-017.range_m": {
      "value": 1.1585,
      "source": "rgbd_optical_flow",
      "step": 59,
      "evidence_ids": [
        "e000377"
      ]
    },
    "point-017.bearing_rad": {
      "value": 0.0584,
      "source": "rgbd_optical_flow",
      "step": 59,
      "evidence_ids": [
        "e000378"
      ]
    },
    "point-018.range_m": {
      "value": 1.0864,
      "source": "rgbd_optical_flow",
      "step": 62,
      "evidence_ids": [
        "e000394"
      ]
    },
    "point-018.bearing_rad": {
      "value": -0.0814,
      "source": "rgbd_optical_flow",
      "step": 62,
      "evidence_ids": [
        "e000395"
      ]
    },
    "point-019.range_m": {
      "value": 1.1457,
      "source": "rgbd_optical_flow",
      "step": 64,
      "evidence_ids": [
        "e000407"
      ]
    },
    "point-019.bearing_rad": {
      "value": 0.2059,
      "source": "rgbd_optical_flow",
      "step": 64,
      "evidence_ids": [
        "e000408"
      ]
    },
    "point-020.range_m": {
      "value": 1.0756,
      "source": "rgbd_optical_flow",
      "step": 69,
      "evidence_ids": [
        "e000443"
      ]
    },
    "point-020.bearing_rad": {
      "value": -0.1079,
      "source": "rgbd_optical_flow",
      "step": 69,
      "evidence_ids": [
        "e000444"
      ]
    },
    "point-021.range_m": {
      "value": 1.1754,
      "source": "rgbd_optical_flow",
      "step": 72,
      "evidence_ids": [
        "e000459"
      ]
    },
    "point-021.bearing_rad": {
      "value": 0.0499,
      "source": "rgbd_optical_flow",
      "step": 72,
      "evidence_ids": [
        "e000460"
      ]
    },
    "point-022.range_m": {
      "value": 1.2446,
      "source": "rgbd_optical_flow",
      "step": 78,
      "evidence_ids": [
        "e000489"
      ]
    },
    "point-022.bearing_rad": {
      "value": 0.0238,
      "source": "rgbd_optical_flow",
      "step": 78,
      "evidence_ids": [
        "e000490"
      ]
    },
    "point-023.range_m": {
      "value": 1.1481,
      "source": "rgbd_optical_flow",
      "step": 80,
      "evidence_ids": [
        "e000502"
      ]
    },
    "point-023.bearing_rad": {
      "value": 0.0824,
      "source": "rgbd_optical_flow",
      "step": 80,
      "evidence_ids": [
        "e000503"
      ]
    },
    "point-024.range_m": {
      "value": 1.1621,
      "source": "rgbd_optical_flow",
      "step": 82,
      "evidence_ids": [
        "e000515"
      ]
    },
    "point-024.bearing_rad": {
      "value": 0.1075,
      "source": "rgbd_optical_flow",
      "step": 82,
      "evidence_ids": [
        "e000516"
      ]
    },
    "point-025.range_m": {
      "value": 1.1911,
      "source": "rgbd_optical_flow",
      "step": 87,
      "evidence_ids": [
        "e000540"
      ]
    },
    "point-025.bearing_rad": {
      "value": 0.0831,
      "source": "rgbd_optical_flow",
      "step": 87,
      "evidence_ids": [
        "e000541"
      ]
    },
    "point-026.range_m": {
      "value": 1.1553,
      "source": "rgbd_optical_flow",
      "step": 92,
      "evidence_ids": [
        "e000567"
      ]
    },
    "point-026.bearing_rad": {
      "value": 0.0596,
      "source": "rgbd_optical_flow",
      "step": 92,
      "evidence_ids": [
        "e000568"
      ]
    },
    "point-027.range_m": {
      "value": 1.0938,
      "source": "rgbd_optical_flow",
      "step": 95,
      "evidence_ids": [
        "e000585"
      ]
    },
    "point-027.bearing_rad": {
      "value": -0.0739,
      "source": "rgbd_optical_flow",
      "step": 95,
      "evidence_ids": [
        "e000586"
      ]
    },
    "point-028.range_m": {
      "value": 1.359,
      "source": "rgbd_optical_flow",
      "step": 97,
      "evidence_ids": [
        "e000599"
      ]
    },
    "point-028.bearing_rad": {
      "value": -0.1233,
      "source": "rgbd_optical_flow",
      "step": 97,
      "evidence_ids": [
        "e000600"
      ]
    },
    "point-029.range_m": {
      "value": 1.2557,
      "source": "rgbd_optical_flow",
      "step": 101,
      "evidence_ids": [
        "e000623"
      ]
    },
    "point-029.bearing_rad": {
      "value": -0.4112,
      "source": "rgbd_optical_flow",
      "step": 101,
      "evidence_ids": [
        "e000624"
      ]
    },
    "point-030.range_m": {
      "value": 1.0958,
      "source": "rgbd_optical_flow",
      "step": 104,
      "evidence_ids": [
        "e000641"
      ]
    },
    "point-030.bearing_rad": {
      "value": -0.0015,
      "source": "rgbd_optical_flow",
      "step": 104,
      "evidence_ids": [
        "e000642"
      ]
    },
    "point-031.range_m": {
      "value": 1.1114,
      "source": "rgbd_optical_flow",
      "step": 106,
      "evidence_ids": [
        "e000653"
      ]
    },
    "point-031.bearing_rad": {
      "value": -0.0802,
      "source": "rgbd_optical_flow",
      "step": 106,
      "evidence_ids": [
        "e000654"
      ]
    },
    "point-032.range_m": {
      "value": 1.3379,
      "source": "rgbd_optical_flow",
      "step": 110,
      "evidence_ids": [
        "e000675"
      ]
    },
    "point-032.bearing_rad": {
      "value": -0.3743,
      "source": "rgbd_optical_flow",
      "step": 110,
      "evidence_ids": [
        "e000676"
      ]
    },
    "point-033.range_m": {
      "value": 1.8869,
      "source": "rgbd_optical_flow",
      "step": 114,
      "evidence_ids": [
        "e000700"
      ]
    },
    "point-033.bearing_rad": {
      "value": -0.136,
      "source": "rgbd_optical_flow",
      "step": 114,
      "evidence_ids": [
        "e000701"
      ]
    },
    "point-034.range_m": {
      "value": 1.1808,
      "source": "rgbd_optical_flow",
      "step": 116,
      "evidence_ids": [
        "e000712"
      ]
    },
    "point-034.bearing_rad": {
      "value": -0.0592,
      "source": "rgbd_optical_flow",
      "step": 116,
      "evidence_ids": [
        "e000713"
      ]
    },
    "point-035.range_m": {
      "value": 1.1329,
      "source": "rgbd_optical_flow",
      "step": 119,
      "evidence_ids": [
        "e000728"
      ]
    },
    "point-035.bearing_rad": {
      "value": -0.0486,
      "source": "rgbd_optical_flow",
      "step": 119,
      "evidence_ids": [
        "e000729"
      ]
    }
  },
  "plans": [
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_for_A",
          "description": "Rotate left 0.6 rad in place to sweep the left sector (currently off-view) for the blue ball task:A, anchored on tracked reference point-001 (green candidate B at bearing +0.404 rad); endpoint when that reference bearing drops to <= -0.15 rad, meaning the left sector has been swept.",
          "preconditions": [
            {
              "object_id": "point-001"
            }
          ],
          "completion": [
            {
              "measurement": "point-001.bearing_rad",
              "op": "le",
              "value": -0.15
            }
          ],
          "active": false,
          "status": "已失效",
          "evidence_ids": [
            "e000012"
          ]
        },
        {
          "subgoal_id": "advance_viewpoint",
          "description": "After the sweep, if A is still unseen but forward geometry around the tracked reference supports it, translate forward ~0.3 m using the observed reference for a new viewpoint and re-inspect for A.",
          "preconditions": [
            {
              "object_id": "point-001"
            }
          ],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 0.3
            }
          ],
          "active": false,
          "status": "已失效",
          "evidence_ids": [
            "e000012"
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
          "subgoal_id": "scan_left_for_A"
        }
      ],
      "recovery": "stop, observe fresh RGB-D and tracked geometry, then pick another supported scan direction or a small safe viewpoint change; abort if geometry stays unknown",
      "plan_id": "plan-0001",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_right_for_A",
          "description": "Rotate right in place from current heading 0 rad (anchored on pose.yaw_rad) to sweep the unseen right-front sector for blue ball A; local endpoint yaw <= -0.55 rad",
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
            "e000028"
          ]
        },
        {
          "subgoal_id": "scan_left_for_A",
          "description": "Rotate back left through the front sector up to yaw >= +0.5 rad to sweep the left-front sector (where green B was noted) for blue ball A",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 0.5
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000039"
          ]
        },
        {
          "subgoal_id": "advance_viewpoint",
          "description": "Short conservative forward translation 0.3 m only after scans show no A and the fresh tracked ray still shows open space ahead; inspect new geometry",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 0.25
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000074"
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
      "recovery": "observe a fresh frame; if A appears, track_point it and confirm with an independent frame before approaching; if no scan/motion branch yields new geometry, stop and abort with reason",
      "plan_id": "plan-0002",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "sweep_left_for_A",
          "description": "Sweep the left-front sector not yet covered from this viewpoint: turn left from yaw ~0.545 to >=1.05 rad, anchored on the confirmed point-003 (green B) ray as a stable reference, looking for the blue ball A.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 1.05
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000084"
          ]
        },
        {
          "subgoal_id": "advance_viewpoint",
          "description": "After the sweep shows no A, translate forward ~0.3 m to a fresh viewpoint using the currently open point-003 ray direction as reference and inspect new geometry.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 0.65
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
          "subgoal_id": "advance_viewpoint"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_viewpoint"
        }
      ],
      "recovery": "observe a fresh frame; if blue A appears, track_point it and confirm with an independent frame before approach; if neither sweep nor advance reveals A, switch sector/direction or stop and abort with reason",
      "plan_id": "plan-0003",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "reacquire_B_ref",
          "description": "Left-front sweep (yaw 0.545 to ~1.04) found no blue A; review switches sector. Turn right ~0.6 rad toward the confirmed green-B ray (point-003 at ~bearing 0.17 rad) so B is back in front-center as a stable observed reference, endpoint yaw <= 0.50 rad.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "le",
              "value": 0.5
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000089"
          ]
        },
        {
          "subgoal_id": "advance_right_front",
          "description": "From the reacquired B reference viewpoint, translate a short ~0.3 m forward along that confirmed B ray (bearing ~0.17 rad) to a fresh viewpoint and inspect the right-front sector for blue A; endpoint pose.x_m >= 0.65.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 0.65
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000093"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "reacquire_B_ref"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_right_front"
        }
      ],
      "recovery": "observe a fresh frame; if blue A appears, track_point it at the current image_id and confirm with an independent frame before approach; if neither the right-front advance nor a later sector change reveals A, stop and abort with reason",
      "plan_id": "plan-0004",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_right_sector",
          "description": "Sustain a forward advance ~0.35 m along current heading, using the tracked green-B ray (point-004, bearing -0.56 rad, range 1.84 m) as stable observed reference, to reach a fresh viewpoint over the right-front sector and inspect for blue A; endpoint point-004.range_m <= 1.60 m.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-004.range_m",
              "op": "le",
              "value": 1.6
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000111"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_right_sector"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_right_sector"
        }
      ],
      "recovery": "observe a fresh frame; if blue A appears track_point at its pixel and verify with an independent frame before approach_A; if no A in the new view, reacquire a stable reference and change view sector with another short translation; if geometry cannot support safe motion, stop and abort with reason",
      "plan_id": "plan-0005",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_right_sector",
          "description": "Turn right 0.45 rad about the current heading (yaw 0.502 -> ~0.05 rad) to sweep the unexplored right/behind sector for blue A, keeping the tracked green-B candidate point-005 (bearing -0.35 rad, range 0.99 m) visible as the observed reference; endpoint = measured yaw <= 0.06 rad.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "le",
              "value": 0.06
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000126"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_right_sector"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "scan_right_sector"
        }
      ],
      "recovery": "observe a fresh frame; if blue A is visible, track_point at its pixel and confirm with an independent frame before any approach_A; if not, take a short translation to a new viewpoint supported by observed geometry; if geometry cannot support motion, stop and abort with a reason",
      "plan_id": "plan-0006",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_viewpoint",
          "description": "Advance ~0.25 m forward along the visible line to confirmed green B reference point-006 (range 1.43 m, bearing 0.15 rad) to gain parallax behind the right-side cabinets and search for blue A; endpoint point-006.range_m <= 1.25 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-006.range_m",
              "op": "le",
              "value": 1.25
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000139"
          ]
        },
        {
          "subgoal_id": "scan_left_sector",
          "description": "Turn left about 0.5 rad to sweep the unsearched left/occluded sector for blue A; endpoint pose.yaw_rad >= 0.60",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 0.6
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000144"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_left_sector"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_viewpoint"
        }
      ],
      "recovery": "observe a fresh frame; re-track a visible feature if point-006 geometry is lost or motion unsupported, then choose another short evidenced move; abort if no safe geometry",
      "plan_id": "plan-0007",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_for_A",
          "description": "Turn left 0.6 rad from yaw 0.576 to sweep the unsearched left sector for blue A; endpoint pose.yaw_rad >= 1.10",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 1.1
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000157"
          ]
        },
        {
          "subgoal_id": "advance_forward",
          "description": "After scan, translate ~0.25 m forward with yaw ~1.1 rad to change viewpoint behind the cabinets and re-inspect for blue A; endpoint pose.x_m >= 1.18",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 1.18
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000175"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_forward"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_forward"
        }
      ],
      "recovery": "observe a fresh frame, re-track a visible feature if point-007 geometry is lost, then choose another short evidenced move; abort if no safe geometry",
      "plan_id": "plan-0008",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_sector",
          "description": "Continue the committed leftward sweep from yaw ~1.16 to ~1.76 (0.6 rad) using the confirmed landmark ray point-009 (1.10 m ahead, bearing 0.09) as fixed reference; endpoint pose.yaw_rad >= 1.70 to view the next unsearched sector for blue A / green B",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 1.7
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000203"
          ]
        },
        {
          "subgoal_id": "advance_forward_explore",
          "description": "After the sweep, translate ~0.25 m along the new heading to change viewpoint behind the cabinet line and re-inspect; endpoint pose.y_m >= 1.20",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.y_m",
              "op": "ge",
              "value": 1.2
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000214"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_forward_explore"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_forward_explore"
        }
      ],
      "recovery": "observe a fresh frame, re-track a visible feature if point-009 geometry is lost, then choose another short evidenced move; abort if no safe geometry",
      "plan_id": "plan-0009",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "sweep_right_reference",
          "description": "Turn right ~0.6 rad from yaw ~1.72 to ~1.12 so the heading aligns with the predicted landmark ray point-009 (episode-frame bearing ~1.10 rad) and opens the unsearched forward-right sector for blue A; endpoint pose.yaw_rad <= 1.15",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "le",
              "value": 1.15
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000221"
          ]
        },
        {
          "subgoal_id": "advance_toward_reference",
          "description": "Translate ~0.4 m forward along the new ~1.12 rad heading using point-009 as the sustained observed reference, changing viewpoint past the cabinet line; endpoint pose.x_m >= 1.35",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "ge",
              "value": 1.35
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000234"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "sweep_right_reference"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_toward_reference"
        }
      ],
      "recovery": "observe a fresh frame, re-track a visible static feature if point-009 geometry is lost, then pick another short evidenced move; abort if no safe direction remains",
      "plan_id": "plan-0010",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_forward_leg",
          "description": "Commit to a forward search leg along current heading (~1.20 rad episode yaw, bearing of point-011 ~0.009 rad) using the tracked floor feature point-011 at 1.26 m as sustained reference, to change viewpoint past the cabinet line and look for blue A / green B; endpoint when point-011 range shrinks to <= 0.9 m",
          "preconditions": [
            {
              "object_id": "point-011"
            }
          ],
          "completion": [
            {
              "measurement": "point-011.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "已失效",
          "evidence_ids": [
            "e000243"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_forward_leg"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_forward_leg"
        }
      ],
      "recovery": "observe a fresh frame; if point-011 geometry is lost, re-track a visible static feature and pick another short evidenced move; abort if no safe direction remains",
      "plan_id": "plan-0011",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_leg",
          "description": "Commit to forward travel along observed floor feature point-011 (range 1.2576 m, bearing 0.009 rad, nearly dead ahead); move base forward 0.4 m to gain a new viewpoint that can reveal the blue ball A or green cube B; local endpoint: point-011 range falls to <= 1.05 m (>=0.2 m measured forward progress)",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-011.range_m",
              "op": "le",
              "value": 1.05
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000254"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_leg"
        }
      ],
      "recovery": "stop, re-observe fresh geometry, reselect a static visible feature, then commit to another supported viewpoint move or abort",
      "plan_id": "plan-0012",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_leg",
          "description": "Commit to a short forward leg along the observed floor feature point-012 (range 1.1055 m, bearing -0.0275 rad, nearly dead ahead) to gain a new viewpoint that may reveal blue ball A or green cube B; local endpoint: point-012 range falls to 0.85 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-012.range_m",
              "op": "le",
              "value": 0.85
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000267"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_leg"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_leg"
        }
      ],
      "recovery": "stop, re-observe fresh geometry, reselect a static visible feature, then commit to another supported viewpoint move or abort",
      "plan_id": "plan-0013",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_leg2",
          "description": "Commit forward along the observed floor feature point-013 (range 1.1031 m, bearing 0.0224 rad, nearly dead ahead), using it as the stable reference; local endpoint is point-013 range falling to 0.95 m to gain a fresh viewpoint that may reveal blue ball A first.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-013.range_m",
              "op": "le",
              "value": 0.95
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000286"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_leg2"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_leg2"
        }
      ],
      "recovery": "stop, re-observe fresh geometry, reselect a static visible feature, then commit another supported viewpoint move or abort",
      "plan_id": "plan-0014",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_sector",
          "description": "Strategy review: after 47 decisions with no A/B sighting, rotate left 0.6 rad from current yaw (~1.275) to sweep a new sector of the scene and look for blue ball A or green block B, instead of sinking more forward into an already-inspected view",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 1.87
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000310"
          ]
        },
        {
          "subgoal_id": "inspect_new_view",
          "description": "After rotation, observe the fresh view; if a blue/green candidate appears, track it, else translate to a new viewpoint along visible floor geometry",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 1.87
            }
          ],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "scan_left_sector"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_left_sector"
        }
      ],
      "recovery": "stop, re-observe fresh geometry, pick another supported direction or abort if no safe motion is supported",
      "plan_id": "plan-0015",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_past_initial_area",
          "description": "Commit to a sustained forward leg along the visible floor ray marked by tracked feature point-014 (bearing -0.04 rad, range 1.09 m at startup); gain a new viewpoint to look for blue ball A and green block B; endpoint is 0.29 m of forward progress",
          "preconditions": [
            {
              "measurement": "point-014.range_m",
              "op": "ge",
              "value": 0.9
            }
          ],
          "completion": [
            {
              "measurement": "pose.y_m",
              "op": "ge",
              "value": 2.95
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000325"
          ]
        },
        {
          "subgoal_id": "inspect_new_view",
          "description": "Observe the fresh view after translation; track any blue/green candidate, otherwise choose another supported direction",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.y_m",
              "op": "ge",
              "value": 2.95
            }
          ],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "advance_past_initial_area"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_new_view"
        }
      ],
      "recovery": "stop, re-observe fresh geometry, then pick another supported direction or abort if no safe motion is supported",
      "plan_id": "plan-0016",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left_sector",
          "description": "Change search branch after review: rotate in place 0.6 rad left from current heading (yaw 1.818 rad) to reveal a new sector for blue ball A / green block B; endpoint is yaw >= 2.35 rad",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 2.35
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000348"
          ]
        },
        {
          "subgoal_id": "inspect_left_view",
          "description": "Observe new view; track any blue/green candidate, else translate 0.25 m along a visible floor ray",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 2.35
            }
          ],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "scan_left_sector"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "inspect_left_view"
        }
      ],
      "recovery": "stop, observe fresh geometry, then translate a short distance along a visible floor ray or abort if no safe motion is supported",
      "plan_id": "plan-0017",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "translate_forward_probe",
          "description": "Translate 0.25 m forward toward visible floor feature point-016 (bearing -0.01 rad, range 1.10 m) to change viewpoint and reveal occluded targets A/B; local endpoint point-016 range <= 0.9 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-016.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000370"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "translate_forward_probe"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "translate_forward_probe"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-016 lost or clearance unclear, track another visible floor feature before any further motion, else abort with reason",
      "plan_id": "plan-0018",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "probe_forward_view",
          "description": "Translate 0.25 m forward along the visible floor feature point-017 (bearing 0.058 rad, range 1.16 m) to change viewpoint and reveal occluded targets A/B; local endpoint point-017.range <= 0.93 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-017.range_m",
              "op": "le",
              "value": 0.93
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000384"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "probe_forward_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "probe_forward_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-017 lost or clearance unclear, track another visible floor feature before further motion, else abort with reason",
      "plan_id": "plan-0019",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Commit one sustained forward leg along the visible floor feature point-018 (bearing -0.081 rad, range 1.09 m): translate 0.4 m forward to change viewpoint and reveal occluded targets A/B; local endpoint point-018.range <= 0.75 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-018.range_m",
              "op": "le",
              "value": 0.75
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000402"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-018 lost or clearance unclear, track another visible floor feature before further motion, else abort with reason",
      "plan_id": "plan-0020",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Sustained forward leg along the visible floor feature point-019 (bearing 0.206 rad, range 1.15 m) to change viewpoint and reveal occluded targets A/B; local endpoint point-019.range <= 0.75 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-019.range_m",
              "op": "le",
              "value": 0.75
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000414"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-019 lost or clearance unclear, track another visible floor feature before further motion, else abort with reason",
      "plan_id": "plan-0021",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Sustained forward leg along tracked floor feature point-020 (bearing 0.009 rad, range 1.14 m) to change viewpoint and reveal occluded targets A/B; local endpoint point-020 range <= 0.90 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-020.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000430"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-020 is lost or clearance unclear, track another visible floor feature before further motion, else abort with reason",
      "plan_id": "plan-0022",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Continue the sustained forward leg along the currently tracked floor reference point-021 (bearing 0.05 rad, range 1.18 m ahead) to change viewpoint and reveal targets A/B hidden behind cabinets; local endpoint point-021 range <= 0.90 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-021.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000467"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-021 is lost or clearance is unclear, track another visible floor feature before further motion, else turn to a new search direction or abort with reason",
      "plan_id": "plan-0023",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Commit to a short forward leg along the tracked floor reference point-022 (bearing 0.024 rad, range 1.24 m ahead) to shift viewpoint and reveal targets A/B hidden behind cabinets; local endpoint point-022 range <= 0.95 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-022.range_m",
              "op": "le",
              "value": 0.95
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000497"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-022 is lost or clearance is unclear, track another visible floor feature before further motion, else turn to a new search direction or abort with reason",
      "plan_id": "plan-0024",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Commit to a short forward leg along the currently tracked floor reference point-023 (bearing 0.082 rad, range 1.15 m, roughly straight ahead) to shift viewpoint and reveal targets A/B hidden behind cabinets; local endpoint point-023 range <= 0.90 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-023.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000509"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-023 is lost or clearance is unclear, track another visible floor feature before further motion, else turn to a new search direction or abort with reason",
      "plan_id": "plan-0025",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Sustained short forward leg along tracked floor reference point-024 (bearing 0.108 rad, range 1.16 m, roughly straight ahead) to reach a new viewpoint and reveal targets A/B hidden behind cabinets; local endpoint point-024 range <= 0.90 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-024.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000522"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-024 is lost or clearance is unclear, track another visible floor feature before further motion, else turn to a new search direction or abort with reason",
      "plan_id": "plan-0026",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Sustained short forward leg along tracked floor reference point-025 (bearing 0.083 rad, range 1.19 m, just left of straight ahead) to reach a new viewpoint and reveal targets A/B hidden behind cabinets; endpoint point-025 range <= 0.90 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-025.range_m",
              "op": "le",
              "value": 0.9
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000548"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-025 lost or clearance unclear, track another visible floor feature before further motion, else turn to a new search direction or abort with reason",
      "plan_id": "plan-0027",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Sustained short forward leg (~0.4 m) along tracked floor reference point-026 (bearing 0.06 rad, range 1.16 m, essentially straight ahead) to reach a new viewpoint past the cabinet line and reveal blue A / green B; endpoint point-026 range <= 0.80 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-026.range_m",
              "op": "le",
              "value": 0.8
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000574"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop, observe fresh geometry; if point-026 lost or forward clearance unclear, track another visible floor feature before further motion, else turn to a new direction or abort with reason",
      "plan_id": "plan-0028",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Sustained short forward leg (~0.45 m) straight along tracked floor reference point-027 (bearing -0.07 rad, range 1.09 m) to reach a new viewpoint past the cabinet line and reveal blue A / green B; endpoint point-027 range <= 0.65 m",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-027.range_m",
              "op": "le",
              "value": 0.65
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000592"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop and observe fresh geometry; if point-027 is lost or forward clearance is unclear, track another visible floor feature ahead before further motion, otherwise commit to a different heading and scan, or abort with reason",
      "plan_id": "plan-0029",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "advance_view",
          "description": "Commit to a short forward leg (~0.45 m) straight along tracked floor reference point-028 (bearing -0.12 rad, range 1.36 m, previously clear floor) to shift viewpoint past the cabinet line and reveal the blue ball A or green cube B; endpoint: point-028 range <= 1.05 m",
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
            "e000606"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_view"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "advance_view"
        }
      ],
      "recovery": "stop and observe fresh geometry; if point-028 is lost or forward clearance is unclear, track another visible floor feature ahead before more motion, otherwise commit to a different heading (turn) and rescan, or abort with reason",
      "plan_id": "plan-0030",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left",
          "description": "Rotate left 0.45 rad in place to survey the sector left of the cabinet line for the blue ball A or green cube B; reference is current yaw 2.59 rad, endpoint yaw >= 3.00 rad",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 3.0
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000625"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_left"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "scan_left"
        }
      ],
      "recovery": "stop, observe fresh frame, track any visible target candidate; if nothing visible, commit to a short forward leg along a fresh tracked floor point",
      "plan_id": "plan-0031",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward",
          "description": "Commit a short forward leg along the currently tracked floor reference point-029 (bearing -0.41 rad, range 1.26 m); endpoint is reduced range <= 0.98 m.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-029.range_m",
              "op": "le",
              "value": 0.98
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000631"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward"
        }
      ],
      "recovery": "Stop and observe fresh geometry. If point-029 is lost or the leg is rejected, re-track a visible floor landmark and choose a new short leg; abort if no safe reference remains.",
      "plan_id": "plan-0032",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_030",
          "description": "Commit a short forward leg along the freshly tracked floor reference point-030 (bearing -0.0015 rad, range 1.10 m, essentially dead ahead); endpoint is reduced range <= 0.85 m, then inspect the new view for blue A / green B candidates.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-030.range_m",
              "op": "le",
              "value": 0.85
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000648"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_030"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_030"
        }
      ],
      "recovery": "Stop and observe fresh geometry. If point-030 is lost or the leg is rejected, re-track a visible floor landmark and choose a new short leg in a different direction; abort if no safe reference remains.",
      "plan_id": "plan-0033",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward_031",
          "description": "Commit a short forward leg along the freshly tracked floor reference point-031 (bearing -0.08 rad, range 1.11 m, essentially ahead); endpoint is point-031 range <= 0.85 m, then inspect the new view for blue A / green B candidates.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-031.range_m",
              "op": "le",
              "value": 0.85
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000661"
          ]
        }
      ],
      "branches": [
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward_031"
        },
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward_031"
        }
      ],
      "recovery": "Stop and observe fresh geometry. If point-031 is lost or the leg is rejected, re-track a visible floor landmark and choose a new short leg in a different direction; abort if no safe reference remains.",
      "plan_id": "plan-0034",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_viewpoint_032",
          "description": "Commit a short leg toward the freshly tracked floor reference point-032 (bearing -0.37 rad right of forward, range 1.34 m) by moving forward and slightly right; endpoint is point-032.range_m <= 0.85 m, then inspect the new view for blue A / green B candidates and cabinet clearance.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-032.range_m",
              "op": "le",
              "value": 0.85
            }
          ],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000683"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_viewpoint_032"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_viewpoint_032"
        }
      ],
      "recovery": "Stop and observe fresh geometry. If point-032 is lost or the leg is rejected, re-track a visible floor landmark and commit a new short leg in a different direction; abort if no safe reference remains.",
      "plan_id": "plan-0035",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_viewpoint_034",
          "description": "Commit a 0.5 m forward-right leg along freshly tracked floor reference point-033 (bearing -0.14 rad right of forward, range 1.89 m) into the open floor ahead; endpoint point-033.range_m <= 1.45 m, then inspect the new view for blue A / green B candidates.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "point-033.range_m",
              "op": "le",
              "value": 1.45
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
          "subgoal_id": "explore_viewpoint_034"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_viewpoint_034"
        }
      ],
      "recovery": "Stop, observe fresh geometry; if point-033 is lost or the leg is rejected, re-track a visible floor landmark and commit a short leg in a different direction; abort if no safe reference remains.",
      "plan_id": "plan-0036",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "shift_south_viewpoint",
          "description": "North edge is boundary-blocked, so shift viewpoint south-west: lateral-left 0.35 m plus 0.25 m backward along tracked floor reference point-033, leaving the north support margin to get a fresh view for blue A / green B.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.y_m",
              "op": "le",
              "value": 5.35
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000704"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "shift_south_viewpoint"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "shift_south_viewpoint"
        }
      ],
      "recovery": "Stop and observe fresh geometry; if point-033 is lost or this lateral leg is rejected, re-track a visible floor landmark and commit a short leg in a different direction; abort if no safe reference remains.",
      "plan_id": "plan-0037",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward",
          "description": "Commit to a forward leg along tracked floor reference point-034 (bearing -0.06 rad, range 1.18 m) to leave the current blocked north-area viewpoint and expose areas where blue A / green B may be occluded; endpoint ~0.45 m closer along that ray.",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "le",
              "value": -3.1
            }
          ],
          "active": false,
          "status": "已完成",
          "evidence_ids": [
            "e000716"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "explore_forward"
        }
      ],
      "recovery": "Stop; observe fresh geometry. If point-034 is lost or this leg is rejected, re-track a visible floor landmark and commit a short leg in a different direction; abort if no safe reference remains.",
      "plan_id": "plan-0038",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left",
          "description": "Rotate left 0.5 rad from yaw 3.05 to sweep the un-viewed left sector for blue A / green B color candidates; keep tracked floor reference point-035 (range 1.13 m, bearing -0.05) in view as a stability check",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.yaw_rad",
              "op": "ge",
              "value": 3.45
            }
          ],
          "active": true,
          "status": "进行中",
          "evidence_ids": [
            "e000736"
          ]
        },
        {
          "subgoal_id": "advance_west",
          "description": "Commit a ~0.45 m translation along the newly observed free floor ray at the post-scan heading (roughly west, x decreasing) to a local endpoint verified by a re-tracked floor point with range <= 0.8 m, moving away from the cabinet side",
          "preconditions": [],
          "completion": [
            {
              "measurement": "pose.x_m",
              "op": "le",
              "value": -3.5
            }
          ],
          "active": true,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "advance_west"
        },
        {
          "on": "search_review_due",
          "subgoal_id": "scan_left"
        }
      ],
      "recovery": "Stop; observe fresh geometry and candidate list. If no target color appears, re-track a visible floor landmark in the new sector and commit a short leg in a different direction; abort if no safe reference remains.",
      "plan_id": "plan-0039",
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
        "call_id": "call_27e1e95a7af4498681982f22",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000012",
      "kind": "plan_rejected",
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
      "value": 0.0
    },
    {
      "evidence_id": "e000014",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.y_m",
      "value": 0.0
    },
    {
      "evidence_id": "e000015",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.yaw_rad",
      "value": 0.0
    },
    {
      "evidence_id": "e000016",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 2,
      "name": "point-001.range_m",
      "value": 1.8874
    },
    {
      "evidence_id": "e000017",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 2,
      "name": "point-001.bearing_rad",
      "value": 0.4041
    },
    {
      "evidence_id": "e000018",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 2,
      "action": {
        "call_id": "call_bc8c2b75a94b4276bff6b01c",
        "tool": "turn",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT",
        "plan_id": "plan-0001",
        "subgoal_id": "scan_left_for_A"
      }
    },
    {
      "evidence_id": "e000019",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 2,
      "plan_id": "plan-0002"
    },
    {
      "evidence_id": "e000020",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.x_m",
      "value": 0.021733950672051968
    },
    {
      "evidence_id": "e000021",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.y_m",
      "value": 0.002238333631713014
    },
    {
      "evidence_id": "e000022",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.yaw_rad",
      "value": -0.5251498275953836
    },
    {
      "evidence_id": "e000023",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 3,
      "action": {
        "call_id": "call_3925ff082663450dba2fde54",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_right_for_A",
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
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 4,
      "action": {
        "call_id": "call_85103fe5b7624151b9b5cf4f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_left_for_A",
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
      "evidence_id": "e000028",
      "kind": "completion_invalidated",
      "source": "memory_verifier",
      "step": 4,
      "plan_id": "plan-0002",
      "subgoal_id": "scan_right_for_A"
    },
    {
      "evidence_id": "e000029",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 5,
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
      "evidence_id": "e000030",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 5,
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
      "evidence_id": "e000031",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.x_m",
      "value": 0.016467470766759758
    },
    {
      "evidence_id": "e000032",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.y_m",
      "value": -0.029697896850089854
    },
    {
      "evidence_id": "e000033",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.yaw_rad",
      "value": 0.01425524642322581
    },
    {
      "evidence_id": "e000034",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 5,
      "name": "point-002.range_m",
      "value": 1.7714
    },
    {
      "evidence_id": "e000035",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 5,
      "name": "point-002.bearing_rad",
      "value": 0.2203
    },
    {
      "evidence_id": "e000036",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 5,
      "action": {
        "call_id": "call_c44c4604063b4dd9a7052913",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000037",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.x_m",
      "value": 0.02602595929445278
    },
    {
      "evidence_id": "e000038",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.y_m",
      "value": 0.0010722378386714658
    },
    {
      "evidence_id": "e000039",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.yaw_rad",
      "value": 0.5274358290212383
    },
    {
      "evidence_id": "e000040",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 6,
      "action": {
        "call_id": "call_722822fd89e9417886363f34",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_left_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.009996138340712338,
            0.030630754316077372
          ],
          "yaw_delta_rad": 0.5131805825980127,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000041",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 7,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.728800401934947,
            0.3835962991607721
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
            442.0,
            183.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000042",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 7,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.728800401934947,
            0.3835962991607721
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
            442.0,
            183.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00004",
          "position_m": [
            0.5275757195336888,
            0.015073591986676821,
            1.3427088260650635
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
      "evidence_id": "e000043",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.x_m",
      "value": 0.02602595929445278
    },
    {
      "evidence_id": "e000044",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.y_m",
      "value": 0.0010722378386714658
    },
    {
      "evidence_id": "e000045",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.yaw_rad",
      "value": 0.5274358290212383
    },
    {
      "evidence_id": "e000046",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 7,
      "name": "point-003.range_m",
      "value": 1.7452
    },
    {
      "evidence_id": "e000047",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 7,
      "name": "point-003.bearing_rad",
      "value": -0.3065
    },
    {
      "evidence_id": "e000048",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 7,
      "action": {
        "call_id": "call_f765e58af5e74228af615fd2",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000049",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 8,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7356391368358615,
            0.44804829979320715
          ]
        },
        "pose_covariance": null,
        "confidence": 0.889,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00005",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00005",
          "pixel_uv": [
            453.3,
            188.64
          ]
        }
      }
    },
    {
      "evidence_id": "e000050",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 8,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7356391368358615,
            0.44804829979320715
          ]
        },
        "pose_covariance": null,
        "confidence": 0.889,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00005",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00005",
          "pixel_uv": [
            453.3,
            188.64
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00005",
          "position_m": [
            0.49022117863197606,
            0.034884653161076945,
            1.144837737083435
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
      "evidence_id": "e000051",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.x_m",
      "value": 0.22347482066740512
    },
    {
      "evidence_id": "e000052",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.y_m",
      "value": 0.13046797781656938
    },
    {
      "evidence_id": "e000053",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.yaw_rad",
      "value": 0.5299051838192056
    },
    {
      "evidence_id": "e000054",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 8,
      "name": "point-003.range_m",
      "value": 1.5452
    },
    {
      "evidence_id": "e000055",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 8,
      "name": "point-003.bearing_rad",
      "value": -0.3229
    },
    {
      "evidence_id": "e000056",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 8,
      "action": {
        "call_id": "call_83427de5aa1a4d419c813545",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "advance_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23574303399091118,
            0.012431102391308693
          ],
          "yaw_delta_rad": 0.0024693547979675046,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000057",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 9,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7356391368358615,
            0.44804829979320715
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
            453.3,
            188.64
          ]
        }
      }
    },
    {
      "evidence_id": "e000058",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 9,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7356391368358615,
            0.44804829979320715
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
            453.3,
            188.64
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00006",
          "position_m": [
            0.49022117863197606,
            0.034884653161076945,
            1.144837737083435
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
      "evidence_id": "e000059",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.x_m",
      "value": 0.22347482066740512
    },
    {
      "evidence_id": "e000060",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.y_m",
      "value": 0.13046797781656938
    },
    {
      "evidence_id": "e000061",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.yaw_rad",
      "value": 0.5299051838192056
    },
    {
      "evidence_id": "e000062",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-003.range_m",
      "value": 1.5452
    },
    {
      "evidence_id": "e000063",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-003.bearing_rad",
      "value": -0.3229
    },
    {
      "evidence_id": "e000064",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 9,
      "action": {
        "call_id": "call_d197c187cb5c44fd881190e7",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000065",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.x_m",
      "value": 0.22347482066740512
    },
    {
      "evidence_id": "e000066",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.y_m",
      "value": 0.13046797781656938
    },
    {
      "evidence_id": "e000067",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.yaw_rad",
      "value": 0.5299051838192056
    },
    {
      "evidence_id": "e000068",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-003.range_m",
      "value": 1.5452
    },
    {
      "evidence_id": "e000069",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-003.bearing_rad",
      "value": -0.3229
    },
    {
      "evidence_id": "e000070",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 10,
      "action": {
        "call_id": "call_9b5b50d7b658458fa26ab562",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000071",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 11,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8591060019182373,
            0.534754314018822
          ]
        },
        "pose_covariance": null,
        "confidence": 0.998,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00007",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00007",
          "pixel_uv": [
            471.95,
            189.64
          ]
        }
      }
    },
    {
      "evidence_id": "e000072",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 11,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8591060019182373,
            0.534754314018822
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
            471.95,
            189.64
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00007",
          "position_m": [
            0.513297122663529,
            0.03534176910142331,
            1.0493783950805664
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
      "evidence_id": "e000073",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 11,
      "object_id": "point-001",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000074",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.x_m",
      "value": 0.42203611572376415
    },
    {
      "evidence_id": "e000075",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.y_m",
      "value": 0.26321068549293675
    },
    {
      "evidence_id": "e000076",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.yaw_rad",
      "value": 0.5447089497438881
    },
    {
      "evidence_id": "e000077",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-003.range_m",
      "value": 1.4625
    },
    {
      "evidence_id": "e000078",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 11,
      "name": "point-003.bearing_rad",
      "value": -0.358
    },
    {
      "evidence_id": "e000079",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 11,
      "action": {
        "call_id": "call_2ef420dfe11240aaab850977",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "advance_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2384246109278561,
            0.014174598393338483
          ],
          "yaw_delta_rad": 0.014803765924682466,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000080",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 11,
      "plan_id": "plan-0003"
    },
    {
      "evidence_id": "e000081",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.x_m",
      "value": 0.41265735142505494
    },
    {
      "evidence_id": "e000082",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.y_m",
      "value": 0.2836542176520081
    },
    {
      "evidence_id": "e000083",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.yaw_rad",
      "value": 1.0435280296058527
    },
    {
      "evidence_id": "e000084",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 12,
      "action": {
        "call_id": "call_a4a84bf0eee24cfbab345366",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "sweep_left_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.002571756279904332,
            0.022344692804925712
          ],
          "yaw_delta_rad": 0.4988190798619647,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000085",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 12,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 12,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 1,
      "recent_action_evidence_ids": [
        "e000084"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000086",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 12,
      "plan_id": "plan-0004"
    },
    {
      "evidence_id": "e000087",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.x_m",
      "value": 0.41721757922870456
    },
    {
      "evidence_id": "e000088",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.y_m",
      "value": 0.2997799407719288
    },
    {
      "evidence_id": "e000089",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.yaw_rad",
      "value": 0.49579464441754173
    },
    {
      "evidence_id": "e000090",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 13,
      "action": {
        "call_id": "call_efe3a96082664fe38db6d515",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "reacquire_B_ref",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01623019553518051,
            0.004173173450904134
          ],
          "yaw_delta_rad": -0.547733385188311,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000091",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 14,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000092",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 14,
      "object_id": "point-003",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000093",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.x_m",
      "value": 0.6535916735234555
    },
    {
      "evidence_id": "e000094",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.y_m",
      "value": 0.3746864423939287
    },
    {
      "evidence_id": "e000095",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.yaw_rad",
      "value": 0.4885585585913181
    },
    {
      "evidence_id": "e000096",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 14,
      "action": {
        "call_id": "call_9d412c5b3b424d808ea006b1",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "advance_right_front",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.24354784154686512,
            -0.046563347353616724
          ],
          "yaw_delta_rad": -0.007236085826223704,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000097",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 15,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.489378930374773,
            0.24233612096510126
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
            562.0,
            277.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000098",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 15,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.489378930374773,
            0.24233612096510126
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
            562.0,
            277.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00010",
          "position_m": [
            0.9741590474995114,
            0.39167219435547374,
            1.252423644065857
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
      "evidence_id": "e000099",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 15,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.8591060019182373,
          0.534754314018822
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          2.489378930374773,
          0.24233612096510126
        ]
      },
      "evidence_ids": [
        "e000098"
      ]
    },
    {
      "evidence_id": "e000100",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 15,
      "object_id": "point-002",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000101",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.x_m",
      "value": 0.6535916735234555
    },
    {
      "evidence_id": "e000102",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.y_m",
      "value": 0.3746864423939287
    },
    {
      "evidence_id": "e000103",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.yaw_rad",
      "value": 0.4885585585913181
    },
    {
      "evidence_id": "e000104",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-004.range_m",
      "value": 1.8406
    },
    {
      "evidence_id": "e000105",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 15,
      "name": "point-004.bearing_rad",
      "value": -0.5605
    },
    {
      "evidence_id": "e000106",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 15,
      "action": {
        "call_id": "call_891433569eda49c5af210ea3",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000107",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 15,
      "plan_id": "plan-0005"
    },
    {
      "evidence_id": "e000108",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.x_m",
      "value": 0.8987771346664764
    },
    {
      "evidence_id": "e000109",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.y_m",
      "value": 0.520390117346234
    },
    {
      "evidence_id": "e000110",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.yaw_rad",
      "value": 0.501824891852831
    },
    {
      "evidence_id": "e000111",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 16,
      "action": {
        "call_id": "call_36342ee9ebba4fb687bf8a06",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0005",
        "subgoal_id": "advance_right_sector",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2848878326352132,
            0.013579177697252115
          ],
          "yaw_delta_rad": 0.01326633326151283,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000112",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 17,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.879679245289256,
            0.6707707656217894
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
            493.0,
            198.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000113",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 17,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.879679245289256,
            0.6707707656217894
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
            493.0,
            198.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00011",
          "position_m": [
            0.3405004701994302,
            0.036306966563051636,
            0.6118590235710144
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
      "evidence_id": "e000114",
      "kind": "relocation_candidate_rejected",
      "source": "memory_rules",
      "step": 17,
      "object_id": "task:B",
      "rejected_pose": {
        "frame": "episode_start",
        "position_m": [
          2.489378930374773,
          0.24233612096510126
        ]
      },
      "supporting_observation": "e000113"
    },
    {
      "evidence_id": "e000115",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 17,
      "object_id": "point-003",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000116",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.x_m",
      "value": 0.8987771346664764
    },
    {
      "evidence_id": "e000117",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.y_m",
      "value": 0.520390117346234
    },
    {
      "evidence_id": "e000118",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.yaw_rad",
      "value": 0.501824891852831
    },
    {
      "evidence_id": "e000119",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-005.range_m",
      "value": 0.9923
    },
    {
      "evidence_id": "e000120",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 17,
      "name": "point-005.bearing_rad",
      "value": -0.3497
    },
    {
      "evidence_id": "e000121",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 17,
      "action": {
        "call_id": "call_cd557436a8de4fec80250b92",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000122",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 17,
      "plan_id": "plan-0006"
    },
    {
      "evidence_id": "e000123",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.x_m",
      "value": 0.8974472612168194
    },
    {
      "evidence_id": "e000124",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.y_m",
      "value": 0.546561315619512
    },
    {
      "evidence_id": "e000125",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.yaw_rad",
      "value": 0.10915941175047705
    },
    {
      "evidence_id": "e000126",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 18,
      "action": {
        "call_id": "call_86ab7fbdb4d148059f94dfde",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_right_sector",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011423124609913089,
            0.023584155838141364
          ],
          "yaw_delta_rad": -0.3926654801023539,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000127",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 19,
      "observation": {
        "object_id": "point-006",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.2846073305590298,
            0.9118565825235814
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
            259.0,
            289.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000128",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 19,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.2846073305590298,
            0.9118565825235814
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
            259.0,
            289.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00012",
          "position_m": [
            -0.21553650499005222,
            0.3901032610976978,
            1.1107046604156494
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
      "evidence_id": "e000129",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.x_m",
      "value": 0.8974472612168194
    },
    {
      "evidence_id": "e000130",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.y_m",
      "value": 0.546561315619512
    },
    {
      "evidence_id": "e000131",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.yaw_rad",
      "value": 0.10915941175047705
    },
    {
      "evidence_id": "e000132",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-006.range_m",
      "value": 1.4345
    },
    {
      "evidence_id": "e000133",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 19,
      "name": "point-006.bearing_rad",
      "value": 0.1483
    },
    {
      "evidence_id": "e000134",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 19,
      "action": {
        "call_id": "call_4284576a01d5482a92b8a5d3",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000135",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 19,
      "plan_id": "plan-0007"
    },
    {
      "evidence_id": "e000136",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.x_m",
      "value": 1.0886821772153072
    },
    {
      "evidence_id": "e000137",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.y_m",
      "value": 0.5827978953897881
    },
    {
      "evidence_id": "e000138",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.yaw_rad",
      "value": 0.12766976036336028
    },
    {
      "evidence_id": "e000139",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 20,
      "action": {
        "call_id": "call_ca907e3df177464faf194b85",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "advance_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.19404440339330806,
            0.015187242084441444
          ],
          "yaw_delta_rad": 0.018510348612883032,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000140",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 21,
      "object_id": "point-003",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000141",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.x_m",
      "value": 1.0865915280487164
    },
    {
      "evidence_id": "e000142",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.y_m",
      "value": 0.5989060647539545
    },
    {
      "evidence_id": "e000143",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.yaw_rad",
      "value": 0.5757107203856642
    },
    {
      "evidence_id": "e000144",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 21,
      "action": {
        "call_id": "call_2c9eaec624524a1fb90f86f8",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "scan_left_sector",
        "motion_feedback": {
          "translation_start_frame_m": [
            -2.2690032194801202e-05,
            0.016243257658637152
          ],
          "yaw_delta_rad": 0.4480409600223041,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000145",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 22,
      "observation": {
        "object_id": "point-007",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7353943796406988,
            0.7414044498890575
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
            561.0,
            222.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000146",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 22,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7353943796406988,
            0.7414044498890575
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
            561.0,
            222.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00014",
          "position_m": [
            0.23359096527450596,
            0.041108140886817815,
            0.30155882239341736
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
      "evidence_id": "e000147",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 22,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          2.2846073305590298,
          0.9118565825235814
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7353943796406988,
          0.7414044498890575
        ]
      },
      "evidence_ids": [
        "e000146"
      ]
    },
    {
      "evidence_id": "e000148",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.x_m",
      "value": 1.0865915280487164
    },
    {
      "evidence_id": "e000149",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.y_m",
      "value": 0.5989060647539545
    },
    {
      "evidence_id": "e000150",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.yaw_rad",
      "value": 0.5757107203856642
    },
    {
      "evidence_id": "e000151",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-007.range_m",
      "value": 0.6642
    },
    {
      "evidence_id": "e000152",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-007.bearing_rad",
      "value": -0.3595
    },
    {
      "evidence_id": "e000153",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 22,
      "action": {
        "call_id": "call_3cd4876e91f7484ba0494146",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000154",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 22,
      "plan_id": "plan-0008"
    },
    {
      "evidence_id": "e000155",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.x_m",
      "value": 1.096221538074728
    },
    {
      "evidence_id": "e000156",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.y_m",
      "value": 0.614384249680125
    },
    {
      "evidence_id": "e000157",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.yaw_rad",
      "value": 1.1200305078496542
    },
    {
      "evidence_id": "e000158",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 23,
      "action": {
        "call_id": "call_f6b2ef8f0910416c8fc25780",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0008",
        "subgoal_id": "scan_left_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.016504511110328947,
            0.007740311022100467
          ],
          "yaw_delta_rad": 0.5443197874639902,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000159",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 24,
      "observation": {
        "object_id": "point-008",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.5303128350410302,
            1.7226730414208486
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
            284.0,
            327.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000160",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.x_m",
      "value": 1.096221538074728
    },
    {
      "evidence_id": "e000161",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.y_m",
      "value": 0.614384249680125
    },
    {
      "evidence_id": "e000162",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.yaw_rad",
      "value": 1.1200305078496542
    },
    {
      "evidence_id": "e000163",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-008.range_m",
      "value": 1.1903
    },
    {
      "evidence_id": "e000164",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 24,
      "name": "point-008.bearing_rad",
      "value": 0.0774
    },
    {
      "evidence_id": "e000165",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 24,
      "action": {
        "call_id": "call_c6d0bfe15fe44a2ba499965b",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000166",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 24,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 24,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 2,
      "recent_action_evidence_ids": [
        "e000165"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000167",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 25,
      "observation": {
        "object_id": "point-008",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.5334245961567703,
            1.8912895989407292
          ]
        },
        "pose_covariance": null,
        "confidence": 0.994,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00016",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00016",
          "pixel_uv": [
            265.48,
            333.16
          ]
        }
      }
    },
    {
      "evidence_id": "e000168",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 25,
      "object_id": "point-004",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000169",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.x_m",
      "value": 1.1746522743330783
    },
    {
      "evidence_id": "e000170",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.y_m",
      "value": 0.7878295357335298
    },
    {
      "evidence_id": "e000171",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.yaw_rad",
      "value": 1.1366207405987154
    },
    {
      "evidence_id": "e000172",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-008.range_m",
      "value": 1.1603
    },
    {
      "evidence_id": "e000173",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-008.bearing_rad",
      "value": 0.1198
    },
    {
      "evidence_id": "e000174",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 25,
      "action": {
        "call_id": "call_d4a94620999542d0b9f7767d",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0008",
        "subgoal_id": "advance_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.19028922528843983,
            0.004965720823777331
          ],
          "yaw_delta_rad": 0.01659023274906124,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000175",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.x_m",
      "value": 1.2658222372152863
    },
    {
      "evidence_id": "e000176",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.y_m",
      "value": 1.0097254283749542
    },
    {
      "evidence_id": "e000177",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.yaw_rad",
      "value": 1.1575956607178153
    },
    {
      "evidence_id": "e000178",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 26,
      "action": {
        "call_id": "call_e86bcabfffbb4b759b05c1b1",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0008",
        "subgoal_id": "advance_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23965955509830117,
            0.01063235407434003
          ],
          "yaw_delta_rad": 0.02097492011909985,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000179",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 27,
      "object_id": "point-005",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000180",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.x_m",
      "value": 1.2658222372152863
    },
    {
      "evidence_id": "e000181",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.y_m",
      "value": 1.0097254283749542
    },
    {
      "evidence_id": "e000182",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.yaw_rad",
      "value": 1.1575956607178153
    },
    {
      "evidence_id": "e000183",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 27,
      "action": {
        "call_id": "call_367428a093cd4b74b0728234",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000184",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 28,
      "observation": {
        "object_id": "point-009",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.6195457040555363,
            2.054083182694093
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00017",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00017",
          "pixel_uv": [
            279.0,
            348.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000185",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 28,
      "object_id": "point-008",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000186",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.x_m",
      "value": 1.2658222372152863
    },
    {
      "evidence_id": "e000187",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.y_m",
      "value": 1.0097254283749542
    },
    {
      "evidence_id": "e000188",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.yaw_rad",
      "value": 1.1575956607178153
    },
    {
      "evidence_id": "e000189",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-009.range_m",
      "value": 1.1026
    },
    {
      "evidence_id": "e000190",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 28,
      "name": "point-009.bearing_rad",
      "value": 0.0866
    },
    {
      "evidence_id": "e000191",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 28,
      "action": {
        "call_id": "call_4a64f14c0cbc4360a00b0658",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000192",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 29,
      "observation": {
        "object_id": "point-009",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.6195457040555363,
            2.054083182694093
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00018",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00018",
          "pixel_uv": [
            279.0,
            348.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000193",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 29,
      "object_id": "point-006",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000194",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.x_m",
      "value": 1.2658222372152863
    },
    {
      "evidence_id": "e000195",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.y_m",
      "value": 1.0097254283749542
    },
    {
      "evidence_id": "e000196",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.yaw_rad",
      "value": 1.1575956607178153
    },
    {
      "evidence_id": "e000197",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-009.range_m",
      "value": 1.1026
    },
    {
      "evidence_id": "e000198",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 29,
      "name": "point-009.bearing_rad",
      "value": 0.0866
    },
    {
      "evidence_id": "e000199",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 29,
      "action": {
        "call_id": "call_1f4808c2f0b04223bc8c30be",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000200",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 29,
      "plan_id": "plan-0009"
    },
    {
      "evidence_id": "e000201",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.x_m",
      "value": 1.2472539136630814
    },
    {
      "evidence_id": "e000202",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.y_m",
      "value": 1.0171502769480631
    },
    {
      "evidence_id": "e000203",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.yaw_rad",
      "value": 1.7073783978285737
    },
    {
      "evidence_id": "e000204",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 30,
      "action": {
        "call_id": "call_d042267954814364b00e14c2",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0009",
        "subgoal_id": "scan_left_sector",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.000655998745087997,
            0.01998701282131484
          ],
          "yaw_delta_rad": 0.5497827371107586,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000205",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 31,
      "object_id": "point-008",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000206",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.x_m",
      "value": 1.2472539136630814
    },
    {
      "evidence_id": "e000207",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.y_m",
      "value": 1.0171502769480631
    },
    {
      "evidence_id": "e000208",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.yaw_rad",
      "value": 1.7073783978285737
    },
    {
      "evidence_id": "e000209",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 31,
      "action": {
        "call_id": "call_1e3607298be9451b80a7ff6a",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000210",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 32,
      "object_id": "task:B",
      "old_state": "contradicted",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000211",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 32,
      "object_id": "point-007",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000212",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 32,
      "object_id": "point-009",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000213",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.x_m",
      "value": 1.2088350561382137
    },
    {
      "evidence_id": "e000214",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.y_m",
      "value": 1.245834958016234
    },
    {
      "evidence_id": "e000215",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.yaw_rad",
      "value": 1.7172215077901016
    },
    {
      "evidence_id": "e000216",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 32,
      "action": {
        "call_id": "call_461ce45c93db4428b6a6f29c",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0009",
        "subgoal_id": "advance_forward_explore",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23178600498986882,
            0.006923861610668144
          ],
          "yaw_delta_rad": 0.00984310996152793,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000217",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 32,
      "plan_id": "plan-0010"
    },
    {
      "evidence_id": "e000218",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.x_m",
      "value": 1.219128496089181
    },
    {
      "evidence_id": "e000219",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.y_m",
      "value": 1.2462062841667414
    },
    {
      "evidence_id": "e000220",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.yaw_rad",
      "value": 1.1845506658508087
    },
    {
      "evidence_id": "e000221",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 33,
      "action": {
        "call_id": "call_69085bfa75e145669f9e6b9d",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "sweep_right_reference",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.0011344861202676152,
            -0.010237466990283611
          ],
          "yaw_delta_rad": -0.5326708419392929,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000222",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 34,
      "observation": {
        "object_id": "point-010",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.5468313270989786,
            2.3787941282424954
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
            275.0,
            340.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000223",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.x_m",
      "value": 1.219128496089181
    },
    {
      "evidence_id": "e000224",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.y_m",
      "value": 1.2462062841667414
    },
    {
      "evidence_id": "e000225",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.yaw_rad",
      "value": 1.1845506658508087
    },
    {
      "evidence_id": "e000226",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-010.range_m",
      "value": 1.1791
    },
    {
      "evidence_id": "e000227",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 34,
      "name": "point-010.bearing_rad",
      "value": 0.1046
    },
    {
      "evidence_id": "e000228",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 34,
      "action": {
        "call_id": "call_089a0b8640a143ae8c1515c5",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000229",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 35,
      "object_id": "point-008",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000230",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 35,
      "object_id": "point-009",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000231",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.x_m",
      "value": 1.3458846448787498
    },
    {
      "evidence_id": "e000232",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.y_m",
      "value": 1.544410227608032
    },
    {
      "evidence_id": "e000233",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.yaw_rad",
      "value": 1.1940681324837192
    },
    {
      "evidence_id": "e000234",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 35,
      "action": {
        "call_id": "call_099a9ae0bcb4451e963c102d",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "advance_toward_reference",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.32398595729312,
            -0.0050806118490050595
          ],
          "yaw_delta_rad": 0.009517466632910754,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000235",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 36,
      "observation": {
        "object_id": "point-011",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7980792642809966,
            2.7178460870326777
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
            317.0,
            329.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000236",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.x_m",
      "value": 1.3458846448787498
    },
    {
      "evidence_id": "e000237",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.y_m",
      "value": 1.544410227608032
    },
    {
      "evidence_id": "e000238",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.yaw_rad",
      "value": 1.1940681324837192
    },
    {
      "evidence_id": "e000239",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-011.range_m",
      "value": 1.2576
    },
    {
      "evidence_id": "e000240",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-011.bearing_rad",
      "value": 0.0089
    },
    {
      "evidence_id": "e000241",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 36,
      "action": {
        "call_id": "call_0d45c23197404a7eb0e35543",
        "tool": "track_point",
        "status": "succeeded"
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
      "kind": "plan_rejected",
      "source": "planning_harness",
      "step": 36,
      "plan_id": "plan-0011"
    },
    {
      "evidence_id": "e000244",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.x_m",
      "value": 1.3458846448787498
    },
    {
      "evidence_id": "e000245",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.y_m",
      "value": 1.544410227608032
    },
    {
      "evidence_id": "e000246",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.yaw_rad",
      "value": 1.1940681324837192
    },
    {
      "evidence_id": "e000247",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-011.range_m",
      "value": 1.2576
    },
    {
      "evidence_id": "e000248",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 37,
      "name": "point-011.bearing_rad",
      "value": 0.0089
    },
    {
      "evidence_id": "e000249",
      "kind": "action_failed",
      "source": "execution_feedback",
      "step": 37,
      "action": {
        "call_id": "call_dd46e6913e77467689f848bd",
        "tool": "move_relative",
        "status": "failed",
        "error_code": "MEMORY_CONSTRAINT",
        "plan_id": "plan-0011",
        "subgoal_id": "advance_forward_leg"
      }
    },
    {
      "evidence_id": "e000250",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 37,
      "plan_id": "plan-0012"
    },
    {
      "evidence_id": "e000251",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.x_m",
      "value": 1.4569073452480954
    },
    {
      "evidence_id": "e000252",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.y_m",
      "value": 1.8557144457422494
    },
    {
      "evidence_id": "e000253",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.yaw_rad",
      "value": 1.1950663711521947
    },
    {
      "evidence_id": "e000254",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 38,
      "action": {
        "call_id": "call_152ef14be67a4b8b928599fa",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0012",
        "subgoal_id": "explore_forward_leg",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3303165025592661,
            0.011285582061735341
          ],
          "yaw_delta_rad": 0.0009982386684752598,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000255",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 39,
      "observation": {
        "object_id": "point-012",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8907049218691772,
            2.872567351780127
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
            329.0,
            350.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000256",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 39,
      "object_id": "point-009",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000257",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.x_m",
      "value": 1.4569073452480954
    },
    {
      "evidence_id": "e000258",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.y_m",
      "value": 1.8557144457422494
    },
    {
      "evidence_id": "e000259",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.yaw_rad",
      "value": 1.1950663711521947
    },
    {
      "evidence_id": "e000260",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-012.range_m",
      "value": 1.1055
    },
    {
      "evidence_id": "e000261",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-012.bearing_rad",
      "value": -0.0275
    },
    {
      "evidence_id": "e000262",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 39,
      "action": {
        "call_id": "call_1c43b87b71b1428cba4325e6",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000263",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 39,
      "plan_id": "plan-0013"
    },
    {
      "evidence_id": "e000264",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.x_m",
      "value": 1.5326754184569467
    },
    {
      "evidence_id": "e000265",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.y_m",
      "value": 2.079851838647066
    },
    {
      "evidence_id": "e000266",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.yaw_rad",
      "value": 1.212864874989325
    },
    {
      "evidence_id": "e000267",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 40,
      "action": {
        "call_id": "call_60658df88c064fd38cfe919c",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "explore_forward_leg",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23630479121050452,
            0.011765095278405774
          ],
          "yaw_delta_rad": 0.01779850383713022,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000268",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.x_m",
      "value": 1.5326754184569467
    },
    {
      "evidence_id": "e000269",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.y_m",
      "value": 2.079851838647066
    },
    {
      "evidence_id": "e000270",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.yaw_rad",
      "value": 1.212864874989325
    },
    {
      "evidence_id": "e000271",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 41,
      "action": {
        "call_id": "call_94d9596595a14404a9de13a7",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000272",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 42,
      "observation": {
        "object_id": "point-013",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8958930493076283,
            3.121413590363794
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00025",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00025",
          "pixel_uv": [
            308.0,
            351.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000273",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.x_m",
      "value": 1.5326754184569467
    },
    {
      "evidence_id": "e000274",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.y_m",
      "value": 2.079851838647066
    },
    {
      "evidence_id": "e000275",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.yaw_rad",
      "value": 1.212864874989325
    },
    {
      "evidence_id": "e000276",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-013.range_m",
      "value": 1.1031
    },
    {
      "evidence_id": "e000277",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-013.bearing_rad",
      "value": 0.0224
    },
    {
      "evidence_id": "e000278",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 42,
      "action": {
        "call_id": "call_c1433818012c46bc9f8f5a24",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000279",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 42,
      "plan_id": "plan-0014"
    },
    {
      "evidence_id": "e000280",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 43,
      "observation": {
        "object_id": "point-013",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8998921326265916,
            3.2884268788203914
          ]
        },
        "pose_covariance": null,
        "confidence": 0.994,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00026",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00026",
          "pixel_uv": [
            294.61,
            351.03
          ]
        }
      }
    },
    {
      "evidence_id": "e000281",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.x_m",
      "value": 1.5929209152784323
    },
    {
      "evidence_id": "e000282",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.y_m",
      "value": 2.2595497959189452
    },
    {
      "evidence_id": "e000283",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.yaw_rad",
      "value": 1.229881192949021
    },
    {
      "evidence_id": "e000284",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-013.range_m",
      "value": 1.0737
    },
    {
      "evidence_id": "e000285",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 43,
      "name": "point-013.bearing_rad",
      "value": 0.0509
    },
    {
      "evidence_id": "e000286",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 43,
      "action": {
        "call_id": "call_100050f827d2430cbd63d518",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0014",
        "subgoal_id": "explore_forward_leg2",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.18941559150229367,
            0.006527589967967401
          ],
          "yaw_delta_rad": 0.017016317959695826,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000287",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 44,
      "object_id": "point-010",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000288",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.x_m",
      "value": 1.674463083405626
    },
    {
      "evidence_id": "e000289",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.y_m",
      "value": 2.5272564818356944
    },
    {
      "evidence_id": "e000290",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.yaw_rad",
      "value": 1.2481092164157592
    },
    {
      "evidence_id": "e000291",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 44,
      "action": {
        "call_id": "call_fc73396eddb54cf384b75460",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0014",
        "subgoal_id": "explore_forward_leg2",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.27956352069520324,
            0.012658308098449242
          ],
          "yaw_delta_rad": 0.018228023466738463,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000292",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.x_m",
      "value": 1.7064484196395031
    },
    {
      "evidence_id": "e000293",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.y_m",
      "value": 2.6596326021134638
    },
    {
      "evidence_id": "e000294",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.yaw_rad",
      "value": 1.274922281506357
    },
    {
      "evidence_id": "e000295",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 45,
      "action": {
        "call_id": "call_f660f50720d74118ad136e38",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0014",
        "subgoal_id": "explore_forward_leg2",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.13568681991706708,
            0.011644133912918065
          ],
          "yaw_delta_rad": 0.026813065090597554,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000296",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 46,
      "object_id": "point-011",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000297",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 46,
      "object_id": "point-013",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000298",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.x_m",
      "value": 1.7064484196395031
    },
    {
      "evidence_id": "e000299",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.y_m",
      "value": 2.6596326021134638
    },
    {
      "evidence_id": "e000300",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.yaw_rad",
      "value": 1.274922281506357
    },
    {
      "evidence_id": "e000301",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 46,
      "action": {
        "call_id": "call_625a68d98bce400a9d3d5e2a",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000302",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.x_m",
      "value": 1.7064484196395031
    },
    {
      "evidence_id": "e000303",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.y_m",
      "value": 2.6596326021134638
    },
    {
      "evidence_id": "e000304",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.yaw_rad",
      "value": 1.274922281506357
    },
    {
      "evidence_id": "e000305",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 47,
      "action": {
        "call_id": "call_d560584d960e474c839d6eaa",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000306",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 47,
      "plan_id": "plan-0015"
    },
    {
      "evidence_id": "e000307",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.x_m",
      "value": 1.7078939950753165
    },
    {
      "evidence_id": "e000308",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.y_m",
      "value": 2.6585591404094218
    },
    {
      "evidence_id": "e000309",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.yaw_rad",
      "value": 1.814466665598913
    },
    {
      "evidence_id": "e000310",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 48,
      "action": {
        "call_id": "call_0d9a19bb06a24861a62c6e8e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0015",
        "subgoal_id": "scan_left_sector",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.000605322135134559,
            -0.0016957574954537021
          ],
          "yaw_delta_rad": 0.5395443840925562,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000311",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 48,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 48,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 4,
      "recent_action_evidence_ids": [
        "e000310"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000312",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 49,
      "observation": {
        "object_id": "point-014",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.4896702362016716,
            3.722849345693233
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00029",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00029",
          "pixel_uv": [
            337.0,
            352.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000313",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 49,
      "object_id": "point-012",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000314",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 49,
      "object_id": "point-013",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000315",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.x_m",
      "value": 1.7078939950753165
    },
    {
      "evidence_id": "e000316",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.y_m",
      "value": 2.6585591404094218
    },
    {
      "evidence_id": "e000317",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.yaw_rad",
      "value": 1.814466665598913
    },
    {
      "evidence_id": "e000318",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 49,
      "name": "point-014.range_m",
      "value": 1.0864
    },
    {
      "evidence_id": "e000319",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 49,
      "name": "point-014.bearing_rad",
      "value": -0.0414
    },
    {
      "evidence_id": "e000320",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 49,
      "action": {
        "call_id": "call_a73e9f4b2b72408faed77f6a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000321",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 49,
      "plan_id": "plan-0016"
    },
    {
      "evidence_id": "e000322",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.x_m",
      "value": 1.6240376992930008
    },
    {
      "evidence_id": "e000323",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.y_m",
      "value": 2.9357151406378663
    },
    {
      "evidence_id": "e000324",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.yaw_rad",
      "value": 1.8184613188120968
    },
    {
      "evidence_id": "e000325",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 50,
      "action": {
        "call_id": "call_f84b77b6b8824c71adf24fd5",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0016",
        "subgoal_id": "advance_past_initial_area",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.28920021687738406,
            0.014510732684277036
          ],
          "yaw_delta_rad": 0.0039946532131835966,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000326",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.x_m",
      "value": 1.6240376992930008
    },
    {
      "evidence_id": "e000327",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.y_m",
      "value": 2.9357151406378663
    },
    {
      "evidence_id": "e000328",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.yaw_rad",
      "value": 1.8184613188120968
    },
    {
      "evidence_id": "e000329",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 51,
      "action": {
        "call_id": "call_4684aad3c4884e439ea18b7c",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000330",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 52,
      "observation": {
        "object_id": "point-015",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.4075503718674622,
            4.127200481321564
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00031",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00031",
          "pixel_uv": [
            347.0,
            330.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000331",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.x_m",
      "value": 1.6240376992930008
    },
    {
      "evidence_id": "e000332",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.y_m",
      "value": 2.9357151406378663
    },
    {
      "evidence_id": "e000333",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.yaw_rad",
      "value": 1.8184613188120968
    },
    {
      "evidence_id": "e000334",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 52,
      "name": "point-015.range_m",
      "value": 1.211
    },
    {
      "evidence_id": "e000335",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 52,
      "name": "point-015.bearing_rad",
      "value": -0.0679
    },
    {
      "evidence_id": "e000336",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 52,
      "action": {
        "call_id": "call_b1121bf6e0a94fbebe9099db",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000337",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 53,
      "observation": {
        "object_id": "point-015",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.4075503718674622,
            4.127200481321564
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
            347.0,
            330.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000338",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 53,
      "object_id": "point-013",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000339",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.x_m",
      "value": 1.6240376992930008
    },
    {
      "evidence_id": "e000340",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.y_m",
      "value": 2.9357151406378663
    },
    {
      "evidence_id": "e000341",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.yaw_rad",
      "value": 1.8184613188120968
    },
    {
      "evidence_id": "e000342",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 53,
      "name": "point-015.range_m",
      "value": 1.211
    },
    {
      "evidence_id": "e000343",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 53,
      "name": "point-015.bearing_rad",
      "value": -0.0679
    },
    {
      "evidence_id": "e000344",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 53,
      "action": {
        "call_id": "call_bc53bd81438e47f79cd05cfe",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000345",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 53,
      "plan_id": "plan-0017"
    },
    {
      "evidence_id": "e000346",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.x_m",
      "value": 1.5921332406763653
    },
    {
      "evidence_id": "e000347",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.y_m",
      "value": 2.939651322859865
    },
    {
      "evidence_id": "e000348",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.yaw_rad",
      "value": 2.361462854528176
    },
    {
      "evidence_id": "e000349",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 54,
      "action": {
        "call_id": "call_430a16ee38dc41178daef56b",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0017",
        "subgoal_id": "scan_left_sector",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011637166041958014,
            0.029966053737809424
          ],
          "yaw_delta_rad": 0.5430015357160789,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000350",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.x_m",
      "value": 1.5921332406763653
    },
    {
      "evidence_id": "e000351",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.y_m",
      "value": 2.939651322859865
    },
    {
      "evidence_id": "e000352",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.yaw_rad",
      "value": 2.361462854528176
    },
    {
      "evidence_id": "e000353",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 55,
      "action": {
        "call_id": "call_bd154d07730c4119b230bded",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000354",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 56,
      "object_id": "point-015",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000355",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.x_m",
      "value": 1.5921332406763653
    },
    {
      "evidence_id": "e000356",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.y_m",
      "value": 2.939651322859865
    },
    {
      "evidence_id": "e000357",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.yaw_rad",
      "value": 2.361462854528176
    },
    {
      "evidence_id": "e000358",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 56,
      "action": {
        "call_id": "call_d71ac1f425f2419fbda87b0a",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000359",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 57,
      "observation": {
        "object_id": "point-016",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.816808425439323,
            3.726122944011987
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00034",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00034",
          "pixel_uv": [
            325.0,
            356.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000360",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.x_m",
      "value": 1.5921332406763653
    },
    {
      "evidence_id": "e000361",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.y_m",
      "value": 2.939651322859865
    },
    {
      "evidence_id": "e000362",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.yaw_rad",
      "value": 2.361462854528176
    },
    {
      "evidence_id": "e000363",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 57,
      "name": "point-016.range_m",
      "value": 1.1044
    },
    {
      "evidence_id": "e000364",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 57,
      "name": "point-016.bearing_rad",
      "value": -0.0124
    },
    {
      "evidence_id": "e000365",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 57,
      "action": {
        "call_id": "call_d576bde4b28247f8be45f86a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000366",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 57,
      "plan_id": "plan-0018"
    },
    {
      "evidence_id": "e000367",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.x_m",
      "value": 1.4488592354538683
    },
    {
      "evidence_id": "e000368",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.y_m",
      "value": 3.058425066394553
    },
    {
      "evidence_id": "e000369",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.yaw_rad",
      "value": 2.364794646462942
    },
    {
      "evidence_id": "e000370",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 58,
      "action": {
        "call_id": "call_4a2d9a87f77b43cfac78a50f",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0018",
        "subgoal_id": "translate_forward_probe",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.18538443895205242,
            0.016347859804046058
          ],
          "yaw_delta_rad": 0.0033317919347659597,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000371",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 59,
      "observation": {
        "object_id": "point-017",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.5767000658940684,
            3.820921225698166
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
            292.0,
            338.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000372",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 59,
      "object_id": "point-014",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000373",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 59,
      "object_id": "point-015",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000374",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.x_m",
      "value": 1.4488592354538683
    },
    {
      "evidence_id": "e000375",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.y_m",
      "value": 3.058425066394553
    },
    {
      "evidence_id": "e000376",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.yaw_rad",
      "value": 2.364794646462942
    },
    {
      "evidence_id": "e000377",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 59,
      "name": "point-017.range_m",
      "value": 1.1585
    },
    {
      "evidence_id": "e000378",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 59,
      "name": "point-017.bearing_rad",
      "value": 0.0584
    },
    {
      "evidence_id": "e000379",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 59,
      "action": {
        "call_id": "call_0b810910239946b286dc2cc9",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000380",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 59,
      "plan_id": "plan-0019"
    },
    {
      "evidence_id": "e000381",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.x_m",
      "value": 1.306264868957284
    },
    {
      "evidence_id": "e000382",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.y_m",
      "value": 3.1828484801915025
    },
    {
      "evidence_id": "e000383",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.yaw_rad",
      "value": 2.3883422881383276
    },
    {
      "evidence_id": "e000384",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 60,
      "action": {
        "call_id": "call_d42745911a5e44669358e13f",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0019",
        "subgoal_id": "probe_forward_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.1889136010943988,
            0.011224552507579588
          ],
          "yaw_delta_rad": 0.023547641675385478,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000385",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 60,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 60,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 5,
      "recent_action_evidence_ids": [
        "e000384"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000386",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.x_m",
      "value": 1.306264868957284
    },
    {
      "evidence_id": "e000387",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.y_m",
      "value": 3.1828484801915025
    },
    {
      "evidence_id": "e000388",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.yaw_rad",
      "value": 2.3883422881383276
    },
    {
      "evidence_id": "e000389",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 61,
      "action": {
        "call_id": "call_d201f1ee7e5746a2acee8c5c",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000390",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 62,
      "observation": {
        "object_id": "point-018",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.5767937515581019,
            3.9879103528947057
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
            353.0,
            354.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000391",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.x_m",
      "value": 1.306264868957284
    },
    {
      "evidence_id": "e000392",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.y_m",
      "value": 3.1828484801915025
    },
    {
      "evidence_id": "e000393",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.yaw_rad",
      "value": 2.3883422881383276
    },
    {
      "evidence_id": "e000394",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 62,
      "name": "point-018.range_m",
      "value": 1.0864
    },
    {
      "evidence_id": "e000395",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 62,
      "name": "point-018.bearing_rad",
      "value": -0.0814
    },
    {
      "evidence_id": "e000396",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 62,
      "action": {
        "call_id": "call_5d2a840c48f24578b25699b4",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000397",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 62,
      "plan_id": "plan-0020"
    },
    {
      "evidence_id": "e000398",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 63,
      "object_id": "point-015",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000399",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.x_m",
      "value": 1.05349905032213
    },
    {
      "evidence_id": "e000400",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.y_m",
      "value": 3.4022408704741207
    },
    {
      "evidence_id": "e000401",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.yaw_rad",
      "value": 2.3958631886537827
    },
    {
      "evidence_id": "e000402",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 63,
      "action": {
        "call_id": "call_0729a43e82f8416785235720",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0020",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3344522756012231,
            0.012855167419512564
          ],
          "yaw_delta_rad": 0.0075209005154550645,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000403",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 64,
      "observation": {
        "object_id": "point-019",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.07074629371457455,
            3.9911457094593774
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
            226.0,
            342.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000404",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.x_m",
      "value": 1.05349905032213
    },
    {
      "evidence_id": "e000405",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.y_m",
      "value": 3.4022408704741207
    },
    {
      "evidence_id": "e000406",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.yaw_rad",
      "value": 2.3958631886537827
    },
    {
      "evidence_id": "e000407",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 64,
      "name": "point-019.range_m",
      "value": 1.1457
    },
    {
      "evidence_id": "e000408",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 64,
      "name": "point-019.bearing_rad",
      "value": 0.2059
    },
    {
      "evidence_id": "e000409",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 64,
      "action": {
        "call_id": "call_257e10de1246459181efdb7d",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000410",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 64,
      "plan_id": "plan-0021"
    },
    {
      "evidence_id": "e000411",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.x_m",
      "value": 0.7975542980351198
    },
    {
      "evidence_id": "e000412",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.y_m",
      "value": 3.6221919729191825
    },
    {
      "evidence_id": "e000413",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.yaw_rad",
      "value": 2.405374191547054
    },
    {
      "evidence_id": "e000414",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 65,
      "action": {
        "call_id": "call_7e450142304447de851b072e",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0021",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.33725381167378277,
            0.012085950585775884
          ],
          "yaw_delta_rad": 0.009511002893271225,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000415",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 66,
      "observation": {
        "object_id": "point-020",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.055881536041618246,
            4.381387841660406
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
            314.0,
            340.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000416",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.x_m",
      "value": 0.7975542980351198
    },
    {
      "evidence_id": "e000417",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.y_m",
      "value": 3.6221919729191825
    },
    {
      "evidence_id": "e000418",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.yaw_rad",
      "value": 2.405374191547054
    },
    {
      "evidence_id": "e000419",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 66,
      "name": "point-020.range_m",
      "value": 1.1423
    },
    {
      "evidence_id": "e000420",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 66,
      "name": "point-020.bearing_rad",
      "value": 0.0092
    },
    {
      "evidence_id": "e000421",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 66,
      "action": {
        "call_id": "call_c858a1e117574a278eec0643",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000422",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 66,
      "plan_id": "plan-0022"
    },
    {
      "evidence_id": "e000423",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 67,
      "observation": {
        "object_id": "point-020",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.2204404669400094,
            4.552146162190178
          ]
        },
        "pose_covariance": null,
        "confidence": 0.998,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00039",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00039",
          "pixel_uv": [
            327.42,
            339.33
          ]
        }
      }
    },
    {
      "evidence_id": "e000424",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 67,
      "object_id": "point-016",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000425",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.x_m",
      "value": 0.615169054594075
    },
    {
      "evidence_id": "e000426",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.y_m",
      "value": 3.776935618194821
    },
    {
      "evidence_id": "e000427",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.yaw_rad",
      "value": 2.417450605340254
    },
    {
      "evidence_id": "e000428",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 67,
      "name": "point-020.range_m",
      "value": 1.1398
    },
    {
      "evidence_id": "e000429",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 67,
      "name": "point-020.bearing_rad",
      "value": -0.0238
    },
    {
      "evidence_id": "e000430",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 67,
      "action": {
        "call_id": "call_af37fd464b43447183ff2df1",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0022",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23905875341826194,
            0.007802896407639939
          ],
          "yaw_delta_rad": 0.012076413793200125,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000431",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 68,
      "observation": {
        "object_id": "point-020",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.308300625446137,
            4.641301880433053
          ]
        },
        "pose_covariance": null,
        "confidence": 0.64,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00040",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00040",
          "pixel_uv": [
            343.92,
            355.24
          ]
        }
      }
    },
    {
      "evidence_id": "e000432",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.x_m",
      "value": 0.47323758562976814
    },
    {
      "evidence_id": "e000433",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.y_m",
      "value": 3.8852227611417756
    },
    {
      "evidence_id": "e000434",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.yaw_rad",
      "value": 2.4320085121475503
    },
    {
      "evidence_id": "e000435",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 68,
      "name": "point-020.range_m",
      "value": 1.0874
    },
    {
      "evidence_id": "e000436",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 68,
      "name": "point-020.bearing_rad",
      "value": -0.0592
    },
    {
      "evidence_id": "e000437",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 68,
      "action": {
        "call_id": "call_a9d8db6512f945babe33569d",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0022",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.17805581021240707,
            0.012914165074968245
          ],
          "yaw_delta_rad": 0.014557906807296295,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000438",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 69,
      "observation": {
        "object_id": "point-020",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.39229286487421955,
            4.726486778640571
          ]
        },
        "pose_covariance": null,
        "confidence": 0.957,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00041",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00041",
          "pixel_uv": [
            365.22,
            358.47
          ]
        }
      }
    },
    {
      "evidence_id": "e000439",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 69,
      "object_id": "point-017",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000440",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.x_m",
      "value": 0.3641343017100792
    },
    {
      "evidence_id": "e000441",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.y_m",
      "value": 3.961735876939076
    },
    {
      "evidence_id": "e000442",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.yaw_rad",
      "value": 2.4585873795593747
    },
    {
      "evidence_id": "e000443",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 69,
      "name": "point-020.range_m",
      "value": 1.0756
    },
    {
      "evidence_id": "e000444",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 69,
      "name": "point-020.bearing_rad",
      "value": -0.1079
    },
    {
      "evidence_id": "e000445",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 69,
      "action": {
        "call_id": "call_437c1ee1c5964a68abfeb69c",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0022",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.13261903706501502,
            0.013037425321724298
          ],
          "yaw_delta_rad": 0.02657886741182436,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000446",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.x_m",
      "value": 0.21021225138670563
    },
    {
      "evidence_id": "e000447",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.y_m",
      "value": 4.076689198799754
    },
    {
      "evidence_id": "e000448",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.yaw_rad",
      "value": 2.476539840430794
    },
    {
      "evidence_id": "e000449",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 70,
      "action": {
        "call_id": "call_154da4e7eeff43f39a557a90",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0022",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.19194432649595913,
            0.007977424933407654
          ],
          "yaw_delta_rad": 0.01795246087141944,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000450",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.x_m",
      "value": 0.21021225138670563
    },
    {
      "evidence_id": "e000451",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.y_m",
      "value": 4.076689198799754
    },
    {
      "evidence_id": "e000452",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.yaw_rad",
      "value": 2.476539840430794
    },
    {
      "evidence_id": "e000453",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 71,
      "action": {
        "call_id": "call_ad6d67a66b6d460a96f69bfb",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000454",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 72,
      "observation": {
        "object_id": "point-021",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.7496732058632827,
            4.754992286629952
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
            296.0,
            329.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000455",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 72,
      "object_id": "point-018",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000456",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.x_m",
      "value": 0.21021225138670563
    },
    {
      "evidence_id": "e000457",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.y_m",
      "value": 4.076689198799754
    },
    {
      "evidence_id": "e000458",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.yaw_rad",
      "value": 2.476539840430794
    },
    {
      "evidence_id": "e000459",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 72,
      "name": "point-021.range_m",
      "value": 1.1754
    },
    {
      "evidence_id": "e000460",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 72,
      "name": "point-021.bearing_rad",
      "value": 0.0499
    },
    {
      "evidence_id": "e000461",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 72,
      "action": {
        "call_id": "call_7a8bb41e64a746c4b28e6e12",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000462",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 72,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 72,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 6,
      "recent_action_evidence_ids": [
        "e000461"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000463",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 72,
      "plan_id": "plan-0023"
    },
    {
      "evidence_id": "e000464",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.x_m",
      "value": 0.02045376434614552
    },
    {
      "evidence_id": "e000465",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.y_m",
      "value": 4.209888475898483
    },
    {
      "evidence_id": "e000466",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.yaw_rad",
      "value": 2.504333702259613
    },
    {
      "evidence_id": "e000467",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 73,
      "action": {
        "call_id": "call_84568b28ab61463488a70e05",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0023",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23151532035061811,
            0.012287687597634725
          ],
          "yaw_delta_rad": 0.027793861828818933,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000468",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 74,
      "object_id": "point-019",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000469",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.x_m",
      "value": 0.02045376434614552
    },
    {
      "evidence_id": "e000470",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.y_m",
      "value": 4.209888475898483
    },
    {
      "evidence_id": "e000471",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.yaw_rad",
      "value": 2.504333702259613
    },
    {
      "evidence_id": "e000472",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 74,
      "action": {
        "call_id": "call_ea3d71fcbf3b422590e7b724",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000473",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.x_m",
      "value": 0.02045376434614552
    },
    {
      "evidence_id": "e000474",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.y_m",
      "value": 4.209888475898483
    },
    {
      "evidence_id": "e000475",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.yaw_rad",
      "value": 2.504333702259613
    },
    {
      "evidence_id": "e000476",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 75,
      "action": {
        "call_id": "call_8b90a86945f94646829817ab",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000477",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.x_m",
      "value": 0.02045376434614552
    },
    {
      "evidence_id": "e000478",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.y_m",
      "value": 4.209888475898483
    },
    {
      "evidence_id": "e000479",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.yaw_rad",
      "value": 2.504333702259613
    },
    {
      "evidence_id": "e000480",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 76,
      "action": {
        "call_id": "call_ace04f6265f34ce28ada5f2c",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000481",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.x_m",
      "value": 0.02045376434614552
    },
    {
      "evidence_id": "e000482",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.y_m",
      "value": 4.209888475898483
    },
    {
      "evidence_id": "e000483",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.yaw_rad",
      "value": 2.504333702259613
    },
    {
      "evidence_id": "e000484",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 77,
      "action": {
        "call_id": "call_0d908001304e40bcab049373",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000485",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 78,
      "observation": {
        "object_id": "point-022",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.9971585496445659,
            4.92639037988372
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00044",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00044",
          "pixel_uv": [
            308.0,
            323.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000486",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.x_m",
      "value": 0.02045376434614552
    },
    {
      "evidence_id": "e000487",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.y_m",
      "value": 4.209888475898483
    },
    {
      "evidence_id": "e000488",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.yaw_rad",
      "value": 2.504333702259613
    },
    {
      "evidence_id": "e000489",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 78,
      "name": "point-022.range_m",
      "value": 1.2446
    },
    {
      "evidence_id": "e000490",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 78,
      "name": "point-022.bearing_rad",
      "value": 0.0238
    },
    {
      "evidence_id": "e000491",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 78,
      "action": {
        "call_id": "call_f7935b17287b43af97738fe1",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000492",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 78,
      "plan_id": "plan-0024"
    },
    {
      "evidence_id": "e000493",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 79,
      "object_id": "point-020",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000494",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.x_m",
      "value": -0.1739347355600402
    },
    {
      "evidence_id": "e000495",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.y_m",
      "value": 4.346572096715512
    },
    {
      "evidence_id": "e000496",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.yaw_rad",
      "value": 2.525718238093573
    },
    {
      "evidence_id": "e000497",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 79,
      "action": {
        "call_id": "call_b7d024aef3dd4652ae549ec0",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0024",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23756182631657233,
            0.005803427656598914
          ],
          "yaw_delta_rad": 0.02138453583396016,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000498",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 80,
      "observation": {
        "object_id": "point-023",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.162499357054927,
            4.930407586497242
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
            282.0,
            337.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000499",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.x_m",
      "value": -0.1739347355600402
    },
    {
      "evidence_id": "e000500",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.y_m",
      "value": 4.346572096715512
    },
    {
      "evidence_id": "e000501",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.yaw_rad",
      "value": 2.525718238093573
    },
    {
      "evidence_id": "e000502",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-023.range_m",
      "value": 1.1481
    },
    {
      "evidence_id": "e000503",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-023.bearing_rad",
      "value": 0.0824
    },
    {
      "evidence_id": "e000504",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 80,
      "action": {
        "call_id": "call_e629738f4c13458b94792617",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000505",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 80,
      "plan_id": "plan-0025"
    },
    {
      "evidence_id": "e000506",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.x_m",
      "value": -0.37413625282071106
    },
    {
      "evidence_id": "e000507",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.y_m",
      "value": 4.47949036404372
    },
    {
      "evidence_id": "e000508",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.yaw_rad",
      "value": 2.546186031117186
    },
    {
      "evidence_id": "e000509",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 81,
      "action": {
        "call_id": "call_1fa9b577e8ea420caaa4bca1",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0025",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.24020144678034644,
            0.007153898771723302
          ],
          "yaw_delta_rad": 0.020467793023613012,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000510",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 82,
      "observation": {
        "object_id": "point-024",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.4006530436238418,
            5.024249511006157
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00046",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00046",
          "pixel_uv": [
            271.0,
            334.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000511",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 82,
      "object_id": "point-021",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000512",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.x_m",
      "value": -0.37413625282071106
    },
    {
      "evidence_id": "e000513",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.y_m",
      "value": 4.47949036404372
    },
    {
      "evidence_id": "e000514",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.yaw_rad",
      "value": 2.546186031117186
    },
    {
      "evidence_id": "e000515",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 82,
      "name": "point-024.range_m",
      "value": 1.1621
    },
    {
      "evidence_id": "e000516",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 82,
      "name": "point-024.bearing_rad",
      "value": 0.1075
    },
    {
      "evidence_id": "e000517",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 82,
      "action": {
        "call_id": "call_84b70780317745038bf6d091",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000518",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 82,
      "plan_id": "plan-0026"
    },
    {
      "evidence_id": "e000519",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.x_m",
      "value": -0.6108719147250697
    },
    {
      "evidence_id": "e000520",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.y_m",
      "value": 4.62541258116028
    },
    {
      "evidence_id": "e000521",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.yaw_rad",
      "value": 2.5653556317870794
    },
    {
      "evidence_id": "e000522",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 83,
      "action": {
        "call_id": "call_d1ebc343682747a3a2c0265f",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0026",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2778381229124114,
            0.011960122157188488
          ],
          "yaw_delta_rad": 0.01916960066989315,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000523",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.x_m",
      "value": -0.6108719147250697
    },
    {
      "evidence_id": "e000524",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.y_m",
      "value": 4.62541258116028
    },
    {
      "evidence_id": "e000525",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.yaw_rad",
      "value": 2.5653556317870794
    },
    {
      "evidence_id": "e000526",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 84,
      "action": {
        "call_id": "call_ec1b2b9d460d4b0587079037",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000527",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 84,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 84,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 7,
      "recent_action_evidence_ids": [
        "e000526"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000528",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.x_m",
      "value": -0.6108719147250697
    },
    {
      "evidence_id": "e000529",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.y_m",
      "value": 4.62541258116028
    },
    {
      "evidence_id": "e000530",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.yaw_rad",
      "value": 2.5653556317870794
    },
    {
      "evidence_id": "e000531",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 85,
      "action": {
        "call_id": "call_37b4713357244385bbfa2e42",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000532",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.x_m",
      "value": -0.6108719147250697
    },
    {
      "evidence_id": "e000533",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.y_m",
      "value": 4.62541258116028
    },
    {
      "evidence_id": "e000534",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.yaw_rad",
      "value": 2.5653556317870794
    },
    {
      "evidence_id": "e000535",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 86,
      "action": {
        "call_id": "call_3127402871224be9a2b0775b",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000536",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 87,
      "observation": {
        "object_id": "point-025",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.6600272791097146,
            5.189330537411828
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
            283.0,
            334.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000537",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.x_m",
      "value": -0.6108719147250697
    },
    {
      "evidence_id": "e000538",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.y_m",
      "value": 4.62541258116028
    },
    {
      "evidence_id": "e000539",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.yaw_rad",
      "value": 2.5653556317870794
    },
    {
      "evidence_id": "e000540",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 87,
      "name": "point-025.range_m",
      "value": 1.1911
    },
    {
      "evidence_id": "e000541",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 87,
      "name": "point-025.bearing_rad",
      "value": 0.0831
    },
    {
      "evidence_id": "e000542",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 87,
      "action": {
        "call_id": "call_bde5ddb0ad6446d6ad966643",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000543",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 87,
      "plan_id": "plan-0027"
    },
    {
      "evidence_id": "e000544",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 88,
      "object_id": "point-022",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000545",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.x_m",
      "value": -0.8954007623523099
    },
    {
      "evidence_id": "e000546",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.y_m",
      "value": 4.798613758053458
    },
    {
      "evidence_id": "e000547",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.yaw_rad",
      "value": 2.574817334512757
    },
    {
      "evidence_id": "e000548",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 88,
      "action": {
        "call_id": "call_b24a3205af1a4a4290d51d8b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0027",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3329553771173746,
            0.009799472327334774
          ],
          "yaw_delta_rad": 0.00946170272567759,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000549",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.x_m",
      "value": -0.8954007623523099
    },
    {
      "evidence_id": "e000550",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.y_m",
      "value": 4.798613758053458
    },
    {
      "evidence_id": "e000551",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.yaw_rad",
      "value": 2.574817334512757
    },
    {
      "evidence_id": "e000552",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 89,
      "action": {
        "call_id": "call_ece949957a534916acb3f20b",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000553",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 90,
      "object_id": "point-023",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000554",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.x_m",
      "value": -0.8954007623523099
    },
    {
      "evidence_id": "e000555",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.y_m",
      "value": 4.798613758053458
    },
    {
      "evidence_id": "e000556",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.yaw_rad",
      "value": 2.574817334512757
    },
    {
      "evidence_id": "e000557",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 90,
      "action": {
        "call_id": "call_2645526633eb4d9eb0074a6e",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000558",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.x_m",
      "value": -0.8954007623523099
    },
    {
      "evidence_id": "e000559",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.y_m",
      "value": 4.798613758053458
    },
    {
      "evidence_id": "e000560",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.yaw_rad",
      "value": 2.574817334512757
    },
    {
      "evidence_id": "e000561",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 91,
      "action": {
        "call_id": "call_c200a3ff6b3c4b999f08c15f",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000562",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 92,
      "observation": {
        "object_id": "point-026",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.9053067197668578,
            5.359794911673753
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
            291.0,
            338.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000563",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 92,
      "object_id": "point-024",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000564",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.x_m",
      "value": -0.8954007623523099
    },
    {
      "evidence_id": "e000565",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.y_m",
      "value": 4.798613758053458
    },
    {
      "evidence_id": "e000566",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.yaw_rad",
      "value": 2.574817334512757
    },
    {
      "evidence_id": "e000567",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 92,
      "name": "point-026.range_m",
      "value": 1.1553
    },
    {
      "evidence_id": "e000568",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 92,
      "name": "point-026.bearing_rad",
      "value": 0.0596
    },
    {
      "evidence_id": "e000569",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 92,
      "action": {
        "call_id": "call_427d80d9e12c4144bc730816",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000570",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 92,
      "plan_id": "plan-0028"
    },
    {
      "evidence_id": "e000571",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.x_m",
      "value": -1.18471459008503
    },
    {
      "evidence_id": "e000572",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.y_m",
      "value": 4.965490317817206
    },
    {
      "evidence_id": "e000573",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.yaw_rad",
      "value": 2.5820697954395917
    },
    {
      "evidence_id": "e000574",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 93,
      "action": {
        "call_id": "call_ac1bf2700fac4640bd6d1073",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0028",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3336741988979879,
            0.014553559898794088
          ],
          "yaw_delta_rad": 0.007252460926834736,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000575",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 94,
      "observation": {
        "object_id": "point-027",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.066289648867524,
            5.612945872842138
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
            349.0,
            352.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000576",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.x_m",
      "value": -1.18471459008503
    },
    {
      "evidence_id": "e000577",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.y_m",
      "value": 4.965490317817206
    },
    {
      "evidence_id": "e000578",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.yaw_rad",
      "value": 2.5820697954395917
    },
    {
      "evidence_id": "e000579",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 94,
      "name": "point-027.range_m",
      "value": 1.0938
    },
    {
      "evidence_id": "e000580",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 94,
      "name": "point-027.bearing_rad",
      "value": -0.0739
    },
    {
      "evidence_id": "e000581",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 94,
      "action": {
        "call_id": "call_972cb77ae3814dde92aac766",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000582",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.x_m",
      "value": -1.18471459008503
    },
    {
      "evidence_id": "e000583",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.y_m",
      "value": 4.965490317817206
    },
    {
      "evidence_id": "e000584",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.yaw_rad",
      "value": 2.5820697954395917
    },
    {
      "evidence_id": "e000585",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 95,
      "name": "point-027.range_m",
      "value": 1.0938
    },
    {
      "evidence_id": "e000586",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 95,
      "name": "point-027.bearing_rad",
      "value": -0.0739
    },
    {
      "evidence_id": "e000587",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 95,
      "action": {
        "call_id": "call_7a2886f62bb6460992b16d80",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000588",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 95,
      "plan_id": "plan-0029"
    },
    {
      "evidence_id": "e000589",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.x_m",
      "value": -1.5018208376941404
    },
    {
      "evidence_id": "e000590",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.y_m",
      "value": 5.178544978896899
    },
    {
      "evidence_id": "e000591",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.yaw_rad",
      "value": 2.5863282551350553
    },
    {
      "evidence_id": "e000592",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 96,
      "action": {
        "call_id": "call_c07c4321a69e462faafd218c",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0029",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3818357822087754,
            -0.012251379739690232
          ],
          "yaw_delta_rad": 0.004258459695463568,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000593",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 96,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 96,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 8,
      "recent_action_evidence_ids": [
        "e000592"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000594",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 97,
      "observation": {
        "object_id": "point-028",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.5597188685698162,
            6.031478813534362
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00051",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00051",
          "pixel_uv": [
            368.0,
            310.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000595",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 97,
      "object_id": "point-025",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000596",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.x_m",
      "value": -1.5018208376941404
    },
    {
      "evidence_id": "e000597",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.y_m",
      "value": 5.178544978896899
    },
    {
      "evidence_id": "e000598",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.yaw_rad",
      "value": 2.5863282551350553
    },
    {
      "evidence_id": "e000599",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 97,
      "name": "point-028.range_m",
      "value": 1.359
    },
    {
      "evidence_id": "e000600",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 97,
      "name": "point-028.bearing_rad",
      "value": -0.1233
    },
    {
      "evidence_id": "e000601",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 97,
      "action": {
        "call_id": "call_0fa8ca9c6736472298306108",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000602",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 97,
      "plan_id": "plan-0030"
    },
    {
      "evidence_id": "e000603",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.x_m",
      "value": -1.8321300886173977
    },
    {
      "evidence_id": "e000604",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.y_m",
      "value": 5.369931462667858
    },
    {
      "evidence_id": "e000605",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.yaw_rad",
      "value": 2.5927973588799955
    },
    {
      "evidence_id": "e000606",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 98,
      "action": {
        "call_id": "call_074e7670be424676aa15467c",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0030",
        "subgoal_id": "advance_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.38157677705516707,
            0.011495678661401776
          ],
          "yaw_delta_rad": 0.006469103744940252,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000607",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.x_m",
      "value": -1.8321300886173977
    },
    {
      "evidence_id": "e000608",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.y_m",
      "value": 5.369931462667858
    },
    {
      "evidence_id": "e000609",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.yaw_rad",
      "value": 2.5927973588799955
    },
    {
      "evidence_id": "e000610",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 99,
      "action": {
        "call_id": "call_19ecf8c6bc9042f091587c3c",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000611",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 100,
      "observation": {
        "object_id": "point-029",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.721659348505104,
            6.037023147373663
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00052",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00052",
          "pixel_uv": [
            358.0,
            349.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000612",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.x_m",
      "value": -1.8321300886173977
    },
    {
      "evidence_id": "e000613",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.y_m",
      "value": 5.369931462667858
    },
    {
      "evidence_id": "e000614",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.yaw_rad",
      "value": 2.5927973588799955
    },
    {
      "evidence_id": "e000615",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 100,
      "name": "point-029.range_m",
      "value": 1.1118
    },
    {
      "evidence_id": "e000616",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 100,
      "name": "point-029.bearing_rad",
      "value": -0.0947
    },
    {
      "evidence_id": "e000617",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 100,
      "action": {
        "call_id": "call_9b70738c5b6c466aac6f869d",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000618",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 100,
      "plan_id": "plan-0031"
    },
    {
      "evidence_id": "e000619",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 101,
      "observation": {
        "object_id": "point-029",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.8969703052549733,
            6.037607986794931
          ]
        },
        "pose_covariance": null,
        "confidence": 0.344,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00053",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00053",
          "pixel_uv": [
            503.56,
            337.07
          ]
        }
      }
    },
    {
      "evidence_id": "e000620",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.x_m",
      "value": -1.8325472122218531
    },
    {
      "evidence_id": "e000621",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.y_m",
      "value": 5.371493815636708
    },
    {
      "evidence_id": "e000622",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.yaw_rad",
      "value": 2.993616932835844
    },
    {
      "evidence_id": "e000623",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 101,
      "name": "point-029.range_m",
      "value": 1.2557
    },
    {
      "evidence_id": "e000624",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 101,
      "name": "point-029.bearing_rad",
      "value": -0.4112
    },
    {
      "evidence_id": "e000625",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 101,
      "action": {
        "call_id": "call_5ffed4c23be34bc093253a12",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0031",
        "subgoal_id": "scan_left",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0011708872509583568,
            -0.0011153304201943276
          ],
          "yaw_delta_rad": 0.40081957395584844,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000626",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 101,
      "plan_id": "plan-0032"
    },
    {
      "evidence_id": "e000627",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 102,
      "object_id": "point-026",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000628",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.x_m",
      "value": -2.065437842671732
    },
    {
      "evidence_id": "e000629",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.y_m",
      "value": 5.396979166706218
    },
    {
      "evidence_id": "e000630",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.yaw_rad",
      "value": 3.002095167060644
    },
    {
      "evidence_id": "e000631",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 102,
      "action": {
        "call_id": "call_6c885bec0cb04affad9170f0",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0032",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23410296365645095,
            0.009129692094719113
          ],
          "yaw_delta_rad": 0.008478234224800207,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000632",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.x_m",
      "value": -2.065437842671732
    },
    {
      "evidence_id": "e000633",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.y_m",
      "value": 5.396979166706218
    },
    {
      "evidence_id": "e000634",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.yaw_rad",
      "value": 3.002095167060644
    },
    {
      "evidence_id": "e000635",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 103,
      "action": {
        "call_id": "call_cacc304412314ed3abb2fbab",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000636",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 104,
      "observation": {
        "object_id": "point-030",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -3.1503568569768223,
            5.5510287119806865
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00055",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00055",
          "pixel_uv": [
            317.0,
            350.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000637",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 104,
      "object_id": "point-027",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000638",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.x_m",
      "value": -2.065437842671732
    },
    {
      "evidence_id": "e000639",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.y_m",
      "value": 5.396979166706218
    },
    {
      "evidence_id": "e000640",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.yaw_rad",
      "value": 3.002095167060644
    },
    {
      "evidence_id": "e000641",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 104,
      "name": "point-030.range_m",
      "value": 1.0958
    },
    {
      "evidence_id": "e000642",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 104,
      "name": "point-030.bearing_rad",
      "value": -0.0015
    },
    {
      "evidence_id": "e000643",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 104,
      "action": {
        "call_id": "call_f4d3c6e951364ae09427e33f",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000644",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 104,
      "plan_id": "plan-0033"
    },
    {
      "evidence_id": "e000645",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.x_m",
      "value": -2.301395625182384
    },
    {
      "evidence_id": "e000646",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.y_m",
      "value": 5.418750458871489
    },
    {
      "evidence_id": "e000647",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.yaw_rad",
      "value": 3.0183819250955923
    },
    {
      "evidence_id": "e000648",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 105,
      "action": {
        "call_id": "call_e311db13d552419dad69b390",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0033",
        "subgoal_id": "explore_forward_030",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2366928872813506,
            0.011249062196810333
          ],
          "yaw_delta_rad": 0.016286758034948168,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000649",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 106,
      "observation": {
        "object_id": "point-031",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -3.3898595350664107,
            5.643223523803514
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00056",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00056",
          "pixel_uv": [
            353.0,
            351.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000650",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.x_m",
      "value": -2.301395625182384
    },
    {
      "evidence_id": "e000651",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.y_m",
      "value": 5.418750458871489
    },
    {
      "evidence_id": "e000652",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.yaw_rad",
      "value": 3.0183819250955923
    },
    {
      "evidence_id": "e000653",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 106,
      "name": "point-031.range_m",
      "value": 1.1114
    },
    {
      "evidence_id": "e000654",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 106,
      "name": "point-031.bearing_rad",
      "value": -0.0802
    },
    {
      "evidence_id": "e000655",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 106,
      "action": {
        "call_id": "call_5654152acc6b4724afcd6d7e",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000656",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 106,
      "plan_id": "plan-0034"
    },
    {
      "evidence_id": "e000657",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 107,
      "object_id": "point-028",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000658",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.x_m",
      "value": -2.533051562423348
    },
    {
      "evidence_id": "e000659",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.y_m",
      "value": 5.439684586614549
    },
    {
      "evidence_id": "e000660",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.yaw_rad",
      "value": 3.0399448863568184
    },
    {
      "evidence_id": "e000661",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 107,
      "action": {
        "call_id": "call_de53dadf44e34e07aaa47f17",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0034",
        "subgoal_id": "explore_forward_031",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2324725777226069,
            0.007694905480814394
          ],
          "yaw_delta_rad": 0.021562961261226032,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000662",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.x_m",
      "value": -2.533051562423348
    },
    {
      "evidence_id": "e000663",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.y_m",
      "value": 5.439684586614549
    },
    {
      "evidence_id": "e000664",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.yaw_rad",
      "value": 3.0399448863568184
    },
    {
      "evidence_id": "e000665",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 108,
      "action": {
        "call_id": "call_f7a858288e0246bf9615e3c3",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000666",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 108,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 108,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 9,
      "recent_action_evidence_ids": [
        "e000665"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000667",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.x_m",
      "value": -2.533051562423348
    },
    {
      "evidence_id": "e000668",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.y_m",
      "value": 5.439684586614549
    },
    {
      "evidence_id": "e000669",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.yaw_rad",
      "value": 3.0399448863568184
    },
    {
      "evidence_id": "e000670",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 109,
      "action": {
        "call_id": "call_0903675efb90458babda5cb1",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000671",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 110,
      "observation": {
        "object_id": "point-032",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -3.7221938748146157,
            6.052613955205048
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00057",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00057",
          "pixel_uv": [
            482.0,
            324.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000672",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.x_m",
      "value": -2.533051562423348
    },
    {
      "evidence_id": "e000673",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.y_m",
      "value": 5.439684586614549
    },
    {
      "evidence_id": "e000674",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.yaw_rad",
      "value": 3.0399448863568184
    },
    {
      "evidence_id": "e000675",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 110,
      "name": "point-032.range_m",
      "value": 1.3379
    },
    {
      "evidence_id": "e000676",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 110,
      "name": "point-032.bearing_rad",
      "value": -0.3743
    },
    {
      "evidence_id": "e000677",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 110,
      "action": {
        "call_id": "call_26cd3d2cad9d4e10b4992a5c",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000678",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 110,
      "plan_id": "plan-0035"
    },
    {
      "evidence_id": "e000679",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 111,
      "object_id": "point-029",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000680",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.x_m",
      "value": -2.897336932080742
    },
    {
      "evidence_id": "e000681",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.y_m",
      "value": 5.614826080472414
    },
    {
      "evidence_id": "e000682",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.yaw_rad",
      "value": 3.034364023525356
    },
    {
      "evidence_id": "e000683",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 111,
      "action": {
        "call_id": "call_f9a6c0332ff74986abecd920",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0035",
        "subgoal_id": "explore_viewpoint_032",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.38017714287404814,
            -0.13727240601561014
          ],
          "yaw_delta_rad": -0.005580862831462419,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000684",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.x_m",
      "value": -2.897336932080742
    },
    {
      "evidence_id": "e000685",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.y_m",
      "value": 5.614826080472414
    },
    {
      "evidence_id": "e000686",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.yaw_rad",
      "value": 3.034364023525356
    },
    {
      "evidence_id": "e000687",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 112,
      "action": {
        "call_id": "call_81d42e249ba248a4bbede873",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000688",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 113,
      "observation": {
        "object_id": "point-033",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -4.728712237334042,
            6.0693363128197
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00058",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00058",
          "pixel_uv": [
            369.0,
            260.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000689",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.x_m",
      "value": -2.897336932080742
    },
    {
      "evidence_id": "e000690",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.y_m",
      "value": 5.614826080472414
    },
    {
      "evidence_id": "e000691",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.yaw_rad",
      "value": 3.034364023525356
    },
    {
      "evidence_id": "e000692",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 113,
      "name": "point-033.range_m",
      "value": 1.8869
    },
    {
      "evidence_id": "e000693",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 113,
      "name": "point-033.bearing_rad",
      "value": -0.136
    },
    {
      "evidence_id": "e000694",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 113,
      "action": {
        "call_id": "call_3fb6c318be2148e39c715390",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000695",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 113,
      "plan_id": "plan-0036"
    },
    {
      "evidence_id": "e000696",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 114,
      "object_id": "point-030",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000697",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.x_m",
      "value": -2.897336932080742
    },
    {
      "evidence_id": "e000698",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.y_m",
      "value": 5.614826080472414
    },
    {
      "evidence_id": "e000699",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.yaw_rad",
      "value": 3.034364023525356
    },
    {
      "evidence_id": "e000700",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 114,
      "name": "point-033.range_m",
      "value": 1.8869
    },
    {
      "evidence_id": "e000701",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 114,
      "name": "point-033.bearing_rad",
      "value": -0.136
    },
    {
      "evidence_id": "e000702",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 114,
      "plan_id": "plan-0037"
    },
    {
      "evidence_id": "e000703",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.x_m",
      "value": -2.727799125330777
    },
    {
      "evidence_id": "e000704",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.y_m",
      "value": 5.309029545767691
    },
    {
      "evidence_id": "e000705",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.yaw_rad",
      "value": 3.052010239885927
    },
    {
      "evidence_id": "e000706",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 115,
      "action": {
        "call_id": "call_9448981640cc48d782ace28b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0037",
        "subgoal_id": "shift_south_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.20129141208687676,
            0.28589570821381144
          ],
          "yaw_delta_rad": 0.017646216360570843,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000707",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 116,
      "observation": {
        "object_id": "point-034",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -3.8955193095079497,
            5.484098879076614
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00059",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00059",
          "pixel_uv": [
            343.0,
            324.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000708",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 116,
      "object_id": "point-031",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000709",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.x_m",
      "value": -2.727799125330777
    },
    {
      "evidence_id": "e000710",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.y_m",
      "value": 5.309029545767691
    },
    {
      "evidence_id": "e000711",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.yaw_rad",
      "value": 3.052010239885927
    },
    {
      "evidence_id": "e000712",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 116,
      "name": "point-034.range_m",
      "value": 1.1808
    },
    {
      "evidence_id": "e000713",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 116,
      "name": "point-034.bearing_rad",
      "value": -0.0592
    },
    {
      "evidence_id": "e000714",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 116,
      "action": {
        "call_id": "call_0b2d1ac65ff7408bacef2adb",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000715",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 116,
      "plan_id": "plan-0038"
    },
    {
      "evidence_id": "e000716",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.x_m",
      "value": -3.1065868073869707
    },
    {
      "evidence_id": "e000717",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.y_m",
      "value": 5.335827139865666
    },
    {
      "evidence_id": "e000718",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.yaw_rad",
      "value": 3.05335263701653
    },
    {
      "evidence_id": "e000719",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 117,
      "action": {
        "call_id": "call_cd1b8b8920444947b52cb7c1",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0038",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.379666194612565,
            0.007197207469414855
          ],
          "yaw_delta_rad": 0.0013423971306032456,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000720",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.x_m",
      "value": -3.1065868073869707
    },
    {
      "evidence_id": "e000721",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.y_m",
      "value": 5.335827139865666
    },
    {
      "evidence_id": "e000722",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.yaw_rad",
      "value": 3.05335263701653
    },
    {
      "evidence_id": "e000723",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 118,
      "action": {
        "call_id": "call_9ef49d53f5134dd28405b423",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000724",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 119,
      "observation": {
        "object_id": "point-035",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -4.228937271063658,
            5.490336028557303
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00061",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00061",
          "pixel_uv": [
            340.0,
            350.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000725",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.x_m",
      "value": -3.1065868073869707
    },
    {
      "evidence_id": "e000726",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.y_m",
      "value": 5.335827139865666
    },
    {
      "evidence_id": "e000727",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.yaw_rad",
      "value": 3.05335263701653
    },
    {
      "evidence_id": "e000728",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 119,
      "name": "point-035.range_m",
      "value": 1.1329
    },
    {
      "evidence_id": "e000729",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 119,
      "name": "point-035.bearing_rad",
      "value": -0.0486
    },
    {
      "evidence_id": "e000730",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 119,
      "action": {
        "call_id": "call_4980fe9b36e54bd4965eef95",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000731",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 119,
      "plan_id": "plan-0039"
    },
    {
      "evidence_id": "e000732",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 120,
      "object_id": "point-032",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000733",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.x_m",
      "value": -3.1232582120948016
    },
    {
      "evidence_id": "e000734",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.y_m",
      "value": 5.335256083791076
    },
    {
      "evidence_id": "e000735",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.yaw_rad",
      "value": -2.7871645064789115
    },
    {
      "evidence_id": "e000736",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 120,
      "action": {
        "call_id": "call_a0b18ceafeb34872a809c98c",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0039",
        "subgoal_id": "scan_left",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.016556217895981672,
            0.002038011028772115
          ],
          "yaw_delta_rad": 0.44266816368414474,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000737",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 120,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 120,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 10,
      "recent_action_evidence_ids": [
        "e000736"
      ],
      "advisory_only": true
    }
  ]
}
```

## 操作经验

## 程序工具
