# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 120,
    "revision": 134,
    "active_plan_id": "plan-0013",
    "public_context": {
      "current_observation": {
        "image_id": "frame-00076",
        "image_size": {
          "width": 640,
          "height": 360
        },
        "tracked_points": [
          {
            "point_id": "point-040",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
            "valid": true,
            "pixel_uv": [
              306.0,
              344.0
            ],
            "relative_xy_m": [
              1.1095,
              0.0294
            ],
            "range_m": 1.1099,
            "bearing_rad": 0.0265,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-033",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
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
            "point_id": "point-034",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
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
            "point_id": "point-035",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
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
            "point_id": "point-036",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
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
            "point_id": "point-037",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
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
            "point_id": "point-038",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
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
            "point_id": "point-039",
            "image_id": "frame-00076",
            "timestamp_s": 178.36000000012353,
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
      }
    },
    "exploration": {
      "successful_turns_without_search_progress": 2,
      "turn_limit": 6,
      "stalled": false,
      "progress_basis": "successful_translation_tool_or_first_task_observation_not_motion_gt",
      "evidence_ids": [
        "e000709",
        "e000720"
      ],
      "recovery": "change_viewpoint_with_translation; inspect_geometry_or_abort_if_motion_unsupported",
      "decisions_since_task_novelty": 120,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "review_due": true,
      "review_count": 10,
      "last_review_step": 120,
      "review_evidence_id": "e000728",
      "review_semantics": "advisory_strategy_review_not_failure_or_motion_prohibition"
    }
  },
  "pose": null,
  "objects": [
    {
      "category": "unclassified_landmark",
      "object_id": "point-001",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00001",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 1,
      "evidence_ids": [
        "e000004"
      ],
      "candidate_pose": null
    },
    {
      "category": "task_target",
      "object_id": "task:B",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00064",
        "pixel_uv": [
          263.82,
          179.91
        ]
      },
      "confidence": 0.95,
      "source": "task_label_rgbd_tracking",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7337469027696255,
          0.6316866157030975
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 102,
      "evidence_ids": [
        "e000005",
        "e000018",
        "e000211",
        "e000225",
        "e000250",
        "e000394",
        "e000416",
        "e000599",
        "e000611",
        "e000621"
      ],
      "candidate_pose": null,
      "task_label": "B",
      "label_description": "绿方块",
      "camera_pose": {
        "frame": "current_camera_optical",
        "image_id": "frame-00064",
        "position_m": [
          -0.5508423536412442,
          0.004962543726497695,
          3.0943360328674316
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
      "object_id": "point-002",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00002",
        "pixel_uv": [
          405.0,
          181.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8071006378272325,
          0.4154377771249777
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 3,
      "evidence_ids": [
        "e000017"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-003",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00004",
        "pixel_uv": [
          322.0,
          343.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.022788372009614137,
          1.1589160584949378
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 6,
      "evidence_ids": [
        "e000033"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-004",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00007",
        "pixel_uv": [
          403.3,
          340.89
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.5553359624337717,
          1.3441421068558588
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 10,
      "evidence_ids": [
        "e000045",
        "e000053",
        "e000061"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-005",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00009",
        "pixel_uv": [
          380.0,
          335.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.8125627785964888,
          1.6285180832952997
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 14,
      "evidence_ids": [
        "e000085"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-006",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00010",
        "pixel_uv": [
          389.0,
          345.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.9676488445518734,
          1.8394945098413829
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 16,
      "evidence_ids": [
        "e000096"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-007",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00013",
        "pixel_uv": [
          320.0,
          327.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.904366142567864,
          1.0324580829583863
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 20,
      "evidence_ids": [
        "e000118"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-008",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00014",
        "pixel_uv": [
          334.0,
          345.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.060607873563844,
          1.031967806718583
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 22,
      "evidence_ids": [
        "e000131"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-009",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00016",
        "pixel_uv": [
          393.0,
          357.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.1503165641470483,
          0.5310635121570023
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 25,
      "evidence_ids": [
        "e000149"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-010",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00017",
        "pixel_uv": [
          283.0,
          325.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.6631584386676679,
          -0.06645025191829919
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 27,
      "evidence_ids": [
        "e000161"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-011",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00019",
        "pixel_uv": [
          315.0,
          356.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.8343063996203226,
          -0.22676625030109182
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 30,
      "evidence_ids": [
        "e000176"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-012",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00020",
        "pixel_uv": [
          308.0,
          338.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.2528045408965418,
          -0.3940875218363813
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 32,
      "evidence_ids": [
        "e000188"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-013",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00023",
        "pixel_uv": [
          122.0,
          183.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7289100234781505,
          0.385903875246704
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 36,
      "evidence_ids": [
        "e000210"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-014",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00024",
        "pixel_uv": [
          337.0,
          206.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288243559517231,
          0.3857075357724057
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 38,
      "evidence_ids": [
        "e000224"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-015",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00025",
        "pixel_uv": [
          320.0,
          250.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          0.4726381095541048,
          1.6500457265541697
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 40,
      "evidence_ids": [
        "e000236"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-016",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00026",
        "pixel_uv": [
          590.0,
          186.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          3.5585268557663294,
          0.34991380889751555
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 42,
      "evidence_ids": [
        "e000249"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-017",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00028",
        "pixel_uv": [
          321.0,
          336.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.9639845085235862,
          1.7569552678963694
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 45,
      "evidence_ids": [
        "e000267"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-018",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00030",
        "pixel_uv": [
          328.11,
          329.68
        ]
      },
      "confidence": 0.986,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.7156117709378118,
          1.9342161608521176
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 48,
      "evidence_ids": [
        "e000279",
        "e000286"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-019",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00031",
        "pixel_uv": [
          292.0,
          350.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.1354059728358505,
          1.3696798798714043
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 50,
      "evidence_ids": [
        "e000300"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-020",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00033",
        "pixel_uv": [
          323.0,
          346.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.560250147919621,
          1.0429490881321608
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 53,
      "evidence_ids": [
        "e000319"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-021",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00035",
        "pixel_uv": [
          384.01,
          347.58
        ]
      },
      "confidence": 0.698,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.650583740993593,
          0.45901551486512787
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 56,
      "evidence_ids": [
        "e000331",
        "e000339"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-022",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00036",
        "pixel_uv": [
          339.0,
          350.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.245141329154603,
          0.031158049185757267
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 58,
      "evidence_ids": [
        "e000350"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-023",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00040",
        "pixel_uv": [
          344.68,
          337.53
        ]
      },
      "confidence": 0.973,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.0064768572910603,
          -0.2395988388252921
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 63,
      "evidence_ids": [
        "e000372",
        "e000380"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-024",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00042",
        "pixel_uv": [
          293.54,
          178.24
        ]
      },
      "confidence": 0.724,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          3.5627703168735936,
          0.5466587278018553
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 66,
      "evidence_ids": [
        "e000393",
        "e000401"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-025",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00043",
        "pixel_uv": [
          486.0,
          179.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7351480619548356,
          0.7310565474983042
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 68,
      "evidence_ids": [
        "e000415"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-026",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00044",
        "pixel_uv": [
          279.0,
          352.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -0.9683462969860226,
          1.7656672927888308
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 71,
      "evidence_ids": [
        "e000436"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-027",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00047",
        "pixel_uv": [
          315.54,
          334.67
        ]
      },
      "confidence": 0.998,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.2085692480224046,
          2.3531729145180145
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 75,
      "evidence_ids": [
        "e000453",
        "e000460"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-028",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00048",
        "pixel_uv": [
          393.0,
          331.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.6188268417301654,
          2.364948594964064
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 78,
      "evidence_ids": [
        "e000476"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-029",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00049",
        "pixel_uv": [
          375.0,
          342.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.7831064536091437,
          2.531871832870544
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 80,
      "evidence_ids": [
        "e000490"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-030",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00051",
        "pixel_uv": [
          300.0,
          339.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.641952848894068,
          1.4598092294189036
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 84,
      "evidence_ids": [
        "e000513"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-031",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00054",
        "pixel_uv": [
          384.0,
          340.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.901221990145237,
          1.0495279633488135
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 88,
      "evidence_ids": [
        "e000534"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-032",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00056",
        "pixel_uv": [
          333.28,
          344.31
        ]
      },
      "confidence": 0.993,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.6626690431494624,
          0.37928903648020923
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 91,
      "evidence_ids": [
        "e000546",
        "e000554"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-033",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00059",
        "pixel_uv": [
          329.0,
          342.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.332478534316229,
          0.12559028456524743
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 95,
      "evidence_ids": [
        "e000575"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-034",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00062",
        "pixel_uv": [
          48.0,
          208.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7287948575177499,
          0.38293231850964426
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 99,
      "evidence_ids": [
        "e000598"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-035",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00064",
        "pixel_uv": [
          263.82,
          179.91
        ]
      },
      "confidence": 0.998,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7337469027696255,
          0.6316866157030975
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 102,
      "evidence_ids": [
        "e000610",
        "e000620"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-036",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00068",
        "pixel_uv": [
          316.0,
          345.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.2125597034692894,
          2.0187062918040426
        ]
      },
      "anchor_node": null,
      "state": "stale",
      "last_seen": 107,
      "evidence_ids": [
        "e000648"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-037",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00070",
        "pixel_uv": [
          400.0,
          354.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.4550934628679877,
          2.2668644114552934
        ]
      },
      "anchor_node": null,
      "state": "unknown",
      "last_seen": 111,
      "evidence_ids": [
        "e000673"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-038",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00073",
        "pixel_uv": [
          351.0,
          321.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -1.782462834853204,
          2.8555709743126543
        ]
      },
      "anchor_node": null,
      "state": "unknown",
      "last_seen": 115,
      "evidence_ids": [
        "e000694"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-039",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00075",
        "pixel_uv": [
          308.0,
          347.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.4489750409057915,
          2.5418376078295264
        ]
      },
      "anchor_node": null,
      "state": "unknown",
      "last_seen": 118,
      "evidence_ids": [
        "e000710"
      ],
      "candidate_pose": null
    },
    {
      "category": "unclassified_landmark",
      "object_id": "point-040",
      "pose_covariance": null,
      "visual_feature": {
        "image_id": "frame-00076",
        "pixel_uv": [
          306.0,
          344.0
        ]
      },
      "confidence": 1.0,
      "source": "rgbd_optical_flow",
      "pose": {
        "frame": "episode_start",
        "position_m": [
          -2.710137898414841,
          1.9601590290460116
        ]
      },
      "anchor_node": null,
      "state": "unknown",
      "last_seen": 120,
      "evidence_ids": [
        "e000721"
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
      "step": 3,
      "evidence_ids": [
        "e000018"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-2",
      "kind": "target_state_changed",
      "step": 6,
      "evidence_ids": [
        "e000034"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-3",
      "kind": "target_state_changed",
      "step": 9,
      "evidence_ids": [
        "e000053"
      ],
      "object_id": "point-004",
      "state": "confirmed"
    },
    {
      "event_id": "event-4",
      "kind": "target_state_changed",
      "step": 9,
      "evidence_ids": [
        "e000054"
      ],
      "object_id": "task:B",
      "state": "unknown"
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
        "e000077"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-8",
      "kind": "target_state_changed",
      "step": 13,
      "evidence_ids": [
        "e000078"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-9",
      "kind": "replan_required",
      "step": 13,
      "evidence_ids": [
        "e000078"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-10",
      "kind": "target_state_changed",
      "step": 13,
      "evidence_ids": [
        "e000079"
      ],
      "object_id": "point-002",
      "state": "stale"
    },
    {
      "event_id": "event-11",
      "kind": "replan_required",
      "step": 13,
      "evidence_ids": [
        "e000079"
      ],
      "object_id": "point-002",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-12",
      "kind": "target_state_changed",
      "step": 13,
      "evidence_ids": [
        "e000080"
      ],
      "object_id": "point-004",
      "state": "predicted"
    },
    {
      "event_id": "event-13",
      "kind": "target_state_changed",
      "step": 16,
      "evidence_ids": [
        "e000097"
      ],
      "object_id": "point-003",
      "state": "stale"
    },
    {
      "event_id": "event-14",
      "kind": "replan_required",
      "step": 16,
      "evidence_ids": [
        "e000097"
      ],
      "object_id": "point-003",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-15",
      "kind": "target_state_changed",
      "step": 16,
      "evidence_ids": [
        "e000098"
      ],
      "object_id": "point-004",
      "state": "unknown"
    },
    {
      "event_id": "event-16",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000119"
      ],
      "object_id": "point-004",
      "state": "stale"
    },
    {
      "event_id": "event-17",
      "kind": "replan_required",
      "step": 20,
      "evidence_ids": [
        "e000119"
      ],
      "object_id": "point-004",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-18",
      "kind": "target_state_changed",
      "step": 24,
      "evidence_ids": [
        "e000143"
      ],
      "object_id": "point-005",
      "state": "stale"
    },
    {
      "event_id": "event-19",
      "kind": "replan_required",
      "step": 24,
      "evidence_ids": [
        "e000143"
      ],
      "object_id": "point-005",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-20",
      "kind": "search_review_due",
      "step": 24,
      "evidence_ids": [
        "e000148"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-21",
      "kind": "target_state_changed",
      "step": 26,
      "evidence_ids": [
        "e000156"
      ],
      "object_id": "point-006",
      "state": "stale"
    },
    {
      "event_id": "event-22",
      "kind": "replan_required",
      "step": 26,
      "evidence_ids": [
        "e000156"
      ],
      "object_id": "point-006",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-23",
      "kind": "target_state_changed",
      "step": 30,
      "evidence_ids": [
        "e000177"
      ],
      "object_id": "point-007",
      "state": "stale"
    },
    {
      "event_id": "event-24",
      "kind": "replan_required",
      "step": 30,
      "evidence_ids": [
        "e000177"
      ],
      "object_id": "point-007",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-25",
      "kind": "target_state_changed",
      "step": 32,
      "evidence_ids": [
        "e000189"
      ],
      "object_id": "point-008",
      "state": "stale"
    },
    {
      "event_id": "event-26",
      "kind": "replan_required",
      "step": 32,
      "evidence_ids": [
        "e000189"
      ],
      "object_id": "point-008",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-27",
      "kind": "target_state_changed",
      "step": 35,
      "evidence_ids": [
        "e000205"
      ],
      "object_id": "point-009",
      "state": "stale"
    },
    {
      "event_id": "event-28",
      "kind": "replan_required",
      "step": 35,
      "evidence_ids": [
        "e000205"
      ],
      "object_id": "point-009",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-29",
      "kind": "target_state_changed",
      "step": 36,
      "evidence_ids": [
        "e000211"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-30",
      "kind": "search_review_due",
      "step": 36,
      "evidence_ids": [
        "e000218"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-31",
      "kind": "target_state_changed",
      "step": 37,
      "evidence_ids": [
        "e000219"
      ],
      "object_id": "point-010",
      "state": "stale"
    },
    {
      "event_id": "event-32",
      "kind": "replan_required",
      "step": 37,
      "evidence_ids": [
        "e000219"
      ],
      "object_id": "point-010",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-33",
      "kind": "target_state_changed",
      "step": 38,
      "evidence_ids": [
        "e000225"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-34",
      "kind": "target_state_changed",
      "step": 40,
      "evidence_ids": [
        "e000237"
      ],
      "object_id": "point-011",
      "state": "stale"
    },
    {
      "event_id": "event-35",
      "kind": "replan_required",
      "step": 40,
      "evidence_ids": [
        "e000237"
      ],
      "object_id": "point-011",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-36",
      "kind": "target_state_changed",
      "step": 41,
      "evidence_ids": [
        "e000244"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-37",
      "kind": "target_state_changed",
      "step": 42,
      "evidence_ids": [
        "e000250",
        "e000251"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-38",
      "kind": "replan_required",
      "step": 42,
      "evidence_ids": [
        "e000250"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-39",
      "kind": "target_state_changed",
      "step": 42,
      "evidence_ids": [
        "e000252"
      ],
      "object_id": "point-012",
      "state": "stale"
    },
    {
      "event_id": "event-40",
      "kind": "replan_required",
      "step": 42,
      "evidence_ids": [
        "e000252"
      ],
      "object_id": "point-012",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-41",
      "kind": "target_state_changed",
      "step": 46,
      "evidence_ids": [
        "e000274"
      ],
      "object_id": "point-013",
      "state": "stale"
    },
    {
      "event_id": "event-42",
      "kind": "replan_required",
      "step": 46,
      "evidence_ids": [
        "e000274"
      ],
      "object_id": "point-013",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-43",
      "kind": "target_state_changed",
      "step": 48,
      "evidence_ids": [
        "e000286"
      ],
      "object_id": "point-018",
      "state": "confirmed"
    },
    {
      "event_id": "event-44",
      "kind": "target_state_changed",
      "step": 48,
      "evidence_ids": [
        "e000287"
      ],
      "object_id": "point-014",
      "state": "stale"
    },
    {
      "event_id": "event-45",
      "kind": "replan_required",
      "step": 48,
      "evidence_ids": [
        "e000287"
      ],
      "object_id": "point-014",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-46",
      "kind": "search_review_due",
      "step": 48,
      "evidence_ids": [
        "e000294"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-47",
      "kind": "target_state_changed",
      "step": 50,
      "evidence_ids": [
        "e000301"
      ],
      "object_id": "point-015",
      "state": "stale"
    },
    {
      "event_id": "event-48",
      "kind": "replan_required",
      "step": 50,
      "evidence_ids": [
        "e000301"
      ],
      "object_id": "point-015",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-49",
      "kind": "target_state_changed",
      "step": 51,
      "evidence_ids": [
        "e000308"
      ],
      "object_id": "point-018",
      "state": "predicted"
    },
    {
      "event_id": "event-50",
      "kind": "target_state_changed",
      "step": 52,
      "evidence_ids": [
        "e000313"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-51",
      "kind": "replan_required",
      "step": 52,
      "evidence_ids": [
        "e000313"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-52",
      "kind": "target_state_changed",
      "step": 52,
      "evidence_ids": [
        "e000314"
      ],
      "object_id": "point-016",
      "state": "stale"
    },
    {
      "event_id": "event-53",
      "kind": "replan_required",
      "step": 52,
      "evidence_ids": [
        "e000314"
      ],
      "object_id": "point-016",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-54",
      "kind": "target_state_changed",
      "step": 54,
      "evidence_ids": [
        "e000326"
      ],
      "object_id": "point-018",
      "state": "unknown"
    },
    {
      "event_id": "event-55",
      "kind": "target_state_changed",
      "step": 55,
      "evidence_ids": [
        "e000332"
      ],
      "object_id": "point-017",
      "state": "stale"
    },
    {
      "event_id": "event-56",
      "kind": "replan_required",
      "step": 55,
      "evidence_ids": [
        "e000332"
      ],
      "object_id": "point-017",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-57",
      "kind": "target_state_changed",
      "step": 58,
      "evidence_ids": [
        "e000351"
      ],
      "object_id": "point-018",
      "state": "stale"
    },
    {
      "event_id": "event-58",
      "kind": "replan_required",
      "step": 58,
      "evidence_ids": [
        "e000351"
      ],
      "object_id": "point-018",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-59",
      "kind": "target_state_changed",
      "step": 60,
      "evidence_ids": [
        "e000362"
      ],
      "object_id": "point-019",
      "state": "stale"
    },
    {
      "event_id": "event-60",
      "kind": "replan_required",
      "step": 60,
      "evidence_ids": [
        "e000362"
      ],
      "object_id": "point-019",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-61",
      "kind": "search_review_due",
      "step": 60,
      "evidence_ids": [
        "e000367"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-62",
      "kind": "target_state_changed",
      "step": 63,
      "evidence_ids": [
        "e000380"
      ],
      "object_id": "point-023",
      "state": "confirmed"
    },
    {
      "event_id": "event-63",
      "kind": "target_state_changed",
      "step": 63,
      "evidence_ids": [
        "e000381"
      ],
      "object_id": "point-020",
      "state": "stale"
    },
    {
      "event_id": "event-64",
      "kind": "replan_required",
      "step": 63,
      "evidence_ids": [
        "e000381"
      ],
      "object_id": "point-020",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-65",
      "kind": "target_state_changed",
      "step": 65,
      "evidence_ids": [
        "e000394"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-66",
      "kind": "target_state_changed",
      "step": 66,
      "evidence_ids": [
        "e000402"
      ],
      "object_id": "point-021",
      "state": "stale"
    },
    {
      "event_id": "event-67",
      "kind": "replan_required",
      "step": 66,
      "evidence_ids": [
        "e000402"
      ],
      "object_id": "point-021",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-68",
      "kind": "target_state_changed",
      "step": 66,
      "evidence_ids": [
        "e000403"
      ],
      "object_id": "point-023",
      "state": "predicted"
    },
    {
      "event_id": "event-69",
      "kind": "target_state_changed",
      "step": 68,
      "evidence_ids": [
        "e000416",
        "e000417"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-70",
      "kind": "key_precondition_invalidated",
      "step": 68,
      "evidence_ids": [
        "e000416"
      ],
      "plan_id": "plan-0010",
      "subgoal_id": "approach_B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-71",
      "kind": "replan_required",
      "step": 68,
      "evidence_ids": [
        "e000416"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-72",
      "kind": "target_state_changed",
      "step": 68,
      "evidence_ids": [
        "e000418"
      ],
      "object_id": "point-022",
      "state": "stale"
    },
    {
      "event_id": "event-73",
      "kind": "replan_required",
      "step": 68,
      "evidence_ids": [
        "e000418"
      ],
      "object_id": "point-022",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-74",
      "kind": "target_state_changed",
      "step": 69,
      "evidence_ids": [
        "e000425"
      ],
      "object_id": "point-023",
      "state": "unknown"
    },
    {
      "event_id": "event-75",
      "kind": "search_review_due",
      "step": 72,
      "evidence_ids": [
        "e000447"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-76",
      "kind": "target_state_changed",
      "step": 73,
      "evidence_ids": [
        "e000448"
      ],
      "object_id": "point-023",
      "state": "stale"
    },
    {
      "event_id": "event-77",
      "kind": "replan_required",
      "step": 73,
      "evidence_ids": [
        "e000448"
      ],
      "object_id": "point-023",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-78",
      "kind": "target_state_changed",
      "step": 75,
      "evidence_ids": [
        "e000460"
      ],
      "object_id": "point-027",
      "state": "confirmed"
    },
    {
      "event_id": "event-79",
      "kind": "target_state_changed",
      "step": 76,
      "evidence_ids": [
        "e000467"
      ],
      "object_id": "point-024",
      "state": "stale"
    },
    {
      "event_id": "event-80",
      "kind": "replan_required",
      "step": 76,
      "evidence_ids": [
        "e000467"
      ],
      "object_id": "point-024",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-81",
      "kind": "target_state_changed",
      "step": 78,
      "evidence_ids": [
        "e000477"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-82",
      "kind": "key_precondition_invalidated",
      "step": 78,
      "evidence_ids": [
        "e000477"
      ],
      "plan_id": "plan-0010",
      "subgoal_id": "approach_B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-83",
      "kind": "replan_required",
      "step": 78,
      "evidence_ids": [
        "e000477"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-84",
      "kind": "target_state_changed",
      "step": 78,
      "evidence_ids": [
        "e000478"
      ],
      "object_id": "point-025",
      "state": "stale"
    },
    {
      "event_id": "event-85",
      "kind": "replan_required",
      "step": 78,
      "evidence_ids": [
        "e000478"
      ],
      "object_id": "point-025",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-86",
      "kind": "target_state_changed",
      "step": 78,
      "evidence_ids": [
        "e000479"
      ],
      "object_id": "point-027",
      "state": "predicted"
    },
    {
      "event_id": "event-87",
      "kind": "target_state_changed",
      "step": 81,
      "evidence_ids": [
        "e000497"
      ],
      "object_id": "point-026",
      "state": "stale"
    },
    {
      "event_id": "event-88",
      "kind": "replan_required",
      "step": 81,
      "evidence_ids": [
        "e000497"
      ],
      "object_id": "point-026",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-89",
      "kind": "target_state_changed",
      "step": 81,
      "evidence_ids": [
        "e000498"
      ],
      "object_id": "point-027",
      "state": "unknown"
    },
    {
      "event_id": "event-90",
      "kind": "search_review_due",
      "step": 84,
      "evidence_ids": [
        "e000520"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-91",
      "kind": "target_state_changed",
      "step": 85,
      "evidence_ids": [
        "e000521"
      ],
      "object_id": "point-027",
      "state": "stale"
    },
    {
      "event_id": "event-92",
      "kind": "replan_required",
      "step": 85,
      "evidence_ids": [
        "e000521"
      ],
      "object_id": "point-027",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-93",
      "kind": "target_state_changed",
      "step": 88,
      "evidence_ids": [
        "e000535"
      ],
      "object_id": "point-028",
      "state": "stale"
    },
    {
      "event_id": "event-94",
      "kind": "replan_required",
      "step": 88,
      "evidence_ids": [
        "e000535"
      ],
      "object_id": "point-028",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-95",
      "kind": "target_state_changed",
      "step": 90,
      "evidence_ids": [
        "e000547"
      ],
      "object_id": "point-029",
      "state": "stale"
    },
    {
      "event_id": "event-96",
      "kind": "replan_required",
      "step": 90,
      "evidence_ids": [
        "e000547"
      ],
      "object_id": "point-029",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-97",
      "kind": "target_state_changed",
      "step": 91,
      "evidence_ids": [
        "e000554"
      ],
      "object_id": "point-032",
      "state": "confirmed"
    },
    {
      "event_id": "event-98",
      "kind": "target_state_changed",
      "step": 94,
      "evidence_ids": [
        "e000569"
      ],
      "object_id": "point-030",
      "state": "stale"
    },
    {
      "event_id": "event-99",
      "kind": "replan_required",
      "step": 94,
      "evidence_ids": [
        "e000569"
      ],
      "object_id": "point-030",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-100",
      "kind": "target_state_changed",
      "step": 94,
      "evidence_ids": [
        "e000570"
      ],
      "object_id": "point-032",
      "state": "predicted"
    },
    {
      "event_id": "event-101",
      "kind": "search_review_due",
      "step": 96,
      "evidence_ids": [
        "e000586"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-102",
      "kind": "target_state_changed",
      "step": 97,
      "evidence_ids": [
        "e000588"
      ],
      "object_id": "point-032",
      "state": "unknown"
    },
    {
      "event_id": "event-103",
      "kind": "target_state_changed",
      "step": 98,
      "evidence_ids": [
        "e000593"
      ],
      "object_id": "point-031",
      "state": "stale"
    },
    {
      "event_id": "event-104",
      "kind": "replan_required",
      "step": 98,
      "evidence_ids": [
        "e000593"
      ],
      "object_id": "point-031",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-105",
      "kind": "target_state_changed",
      "step": 99,
      "evidence_ids": [
        "e000599"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-106",
      "kind": "target_state_changed",
      "step": 101,
      "evidence_ids": [
        "e000611"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-107",
      "kind": "target_state_changed",
      "step": 101,
      "evidence_ids": [
        "e000612"
      ],
      "object_id": "point-032",
      "state": "stale"
    },
    {
      "event_id": "event-108",
      "kind": "replan_required",
      "step": 101,
      "evidence_ids": [
        "e000612"
      ],
      "object_id": "point-032",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-109",
      "kind": "target_state_changed",
      "step": 102,
      "evidence_ids": [
        "e000620"
      ],
      "object_id": "point-035",
      "state": "confirmed"
    },
    {
      "event_id": "event-110",
      "kind": "target_state_changed",
      "step": 105,
      "evidence_ids": [
        "e000637"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-111",
      "kind": "target_state_changed",
      "step": 105,
      "evidence_ids": [
        "e000638"
      ],
      "object_id": "point-033",
      "state": "stale"
    },
    {
      "event_id": "event-112",
      "kind": "replan_required",
      "step": 105,
      "evidence_ids": [
        "e000638"
      ],
      "object_id": "point-033",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-113",
      "kind": "target_state_changed",
      "step": 105,
      "evidence_ids": [
        "e000639"
      ],
      "object_id": "point-035",
      "state": "predicted"
    },
    {
      "event_id": "event-114",
      "kind": "target_state_changed",
      "step": 108,
      "evidence_ids": [
        "e000655"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-115",
      "kind": "target_state_changed",
      "step": 108,
      "evidence_ids": [
        "e000656"
      ],
      "object_id": "point-035",
      "state": "unknown"
    },
    {
      "event_id": "event-116",
      "kind": "search_review_due",
      "step": 108,
      "evidence_ids": [
        "e000663"
      ],
      "reason": "search_budget_elapsed",
      "advisory_only": true
    },
    {
      "event_id": "event-117",
      "kind": "target_state_changed",
      "step": 109,
      "evidence_ids": [
        "e000664"
      ],
      "object_id": "point-034",
      "state": "stale"
    },
    {
      "event_id": "event-118",
      "kind": "replan_required",
      "step": 109,
      "evidence_ids": [
        "e000664"
      ],
      "object_id": "point-034",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-119",
      "kind": "target_state_changed",
      "step": 112,
      "evidence_ids": [
        "e000680"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-120",
      "kind": "replan_required",
      "step": 112,
      "evidence_ids": [
        "e000680"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-121",
      "kind": "target_state_changed",
      "step": 112,
      "evidence_ids": [
        "e000681"
      ],
      "object_id": "point-035",
      "state": "stale"
    },
    {
      "event_id": "event-122",
      "kind": "replan_required",
      "step": 112,
      "evidence_ids": [
        "e000681"
      ],
      "object_id": "point-035",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-123",
      "kind": "target_state_changed",
      "step": 117,
      "evidence_ids": [
        "e000705"
      ],
      "object_id": "point-036",
      "state": "stale"
    },
    {
      "event_id": "event-124",
      "kind": "replan_required",
      "step": 117,
      "evidence_ids": [
        "e000705"
      ],
      "object_id": "point-036",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-125",
      "kind": "search_review_due",
      "step": 120,
      "evidence_ids": [
        "e000728"
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
      "value": -1.6090542446197496,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000722"
      ]
    },
    "pose.y_m": {
      "value": 1.8206262467142207,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000723"
      ]
    },
    "pose.yaw_rad": {
      "value": 2.9890491631736364,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000724"
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
      "value": 1.8432,
      "source": "rgbd_optical_flow",
      "step": 3,
      "evidence_ids": [
        "e000022"
      ]
    },
    "point-002.bearing_rad": {
      "value": -0.221,
      "source": "rgbd_optical_flow",
      "step": 3,
      "evidence_ids": [
        "e000023"
      ]
    },
    "point-003.range_m": {
      "value": 1.1192,
      "source": "rgbd_optical_flow",
      "step": 6,
      "evidence_ids": [
        "e000038"
      ]
    },
    "point-003.bearing_rad": {
      "value": -0.0109,
      "source": "rgbd_optical_flow",
      "step": 6,
      "evidence_ids": [
        "e000039"
      ]
    },
    "point-004.range_m": {
      "value": 1.1714,
      "source": "rgbd_optical_flow",
      "step": 10,
      "evidence_ids": [
        "e000065"
      ]
    },
    "point-004.bearing_rad": {
      "value": -0.1937,
      "source": "rgbd_optical_flow",
      "step": 10,
      "evidence_ids": [
        "e000066"
      ]
    },
    "point-005.range_m": {
      "value": 1.2109,
      "source": "rgbd_optical_flow",
      "step": 14,
      "evidence_ids": [
        "e000089"
      ]
    },
    "point-005.bearing_rad": {
      "value": -0.1407,
      "source": "rgbd_optical_flow",
      "step": 14,
      "evidence_ids": [
        "e000090"
      ]
    },
    "point-006.range_m": {
      "value": 1.1463,
      "source": "rgbd_optical_flow",
      "step": 16,
      "evidence_ids": [
        "e000102"
      ]
    },
    "point-006.bearing_rad": {
      "value": -0.1624,
      "source": "rgbd_optical_flow",
      "step": 16,
      "evidence_ids": [
        "e000103"
      ]
    },
    "point-007.range_m": {
      "value": 1.1812,
      "source": "rgbd_optical_flow",
      "step": 20,
      "evidence_ids": [
        "e000123"
      ]
    },
    "point-007.bearing_rad": {
      "value": -0.0072,
      "source": "rgbd_optical_flow",
      "step": 20,
      "evidence_ids": [
        "e000124"
      ]
    },
    "point-008.range_m": {
      "value": 1.1107,
      "source": "rgbd_optical_flow",
      "step": 22,
      "evidence_ids": [
        "e000135"
      ]
    },
    "point-008.bearing_rad": {
      "value": -0.0368,
      "source": "rgbd_optical_flow",
      "step": 22,
      "evidence_ids": [
        "e000136"
      ]
    },
    "point-009.range_m": {
      "value": 1.0791,
      "source": "rgbd_optical_flow",
      "step": 25,
      "evidence_ids": [
        "e000153"
      ]
    },
    "point-009.bearing_rad": {
      "value": -0.1632,
      "source": "rgbd_optical_flow",
      "step": 25,
      "evidence_ids": [
        "e000154"
      ]
    },
    "point-010.range_m": {
      "value": 1.1769,
      "source": "rgbd_optical_flow",
      "step": 27,
      "evidence_ids": [
        "e000165"
      ]
    },
    "point-010.bearing_rad": {
      "value": 0.0802,
      "source": "rgbd_optical_flow",
      "step": 27,
      "evidence_ids": [
        "e000166"
      ]
    },
    "point-011.range_m": {
      "value": 1.0624,
      "source": "rgbd_optical_flow",
      "step": 30,
      "evidence_ids": [
        "e000181"
      ]
    },
    "point-011.bearing_rad": {
      "value": 0.0028,
      "source": "rgbd_optical_flow",
      "step": 30,
      "evidence_ids": [
        "e000182"
      ]
    },
    "point-012.range_m": {
      "value": 1.1218,
      "source": "rgbd_optical_flow",
      "step": 32,
      "evidence_ids": [
        "e000193"
      ]
    },
    "point-012.bearing_rad": {
      "value": 0.0212,
      "source": "rgbd_optical_flow",
      "step": 32,
      "evidence_ids": [
        "e000194"
      ]
    },
    "point-013.range_m": {
      "value": 3.0603,
      "source": "rgbd_optical_flow",
      "step": 36,
      "evidence_ids": [
        "e000215"
      ]
    },
    "point-013.bearing_rad": {
      "value": 0.5086,
      "source": "rgbd_optical_flow",
      "step": 36,
      "evidence_ids": [
        "e000216"
      ]
    },
    "point-014.range_m": {
      "value": 3.0457,
      "source": "rgbd_optical_flow",
      "step": 38,
      "evidence_ids": [
        "e000229"
      ]
    },
    "point-014.bearing_rad": {
      "value": -0.0517,
      "source": "rgbd_optical_flow",
      "step": 38,
      "evidence_ids": [
        "e000230"
      ]
    },
    "point-015.range_m": {
      "value": 2.1626,
      "source": "rgbd_optical_flow",
      "step": 40,
      "evidence_ids": [
        "e000241"
      ]
    },
    "point-015.bearing_rad": {
      "value": -0.0024,
      "source": "rgbd_optical_flow",
      "step": 40,
      "evidence_ids": [
        "e000242"
      ]
    },
    "point-016.range_m": {
      "value": 4.6074,
      "source": "rgbd_optical_flow",
      "step": 42,
      "evidence_ids": [
        "e000256"
      ]
    },
    "point-016.bearing_rad": {
      "value": -0.6689,
      "source": "rgbd_optical_flow",
      "step": 42,
      "evidence_ids": [
        "e000257"
      ]
    },
    "point-017.range_m": {
      "value": 1.111,
      "source": "rgbd_optical_flow",
      "step": 45,
      "evidence_ids": [
        "e000271"
      ]
    },
    "point-017.bearing_rad": {
      "value": -0.0128,
      "source": "rgbd_optical_flow",
      "step": 45,
      "evidence_ids": [
        "e000272"
      ]
    },
    "point-018.range_m": {
      "value": 1.1967,
      "source": "rgbd_optical_flow",
      "step": 48,
      "evidence_ids": [
        "e000291"
      ]
    },
    "point-018.bearing_rad": {
      "value": -0.0217,
      "source": "rgbd_optical_flow",
      "step": 48,
      "evidence_ids": [
        "e000292"
      ]
    },
    "point-019.range_m": {
      "value": 1.0764,
      "source": "rgbd_optical_flow",
      "step": 50,
      "evidence_ids": [
        "e000305"
      ]
    },
    "point-019.bearing_rad": {
      "value": 0.0597,
      "source": "rgbd_optical_flow",
      "step": 50,
      "evidence_ids": [
        "e000306"
      ]
    },
    "point-020.range_m": {
      "value": 1.0934,
      "source": "rgbd_optical_flow",
      "step": 53,
      "evidence_ids": [
        "e000323"
      ]
    },
    "point-020.bearing_rad": {
      "value": -0.0102,
      "source": "rgbd_optical_flow",
      "step": 53,
      "evidence_ids": [
        "e000324"
      ]
    },
    "point-021.range_m": {
      "value": 1.1227,
      "source": "rgbd_optical_flow",
      "step": 56,
      "evidence_ids": [
        "e000343"
      ]
    },
    "point-021.bearing_rad": {
      "value": -0.1526,
      "source": "rgbd_optical_flow",
      "step": 56,
      "evidence_ids": [
        "e000344"
      ]
    },
    "point-022.range_m": {
      "value": 1.0847,
      "source": "rgbd_optical_flow",
      "step": 58,
      "evidence_ids": [
        "e000355"
      ]
    },
    "point-022.bearing_rad": {
      "value": -0.0482,
      "source": "rgbd_optical_flow",
      "step": 58,
      "evidence_ids": [
        "e000356"
      ]
    },
    "point-023.range_m": {
      "value": 1.1374,
      "source": "rgbd_optical_flow",
      "step": 63,
      "evidence_ids": [
        "e000385"
      ]
    },
    "point-023.bearing_rad": {
      "value": -0.0642,
      "source": "rgbd_optical_flow",
      "step": 63,
      "evidence_ids": [
        "e000386"
      ]
    },
    "point-024.range_m": {
      "value": 5.0898,
      "source": "rgbd_optical_flow",
      "step": 66,
      "evidence_ids": [
        "e000407"
      ]
    },
    "point-024.bearing_rad": {
      "value": 0.078,
      "source": "rgbd_optical_flow",
      "step": 66,
      "evidence_ids": [
        "e000408"
      ]
    },
    "point-025.range_m": {
      "value": 3.2472,
      "source": "rgbd_optical_flow",
      "step": 69,
      "evidence_ids": [
        "e000429"
      ]
    },
    "point-025.bearing_rad": {
      "value": -0.4433,
      "source": "rgbd_optical_flow",
      "step": 69,
      "evidence_ids": [
        "e000430"
      ]
    },
    "point-026.range_m": {
      "value": 1.0678,
      "source": "rgbd_optical_flow",
      "step": 71,
      "evidence_ids": [
        "e000440"
      ]
    },
    "point-026.bearing_rad": {
      "value": 0.0893,
      "source": "rgbd_optical_flow",
      "step": 71,
      "evidence_ids": [
        "e000441"
      ]
    },
    "point-027.range_m": {
      "value": 1.166,
      "source": "rgbd_optical_flow",
      "step": 75,
      "evidence_ids": [
        "e000464"
      ]
    },
    "point-027.bearing_rad": {
      "value": 0.0046,
      "source": "rgbd_optical_flow",
      "step": 75,
      "evidence_ids": [
        "e000465"
      ]
    },
    "point-028.range_m": {
      "value": 1.181,
      "source": "rgbd_optical_flow",
      "step": 78,
      "evidence_ids": [
        "e000483"
      ]
    },
    "point-028.bearing_rad": {
      "value": -0.1747,
      "source": "rgbd_optical_flow",
      "step": 78,
      "evidence_ids": [
        "e000484"
      ]
    },
    "point-029.range_m": {
      "value": 1.1557,
      "source": "rgbd_optical_flow",
      "step": 81,
      "evidence_ids": [
        "e000502"
      ]
    },
    "point-029.bearing_rad": {
      "value": -0.1287,
      "source": "rgbd_optical_flow",
      "step": 81,
      "evidence_ids": [
        "e000503"
      ]
    },
    "point-030.range_m": {
      "value": 1.1512,
      "source": "rgbd_optical_flow",
      "step": 84,
      "evidence_ids": [
        "e000517"
      ]
    },
    "point-030.bearing_rad": {
      "value": 0.045,
      "source": "rgbd_optical_flow",
      "step": 84,
      "evidence_ids": [
        "e000518"
      ]
    },
    "point-031.range_m": {
      "value": 1.1878,
      "source": "rgbd_optical_flow",
      "step": 88,
      "evidence_ids": [
        "e000539"
      ]
    },
    "point-031.bearing_rad": {
      "value": -0.1548,
      "source": "rgbd_optical_flow",
      "step": 88,
      "evidence_ids": [
        "e000540"
      ]
    },
    "point-032.range_m": {
      "value": 1.1311,
      "source": "rgbd_optical_flow",
      "step": 91,
      "evidence_ids": [
        "e000558"
      ]
    },
    "point-032.bearing_rad": {
      "value": -0.0381,
      "source": "rgbd_optical_flow",
      "step": 91,
      "evidence_ids": [
        "e000559"
      ]
    },
    "point-033.range_m": {
      "value": 1.1525,
      "source": "rgbd_optical_flow",
      "step": 95,
      "evidence_ids": [
        "e000579"
      ]
    },
    "point-033.bearing_rad": {
      "value": -0.0212,
      "source": "rgbd_optical_flow",
      "step": 95,
      "evidence_ids": [
        "e000580"
      ]
    },
    "point-034.range_m": {
      "value": 3.7439,
      "source": "rgbd_optical_flow",
      "step": 99,
      "evidence_ids": [
        "e000603"
      ]
    },
    "point-034.bearing_rad": {
      "value": 0.6598,
      "source": "rgbd_optical_flow",
      "step": 99,
      "evidence_ids": [
        "e000604"
      ]
    },
    "point-035.range_m": {
      "value": 3.4594,
      "source": "rgbd_optical_flow",
      "step": 102,
      "evidence_ids": [
        "e000625"
      ]
    },
    "point-035.bearing_rad": {
      "value": 0.1607,
      "source": "rgbd_optical_flow",
      "step": 102,
      "evidence_ids": [
        "e000626"
      ]
    },
    "point-036.range_m": {
      "value": 1.1557,
      "source": "rgbd_optical_flow",
      "step": 108,
      "evidence_ids": [
        "e000660"
      ]
    },
    "point-036.bearing_rad": {
      "value": 0.0145,
      "source": "rgbd_optical_flow",
      "step": 108,
      "evidence_ids": [
        "e000661"
      ]
    },
    "point-037.range_m": {
      "value": 1.1032,
      "source": "rgbd_optical_flow",
      "step": 111,
      "evidence_ids": [
        "e000677"
      ]
    },
    "point-037.bearing_rad": {
      "value": -0.1784,
      "source": "rgbd_optical_flow",
      "step": 111,
      "evidence_ids": [
        "e000678"
      ]
    },
    "point-038.range_m": {
      "value": 1.2749,
      "source": "rgbd_optical_flow",
      "step": 115,
      "evidence_ids": [
        "e000698"
      ]
    },
    "point-038.bearing_rad": {
      "value": -0.0779,
      "source": "rgbd_optical_flow",
      "step": 115,
      "evidence_ids": [
        "e000699"
      ]
    },
    "point-039.range_m": {
      "value": 1.1176,
      "source": "rgbd_optical_flow",
      "step": 118,
      "evidence_ids": [
        "e000714"
      ]
    },
    "point-039.bearing_rad": {
      "value": 0.0226,
      "source": "rgbd_optical_flow",
      "step": 118,
      "evidence_ids": [
        "e000715"
      ]
    },
    "point-040.range_m": {
      "value": 1.1099,
      "source": "rgbd_optical_flow",
      "step": 120,
      "evidence_ids": [
        "e000725"
      ]
    },
    "point-040.bearing_rad": {
      "value": 0.0265,
      "source": "rgbd_optical_flow",
      "step": 120,
      "evidence_ids": [
        "e000726"
      ]
    }
  },
  "plans": [
    {
      "subgoals": [
        {
          "subgoal_id": "search_A",
          "description": "scan view left to locate blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000016"
          ]
        },
        {
          "subgoal_id": "explore_A",
          "description": "change viewpoint with short safe translation if scanning stalls",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000044"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_A"
        }
      ],
      "recovery": "stop, observe fresh geometry, then choose a safe local translation or abort",
      "plan_id": "plan-0001",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_A_translate",
          "description": "short forward translation along clear floor (tracked point at ~1.18 m ahead-right) to gain parallax for locating blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000060"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_A_translate"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, re-check geometry, then choose another conservative translation or abort with reason",
      "plan_id": "plan-0002",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_for_A",
          "description": "turn to scan surroundings for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000113"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_for_A"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then reverse scan direction or take a short conservative translation",
      "plan_id": "plan-0003",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_forward",
          "description": "move cautiously forward along tracked clear ray to change viewpoint and search for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000130"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then try a small turn or reverse direction with conservative motion",
      "plan_id": "plan-0004",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_left",
          "description": "turn left to scan the room for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000147"
          ]
        },
        {
          "subgoal_id": "explore_forward",
          "description": "move cautiously forward to a new viewpoint to search for A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000171"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_forward"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then try a small turn or reverse direction with conservative motion",
      "plan_id": "plan-0005",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_A",
          "description": "turn left to scan the room for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000204"
          ]
        },
        {
          "subgoal_id": "explore_viewpoint",
          "description": "move cautiously to a new viewpoint to search for A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000248"
          ]
        },
        {
          "subgoal_id": "inspect_A",
          "description": "track and verify blue ball A geometry",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_A",
          "description": "stop at 1.0 m standoff facing A",
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
          "subgoal_id": "explore_viewpoint"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then try a small turn or reverse direction with conservative motion",
      "plan_id": "plan-0006",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_A",
          "description": "turn to scan the room for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000299"
          ]
        },
        {
          "subgoal_id": "explore_viewpoint",
          "description": "move cautiously to a new viewpoint to search for A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000312"
          ]
        },
        {
          "subgoal_id": "inspect_A",
          "description": "track and verify blue ball A geometry",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_A",
          "description": "stop at 1.0 m standoff facing A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "inspect_B",
          "description": "track and verify green square B geometry",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_B",
          "description": "stop at 1.0 m standoff facing B",
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
          "subgoal_id": "explore_viewpoint"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then try a small turn or controlled translation with conservative motion",
      "plan_id": "plan-0007",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_viewpoint",
          "description": "move cautiously forward to a new viewpoint to search for A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000387"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_viewpoint"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, inspect tracked geometry, then choose a small turn or abort if clearance is insufficient",
      "plan_id": "plan-0008",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_view",
          "description": "turn left to reveal blue ball A and green box B while stationary",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000392"
          ]
        },
        {
          "subgoal_id": "approach_A",
          "description": "approach confirmed blue ball A to the required standoff and heading",
          "preconditions": [
            {
              "object_id": "task:A"
            }
          ],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_B",
          "description": "after the A checkpoint, approach confirmed green box B to the required standoff and heading",
          "preconditions": [
            {
              "object_id": "task:B"
            }
          ],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_view"
        }
      ],
      "recovery": "stop, observe fresh RGB-D; if no target is visible, translate to a new viewpoint using measured clear geometry, or abort if clearance is insufficient",
      "plan_id": "plan-0009",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_view",
          "description": "turn left to scan for blue ball A and green box B",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000414"
          ]
        },
        {
          "subgoal_id": "explore_viewpoint",
          "description": "translate to a new viewpoint if A not yet visible",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000446"
          ]
        },
        {
          "subgoal_id": "approach_A",
          "description": "approach confirmed blue ball A to required standoff and heading",
          "preconditions": [
            {
              "object_id": "task:A"
            }
          ],
          "completion": [],
          "active": false,
          "status": "待做",
          "evidence_ids": []
        },
        {
          "subgoal_id": "approach_B",
          "description": "after A checkpoint, approach confirmed green box B to required standoff and heading",
          "preconditions": [
            {
              "object_id": "task:B"
            }
          ],
          "completion": [],
          "active": false,
          "status": "已失效",
          "evidence_ids": [
            "e000477"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_viewpoint"
        }
      ],
      "recovery": "stop, observe fresh RGB-D; translate to a measured-clear viewpoint to search for A; abort if no safe clearance",
      "plan_id": "plan-0010",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_for_targets",
          "description": "turn left to scan room for blue ball A and green box B",
          "preconditions": [],
          "completion": [],
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
          "subgoal_id": "scan_for_targets"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then track any new candidate point or translate to a new viewpoint; abort if geometry stays unsafe",
      "plan_id": "plan-0011",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "explore_viewpoint",
          "description": "short forward translation to change viewpoint and search for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000627"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_viewpoint"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then track any new candidate or pick another safe viewpoint; abort if geometry unsafe",
      "plan_id": "plan-0012",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_A",
          "description": "rotate left to search for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": true,
          "status": "进行中",
          "evidence_ids": [
            "e000636"
          ]
        },
        {
          "subgoal_id": "explore_viewpoint",
          "description": "translate to a new viewpoint if scan stalls",
          "preconditions": [],
          "completion": [],
          "active": true,
          "status": "进行中",
          "evidence_ids": [
            "e000668"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "explore_viewpoint"
        }
      ],
      "recovery": "stop, observe fresh RGB-D, then track any new blue candidate or translate to another safe viewpoint; abort if geometry unsafe",
      "plan_id": "plan-0013",
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
        "call_id": "call_4b8d8b10203f4f449490e730",
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
      "value": 0.011245649140702809
    },
    {
      "evidence_id": "e000014",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.y_m",
      "value": 0.0002710400063774052
    },
    {
      "evidence_id": "e000015",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 2,
      "name": "pose.yaw_rad",
      "value": 0.4481650239534403
    },
    {
      "evidence_id": "e000016",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 2,
      "action": {
        "call_id": "call_704c116b7bed470e909cde5e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "search_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011245649140702809,
            0.0002710400063774052
          ],
          "yaw_delta_rad": 0.4481650239534405,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000017",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 3,
      "observation": {
        "object_id": "point-002",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8071006378272325,
            0.4154377771249777
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
            405.0,
            181.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000018",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 3,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8071006378272325,
            0.4154377771249777
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
            405.0,
            181.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00002",
          "position_m": [
            0.4050738683185717,
            0.0071065590933082744,
            1.4770705699920654
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
      "evidence_id": "e000019",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.x_m",
      "value": 0.011245649140702809
    },
    {
      "evidence_id": "e000020",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.y_m",
      "value": 0.0002710400063774052
    },
    {
      "evidence_id": "e000021",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 3,
      "name": "pose.yaw_rad",
      "value": 0.4481650239534403
    },
    {
      "evidence_id": "e000022",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 3,
      "name": "point-002.range_m",
      "value": 1.8432
    },
    {
      "evidence_id": "e000023",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 3,
      "name": "point-002.bearing_rad",
      "value": -0.221
    },
    {
      "evidence_id": "e000024",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 3,
      "action": {
        "call_id": "call_fe9b61bc42274523bb34624c",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000025",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.x_m",
      "value": 0.015143485009916987
    },
    {
      "evidence_id": "e000026",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.y_m",
      "value": 0.01696141705730058
    },
    {
      "evidence_id": "e000027",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.yaw_rad",
      "value": 0.9937935056568327
    },
    {
      "evidence_id": "e000028",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 4,
      "action": {
        "call_id": "call_7ee4fad00b9b4644921f461c",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "search_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010745049236705953,
            0.013353116769731345
          ],
          "yaw_delta_rad": 0.5456284817033925,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000029",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.x_m",
      "value": -0.0034067127632427027
    },
    {
      "evidence_id": "e000030",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.y_m",
      "value": 0.04005616220150885
    },
    {
      "evidence_id": "e000031",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.yaw_rad",
      "value": 1.5582894875361317
    },
    {
      "evidence_id": "e000032",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 5,
      "action": {
        "call_id": "call_81dee38f856e44069f15bfb5",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "search_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.009236337660064006,
            0.028145464240771613
          ],
          "yaw_delta_rad": 0.5644959818792992,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000033",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 6,
      "observation": {
        "object_id": "point-003",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.022788372009614137,
            1.1589160584949378
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
            322.0,
            343.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000034",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 6,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000035",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.x_m",
      "value": -0.0034067127632427027
    },
    {
      "evidence_id": "e000036",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.y_m",
      "value": 0.04005616220150885
    },
    {
      "evidence_id": "e000037",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.yaw_rad",
      "value": 1.5582894875361317
    },
    {
      "evidence_id": "e000038",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-003.range_m",
      "value": 1.1192
    },
    {
      "evidence_id": "e000039",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-003.bearing_rad",
      "value": -0.0109
    },
    {
      "evidence_id": "e000040",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 6,
      "action": {
        "call_id": "call_dda00de39c93475a9b76a74d",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000041",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.x_m",
      "value": -0.021839566145883296
    },
    {
      "evidence_id": "e000042",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.y_m",
      "value": 0.0487042929463472
    },
    {
      "evidence_id": "e000043",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.yaw_rad",
      "value": 2.1082780031698944
    },
    {
      "evidence_id": "e000044",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 7,
      "action": {
        "call_id": "call_c3e7355d513c408fa00651c0",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "explore_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.008416923654651255,
            0.018539569719859067
          ],
          "yaw_delta_rad": 0.5499885156337623,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000045",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 8,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.3916467527407389,
            1.1742775001358208
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
            418.0,
            339.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000046",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.x_m",
      "value": -0.021839566145883296
    },
    {
      "evidence_id": "e000047",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.y_m",
      "value": 0.0487042929463472
    },
    {
      "evidence_id": "e000048",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.yaw_rad",
      "value": 2.1082780031698944
    },
    {
      "evidence_id": "e000049",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 8,
      "name": "point-004.range_m",
      "value": 1.1848
    },
    {
      "evidence_id": "e000050",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 8,
      "name": "point-004.bearing_rad",
      "value": -0.2201
    },
    {
      "evidence_id": "e000051",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 8,
      "action": {
        "call_id": "call_ff9c815f33114cafbfd44fe1",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000052",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 8,
      "plan_id": "plan-0002"
    },
    {
      "evidence_id": "e000053",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 9,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.5553359624337717,
            1.3441421068558588
          ]
        },
        "pose_covariance": null,
        "confidence": 0.99,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00006",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00006",
          "pixel_uv": [
            403.3,
            340.89
          ]
        }
      }
    },
    {
      "evidence_id": "e000054",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 9,
      "object_id": "task:B",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000055",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.x_m",
      "value": -0.14948474393079503
    },
    {
      "evidence_id": "e000056",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.y_m",
      "value": 0.2453062690531192
    },
    {
      "evidence_id": "e000057",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.yaw_rad",
      "value": 2.1182299165630254
    },
    {
      "evidence_id": "e000058",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-004.range_m",
      "value": 1.1714
    },
    {
      "evidence_id": "e000059",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 9,
      "name": "point-004.bearing_rad",
      "value": -0.1937
    },
    {
      "evidence_id": "e000060",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 9,
      "action": {
        "call_id": "call_fbfaeb73c64143de8f6dfa42",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "explore_A_translate",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23423229942617357,
            0.00899212579743193
          ],
          "yaw_delta_rad": 0.009951913393130951,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000061",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 10,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.5553359624337717,
            1.3441421068558588
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
            403.3,
            340.89
          ]
        }
      }
    },
    {
      "evidence_id": "e000062",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.x_m",
      "value": -0.14948474393079503
    },
    {
      "evidence_id": "e000063",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.y_m",
      "value": 0.2453062690531192
    },
    {
      "evidence_id": "e000064",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.yaw_rad",
      "value": 2.1182299165630254
    },
    {
      "evidence_id": "e000065",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-004.range_m",
      "value": 1.1714
    },
    {
      "evidence_id": "e000066",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 10,
      "name": "point-004.bearing_rad",
      "value": -0.1937
    },
    {
      "evidence_id": "e000067",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 10,
      "action": {
        "call_id": "call_bb6edd750c9d4cae99575d2c",
        "tool": "observe",
        "status": "succeeded"
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
      "value": -0.3224513287572933
    },
    {
      "evidence_id": "e000070",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.y_m",
      "value": 0.5212764580226035
    },
    {
      "evidence_id": "e000071",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.yaw_rad",
      "value": 2.128208445975178
    },
    {
      "evidence_id": "e000072",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 11,
      "action": {
        "call_id": "call_cffc1da2c6d64995bf0a099c",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "explore_A_translate",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3256694621240086,
            0.004047975574763357
          ],
          "yaw_delta_rad": 0.009978529412152604,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000073",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.x_m",
      "value": -0.3224513287572933
    },
    {
      "evidence_id": "e000074",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.y_m",
      "value": 0.5212764580226035
    },
    {
      "evidence_id": "e000075",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.yaw_rad",
      "value": 2.128208445975178
    },
    {
      "evidence_id": "e000076",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 12,
      "action": {
        "call_id": "call_a981ff4816f54ba49bbc6ebe",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000077",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 12,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 12,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 1,
      "recent_action_evidence_ids": [
        "e000076"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000078",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 13,
      "object_id": "task:B",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000079",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 13,
      "object_id": "point-002",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000080",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 13,
      "object_id": "point-004",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000081",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.x_m",
      "value": -0.3224513287572933
    },
    {
      "evidence_id": "e000082",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.y_m",
      "value": 0.5212764580226035
    },
    {
      "evidence_id": "e000083",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.yaw_rad",
      "value": 2.128208445975178
    },
    {
      "evidence_id": "e000084",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 13,
      "action": {
        "call_id": "call_105a663cafbe4eebba450967",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000085",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 14,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.8125627785964888,
            1.6285180832952997
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
            380.0,
            335.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000086",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.x_m",
      "value": -0.3224513287572933
    },
    {
      "evidence_id": "e000087",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.y_m",
      "value": 0.5212764580226035
    },
    {
      "evidence_id": "e000088",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.yaw_rad",
      "value": 2.128208445975178
    },
    {
      "evidence_id": "e000089",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-005.range_m",
      "value": 1.2109
    },
    {
      "evidence_id": "e000090",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 14,
      "name": "point-005.bearing_rad",
      "value": -0.1407
    },
    {
      "evidence_id": "e000091",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 14,
      "action": {
        "call_id": "call_6fb014526e984e038c929902",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000092",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.x_m",
      "value": -0.5037875079527196
    },
    {
      "evidence_id": "e000093",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.y_m",
      "value": 0.7912663903900646
    },
    {
      "evidence_id": "e000094",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.yaw_rad",
      "value": 2.149778368804192
    },
    {
      "evidence_id": "e000095",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 15,
      "action": {
        "call_id": "call_0c1db6168e7c4f729954655a",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "explore_A_translate",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3250460810832334,
            0.011064295613102848
          ],
          "yaw_delta_rad": 0.021569922829014043,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000096",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 16,
      "observation": {
        "object_id": "point-006",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.9676488445518734,
            1.8394945098413829
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
            389.0,
            345.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000097",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 16,
      "object_id": "point-003",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000098",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 16,
      "object_id": "point-004",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000099",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.x_m",
      "value": -0.5037875079527196
    },
    {
      "evidence_id": "e000100",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.y_m",
      "value": 0.7912663903900646
    },
    {
      "evidence_id": "e000101",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.yaw_rad",
      "value": 2.149778368804192
    },
    {
      "evidence_id": "e000102",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-006.range_m",
      "value": 1.1463
    },
    {
      "evidence_id": "e000103",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 16,
      "name": "point-006.bearing_rad",
      "value": -0.1624
    },
    {
      "evidence_id": "e000104",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 16,
      "action": {
        "call_id": "call_4747b23c34eb4015afd95d65",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000105",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.x_m",
      "value": -0.7016745604634742
    },
    {
      "evidence_id": "e000106",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.y_m",
      "value": 1.0623372724424167
    },
    {
      "evidence_id": "e000107",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.yaw_rad",
      "value": 2.1525340283645793
    },
    {
      "evidence_id": "e000108",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 17,
      "action": {
        "call_id": "call_81fc39801421487e8fe83d96",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "explore_A_translate",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.33517005963358704,
            0.017312994346793897
          ],
          "yaw_delta_rad": 0.002755659560387258,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000109",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 17,
      "plan_id": "plan-0003"
    },
    {
      "evidence_id": "e000110",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.x_m",
      "value": -0.7198082840123297
    },
    {
      "evidence_id": "e000111",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.y_m",
      "value": 1.064923507040557
    },
    {
      "evidence_id": "e000112",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.yaw_rad",
      "value": 2.6498378557384132
    },
    {
      "evidence_id": "e000113",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 18,
      "action": {
        "call_id": "call_d28a297d241243cc917a9b74",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.012124879828979331,
            0.01372981530377369
          ],
          "yaw_delta_rad": 0.49730382737383394,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000114",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.x_m",
      "value": -0.7241629681154411
    },
    {
      "evidence_id": "e000115",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.y_m",
      "value": 1.0817141182477146
    },
    {
      "evidence_id": "e000116",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.yaw_rad",
      "value": -3.0926856958292515
    },
    {
      "evidence_id": "e000117",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 19,
      "action": {
        "call_id": "call_35182aea15b74c6cb2182a4b",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_for_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011766759930008017,
            -0.012744852258750689
          ],
          "yaw_delta_rad": 0.5406617556119215,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000118",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 20,
      "observation": {
        "object_id": "point-007",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.904366142567864,
            1.0324580829583863
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
            320.0,
            327.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000119",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 20,
      "object_id": "point-004",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000120",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.x_m",
      "value": -0.7241629681154411
    },
    {
      "evidence_id": "e000121",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.y_m",
      "value": 1.0817141182477146
    },
    {
      "evidence_id": "e000122",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.yaw_rad",
      "value": -3.0926856958292515
    },
    {
      "evidence_id": "e000123",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-007.range_m",
      "value": 1.1812
    },
    {
      "evidence_id": "e000124",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-007.bearing_rad",
      "value": -0.0072
    },
    {
      "evidence_id": "e000125",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 20,
      "action": {
        "call_id": "call_06ff23b569de40c28f297a9b",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000126",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 20,
      "plan_id": "plan-0004"
    },
    {
      "evidence_id": "e000127",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.x_m",
      "value": -0.9503157018923857
    },
    {
      "evidence_id": "e000128",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.y_m",
      "value": 1.0638415188506356
    },
    {
      "evidence_id": "e000129",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.yaw_rad",
      "value": -3.0761528195421524
    },
    {
      "evidence_id": "e000130",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 21,
      "action": {
        "call_id": "call_592c0e4c80f7441790e38db0",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.22675606744250296,
            0.006795195508967643
          ],
          "yaw_delta_rad": 0.016532876287099096,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000131",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 22,
      "observation": {
        "object_id": "point-008",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.060607873563844,
            1.031967806718583
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
            334.0,
            345.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000132",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.x_m",
      "value": -0.9503157018923857
    },
    {
      "evidence_id": "e000133",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.y_m",
      "value": 1.0638415188506356
    },
    {
      "evidence_id": "e000134",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.yaw_rad",
      "value": -3.0761528195421524
    },
    {
      "evidence_id": "e000135",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-008.range_m",
      "value": 1.1107
    },
    {
      "evidence_id": "e000136",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 22,
      "name": "point-008.bearing_rad",
      "value": -0.0368
    },
    {
      "evidence_id": "e000137",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 22,
      "action": {
        "call_id": "call_1f51fa4165884b79b4eab7f1",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000138",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.x_m",
      "value": -1.189287629875099
    },
    {
      "evidence_id": "e000139",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.y_m",
      "value": 1.036758205514786
    },
    {
      "evidence_id": "e000140",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.yaw_rad",
      "value": -3.0586886479880637
    },
    {
      "evidence_id": "e000141",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 23,
      "action": {
        "call_id": "call_a75d3e5aaa364f1080e826d3",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2402314900659556,
            0.011398219409788732
          ],
          "yaw_delta_rad": 0.017464171554088637,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000142",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 23,
      "plan_id": "plan-0005"
    },
    {
      "evidence_id": "e000143",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 24,
      "object_id": "point-005",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000144",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.x_m",
      "value": -1.1882073677886984
    },
    {
      "evidence_id": "e000145",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.y_m",
      "value": 1.0198119385306224
    },
    {
      "evidence_id": "e000146",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.yaw_rad",
      "value": -2.508399851349433
    },
    {
      "evidence_id": "e000147",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 24,
      "action": {
        "call_id": "call_91f97b8c563c4cfba17ad916",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0005",
        "subgoal_id": "scan_left",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00032675276879150076,
            0.01697751935654783
          ],
          "yaw_delta_rad": 0.5502887966386307,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000148",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 24,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 24,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 2,
      "recent_action_evidence_ids": [
        "e000147"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000149",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 25,
      "observation": {
        "object_id": "point-009",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.1503165641470483,
            0.5310635121570023
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
            393.0,
            357.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000150",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.x_m",
      "value": -1.1882073677886984
    },
    {
      "evidence_id": "e000151",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.y_m",
      "value": 1.0198119385306224
    },
    {
      "evidence_id": "e000152",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.yaw_rad",
      "value": -2.508399851349433
    },
    {
      "evidence_id": "e000153",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-009.range_m",
      "value": 1.0791
    },
    {
      "evidence_id": "e000154",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 25,
      "name": "point-009.bearing_rad",
      "value": -0.1632
    },
    {
      "evidence_id": "e000155",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 25,
      "action": {
        "call_id": "call_f26c34024af14e248215c47f",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000156",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 26,
      "object_id": "point-006",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000157",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.x_m",
      "value": -1.1854258436422336
    },
    {
      "evidence_id": "e000158",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.y_m",
      "value": 1.0091089829220068
    },
    {
      "evidence_id": "e000159",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.yaw_rad",
      "value": -2.069005411123569
    },
    {
      "evidence_id": "e000160",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 26,
      "action": {
        "call_id": "call_9e5fb029ca1949ac8a14150f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0005",
        "subgoal_id": "scan_left",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.004090865792304913,
            0.010273993985140877
          ],
          "yaw_delta_rad": 0.4393944402258638,
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
      "step": 27,
      "observation": {
        "object_id": "point-010",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.6631584386676679,
            -0.06645025191829919
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
            283.0,
            325.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000162",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.x_m",
      "value": -1.1854258436422336
    },
    {
      "evidence_id": "e000163",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.y_m",
      "value": 1.0091089829220068
    },
    {
      "evidence_id": "e000164",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.yaw_rad",
      "value": -2.069005411123569
    },
    {
      "evidence_id": "e000165",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-010.range_m",
      "value": 1.1769
    },
    {
      "evidence_id": "e000166",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 27,
      "name": "point-010.bearing_rad",
      "value": 0.0802
    },
    {
      "evidence_id": "e000167",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 27,
      "action": {
        "call_id": "call_8d1c3ee7b0f245a5b6b19cc6",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000168",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.x_m",
      "value": -1.3374532958789105
    },
    {
      "evidence_id": "e000169",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.y_m",
      "value": 0.7122969814903173
    },
    {
      "evidence_id": "e000170",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.yaw_rad",
      "value": -2.0602714316366533
    },
    {
      "evidence_id": "e000171",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 28,
      "action": {
        "call_id": "call_a9ce04b526444585a5dd2227",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0005",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.33337825317870107,
            0.008285573907598681
          ],
          "yaw_delta_rad": 0.0087339794869159,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000172",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.x_m",
      "value": -1.3374532958789105
    },
    {
      "evidence_id": "e000173",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.y_m",
      "value": 0.7122969814903173
    },
    {
      "evidence_id": "e000174",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.yaw_rad",
      "value": -2.0602714316366533
    },
    {
      "evidence_id": "e000175",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 29,
      "action": {
        "call_id": "call_78d9e744f68f41f187942c76",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000176",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 30,
      "observation": {
        "object_id": "point-011",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.8343063996203226,
            -0.22676625030109182
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00019",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00019",
          "pixel_uv": [
            315.0,
            356.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000177",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 30,
      "object_id": "point-007",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000178",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.x_m",
      "value": -1.3374532958789105
    },
    {
      "evidence_id": "e000179",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.y_m",
      "value": 0.7122969814903173
    },
    {
      "evidence_id": "e000180",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.yaw_rad",
      "value": -2.0602714316366533
    },
    {
      "evidence_id": "e000181",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-011.range_m",
      "value": 1.0624
    },
    {
      "evidence_id": "e000182",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 30,
      "name": "point-011.bearing_rad",
      "value": 0.0028
    },
    {
      "evidence_id": "e000183",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 30,
      "action": {
        "call_id": "call_6fbd257d58d84cd787e96a93",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000184",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.x_m",
      "value": -1.3385951405159016
    },
    {
      "evidence_id": "e000185",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.y_m",
      "value": 0.7243795822918315
    },
    {
      "evidence_id": "e000186",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.yaw_rad",
      "value": -1.5154608884237837
    },
    {
      "evidence_id": "e000187",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 31,
      "action": {
        "call_id": "call_2b1d0f6fe9b54fa6b73f37e1",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0005",
        "subgoal_id": "scan_left",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.010127006244344715,
            -0.006688557081372803
          ],
          "yaw_delta_rad": 0.5448105432128698,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000188",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 32,
      "observation": {
        "object_id": "point-012",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.2528045408965418,
            -0.3940875218363813
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00020",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00020",
          "pixel_uv": [
            308.0,
            338.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000189",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 32,
      "object_id": "point-008",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000190",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.x_m",
      "value": -1.3385951405159016
    },
    {
      "evidence_id": "e000191",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.y_m",
      "value": 0.7243795822918315
    },
    {
      "evidence_id": "e000192",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.yaw_rad",
      "value": -1.5154608884237837
    },
    {
      "evidence_id": "e000193",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-012.range_m",
      "value": 1.1218
    },
    {
      "evidence_id": "e000194",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 32,
      "name": "point-012.bearing_rad",
      "value": 0.0212
    },
    {
      "evidence_id": "e000195",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 32,
      "action": {
        "call_id": "call_5f073adf580348d9a06ac4c4",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000196",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.x_m",
      "value": -1.3070540367609293
    },
    {
      "evidence_id": "e000197",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.y_m",
      "value": 0.3903896286550577
    },
    {
      "evidence_id": "e000198",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.yaw_rad",
      "value": -1.4970159448439035
    },
    {
      "evidence_id": "e000199",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 33,
      "action": {
        "call_id": "call_2d338c67bd6142919d052968",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0005",
        "subgoal_id": "explore_forward",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.33522319391907995,
            0.013020776285122236
          ],
          "yaw_delta_rad": 0.018444943579880135,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000200",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 33,
      "plan_id": "plan-0006"
    },
    {
      "evidence_id": "e000201",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.x_m",
      "value": -1.3138903408976812
    },
    {
      "evidence_id": "e000202",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.y_m",
      "value": 0.3839524957996195
    },
    {
      "evidence_id": "e000203",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.yaw_rad",
      "value": -1.051485036761753
    },
    {
      "evidence_id": "e000204",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 34,
      "action": {
        "call_id": "call_233481adaf204d61b6c3fbe8",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.005915692743638136,
            -0.00729220906252694
          ],
          "yaw_delta_rad": 0.44553090808215057,
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
      "step": 35,
      "object_id": "point-009",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000206",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.x_m",
      "value": -1.3314009332639403
    },
    {
      "evidence_id": "e000207",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.y_m",
      "value": 0.37486358338862014
    },
    {
      "evidence_id": "e000208",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.yaw_rad",
      "value": -0.5049762840926847
    },
    {
      "evidence_id": "e000209",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 35,
      "action": {
        "call_id": "call_43ef146e6375463e973d616e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.0007995569052364915,
            -0.019712683292423525
          ],
          "yaw_delta_rad": 0.5465087526690682,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000210",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 36,
      "observation": {
        "object_id": "point-013",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7289100234781505,
            0.385903875246704
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
            122.0,
            183.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000211",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 36,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7289100234781505,
            0.385903875246704
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00023",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00023",
          "pixel_uv": [
            122.0,
            183.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00023",
          "position_m": [
            -1.4903088090217118,
            0.02641053585608097,
            2.3525686264038086
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
      "evidence_id": "e000212",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.x_m",
      "value": -1.3314009332639403
    },
    {
      "evidence_id": "e000213",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.y_m",
      "value": 0.37486358338862014
    },
    {
      "evidence_id": "e000214",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.yaw_rad",
      "value": -0.5049762840926847
    },
    {
      "evidence_id": "e000215",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-013.range_m",
      "value": 3.0603
    },
    {
      "evidence_id": "e000216",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 36,
      "name": "point-013.bearing_rad",
      "value": 0.5086
    },
    {
      "evidence_id": "e000217",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 36,
      "action": {
        "call_id": "call_b973931a000e44cc881b1c0e",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000218",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 36,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 36,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 3,
      "recent_action_evidence_ids": [
        "e000217"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000219",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 37,
      "object_id": "point-010",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000220",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.x_m",
      "value": -1.316806575025184
    },
    {
      "evidence_id": "e000221",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.y_m",
      "value": 0.4000631018266525
    },
    {
      "evidence_id": "e000222",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.yaw_rad",
      "value": 0.04695670966466525
    },
    {
      "evidence_id": "e000223",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 37,
      "action": {
        "call_id": "call_d8d732cf78624ce4a2c65d31",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0005815857728412293,
            0.029114820622815354
          ],
          "yaw_delta_rad": 0.55193299375735,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000224",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 38,
      "observation": {
        "object_id": "point-014",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288243559517231,
            0.3857075357724057
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
            337.0,
            206.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000225",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 38,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288243559517231,
            0.3857075357724057
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00024",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00024",
          "pixel_uv": [
            337.0,
            206.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00024",
          "position_m": [
            0.15309140239441024,
            0.23182412362582125,
            2.727381467819214
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
      "evidence_id": "e000226",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.x_m",
      "value": -1.316806575025184
    },
    {
      "evidence_id": "e000227",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.y_m",
      "value": 0.4000631018266525
    },
    {
      "evidence_id": "e000228",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.yaw_rad",
      "value": 0.04695670966466525
    },
    {
      "evidence_id": "e000229",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-014.range_m",
      "value": 3.0457
    },
    {
      "evidence_id": "e000230",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 38,
      "name": "point-014.bearing_rad",
      "value": -0.0517
    },
    {
      "evidence_id": "e000231",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 38,
      "action": {
        "call_id": "call_a0cc4364cdbb447eafdc5d15",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000232",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.x_m",
      "value": -1.3076118760932343
    },
    {
      "evidence_id": "e000233",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.y_m",
      "value": 0.4222123670942432
    },
    {
      "evidence_id": "e000234",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.yaw_rad",
      "value": 0.606136055137119
    },
    {
      "evidence_id": "e000235",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 39,
      "action": {
        "call_id": "call_5a888079b3c243c2974e84ad",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010224238400240282,
            0.021693256774360695
          ],
          "yaw_delta_rad": 0.5591793454724536,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000236",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 40,
      "observation": {
        "object_id": "point-015",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            0.4726381095541048,
            1.6500457265541697
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
            320.0,
            250.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000237",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 40,
      "object_id": "point-011",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000238",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.x_m",
      "value": -1.3076118760932343
    },
    {
      "evidence_id": "e000239",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.y_m",
      "value": 0.4222123670942432
    },
    {
      "evidence_id": "e000240",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.yaw_rad",
      "value": 0.606136055137119
    },
    {
      "evidence_id": "e000241",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-015.range_m",
      "value": 2.1626
    },
    {
      "evidence_id": "e000242",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 40,
      "name": "point-015.bearing_rad",
      "value": -0.0024
    },
    {
      "evidence_id": "e000243",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 40,
      "action": {
        "call_id": "call_b382f2aa21b74ef287f87074",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000244",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 41,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000245",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.x_m",
      "value": -1.0404694374349657
    },
    {
      "evidence_id": "e000246",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.y_m",
      "value": 0.6284576386994877
    },
    {
      "evidence_id": "e000247",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.yaw_rad",
      "value": 0.6083879437807905
    },
    {
      "evidence_id": "e000248",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 41,
      "action": {
        "call_id": "call_e3c981b40b714733b7778061",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3370495919714198,
            0.01731378478864065
          ],
          "yaw_delta_rad": 0.0022518886436717622,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000249",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 42,
      "observation": {
        "object_id": "point-016",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.5585268557663294,
            0.34991380889751555
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
            590.0,
            186.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000250",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 42,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.5585268557663294,
            0.34991380889751555
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00026",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00026",
          "pixel_uv": [
            590.0,
            186.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00026",
          "position_m": [
            2.857920917970535,
            0.06867462464624206,
            3.293942928314209
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
      "evidence_id": "e000251",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 42,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288243559517231,
          0.3857075357724057
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          3.5585268557663294,
          0.34991380889751555
        ]
      },
      "evidence_ids": [
        "e000250"
      ]
    },
    {
      "evidence_id": "e000252",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 42,
      "object_id": "point-012",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000253",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.x_m",
      "value": -1.0404694374349657
    },
    {
      "evidence_id": "e000254",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.y_m",
      "value": 0.6284576386994877
    },
    {
      "evidence_id": "e000255",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.yaw_rad",
      "value": 0.6083879437807905
    },
    {
      "evidence_id": "e000256",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-016.range_m",
      "value": 4.6074
    },
    {
      "evidence_id": "e000257",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 42,
      "name": "point-016.bearing_rad",
      "value": -0.6689
    },
    {
      "evidence_id": "e000258",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 42,
      "action": {
        "call_id": "call_73d5db0fbd3640a795113f18",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000259",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.x_m",
      "value": -1.0477649617952343
    },
    {
      "evidence_id": "e000260",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.y_m",
      "value": 0.6429391884512334
    },
    {
      "evidence_id": "e000261",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.yaw_rad",
      "value": 1.056224080911588
    },
    {
      "evidence_id": "e000262",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 43,
      "action": {
        "call_id": "call_90439f6a19204797a254c227",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.002290371425855614,
            0.016052855124095076
          ],
          "yaw_delta_rad": 0.4478361371307975,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000263",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.x_m",
      "value": -1.0609770069920834
    },
    {
      "evidence_id": "e000264",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.y_m",
      "value": 0.6502064683755214
    },
    {
      "evidence_id": "e000265",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.yaw_rad",
      "value": 1.4961640716036426
    },
    {
      "evidence_id": "e000266",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 44,
      "action": {
        "call_id": "call_3ad5150f6c12491495b40cfb",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.00017628227756823385,
            0.015077812186791422
          ],
          "yaw_delta_rad": 0.4399399906920545,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000267",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 45,
      "observation": {
        "object_id": "point-017",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.9639845085235862,
            1.7569552678963694
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
            321.0,
            336.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000268",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.x_m",
      "value": -1.0609770069920834
    },
    {
      "evidence_id": "e000269",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.y_m",
      "value": 0.6502064683755214
    },
    {
      "evidence_id": "e000270",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.yaw_rad",
      "value": 1.4961640716036426
    },
    {
      "evidence_id": "e000271",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 45,
      "name": "point-017.range_m",
      "value": 1.111
    },
    {
      "evidence_id": "e000272",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 45,
      "name": "point-017.bearing_rad",
      "value": -0.0128
    },
    {
      "evidence_id": "e000273",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 45,
      "action": {
        "call_id": "call_29d5c17b05164c46a2f0adac",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000274",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 46,
      "object_id": "point-013",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000275",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.x_m",
      "value": -1.076975926363134
    },
    {
      "evidence_id": "e000276",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.y_m",
      "value": 0.6566312575462144
    },
    {
      "evidence_id": "e000277",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.yaw_rad",
      "value": 2.032725193944724
    },
    {
      "evidence_id": "e000278",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 46,
      "action": {
        "call_id": "call_30e84883dfd1496a8b88e373",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.005213977237339648,
            0.016433434768718665
          ],
          "yaw_delta_rad": 0.5365611223410811,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000279",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 47,
      "observation": {
        "object_id": "point-018",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.552828342897145,
            1.7659143808644873
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
            343.0,
            329.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000280",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.x_m",
      "value": -1.076975926363134
    },
    {
      "evidence_id": "e000281",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.y_m",
      "value": 0.6566312575462144
    },
    {
      "evidence_id": "e000282",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.yaw_rad",
      "value": 2.032725193944724
    },
    {
      "evidence_id": "e000283",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 47,
      "name": "point-018.range_m",
      "value": 1.207
    },
    {
      "evidence_id": "e000284",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 47,
      "name": "point-018.bearing_rad",
      "value": -0.0567
    },
    {
      "evidence_id": "e000285",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 47,
      "action": {
        "call_id": "call_5d52ea3c612e4f3bb27be7e8",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000286",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 48,
      "observation": {
        "object_id": "point-018",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.7156117709378118,
            1.9342161608521176
          ]
        },
        "pose_covariance": null,
        "confidence": 0.986,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00030",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00030",
          "pixel_uv": [
            328.11,
            329.68
          ]
        }
      }
    },
    {
      "evidence_id": "e000287",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 48,
      "object_id": "point-014",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000288",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.x_m",
      "value": -1.192765904619734
    },
    {
      "evidence_id": "e000289",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.y_m",
      "value": 0.8577956296125381
    },
    {
      "evidence_id": "e000290",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.yaw_rad",
      "value": 2.044688430565351
    },
    {
      "evidence_id": "e000291",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 48,
      "name": "point-018.range_m",
      "value": 1.1967
    },
    {
      "evidence_id": "e000292",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 48,
      "name": "point-018.bearing_rad",
      "value": -0.0217
    },
    {
      "evidence_id": "e000293",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 48,
      "action": {
        "call_id": "call_6e13a4f3a5ff44c7905466da",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0006",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23168601572485287,
            0.014000491814413346
          ],
          "yaw_delta_rad": 0.01196323662062726,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000294",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 48,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 48,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 4,
      "recent_action_evidence_ids": [
        "e000293"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000295",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 48,
      "plan_id": "plan-0007"
    },
    {
      "evidence_id": "e000296",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.x_m",
      "value": -1.1839249189262326
    },
    {
      "evidence_id": "e000297",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.y_m",
      "value": 0.8663353715562316
    },
    {
      "evidence_id": "e000298",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.yaw_rad",
      "value": 2.5953282667584103
    },
    {
      "evidence_id": "e000299",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 49,
      "action": {
        "call_id": "call_38212b9caee24ffb8c2a649d",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.003564042979757661,
            -0.011763835179737015
          ],
          "yaw_delta_rad": 0.5506398361930591,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000300",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 50,
      "observation": {
        "object_id": "point-019",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.1354059728358505,
            1.3696798798714043
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
            292.0,
            350.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000301",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 50,
      "object_id": "point-015",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000302",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.x_m",
      "value": -1.1839249189262326
    },
    {
      "evidence_id": "e000303",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.y_m",
      "value": 0.8663353715562316
    },
    {
      "evidence_id": "e000304",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.yaw_rad",
      "value": 2.5953282667584103
    },
    {
      "evidence_id": "e000305",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 50,
      "name": "point-019.range_m",
      "value": 1.0764
    },
    {
      "evidence_id": "e000306",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 50,
      "name": "point-019.bearing_rad",
      "value": 0.0597
    },
    {
      "evidence_id": "e000307",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 50,
      "action": {
        "call_id": "call_9f7a5b0a736e436caa83b97a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000308",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 51,
      "object_id": "point-018",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000309",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.x_m",
      "value": -1.4729778825080728
    },
    {
      "evidence_id": "e000310",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.y_m",
      "value": 1.0365542612967469
    },
    {
      "evidence_id": "e000311",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.yaw_rad",
      "value": 2.60768037613128
    },
    {
      "evidence_id": "e000312",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 51,
      "action": {
        "call_id": "call_e66432ee9957494ca374e29b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3354159352385697,
            0.004715566559172268
          ],
          "yaw_delta_rad": 0.01235210937286979,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000313",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 52,
      "object_id": "task:B",
      "old_state": "contradicted",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000314",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 52,
      "object_id": "point-016",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000315",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.x_m",
      "value": -1.466792831792867
    },
    {
      "evidence_id": "e000316",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.y_m",
      "value": 1.0426363440253414
    },
    {
      "evidence_id": "e000317",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.yaw_rad",
      "value": -3.1316357479737804
    },
    {
      "evidence_id": "e000318",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 52,
      "action": {
        "call_id": "call_63139e96900c40749fba5cbe",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.002229029630846862,
            -0.008383198051575783
          ],
          "yaw_delta_rad": 0.5438691830745253,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000319",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 53,
      "observation": {
        "object_id": "point-020",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.560250147919621,
            1.0429490881321608
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
            323.0,
            346.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000320",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.x_m",
      "value": -1.466792831792867
    },
    {
      "evidence_id": "e000321",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.y_m",
      "value": 1.0426363440253414
    },
    {
      "evidence_id": "e000322",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.yaw_rad",
      "value": -3.1316357479737804
    },
    {
      "evidence_id": "e000323",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 53,
      "name": "point-020.range_m",
      "value": 1.0934
    },
    {
      "evidence_id": "e000324",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 53,
      "name": "point-020.bearing_rad",
      "value": -0.0102
    },
    {
      "evidence_id": "e000325",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 53,
      "action": {
        "call_id": "call_1eab18f4e07045e199668917",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000326",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 54,
      "object_id": "point-018",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000327",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.x_m",
      "value": -1.4743593454473027
    },
    {
      "evidence_id": "e000328",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.y_m",
      "value": 1.025131934964493
    },
    {
      "evidence_id": "e000329",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.yaw_rad",
      "value": -2.5927307131372785
    },
    {
      "evidence_id": "e000330",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 54,
      "action": {
        "call_id": "call_b4fcfd390ac047c295b95309",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.007740425454618851,
            0.017428203557273775
          ],
          "yaw_delta_rad": 0.5389050348365019,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000331",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 55,
      "observation": {
        "object_id": "point-021",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.4835280140808673,
            0.6209677007126745
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
            394.0,
            352.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000332",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 55,
      "object_id": "point-017",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000333",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.x_m",
      "value": -1.4743593454473027
    },
    {
      "evidence_id": "e000334",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.y_m",
      "value": 1.025131934964493
    },
    {
      "evidence_id": "e000335",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.yaw_rad",
      "value": -2.5927307131372785
    },
    {
      "evidence_id": "e000336",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 55,
      "name": "point-021.range_m",
      "value": 1.087
    },
    {
      "evidence_id": "e000337",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 55,
      "name": "point-021.bearing_rad",
      "value": -0.1679
    },
    {
      "evidence_id": "e000338",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 55,
      "action": {
        "call_id": "call_62b5275a86f64ad695b04acb",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000339",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 56,
      "observation": {
        "object_id": "point-021",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.650583740993593,
            0.45901551486512787
          ]
        },
        "pose_covariance": null,
        "confidence": 0.698,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00035",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00035",
          "pixel_uv": [
            384.01,
            347.58
          ]
        }
      }
    },
    {
      "evidence_id": "e000340",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.x_m",
      "value": -1.6220124599827443
    },
    {
      "evidence_id": "e000341",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.y_m",
      "value": 0.9091039171592797
    },
    {
      "evidence_id": "e000342",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.yaw_rad",
      "value": -2.576569041834584
    },
    {
      "evidence_id": "e000343",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 56,
      "name": "point-021.range_m",
      "value": 1.1227
    },
    {
      "evidence_id": "e000344",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 56,
      "name": "point-021.bearing_rad",
      "value": -0.1526
    },
    {
      "evidence_id": "e000345",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 56,
      "action": {
        "call_id": "call_e573566cc5b14aa0bc4b3bf8",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.18649940142529642,
            0.021952594740240222
          ],
          "yaw_delta_rad": 0.016161671302694636,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000346",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.x_m",
      "value": -1.6242576967386924
    },
    {
      "evidence_id": "e000347",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.y_m",
      "value": 0.9205366890225956
    },
    {
      "evidence_id": "e000348",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.yaw_rad",
      "value": -2.132015831981855
    },
    {
      "evidence_id": "e000349",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 57,
      "action": {
        "call_id": "call_54c5fedbfdfd4039be2aa40c",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.0042252418853312036,
            -0.010858024294471337
          ],
          "yaw_delta_rad": 0.44455320985272895,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000350",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 58,
      "observation": {
        "object_id": "point-022",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.245141329154603,
            0.031158049185757267
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
            339.0,
            350.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000351",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 58,
      "object_id": "point-018",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000352",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.x_m",
      "value": -1.6242576967386924
    },
    {
      "evidence_id": "e000353",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.y_m",
      "value": 0.9205366890225956
    },
    {
      "evidence_id": "e000354",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.yaw_rad",
      "value": -2.132015831981855
    },
    {
      "evidence_id": "e000355",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 58,
      "name": "point-022.range_m",
      "value": 1.0847
    },
    {
      "evidence_id": "e000356",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 58,
      "name": "point-022.bearing_rad",
      "value": -0.0482
    },
    {
      "evidence_id": "e000357",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 58,
      "action": {
        "call_id": "call_147bbad8c1064e6a8b9354f5",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000358",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.x_m",
      "value": -1.6191578191322749
    },
    {
      "evidence_id": "e000359",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.y_m",
      "value": 0.909955931203757
    },
    {
      "evidence_id": "e000360",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.yaw_rad",
      "value": -1.5839280104643978
    },
    {
      "evidence_id": "e000361",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 59,
      "action": {
        "call_id": "call_b1ed117f43e247dc9c003523",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.006243488490343809,
            0.009948871247146347
          ],
          "yaw_delta_rad": 0.5480878215174574,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000362",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 60,
      "object_id": "point-019",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000363",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.x_m",
      "value": -1.6293873279447408
    },
    {
      "evidence_id": "e000364",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.y_m",
      "value": 0.9255316389821108
    },
    {
      "evidence_id": "e000365",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.yaw_rad",
      "value": -1.0485779603811045
    },
    {
      "evidence_id": "e000366",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 60,
      "action": {
        "call_id": "call_e12d2080530f4460834f8460",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0007",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.01544003803827168,
            -0.010433156220325104
          ],
          "yaw_delta_rad": 0.5353500500832933,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000367",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 60,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 60,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 5,
      "recent_action_evidence_ids": [
        "e000366"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000368",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.x_m",
      "value": -1.6293873279447408
    },
    {
      "evidence_id": "e000369",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.y_m",
      "value": 0.9255316389821108
    },
    {
      "evidence_id": "e000370",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.yaw_rad",
      "value": -1.0485779603811045
    },
    {
      "evidence_id": "e000371",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 61,
      "action": {
        "call_id": "call_f7652dc988aa4d76a8e1a559",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000372",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 62,
      "observation": {
        "object_id": "point-023",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.1691014125158508,
            -0.07272930689215748
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00039",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00039",
          "pixel_uv": [
            356.0,
            335.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000373",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.x_m",
      "value": -1.6293873279447408
    },
    {
      "evidence_id": "e000374",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.y_m",
      "value": 0.9255316389821108
    },
    {
      "evidence_id": "e000375",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.yaw_rad",
      "value": -1.0485779603811045
    },
    {
      "evidence_id": "e000376",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 62,
      "name": "point-023.range_m",
      "value": 1.0992
    },
    {
      "evidence_id": "e000377",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 62,
      "name": "point-023.bearing_rad",
      "value": -0.0901
    },
    {
      "evidence_id": "e000378",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 62,
      "action": {
        "call_id": "call_61d22093c6ff4066a1ad5b40",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000379",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 62,
      "plan_id": "plan-0008"
    },
    {
      "evidence_id": "e000380",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 63,
      "observation": {
        "object_id": "point-023",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.0064768572910603,
            -0.2395988388252921
          ]
        },
        "pose_covariance": null,
        "confidence": 0.973,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00040",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00040",
          "pixel_uv": [
            344.68,
            337.53
          ]
        }
      }
    },
    {
      "evidence_id": "e000381",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 63,
      "object_id": "point-020",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000382",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.x_m",
      "value": -1.5267127470426034
    },
    {
      "evidence_id": "e000383",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.y_m",
      "value": 0.7717833980240707
    },
    {
      "evidence_id": "e000384",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.yaw_rad",
      "value": -1.0315691833104303
    },
    {
      "evidence_id": "e000385",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 63,
      "name": "point-023.range_m",
      "value": 1.1374
    },
    {
      "evidence_id": "e000386",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 63,
      "name": "point-023.bearing_rad",
      "value": -0.0642
    },
    {
      "evidence_id": "e000387",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 63,
      "action": {
        "call_id": "call_12c4d9cd77b84b2aa675170d",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0008",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.18447037056047053,
            0.012299331136437663
          ],
          "yaw_delta_rad": 0.017008777070674164,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000388",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 63,
      "plan_id": "plan-0009"
    },
    {
      "evidence_id": "e000389",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.x_m",
      "value": -1.5401452075806048
    },
    {
      "evidence_id": "e000390",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.y_m",
      "value": 0.7821752894408046
    },
    {
      "evidence_id": "e000391",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.yaw_rad",
      "value": -0.48709087549546315
    },
    {
      "evidence_id": "e000392",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 64,
      "action": {
        "call_id": "call_57d2aa284984419ca1bb5a52",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0009",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.015814547245242356,
            -0.00619051684030861
          ],
          "yaw_delta_rad": 0.5444783078149671,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000393",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 65,
      "observation": {
        "object_id": "point-024",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.56311870762028,
            0.6030204351707134
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
            157.0,
            169.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000394",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 65,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.56311870762028,
            0.6030204351707134
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00041",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00041",
          "pixel_uv": [
            157.0,
            169.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00041",
          "position_m": [
            -2.225807896099237,
            -0.14382143328641225,
            4.270389080047607
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
      "evidence_id": "e000395",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.x_m",
      "value": -1.5401452075806048
    },
    {
      "evidence_id": "e000396",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.y_m",
      "value": 0.7821752894408046
    },
    {
      "evidence_id": "e000397",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.yaw_rad",
      "value": -0.48709087549546315
    },
    {
      "evidence_id": "e000398",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 65,
      "name": "point-024.range_m",
      "value": 5.1064
    },
    {
      "evidence_id": "e000399",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 65,
      "name": "point-024.bearing_rad",
      "value": 0.452
    },
    {
      "evidence_id": "e000400",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 65,
      "action": {
        "call_id": "call_7798ee93440d4cd180324abf",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000401",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 66,
      "observation": {
        "object_id": "point-024",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.5627703168735936,
            0.5466587278018553
          ]
        },
        "pose_covariance": null,
        "confidence": 0.724,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00042",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00042",
          "pixel_uv": [
            293.54,
            178.24
          ]
        }
      }
    },
    {
      "evidence_id": "e000402",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 66,
      "object_id": "point-021",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000403",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 66,
      "object_id": "point-023",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000404",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.x_m",
      "value": -1.5208747115663863
    },
    {
      "evidence_id": "e000405",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.y_m",
      "value": 0.7962302903194569
    },
    {
      "evidence_id": "e000406",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.yaw_rad",
      "value": -0.12703405799232956
    },
    {
      "evidence_id": "e000407",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 66,
      "name": "point-024.range_m",
      "value": 5.0898
    },
    {
      "evidence_id": "e000408",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 66,
      "name": "point-024.bearing_rad",
      "value": 0.078
    },
    {
      "evidence_id": "e000409",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 66,
      "action": {
        "call_id": "call_234e17be4ca54d03a812d2e4",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0009",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010450760535407201,
            0.02144007160819423
          ],
          "yaw_delta_rad": 0.3600568175031338,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000410",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 66,
      "plan_id": "plan-0010"
    },
    {
      "evidence_id": "e000411",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.x_m",
      "value": -1.510951084724814
    },
    {
      "evidence_id": "e000412",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.y_m",
      "value": 0.812925405592519
    },
    {
      "evidence_id": "e000413",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.yaw_rad",
      "value": 0.41806121819701025
    },
    {
      "evidence_id": "e000414",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 67,
      "action": {
        "call_id": "call_762d49d979f24cc09809c775",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.007728513856225602,
            0.017817837052957315
          ],
          "yaw_delta_rad": 0.5450952761893397,
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
      "step": 68,
      "observation": {
        "object_id": "point-025",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7351480619548356,
            0.7310565474983042
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
            486.0,
            179.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000416",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 68,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7351480619548356,
            0.7310565474983042
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00043",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00043",
          "pixel_uv": [
            486.0,
            179.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00043",
          "position_m": [
            1.394599708132873,
            -0.004187987111510129,
            2.611370325088501
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
      "evidence_id": "e000417",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 68,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          3.56311870762028,
          0.6030204351707134
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7351480619548356,
          0.7310565474983042
        ]
      },
      "evidence_ids": [
        "e000416"
      ]
    },
    {
      "evidence_id": "e000418",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 68,
      "object_id": "point-022",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000419",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.x_m",
      "value": -1.510951084724814
    },
    {
      "evidence_id": "e000420",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.y_m",
      "value": 0.812925405592519
    },
    {
      "evidence_id": "e000421",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.yaw_rad",
      "value": 0.41806121819701025
    },
    {
      "evidence_id": "e000422",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 68,
      "name": "point-025.range_m",
      "value": 3.2472
    },
    {
      "evidence_id": "e000423",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 68,
      "name": "point-025.bearing_rad",
      "value": -0.4433
    },
    {
      "evidence_id": "e000424",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 68,
      "action": {
        "call_id": "call_e53a4611540a48f08660748f",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000425",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 69,
      "object_id": "point-023",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000426",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.x_m",
      "value": -1.510951084724814
    },
    {
      "evidence_id": "e000427",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.y_m",
      "value": 0.812925405592519
    },
    {
      "evidence_id": "e000428",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.yaw_rad",
      "value": 0.41806121819701025
    },
    {
      "evidence_id": "e000429",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 69,
      "name": "point-025.range_m",
      "value": 3.2472
    },
    {
      "evidence_id": "e000430",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 69,
      "name": "point-025.bearing_rad",
      "value": -0.4433
    },
    {
      "evidence_id": "e000431",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 69,
      "action": {
        "call_id": "call_7308f64a0ad640358210cfdc",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000432",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.x_m",
      "value": -1.5040375207195131
    },
    {
      "evidence_id": "e000433",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.y_m",
      "value": 0.8420168162475609
    },
    {
      "evidence_id": "e000434",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.yaw_rad",
      "value": 0.9559558453488108
    },
    {
      "evidence_id": "e000435",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 70,
      "action": {
        "call_id": "call_45a1af306a8b46578cc92c22",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.018128957118447888,
            0.023779160097723174
          ],
          "yaw_delta_rad": 0.5378946271518004,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000436",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 71,
      "observation": {
        "object_id": "point-026",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -0.9683462969860226,
            1.7656672927888308
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
            279.0,
            352.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000437",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.x_m",
      "value": -1.5040375207195131
    },
    {
      "evidence_id": "e000438",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.y_m",
      "value": 0.8420168162475609
    },
    {
      "evidence_id": "e000439",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.yaw_rad",
      "value": 0.9559558453488108
    },
    {
      "evidence_id": "e000440",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 71,
      "name": "point-026.range_m",
      "value": 1.0678
    },
    {
      "evidence_id": "e000441",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 71,
      "name": "point-026.bearing_rad",
      "value": 0.0893
    },
    {
      "evidence_id": "e000442",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 71,
      "action": {
        "call_id": "call_ba8e6e77866b412abd8632e5",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000443",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.x_m",
      "value": -1.3796285132737753
    },
    {
      "evidence_id": "e000444",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.y_m",
      "value": 1.0449683890322377
    },
    {
      "evidence_id": "e000445",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.yaw_rad",
      "value": 0.9720423712415721
    },
    {
      "evidence_id": "e000446",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 72,
      "action": {
        "call_id": "call_e0bb3897edb7455bacf950f1",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.237546759183268,
            0.015442772773507321
          ],
          "yaw_delta_rad": 0.016086525892761383,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000447",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 72,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 72,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 6,
      "recent_action_evidence_ids": [
        "e000446"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000448",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 73,
      "object_id": "point-023",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000449",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.x_m",
      "value": -1.3814398074869036
    },
    {
      "evidence_id": "e000450",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.y_m",
      "value": 1.0507725700146746
    },
    {
      "evidence_id": "e000451",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.yaw_rad",
      "value": 1.4201199272301142
    },
    {
      "evidence_id": "e000452",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 73,
      "action": {
        "call_id": "call_fc01dc1342d84dc782a05681",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.003773607098382984,
            0.00476751434926291
          ],
          "yaw_delta_rad": 0.44807755598854193,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000453",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 74,
      "observation": {
        "object_id": "point-027",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.2111622505910897,
            2.1896160902656323
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
            319.0,
            339.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000454",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.x_m",
      "value": -1.3814398074869036
    },
    {
      "evidence_id": "e000455",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.y_m",
      "value": 1.0507725700146746
    },
    {
      "evidence_id": "e000456",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.yaw_rad",
      "value": 1.4201199272301142
    },
    {
      "evidence_id": "e000457",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 74,
      "name": "point-027.range_m",
      "value": 1.1515
    },
    {
      "evidence_id": "e000458",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 74,
      "name": "point-027.bearing_rad",
      "value": 0.0023
    },
    {
      "evidence_id": "e000459",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 74,
      "action": {
        "call_id": "call_81e53113979a417aba3ca16c",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000460",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 75,
      "observation": {
        "object_id": "point-027",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.2085692480224046,
            2.3531729145180145
          ]
        },
        "pose_covariance": null,
        "confidence": 0.998,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00047",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00047",
          "pixel_uv": [
            315.54,
            334.67
          ]
        }
      }
    },
    {
      "evidence_id": "e000461",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.x_m",
      "value": -1.3645619093415016
    },
    {
      "evidence_id": "e000462",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.y_m",
      "value": 1.1976425689127659
    },
    {
      "evidence_id": "e000463",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.yaw_rad",
      "value": 1.4320655203007338
    },
    {
      "evidence_id": "e000464",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 75,
      "name": "point-027.range_m",
      "value": 1.166
    },
    {
      "evidence_id": "e000465",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 75,
      "name": "point-027.bearing_rad",
      "value": 0.0046
    },
    {
      "evidence_id": "e000466",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 75,
      "action": {
        "call_id": "call_e21d269bccf040d1b2cf99b5",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.14773941731701135,
            0.00535953290519795
          ],
          "yaw_delta_rad": 0.011945593070619598,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000467",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 76,
      "object_id": "point-024",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000468",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.x_m",
      "value": -1.3618334170810278
    },
    {
      "evidence_id": "e000469",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.y_m",
      "value": 1.2122684703470443
    },
    {
      "evidence_id": "e000470",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.yaw_rad",
      "value": 1.9648876527481016
    },
    {
      "evidence_id": "e000471",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 76,
      "action": {
        "call_id": "call_bf70c86bad164d228eb86c3e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.014862693146167566,
            -0.0006797170172627158
          ],
          "yaw_delta_rad": 0.5328221324473681,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000472",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.x_m",
      "value": -1.3618334170810278
    },
    {
      "evidence_id": "e000473",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.y_m",
      "value": 1.2122684703470443
    },
    {
      "evidence_id": "e000474",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.yaw_rad",
      "value": 1.9648876527481016
    },
    {
      "evidence_id": "e000475",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 77,
      "action": {
        "call_id": "call_cf0ddd870e14430798972d63",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000476",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 78,
      "observation": {
        "object_id": "point-028",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.6188268417301654,
            2.364948594964064
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00048",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00048",
          "pixel_uv": [
            393.0,
            331.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000477",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 78,
      "object_id": "task:B",
      "old_state": "contradicted",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000478",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 78,
      "object_id": "point-025",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000479",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 78,
      "object_id": "point-027",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000480",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.x_m",
      "value": -1.3618334170810278
    },
    {
      "evidence_id": "e000481",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.y_m",
      "value": 1.2122684703470443
    },
    {
      "evidence_id": "e000482",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.yaw_rad",
      "value": 1.9648876527481016
    },
    {
      "evidence_id": "e000483",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 78,
      "name": "point-028.range_m",
      "value": 1.181
    },
    {
      "evidence_id": "e000484",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 78,
      "name": "point-028.bearing_rad",
      "value": -0.1747
    },
    {
      "evidence_id": "e000485",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 78,
      "action": {
        "call_id": "call_9c776435388d4b31adbb6c92",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000486",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.x_m",
      "value": -1.4609755368735817
    },
    {
      "evidence_id": "e000487",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.y_m",
      "value": 1.4220072273969273
    },
    {
      "evidence_id": "e000488",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.yaw_rad",
      "value": 1.9820444479464803
    },
    {
      "evidence_id": "e000489",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 79,
      "action": {
        "call_id": "call_ba58f071d83b40e895cafefc",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2317289436039115,
            0.011009215322004037
          ],
          "yaw_delta_rad": 0.01715679519837865,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000490",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 80,
      "observation": {
        "object_id": "point-029",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.7831064536091437,
            2.531871832870544
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
            375.0,
            342.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000491",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.x_m",
      "value": -1.4609755368735817
    },
    {
      "evidence_id": "e000492",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.y_m",
      "value": 1.4220072273969273
    },
    {
      "evidence_id": "e000493",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.yaw_rad",
      "value": 1.9820444479464803
    },
    {
      "evidence_id": "e000494",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-029.range_m",
      "value": 1.1557
    },
    {
      "evidence_id": "e000495",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-029.bearing_rad",
      "value": -0.1287
    },
    {
      "evidence_id": "e000496",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 80,
      "action": {
        "call_id": "call_b0229475e63b4fb8966901bb",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000497",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 81,
      "object_id": "point-026",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000498",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 81,
      "object_id": "point-027",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000499",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.x_m",
      "value": -1.4609755368735817
    },
    {
      "evidence_id": "e000500",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.y_m",
      "value": 1.4220072273969273
    },
    {
      "evidence_id": "e000501",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.yaw_rad",
      "value": 1.9820444479464803
    },
    {
      "evidence_id": "e000502",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 81,
      "name": "point-029.range_m",
      "value": 1.1557
    },
    {
      "evidence_id": "e000503",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 81,
      "name": "point-029.bearing_rad",
      "value": -0.1287
    },
    {
      "evidence_id": "e000504",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 81,
      "action": {
        "call_id": "call_4d86443fd1c6494cb34221f3",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000505",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.x_m",
      "value": -1.469133836368073
    },
    {
      "evidence_id": "e000506",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.y_m",
      "value": 1.4287839421514217
    },
    {
      "evidence_id": "e000507",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.yaw_rad",
      "value": 2.535253026367389
    },
    {
      "evidence_id": "e000508",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 82,
      "action": {
        "call_id": "call_6ba9a07877844891b20da773",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00947300023840458,
            0.004769064896683702
          ],
          "yaw_delta_rad": 0.5532085784209086,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000509",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.x_m",
      "value": -1.4911107272862871
    },
    {
      "evidence_id": "e000510",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.y_m",
      "value": 1.428573654615443
    },
    {
      "evidence_id": "e000511",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.yaw_rad",
      "value": 3.0694486774974936
    },
    {
      "evidence_id": "e000512",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 83,
      "action": {
        "call_id": "call_0c595c72360b4836b988e797",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.017939442658286862,
            0.01269662759904815
          ],
          "yaw_delta_rad": 0.5341956511301045,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000513",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 84,
      "observation": {
        "object_id": "point-030",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.641952848894068,
            1.4598092294189036
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
            300.0,
            339.0
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
      "value": -1.4911107272862871
    },
    {
      "evidence_id": "e000515",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.y_m",
      "value": 1.428573654615443
    },
    {
      "evidence_id": "e000516",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.yaw_rad",
      "value": 3.0694486774974936
    },
    {
      "evidence_id": "e000517",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 84,
      "name": "point-030.range_m",
      "value": 1.1512
    },
    {
      "evidence_id": "e000518",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 84,
      "name": "point-030.bearing_rad",
      "value": 0.045
    },
    {
      "evidence_id": "e000519",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 84,
      "action": {
        "call_id": "call_3a32cfa813fb4536aec92516",
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
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 85,
      "object_id": "point-027",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000522",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.x_m",
      "value": -1.76733126217947
    },
    {
      "evidence_id": "e000523",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.y_m",
      "value": 1.445507319909676
    },
    {
      "evidence_id": "e000524",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.yaw_rad",
      "value": 3.0901020958856478
    },
    {
      "evidence_id": "e000525",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 85,
      "action": {
        "call_id": "call_f9d75765c35b4d7d800e5a42",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.276722619226784,
            0.003020749119245653
          ],
          "yaw_delta_rad": 0.020653418388154154,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000526",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.x_m",
      "value": -1.76733126217947
    },
    {
      "evidence_id": "e000527",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.y_m",
      "value": 1.445507319909676
    },
    {
      "evidence_id": "e000528",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.yaw_rad",
      "value": 3.0901020958856478
    },
    {
      "evidence_id": "e000529",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 86,
      "action": {
        "call_id": "call_0f2dbb200d854cec9df50e10",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000530",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.x_m",
      "value": -1.7816895003925795
    },
    {
      "evidence_id": "e000531",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.y_m",
      "value": 1.446402722420509
    },
    {
      "evidence_id": "e000532",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.yaw_rad",
      "value": -2.6461461776048334
    },
    {
      "evidence_id": "e000533",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 87,
      "action": {
        "call_id": "call_4a2bae5e3af14112a186cd80",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.014385292985472389,
            -0.00015522874386580303
          ],
          "yaw_delta_rad": 0.5469370336891046,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000534",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 88,
      "observation": {
        "object_id": "point-031",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.901221990145237,
            1.0495279633488135
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00054",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00054",
          "pixel_uv": [
            384.0,
            340.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000535",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 88,
      "object_id": "point-028",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000536",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.x_m",
      "value": -1.7816895003925795
    },
    {
      "evidence_id": "e000537",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.y_m",
      "value": 1.446402722420509
    },
    {
      "evidence_id": "e000538",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.yaw_rad",
      "value": -2.6461461776048334
    },
    {
      "evidence_id": "e000539",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 88,
      "name": "point-031.range_m",
      "value": 1.1878
    },
    {
      "evidence_id": "e000540",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 88,
      "name": "point-031.bearing_rad",
      "value": -0.1548
    },
    {
      "evidence_id": "e000541",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 88,
      "action": {
        "call_id": "call_d502f0f549c7441084e881d1",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000542",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.x_m",
      "value": -1.7873395408049388
    },
    {
      "evidence_id": "e000543",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.y_m",
      "value": 1.425910603266523
    },
    {
      "evidence_id": "e000544",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.yaw_rad",
      "value": -2.243649491167448
    },
    {
      "evidence_id": "e000545",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 89,
      "action": {
        "call_id": "call_30169fb37a174fc5a5633663",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.014713115231711683,
            0.015341908103649632
          ],
          "yaw_delta_rad": 0.40249668643738534,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000546",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 90,
      "observation": {
        "object_id": "point-032",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.4921595625798347,
            0.5441957588268734
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
            319.0,
            342.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000547",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 90,
      "object_id": "point-029",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000548",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.x_m",
      "value": -1.7873395408049388
    },
    {
      "evidence_id": "e000549",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.y_m",
      "value": 1.425910603266523
    },
    {
      "evidence_id": "e000550",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.yaw_rad",
      "value": -2.243649491167448
    },
    {
      "evidence_id": "e000551",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 90,
      "name": "point-032.range_m",
      "value": 1.1288
    },
    {
      "evidence_id": "e000552",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 90,
      "name": "point-032.bearing_rad",
      "value": -0.0015
    },
    {
      "evidence_id": "e000553",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 90,
      "action": {
        "call_id": "call_3bf39e7c08e04d8eaa1778a9",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000554",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 91,
      "observation": {
        "object_id": "point-032",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.6626690431494624,
            0.37928903648020923
          ]
        },
        "pose_covariance": null,
        "confidence": 0.993,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00056",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00056",
          "pixel_uv": [
            333.28,
            344.31
          ]
        }
      }
    },
    {
      "evidence_id": "e000555",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.x_m",
      "value": -1.9260685023478115
    },
    {
      "evidence_id": "e000556",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.y_m",
      "value": 1.2376868074994003
    },
    {
      "evidence_id": "e000557",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.yaw_rad",
      "value": -2.241955757980595
    },
    {
      "evidence_id": "e000558",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 91,
      "name": "point-032.range_m",
      "value": 1.1311
    },
    {
      "evidence_id": "e000559",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 91,
      "name": "point-032.bearing_rad",
      "value": -0.0381
    },
    {
      "evidence_id": "e000560",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 91,
      "action": {
        "call_id": "call_e515ce563767486797892a3b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23365843848970852,
            0.008812274751644436
          ],
          "yaw_delta_rad": 0.0016937331868529526,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000561",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.x_m",
      "value": -1.936152561140939
    },
    {
      "evidence_id": "e000562",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.y_m",
      "value": 1.2415926059518003
    },
    {
      "evidence_id": "e000563",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.yaw_rad",
      "value": -1.7945624152188089
    },
    {
      "evidence_id": "e000564",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 92,
      "action": {
        "call_id": "call_7fe3b1fd05274f019bf6c69a",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0032125840017404755,
            -0.010325832040362738
          ],
          "yaw_delta_rad": 0.44739334276178644,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000565",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.x_m",
      "value": -1.9277176290346802
    },
    {
      "evidence_id": "e000566",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.y_m",
      "value": 1.2302209256965695
    },
    {
      "evidence_id": "e000567",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.yaw_rad",
      "value": -1.3451032169790607
    },
    {
      "evidence_id": "e000568",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 93,
      "action": {
        "call_id": "call_9d7d5831d3f34b618b1f5a8e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.009216429042122226,
            0.010748052250334837
          ],
          "yaw_delta_rad": 0.4494591982397482,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000569",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 94,
      "object_id": "point-030",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000570",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 94,
      "object_id": "point-032",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000571",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.x_m",
      "value": -1.9319370550900825
    },
    {
      "evidence_id": "e000572",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.y_m",
      "value": 1.2062043338073114
    },
    {
      "evidence_id": "e000573",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.yaw_rad",
      "value": -1.9045838082108122
    },
    {
      "evidence_id": "e000574",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 94,
      "action": {
        "call_id": "call_20424992f123487987f744af",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "scan_view",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.022463281382188123,
            -0.009486897899568246
          ],
          "yaw_delta_rad": -0.5594805912317513,
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
      "step": 95,
      "observation": {
        "object_id": "point-033",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.332478534316229,
            0.12559028456524743
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
            329.0,
            342.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000576",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.x_m",
      "value": -1.9319370550900825
    },
    {
      "evidence_id": "e000577",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.y_m",
      "value": 1.2062043338073114
    },
    {
      "evidence_id": "e000578",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.yaw_rad",
      "value": -1.9045838082108122
    },
    {
      "evidence_id": "e000579",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 95,
      "name": "point-033.range_m",
      "value": 1.1525
    },
    {
      "evidence_id": "e000580",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 95,
      "name": "point-033.bearing_rad",
      "value": -0.0212
    },
    {
      "evidence_id": "e000581",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 95,
      "action": {
        "call_id": "call_fcf375af9c3f4c36bfb386d5",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000582",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.x_m",
      "value": -1.9986927258394558
    },
    {
      "evidence_id": "e000583",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.y_m",
      "value": 0.984127450457685
    },
    {
      "evidence_id": "e000584",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.yaw_rad",
      "value": -1.8935457316568451
    },
    {
      "evidence_id": "e000585",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 96,
      "action": {
        "call_id": "call_24d9c8859fdf44ab8f596efa",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0010",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23169081983589435,
            0.009686366669367813
          ],
          "yaw_delta_rad": 0.011038076553966825,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000586",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 96,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 96,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 8,
      "recent_action_evidence_ids": [
        "e000585"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000587",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 96,
      "plan_id": "plan-0011"
    },
    {
      "evidence_id": "e000588",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 97,
      "object_id": "point-032",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000589",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.x_m",
      "value": -1.9817666074126914
    },
    {
      "evidence_id": "e000590",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.y_m",
      "value": 0.9697712359036437
    },
    {
      "evidence_id": "e000591",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.yaw_rad",
      "value": -1.3572901943421665
    },
    {
      "evidence_id": "e000592",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 97,
      "action": {
        "call_id": "call_3393fe4a3a1440afa607a6cd",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0011",
        "subgoal_id": "scan_for_targets",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.008246414550509578,
            0.020605606721949773
          ],
          "yaw_delta_rad": 0.5362555373146787,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000593",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 98,
      "object_id": "point-031",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000594",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.x_m",
      "value": -1.971559174165546
    },
    {
      "evidence_id": "e000595",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.y_m",
      "value": 0.9525236809838116
    },
    {
      "evidence_id": "e000596",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.yaw_rad",
      "value": -0.8125036176705527
    },
    {
      "evidence_id": "e000597",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 98,
      "action": {
        "call_id": "call_e3ae305dedb2431eac26caa4",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0011",
        "subgoal_id": "scan_for_targets",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01901876195868531,
            0.0063211183952222375
          ],
          "yaw_delta_rad": 0.5447865766716138,
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
      "step": 99,
      "observation": {
        "object_id": "point-034",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7287948575177499,
            0.38293231850964426
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00062",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00062",
          "pixel_uv": [
            48.0,
            208.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000599",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 99,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7287948575177499,
            0.38293231850964426
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00062",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00062",
          "pixel_uv": [
            48.0,
            208.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00062",
          "position_m": [
            -2.2975208246528,
            0.24117621916244864,
            2.638291358947754
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
      "evidence_id": "e000600",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.x_m",
      "value": -1.971559174165546
    },
    {
      "evidence_id": "e000601",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.y_m",
      "value": 0.9525236809838116
    },
    {
      "evidence_id": "e000602",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.yaw_rad",
      "value": -0.8125036176705527
    },
    {
      "evidence_id": "e000603",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 99,
      "name": "point-034.range_m",
      "value": 3.7439
    },
    {
      "evidence_id": "e000604",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 99,
      "name": "point-034.bearing_rad",
      "value": 0.6598
    },
    {
      "evidence_id": "e000605",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 99,
      "action": {
        "call_id": "call_c1b5a266f0ef4831b523619a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000606",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.x_m",
      "value": -1.9429349642157752
    },
    {
      "evidence_id": "e000607",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.y_m",
      "value": 0.9552809924939454
    },
    {
      "evidence_id": "e000608",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.yaw_rad",
      "value": -0.2595170007410151
    },
    {
      "evidence_id": "e000609",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 100,
      "action": {
        "call_id": "call_e9ca2f34219c4d2196efb380",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0011",
        "subgoal_id": "scan_for_targets",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.017682541850662765,
            0.022677651459356418
          ],
          "yaw_delta_rad": 0.5529866169295374,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000610",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 101,
      "observation": {
        "object_id": "point-035",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7332614398753667,
            0.624026032459596
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00063",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00063",
          "pixel_uv": [
            261.0,
            178.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000611",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 101,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7332614398753667,
            0.624026032459596
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00063",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00063",
          "pixel_uv": [
            261.0,
            178.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00063",
          "position_m": [
            -0.6224184520994362,
            -0.015959447489729134,
            3.3171088695526123
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
      "evidence_id": "e000612",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 101,
      "object_id": "point-032",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000613",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.x_m",
      "value": -1.9429349642157752
    },
    {
      "evidence_id": "e000614",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.y_m",
      "value": 0.9552809924939454
    },
    {
      "evidence_id": "e000615",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.yaw_rad",
      "value": -0.2595170007410151
    },
    {
      "evidence_id": "e000616",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 101,
      "name": "point-035.range_m",
      "value": 3.6911
    },
    {
      "evidence_id": "e000617",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 101,
      "name": "point-035.bearing_rad",
      "value": 0.1697
    },
    {
      "evidence_id": "e000618",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 101,
      "action": {
        "call_id": "call_979ff029b1d649e18933466f",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000619",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 101,
      "plan_id": "plan-0012"
    },
    {
      "evidence_id": "e000620",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 102,
      "observation": {
        "object_id": "point-035",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7337469027696255,
            0.6316866157030975
          ]
        },
        "pose_covariance": null,
        "confidence": 0.998,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00064",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00064",
          "pixel_uv": [
            263.82,
            179.91
          ]
        }
      }
    },
    {
      "evidence_id": "e000621",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 102,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7337469027696255,
            0.6316866157030975
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00064",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00064",
          "pixel_uv": [
            263.82,
            179.91
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00064",
          "position_m": [
            -0.5508423536412442,
            0.004962543726497695,
            3.0943360328674316
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
      "evidence_id": "e000622",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.x_m",
      "value": -1.7146781722247129
    },
    {
      "evidence_id": "e000623",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.y_m",
      "value": 0.9066153194615343
    },
    {
      "evidence_id": "e000624",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.yaw_rad",
      "value": -0.24024861657398497
    },
    {
      "evidence_id": "e000625",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 102,
      "name": "point-035.range_m",
      "value": 3.4594
    },
    {
      "evidence_id": "e000626",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 102,
      "name": "point-035.bearing_rad",
      "value": 0.1607
    },
    {
      "evidence_id": "e000627",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 102,
      "action": {
        "call_id": "call_3fcda327506c4a64a3423aab",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0012",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23310167423003222,
            0.011537776774772274
          ],
          "yaw_delta_rad": 0.019268384167030028,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000628",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.x_m",
      "value": -1.389975720792266
    },
    {
      "evidence_id": "e000629",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.y_m",
      "value": 0.8371526513716818
    },
    {
      "evidence_id": "e000630",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.yaw_rad",
      "value": -0.22954617850534154
    },
    {
      "evidence_id": "e000631",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 103,
      "action": {
        "call_id": "call_5fc60c28d5b042fc943c234b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0012",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.3319048556996421,
            0.009793415512535208
          ],
          "yaw_delta_rad": 0.01070243806864335,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000632",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 103,
      "plan_id": "plan-0013"
    },
    {
      "evidence_id": "e000633",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.x_m",
      "value": -1.3773536145578424
    },
    {
      "evidence_id": "e000634",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.y_m",
      "value": 0.8348367813856932
    },
    {
      "evidence_id": "e000635",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.yaw_rad",
      "value": 0.30223935782427114
    },
    {
      "evidence_id": "e000636",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 104,
      "action": {
        "call_id": "call_632d5b90074e4870a44a201a",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01281796824076506,
            0.0006168547347792756
          ],
          "yaw_delta_rad": 0.5317855363296129,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000637",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 105,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000638",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 105,
      "object_id": "point-033",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000639",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 105,
      "object_id": "point-035",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000640",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.x_m",
      "value": -1.3727205873427524
    },
    {
      "evidence_id": "e000641",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.y_m",
      "value": 0.8588688254930553
    },
    {
      "evidence_id": "e000642",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.yaw_rad",
      "value": 0.8570451101116602
    },
    {
      "evidence_id": "e000643",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 105,
      "action": {
        "call_id": "call_01555bdb2f4449138c163a9d",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01157637234459967,
            0.021563665933536192
          ],
          "yaw_delta_rad": 0.5548057522873888,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000644",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.x_m",
      "value": -1.3852570803140212
    },
    {
      "evidence_id": "e000645",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.y_m",
      "value": 0.8759599437324554
    },
    {
      "evidence_id": "e000646",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.yaw_rad",
      "value": 1.4062695795324838
    },
    {
      "evidence_id": "e000647",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 106,
      "action": {
        "call_id": "call_de0fb0e4830c4a8e9bf42d20",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0047120552396002074,
            0.02066558767881478
          ],
          "yaw_delta_rad": 0.5492244694208237,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000648",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 107,
      "observation": {
        "object_id": "point-036",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.2125597034692894,
            2.0187062918040426
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00068",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00068",
          "pixel_uv": [
            316.0,
            345.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000649",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.x_m",
      "value": -1.3852570803140212
    },
    {
      "evidence_id": "e000650",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.y_m",
      "value": 0.8759599437324554
    },
    {
      "evidence_id": "e000651",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.yaw_rad",
      "value": 1.4062695795324838
    },
    {
      "evidence_id": "e000652",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 107,
      "name": "point-036.range_m",
      "value": 1.1557
    },
    {
      "evidence_id": "e000653",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 107,
      "name": "point-036.bearing_rad",
      "value": 0.0145
    },
    {
      "evidence_id": "e000654",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 107,
      "action": {
        "call_id": "call_5df7eaf635cb4f279667cb6f",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000655",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 108,
      "object_id": "task:B",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000656",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 108,
      "object_id": "point-035",
      "old_state": "predicted",
      "state": "unknown",
      "unobserved_steps": 6
    },
    {
      "evidence_id": "e000657",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.x_m",
      "value": -1.3852570803140212
    },
    {
      "evidence_id": "e000658",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.y_m",
      "value": 0.8759599437324554
    },
    {
      "evidence_id": "e000659",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.yaw_rad",
      "value": 1.4062695795324838
    },
    {
      "evidence_id": "e000660",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 108,
      "name": "point-036.range_m",
      "value": 1.1557
    },
    {
      "evidence_id": "e000661",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 108,
      "name": "point-036.bearing_rad",
      "value": 0.0145
    },
    {
      "evidence_id": "e000662",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 108,
      "action": {
        "call_id": "call_d5144a73001a4817a201b2e8",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000663",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 108,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 108,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 9,
      "recent_action_evidence_ids": [
        "e000662"
      ],
      "advisory_only": true
    },
    {
      "evidence_id": "e000664",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 109,
      "object_id": "point-034",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000665",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.x_m",
      "value": -1.340115959156814
    },
    {
      "evidence_id": "e000666",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.y_m",
      "value": 1.1501399394289586
    },
    {
      "evidence_id": "e000667",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.yaw_rad",
      "value": 1.4099586173728473
    },
    {
      "evidence_id": "e000668",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 109,
      "action": {
        "call_id": "call_ca1feb8fae12463b94d20f5a",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.27787092346464815,
            0.0003751697854243105
          ],
          "yaw_delta_rad": 0.0036890378403633406,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000669",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.x_m",
      "value": -1.3397310453695408
    },
    {
      "evidence_id": "e000670",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.y_m",
      "value": 1.169698224121344
    },
    {
      "evidence_id": "e000671",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.yaw_rad",
      "value": 1.8539837787997397
    },
    {
      "evidence_id": "e000672",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 110,
      "action": {
        "call_id": "call_c38acb2a1cb042da9265da1d",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.019367497274971956,
            0.002752218747844098
          ],
          "yaw_delta_rad": 0.4440251614268922,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000673",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 111,
      "observation": {
        "object_id": "point-037",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.4550934628679877,
            2.2668644114552934
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00070",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00070",
          "pixel_uv": [
            400.0,
            354.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000674",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.x_m",
      "value": -1.3397310453695408
    },
    {
      "evidence_id": "e000675",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.y_m",
      "value": 1.169698224121344
    },
    {
      "evidence_id": "e000676",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.yaw_rad",
      "value": 1.8539837787997397
    },
    {
      "evidence_id": "e000677",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 111,
      "name": "point-037.range_m",
      "value": 1.1032
    },
    {
      "evidence_id": "e000678",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 111,
      "name": "point-037.bearing_rad",
      "value": -0.1784
    },
    {
      "evidence_id": "e000679",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 111,
      "action": {
        "call_id": "call_c8649424f69e466396e9395d",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000680",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 112,
      "object_id": "task:B",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000681",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 112,
      "object_id": "point-035",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000682",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.x_m",
      "value": -1.4165534568187585
    },
    {
      "evidence_id": "e000683",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.y_m",
      "value": 1.3934848997693219
    },
    {
      "evidence_id": "e000684",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.yaw_rad",
      "value": 1.8609529522238737
    },
    {
      "evidence_id": "e000685",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 112,
      "action": {
        "call_id": "call_8787093445794cb3ae02f691",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23633871296593764,
            0.011232624450691661
          ],
          "yaw_delta_rad": 0.006969173424133945,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000686",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.x_m",
      "value": -1.497044696186071
    },
    {
      "evidence_id": "e000687",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.y_m",
      "value": 1.6130661951991936
    },
    {
      "evidence_id": "e000688",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.yaw_rad",
      "value": 1.8744819525018852
    },
    {
      "evidence_id": "e000689",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 113,
      "action": {
        "call_id": "call_73c2f07101fc4ab3aa74688b",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.23343132374153602,
            0.01430391603095972
          ],
          "yaw_delta_rad": 0.013529000278011516,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000690",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.x_m",
      "value": -1.497044696186071
    },
    {
      "evidence_id": "e000691",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.y_m",
      "value": 1.6130661951991936
    },
    {
      "evidence_id": "e000692",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.yaw_rad",
      "value": 1.8744819525018852
    },
    {
      "evidence_id": "e000693",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 114,
      "action": {
        "call_id": "call_fc6c03ff744d4ec68bfca546",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000694",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 115,
      "observation": {
        "object_id": "point-038",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -1.782462834853204,
            2.8555709743126543
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00073",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00073",
          "pixel_uv": [
            351.0,
            321.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000695",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.x_m",
      "value": -1.497044696186071
    },
    {
      "evidence_id": "e000696",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.y_m",
      "value": 1.6130661951991936
    },
    {
      "evidence_id": "e000697",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.yaw_rad",
      "value": 1.8744819525018852
    },
    {
      "evidence_id": "e000698",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 115,
      "name": "point-038.range_m",
      "value": 1.2749
    },
    {
      "evidence_id": "e000699",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 115,
      "name": "point-038.bearing_rad",
      "value": -0.0779
    },
    {
      "evidence_id": "e000700",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 115,
      "action": {
        "call_id": "call_7f8a4eefe401486f9ce5c609",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000701",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.x_m",
      "value": -1.576920035820003
    },
    {
      "evidence_id": "e000702",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.y_m",
      "value": 1.8287989082973453
    },
    {
      "evidence_id": "e000703",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.yaw_rad",
      "value": 1.894842785870383
    },
    {
      "evidence_id": "e000704",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 116,
      "action": {
        "call_id": "call_e7c5992dd7bf433baa947735",
        "tool": "move_relative",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "explore_viewpoint",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.2297468203812905,
            0.011707771223101723
          ],
          "yaw_delta_rad": 0.02036083336849792,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000705",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 117,
      "object_id": "point-036",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000706",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.x_m",
      "value": -1.5853874955650893
    },
    {
      "evidence_id": "e000707",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.y_m",
      "value": 1.8324604644618954
    },
    {
      "evidence_id": "e000708",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.yaw_rad",
      "value": 2.4312802453615165
    },
    {
      "evidence_id": "e000709",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 117,
      "action": {
        "call_id": "call_8eceeaff9eff494995c0db25",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.006167071294890825,
            0.006860910998150489
          ],
          "yaw_delta_rad": 0.5364374594911334,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000710",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 118,
      "observation": {
        "object_id": "point-039",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.4489750409057915,
            2.5418376078295264
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00075",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00075",
          "pixel_uv": [
            308.0,
            347.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000711",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.x_m",
      "value": -1.5853874955650893
    },
    {
      "evidence_id": "e000712",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.y_m",
      "value": 1.8324604644618954
    },
    {
      "evidence_id": "e000713",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.yaw_rad",
      "value": 2.4312802453615165
    },
    {
      "evidence_id": "e000714",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 118,
      "name": "point-039.range_m",
      "value": 1.1176
    },
    {
      "evidence_id": "e000715",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 118,
      "name": "point-039.bearing_rad",
      "value": 0.0226
    },
    {
      "evidence_id": "e000716",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 118,
      "action": {
        "call_id": "call_742b46e80ec947aa8c3b3751",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000717",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.x_m",
      "value": -1.6090542446197496
    },
    {
      "evidence_id": "e000718",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.y_m",
      "value": 1.8206262467142207
    },
    {
      "evidence_id": "e000719",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.yaw_rad",
      "value": 2.9890491631736364
    },
    {
      "evidence_id": "e000720",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 119,
      "action": {
        "call_id": "call_68daf123223f42cdb3041a0e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0013",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01022639373087062,
            0.02440460185655281
          ],
          "yaw_delta_rad": 0.5577689178121199,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000721",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 120,
      "observation": {
        "object_id": "point-040",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            -2.710137898414841,
            1.9601590290460116
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00076",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00076",
          "pixel_uv": [
            306.0,
            344.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000722",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.x_m",
      "value": -1.6090542446197496
    },
    {
      "evidence_id": "e000723",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.y_m",
      "value": 1.8206262467142207
    },
    {
      "evidence_id": "e000724",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.yaw_rad",
      "value": 2.9890491631736364
    },
    {
      "evidence_id": "e000725",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 120,
      "name": "point-040.range_m",
      "value": 1.1099
    },
    {
      "evidence_id": "e000726",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 120,
      "name": "point-040.bearing_rad",
      "value": 0.0265
    },
    {
      "evidence_id": "e000727",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 120,
      "action": {
        "call_id": "call_cd27dcf430f8458cbd3cab5e",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000728",
      "kind": "search_review_due",
      "source": "memory_verifier",
      "step": 120,
      "reason": "no_first_task_observation_within_search_budget",
      "decisions_since_task_novelty": 120,
      "last_task_novelty_step": 0,
      "review_interval_decisions": 12,
      "window_index": 10,
      "recent_action_evidence_ids": [
        "e000727"
      ],
      "advisory_only": true
    }
  ]
}
```

## 操作经验

## 程序工具
