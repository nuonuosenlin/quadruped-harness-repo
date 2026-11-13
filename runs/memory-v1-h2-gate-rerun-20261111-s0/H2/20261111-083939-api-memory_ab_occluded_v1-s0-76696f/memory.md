# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 120,
    "revision": 125,
    "active_plan_id": "plan-0004",
    "public_context": {
      "image_id": "frame-00100",
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
        "image_id": "frame-00100",
        "image_size": {
          "width": 640,
          "height": 360
        },
        "tracked_points": [
          {
            "point_id": "point-020",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
            "valid": true,
            "pixel_uv": [
              317.0,
              183.0
            ],
            "relative_xy_m": [
              1.8293,
              0.0127
            ],
            "range_m": 1.8294,
            "bearing_rad": 0.007,
            "confidence": 1.0,
            "loss_reason": null,
            "source": "rgbd_optical_flow"
          },
          {
            "point_id": "point-013",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
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
            "point_id": "point-014",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
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
            "point_id": "point-015",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
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
            "point_id": "point-016",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
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
            "point_id": "point-017",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
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
            "point_id": "point-018",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
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
            "point_id": "point-019",
            "image_id": "frame-00100",
            "timestamp_s": 236.12000000039933,
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
        "target_candidates": [
          {
            "object_id": "task:B",
            "task_label": "B",
            "description": "绿方块",
            "color": "green",
            "image_id": "frame-00100",
            "pixel_uv": [
              317,
              183
            ],
            "camera_xyz_m": [
              -0.012096744867433333,
              0.016935442814406666,
              1.5085567235946655
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
          "image_id": "frame-00100",
          "pixel_uv": [
            204.0,
            189.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            317.0,
            183.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            595.0,
            196.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            597.0,
            15.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            207.0,
            37.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            469.0,
            110.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            305.0,
            170.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            470.0,
            50.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            305.0,
            69.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            468.0,
            183.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            305.0,
            114.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            323.0,
            240.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            322.0,
            258.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            373.0,
            335.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            375.0,
            354.0
          ],
          "source": "rgb_corner_detector",
          "category": "unclassified_visual_feature"
        },
        {
          "image_id": "frame-00100",
          "pixel_uv": [
            245.0,
            249.0
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
      -0.08491613033242727,
      0.14496089750037075
    ],
    "yaw_rad": 0.12384347185088797,
    "source": "simulated_proprioception",
    "provenance": "existing_public_idealized_simulator_odometry"
  },
  "objects": [
    {
      "object_id": "point-001",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354,
          0.7421
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00001",
        "pixel_uv": [
          156.0,
          248.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 1,
      "evidence_ids": [
        "e000004"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "task:B",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288048201410928,
          0.38353183834067883
        ]
      },
      "category": "task_target",
      "confidence": 0.95,
      "visual_feature": {
        "image_id": "frame-00100",
        "pixel_uv": [
          317.0,
          183.0
        ]
      },
      "source": "task_label_rgbd_tracking",
      "anchor_node": null,
      "state": "confirmed",
      "last_seen": 120,
      "evidence_ids": [
        "e000005",
        "e000022",
        "e000034",
        "e000099",
        "e000116",
        "e000188",
        "e000200",
        "e000225",
        "e000281",
        "e000293",
        "e000322",
        "e000380",
        "e000396",
        "e000411",
        "e000472",
        "e000488",
        "e000500",
        "e000522",
        "e000589",
        "e000601"
      ],
      "candidate_pose": null,
      "task_label": "B",
      "label_description": "绿方块",
      "camera_pose": {
        "frame": "current_camera_optical",
        "image_id": "frame-00100",
        "position_m": [
          -0.012096744867433333,
          0.016935442814406666,
          1.5085567235946655
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
      "object_id": "point-002",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7393738185676924,
          0.382003556520252
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00003",
        "pixel_uv": [
          234.0,
          174.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 4,
      "evidence_ids": [
        "e000021"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-003",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.4023327436808373,
          1.0034175641810097
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00004",
        "pixel_uv": [
          384.0,
          235.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 6,
      "evidence_ids": [
        "e000033"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-004",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7289053975452315,
          0.38859899143529847
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00017",
        "pixel_uv": [
          127.0,
          282.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 20,
      "evidence_ids": [
        "e000098"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-005",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.808891831001307,
          0.4879328252178292
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00019",
        "pixel_uv": [
          591.0,
          182.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 23,
      "evidence_ids": [
        "e000115"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-006",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7354859052592504,
          0.3821052711022028
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00034",
        "pixel_uv": [
          20.0,
          193.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 39,
      "evidence_ids": [
        "e000187"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-007",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7353858588714828,
          0.7419368256821057
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00035",
        "pixel_uv": [
          167.0,
          251.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 41,
      "evidence_ids": [
        "e000199"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-008",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7342863290842825,
          0.6852968235508405
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00039",
        "pixel_uv": [
          630.0,
          292.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 46,
      "evidence_ids": [
        "e000224"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-009",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288757019836785,
          0.3889285043101871
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00050",
        "pixel_uv": [
          153.0,
          284.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 58,
      "evidence_ids": [
        "e000280"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-010",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7315112103171602,
          0.3821811098989973
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00051",
        "pixel_uv": [
          336.0,
          185.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 60,
      "evidence_ids": [
        "e000292"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-011",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          2.8030046064675997,
          0.414336577286907
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00056",
        "pixel_uv": [
          552.0,
          244.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 66,
      "evidence_ids": [
        "e000321"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-012",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.772913822102048,
          0.3807952714390636
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 0.239,
      "visual_feature": {
        "image_id": "frame-00068",
        "pixel_uv": [
          395.15,
          257.83
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 79,
      "evidence_ids": [
        "e000379",
        "e000388"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-013",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          3.5644271928668174,
          0.6707092282798046
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00068",
        "pixel_uv": [
          386.0,
          177.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 80,
      "evidence_ids": [
        "e000395"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-014",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7339286944445838,
          0.6625421118502557
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00069",
        "pixel_uv": [
          617.0,
          304.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 82,
      "evidence_ids": [
        "e000410"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-015",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.882980351193795,
          0.3793671784950846
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00081",
        "pixel_uv": [
          184.0,
          270.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 95,
      "evidence_ids": [
        "e000471"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-016",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7289218991869801,
          0.38980959013163663
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00083",
        "pixel_uv": [
          133.0,
          272.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 98,
      "evidence_ids": [
        "e000487"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-017",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.728840642044429,
          0.3861067169094535
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00084",
        "pixel_uv": [
          324.0,
          183.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 100,
      "evidence_ids": [
        "e000499"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-018",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.8590894632132973,
          0.566667624794196
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00087",
        "pixel_uv": [
          588.0,
          179.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "stale",
      "last_seen": 104,
      "evidence_ids": [
        "e000521"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-019",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7431237530184007,
          0.38200652915516187
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00099",
        "pixel_uv": [
          129.0,
          272.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "unknown",
      "last_seen": 118,
      "evidence_ids": [
        "e000588"
      ],
      "candidate_pose": null
    },
    {
      "object_id": "point-020",
      "pose_covariance": null,
      "pose": {
        "frame": "episode_start",
        "position_m": [
          1.7288048201410928,
          0.38353183834067883
        ]
      },
      "category": "unclassified_landmark",
      "confidence": 1.0,
      "visual_feature": {
        "image_id": "frame-00100",
        "pixel_uv": [
          317.0,
          183.0
        ]
      },
      "source": "rgbd_optical_flow",
      "anchor_node": null,
      "state": "unknown",
      "last_seen": 120,
      "evidence_ids": [
        "e000600"
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
      "step": 6,
      "evidence_ids": [
        "e000034",
        "e000035"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-2",
      "kind": "replan_required",
      "step": 6,
      "evidence_ids": [
        "e000034"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-3",
      "kind": "target_state_changed",
      "step": 11,
      "evidence_ids": [
        "e000058"
      ],
      "object_id": "point-001",
      "state": "stale"
    },
    {
      "event_id": "event-4",
      "kind": "replan_required",
      "step": 11,
      "evidence_ids": [
        "e000058"
      ],
      "object_id": "point-001",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-5",
      "kind": "target_state_changed",
      "step": 14,
      "evidence_ids": [
        "e000071"
      ],
      "object_id": "point-002",
      "state": "stale"
    },
    {
      "event_id": "event-6",
      "kind": "replan_required",
      "step": 14,
      "evidence_ids": [
        "e000071"
      ],
      "object_id": "point-002",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-7",
      "kind": "target_state_changed",
      "step": 16,
      "evidence_ids": [
        "e000080"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-8",
      "kind": "replan_required",
      "step": 16,
      "evidence_ids": [
        "e000080"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-9",
      "kind": "target_state_changed",
      "step": 16,
      "evidence_ids": [
        "e000081"
      ],
      "object_id": "point-003",
      "state": "stale"
    },
    {
      "event_id": "event-10",
      "kind": "replan_required",
      "step": 16,
      "evidence_ids": [
        "e000081"
      ],
      "object_id": "point-003",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-11",
      "kind": "target_state_changed",
      "step": 20,
      "evidence_ids": [
        "e000099",
        "e000100"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-12",
      "kind": "replan_required",
      "step": 20,
      "evidence_ids": [
        "e000099"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-13",
      "kind": "target_state_changed",
      "step": 23,
      "evidence_ids": [
        "e000116"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-14",
      "kind": "target_state_changed",
      "step": 30,
      "evidence_ids": [
        "e000147"
      ],
      "object_id": "point-004",
      "state": "stale"
    },
    {
      "event_id": "event-15",
      "kind": "replan_required",
      "step": 30,
      "evidence_ids": [
        "e000147"
      ],
      "object_id": "point-004",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-16",
      "kind": "target_state_changed",
      "step": 33,
      "evidence_ids": [
        "e000160"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-17",
      "kind": "replan_required",
      "step": 33,
      "evidence_ids": [
        "e000160"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-18",
      "kind": "target_state_changed",
      "step": 33,
      "evidence_ids": [
        "e000161"
      ],
      "object_id": "point-005",
      "state": "stale"
    },
    {
      "event_id": "event-19",
      "kind": "replan_required",
      "step": 33,
      "evidence_ids": [
        "e000161"
      ],
      "object_id": "point-005",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-20",
      "kind": "target_state_changed",
      "step": 39,
      "evidence_ids": [
        "e000188"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-21",
      "kind": "target_state_changed",
      "step": 41,
      "evidence_ids": [
        "e000200"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-22",
      "kind": "target_state_changed",
      "step": 44,
      "evidence_ids": [
        "e000215"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-23",
      "kind": "target_state_changed",
      "step": 46,
      "evidence_ids": [
        "e000225"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-24",
      "kind": "target_state_changed",
      "step": 49,
      "evidence_ids": [
        "e000240"
      ],
      "object_id": "point-006",
      "state": "stale"
    },
    {
      "event_id": "event-25",
      "kind": "replan_required",
      "step": 49,
      "evidence_ids": [
        "e000240"
      ],
      "object_id": "point-006",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-26",
      "kind": "target_state_changed",
      "step": 51,
      "evidence_ids": [
        "e000249"
      ],
      "object_id": "point-007",
      "state": "stale"
    },
    {
      "event_id": "event-27",
      "kind": "replan_required",
      "step": 51,
      "evidence_ids": [
        "e000249"
      ],
      "object_id": "point-007",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-28",
      "kind": "target_state_changed",
      "step": 56,
      "evidence_ids": [
        "e000270"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-29",
      "kind": "replan_required",
      "step": 56,
      "evidence_ids": [
        "e000270"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-30",
      "kind": "target_state_changed",
      "step": 56,
      "evidence_ids": [
        "e000271"
      ],
      "object_id": "point-008",
      "state": "stale"
    },
    {
      "event_id": "event-31",
      "kind": "replan_required",
      "step": 56,
      "evidence_ids": [
        "e000271"
      ],
      "object_id": "point-008",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-32",
      "kind": "target_state_changed",
      "step": 58,
      "evidence_ids": [
        "e000281"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-33",
      "kind": "target_state_changed",
      "step": 60,
      "evidence_ids": [
        "e000293"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-34",
      "kind": "target_state_changed",
      "step": 63,
      "evidence_ids": [
        "e000308"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-35",
      "kind": "target_state_changed",
      "step": 66,
      "evidence_ids": [
        "e000322",
        "e000323"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-36",
      "kind": "replan_required",
      "step": 66,
      "evidence_ids": [
        "e000322"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-37",
      "kind": "target_state_changed",
      "step": 68,
      "evidence_ids": [
        "e000335"
      ],
      "object_id": "point-009",
      "state": "stale"
    },
    {
      "event_id": "event-38",
      "kind": "replan_required",
      "step": 68,
      "evidence_ids": [
        "e000335"
      ],
      "object_id": "point-009",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-39",
      "kind": "target_state_changed",
      "step": 70,
      "evidence_ids": [
        "e000344"
      ],
      "object_id": "point-010",
      "state": "stale"
    },
    {
      "event_id": "event-40",
      "kind": "replan_required",
      "step": 70,
      "evidence_ids": [
        "e000344"
      ],
      "object_id": "point-010",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-41",
      "kind": "target_state_changed",
      "step": 76,
      "evidence_ids": [
        "e000369"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-42",
      "kind": "replan_required",
      "step": 76,
      "evidence_ids": [
        "e000369"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-43",
      "kind": "target_state_changed",
      "step": 76,
      "evidence_ids": [
        "e000370"
      ],
      "object_id": "point-011",
      "state": "stale"
    },
    {
      "event_id": "event-44",
      "kind": "replan_required",
      "step": 76,
      "evidence_ids": [
        "e000370"
      ],
      "object_id": "point-011",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-45",
      "kind": "target_state_changed",
      "step": 78,
      "evidence_ids": [
        "e000380",
        "e000381"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-46",
      "kind": "replan_required",
      "step": 78,
      "evidence_ids": [
        "e000380"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-47",
      "kind": "target_state_changed",
      "step": 80,
      "evidence_ids": [
        "e000396",
        "e000397"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-48",
      "kind": "replan_required",
      "step": 80,
      "evidence_ids": [
        "e000396"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-49",
      "kind": "target_state_changed",
      "step": 82,
      "evidence_ids": [
        "e000411",
        "e000412"
      ],
      "object_id": "task:B"
    },
    {
      "event_id": "event-50",
      "kind": "replan_required",
      "step": 82,
      "evidence_ids": [
        "e000411"
      ],
      "object_id": "task:B",
      "reason": "positive_position_contradiction"
    },
    {
      "event_id": "event-51",
      "kind": "target_state_changed",
      "step": 89,
      "evidence_ids": [
        "e000443"
      ],
      "object_id": "point-012",
      "state": "stale"
    },
    {
      "event_id": "event-52",
      "kind": "replan_required",
      "step": 89,
      "evidence_ids": [
        "e000443"
      ],
      "object_id": "point-012",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-53",
      "kind": "target_state_changed",
      "step": 90,
      "evidence_ids": [
        "e000448"
      ],
      "object_id": "point-013",
      "state": "stale"
    },
    {
      "event_id": "event-54",
      "kind": "replan_required",
      "step": 90,
      "evidence_ids": [
        "e000448"
      ],
      "object_id": "point-013",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-55",
      "kind": "target_state_changed",
      "step": 92,
      "evidence_ids": [
        "e000457"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-56",
      "kind": "replan_required",
      "step": 92,
      "evidence_ids": [
        "e000457"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-57",
      "kind": "target_state_changed",
      "step": 92,
      "evidence_ids": [
        "e000458"
      ],
      "object_id": "point-014",
      "state": "stale"
    },
    {
      "event_id": "event-58",
      "kind": "replan_required",
      "step": 92,
      "evidence_ids": [
        "e000458"
      ],
      "object_id": "point-014",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-59",
      "kind": "target_state_changed",
      "step": 95,
      "evidence_ids": [
        "e000472"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-60",
      "kind": "target_state_changed",
      "step": 100,
      "evidence_ids": [
        "e000500"
      ],
      "object_id": "task:B",
      "state": "confirmed"
    },
    {
      "event_id": "event-61",
      "kind": "target_state_changed",
      "step": 103,
      "evidence_ids": [
        "e000516"
      ],
      "object_id": "task:B",
      "state": "predicted"
    },
    {
      "event_id": "event-62",
      "kind": "target_state_changed",
      "step": 104,
      "evidence_ids": [
        "e000522"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-63",
      "kind": "target_state_changed",
      "step": 105,
      "evidence_ids": [
        "e000529"
      ],
      "object_id": "point-015",
      "state": "stale"
    },
    {
      "event_id": "event-64",
      "kind": "replan_required",
      "step": 105,
      "evidence_ids": [
        "e000529"
      ],
      "object_id": "point-015",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-65",
      "kind": "target_state_changed",
      "step": 108,
      "evidence_ids": [
        "e000544"
      ],
      "object_id": "point-016",
      "state": "stale"
    },
    {
      "event_id": "event-66",
      "kind": "replan_required",
      "step": 108,
      "evidence_ids": [
        "e000544"
      ],
      "object_id": "point-016",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-67",
      "kind": "target_state_changed",
      "step": 110,
      "evidence_ids": [
        "e000553"
      ],
      "object_id": "point-017",
      "state": "stale"
    },
    {
      "event_id": "event-68",
      "kind": "replan_required",
      "step": 110,
      "evidence_ids": [
        "e000553"
      ],
      "object_id": "point-017",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-69",
      "kind": "target_state_changed",
      "step": 114,
      "evidence_ids": [
        "e000570"
      ],
      "object_id": "task:B",
      "state": "stale"
    },
    {
      "event_id": "event-70",
      "kind": "replan_required",
      "step": 114,
      "evidence_ids": [
        "e000570"
      ],
      "object_id": "task:B",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-71",
      "kind": "target_state_changed",
      "step": 114,
      "evidence_ids": [
        "e000571"
      ],
      "object_id": "point-018",
      "state": "stale"
    },
    {
      "event_id": "event-72",
      "kind": "replan_required",
      "step": 114,
      "evidence_ids": [
        "e000571"
      ],
      "object_id": "point-018",
      "reason": "verification_expired"
    },
    {
      "event_id": "event-73",
      "kind": "target_state_changed",
      "step": 118,
      "evidence_ids": [
        "e000589"
      ],
      "object_id": "task:B",
      "state": "unknown"
    },
    {
      "event_id": "event-74",
      "kind": "target_state_changed",
      "step": 120,
      "evidence_ids": [
        "e000601"
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
      "value": -0.08491613033242727,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000602"
      ]
    },
    "pose.y_m": {
      "value": 0.14496089750037075,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000603"
      ]
    },
    "pose.yaw_rad": {
      "value": 0.12384347185088797,
      "source": "simulated_proprioception",
      "step": 120,
      "evidence_ids": [
        "e000604"
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
        "e000026"
      ]
    },
    "point-002.bearing_rad": {
      "value": 0.2203,
      "source": "rgbd_optical_flow",
      "step": 4,
      "evidence_ids": [
        "e000027"
      ]
    },
    "point-003.range_m": {
      "value": 2.5778,
      "source": "rgbd_optical_flow",
      "step": 6,
      "evidence_ids": [
        "e000039"
      ]
    },
    "point-003.bearing_rad": {
      "value": -0.1814,
      "source": "rgbd_optical_flow",
      "step": 6,
      "evidence_ids": [
        "e000040"
      ]
    },
    "point-004.range_m": {
      "value": 1.7189,
      "source": "rgbd_optical_flow",
      "step": 20,
      "evidence_ids": [
        "e000104"
      ]
    },
    "point-004.bearing_rad": {
      "value": 0.4547,
      "source": "rgbd_optical_flow",
      "step": 20,
      "evidence_ids": [
        "e000105"
      ]
    },
    "point-005.range_m": {
      "value": 1.8182,
      "source": "rgbd_optical_flow",
      "step": 23,
      "evidence_ids": [
        "e000120"
      ]
    },
    "point-005.bearing_rad": {
      "value": -0.5987,
      "source": "rgbd_optical_flow",
      "step": 23,
      "evidence_ids": [
        "e000121"
      ]
    },
    "point-006.range_m": {
      "value": 1.7732,
      "source": "rgbd_optical_flow",
      "step": 39,
      "evidence_ids": [
        "e000192"
      ]
    },
    "point-006.bearing_rad": {
      "value": 0.6399,
      "source": "rgbd_optical_flow",
      "step": 39,
      "evidence_ids": [
        "e000193"
      ]
    },
    "point-007.range_m": {
      "value": 1.867,
      "source": "rgbd_optical_flow",
      "step": 41,
      "evidence_ids": [
        "e000204"
      ]
    },
    "point-007.bearing_rad": {
      "value": 0.3791,
      "source": "rgbd_optical_flow",
      "step": 41,
      "evidence_ids": [
        "e000205"
      ]
    },
    "point-008.range_m": {
      "value": 1.8238,
      "source": "rgbd_optical_flow",
      "step": 46,
      "evidence_ids": [
        "e000229"
      ]
    },
    "point-008.bearing_rad": {
      "value": -0.6694,
      "source": "rgbd_optical_flow",
      "step": 46,
      "evidence_ids": [
        "e000230"
      ]
    },
    "point-009.range_m": {
      "value": 1.7579,
      "source": "rgbd_optical_flow",
      "step": 58,
      "evidence_ids": [
        "e000285"
      ]
    },
    "point-009.bearing_rad": {
      "value": 0.4053,
      "source": "rgbd_optical_flow",
      "step": 58,
      "evidence_ids": [
        "e000286"
      ]
    },
    "point-010.range_m": {
      "value": 1.752,
      "source": "rgbd_optical_flow",
      "step": 60,
      "evidence_ids": [
        "e000297"
      ]
    },
    "point-010.bearing_rad": {
      "value": -0.0431,
      "source": "rgbd_optical_flow",
      "step": 60,
      "evidence_ids": [
        "e000298"
      ]
    },
    "point-011.range_m": {
      "value": 2.7961,
      "source": "rgbd_optical_flow",
      "step": 66,
      "evidence_ids": [
        "e000327"
      ]
    },
    "point-011.bearing_rad": {
      "value": -0.5758,
      "source": "rgbd_optical_flow",
      "step": 66,
      "evidence_ids": [
        "e000328"
      ]
    },
    "point-012.range_m": {
      "value": 1.7647,
      "source": "rgbd_optical_flow",
      "step": 80,
      "evidence_ids": [
        "e000403"
      ]
    },
    "point-012.bearing_rad": {
      "value": -0.2012,
      "source": "rgbd_optical_flow",
      "step": 80,
      "evidence_ids": [
        "e000404"
      ]
    },
    "point-013.range_m": {
      "value": 3.5793,
      "source": "rgbd_optical_flow",
      "step": 80,
      "evidence_ids": [
        "e000401"
      ]
    },
    "point-013.bearing_rad": {
      "value": -0.1904,
      "source": "rgbd_optical_flow",
      "step": 80,
      "evidence_ids": [
        "e000402"
      ]
    },
    "point-014.range_m": {
      "value": 1.789,
      "source": "rgbd_optical_flow",
      "step": 82,
      "evidence_ids": [
        "e000416"
      ]
    },
    "point-014.bearing_rad": {
      "value": -0.6408,
      "source": "rgbd_optical_flow",
      "step": 82,
      "evidence_ids": [
        "e000417"
      ]
    },
    "point-015.range_m": {
      "value": 1.9835,
      "source": "rgbd_optical_flow",
      "step": 95,
      "evidence_ids": [
        "e000476"
      ]
    },
    "point-015.bearing_rad": {
      "value": 0.3457,
      "source": "rgbd_optical_flow",
      "step": 95,
      "evidence_ids": [
        "e000477"
      ]
    },
    "point-016.range_m": {
      "value": 1.8204,
      "source": "rgbd_optical_flow",
      "step": 98,
      "evidence_ids": [
        "e000492"
      ]
    },
    "point-016.bearing_rad": {
      "value": 0.4491,
      "source": "rgbd_optical_flow",
      "step": 98,
      "evidence_ids": [
        "e000493"
      ]
    },
    "point-017.range_m": {
      "value": 1.8078,
      "source": "rgbd_optical_flow",
      "step": 100,
      "evidence_ids": [
        "e000504"
      ]
    },
    "point-017.bearing_rad": {
      "value": -0.0116,
      "source": "rgbd_optical_flow",
      "step": 100,
      "evidence_ids": [
        "e000505"
      ]
    },
    "point-018.range_m": {
      "value": 1.9588,
      "source": "rgbd_optical_flow",
      "step": 105,
      "evidence_ids": [
        "e000533"
      ]
    },
    "point-018.bearing_rad": {
      "value": -0.602,
      "source": "rgbd_optical_flow",
      "step": 105,
      "evidence_ids": [
        "e000534"
      ]
    },
    "point-019.range_m": {
      "value": 1.8637,
      "source": "rgbd_optical_flow",
      "step": 118,
      "evidence_ids": [
        "e000593"
      ]
    },
    "point-019.bearing_rad": {
      "value": 0.4596,
      "source": "rgbd_optical_flow",
      "step": 118,
      "evidence_ids": [
        "e000594"
      ]
    },
    "point-020.range_m": {
      "value": 1.8294,
      "source": "rgbd_optical_flow",
      "step": 120,
      "evidence_ids": [
        "e000605"
      ]
    },
    "point-020.bearing_rad": {
      "value": 0.007,
      "source": "rgbd_optical_flow",
      "step": 120,
      "evidence_ids": [
        "e000606"
      ]
    }
  },
  "plans": [
    {
      "subgoals": [
        {
          "subgoal_id": "scan_A",
          "description": "scan scene to locate blue ball A before approaching B",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000016"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_A"
        }
      ],
      "recovery": "observe and re-plan a safe scan",
      "plan_id": "plan-0001",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_A",
          "description": "rotate conservatively to visually locate blue ball A",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000178"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_A"
        }
      ],
      "recovery": "observe, then continue safe scan or replan exploration",
      "plan_id": "plan-0002",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_A",
          "description": "rotate conservatively to look for blue ball A before approaching B",
          "preconditions": [],
          "completion": [],
          "active": false,
          "status": "进行中",
          "evidence_ids": [
            "e000334"
          ]
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_A"
        }
      ],
      "recovery": "observe current view, then continue safe scan or abort if no target appears",
      "plan_id": "plan-0003",
      "active": false
    },
    {
      "subgoals": [
        {
          "subgoal_id": "scan_A",
          "description": "turn conservatively to search for blue ball A",
          "preconditions": [],
          "completion": [],
          "active": true,
          "status": "进行中",
          "evidence_ids": [
            "e000520"
          ]
        },
        {
          "subgoal_id": "approach_A",
          "description": "stand 1.0 m from A facing it, then stop",
          "preconditions": [
            {
              "object_id": "task:A"
            }
          ],
          "completion": [],
          "active": true,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [
        {
          "on": "skill_stuck",
          "subgoal_id": "scan_A"
        }
      ],
      "recovery": "stop, observe current view, then resume conservative scanning or abort if no target visible",
      "plan_id": "plan-0004",
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
        "call_id": "call_b978df87b81946a08f8bbae5",
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
        "call_id": "call_08662797845346c995b58868",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
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
        "call_id": "call_9fb87b3c4ba64bd78dc22d1c",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
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
      "evidence_id": "e000022",
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
      "evidence_id": "e000023",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.x_m",
      "value": 0.016467470766759758
    },
    {
      "evidence_id": "e000024",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.y_m",
      "value": -0.029697896850089854
    },
    {
      "evidence_id": "e000025",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 4,
      "name": "pose.yaw_rad",
      "value": 0.01425524642322581
    },
    {
      "evidence_id": "e000026",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 4,
      "name": "point-002.range_m",
      "value": 1.7714
    },
    {
      "evidence_id": "e000027",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 4,
      "name": "point-002.bearing_rad",
      "value": 0.2203
    },
    {
      "evidence_id": "e000028",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 4,
      "action": {
        "call_id": "call_54583709b02944e5b53fd640",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000029",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.x_m",
      "value": 0.027177836874104234
    },
    {
      "evidence_id": "e000030",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.y_m",
      "value": 0.0016069939273824119
    },
    {
      "evidence_id": "e000031",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 5,
      "name": "pose.yaw_rad",
      "value": 0.5805266485365677
    },
    {
      "evidence_id": "e000032",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 5,
      "action": {
        "call_id": "call_b59e9a53f3204a1aaa387c1f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011155521706283146,
            0.031149036328648547
          ],
          "yaw_delta_rad": 0.5662714021133417,
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
            2.4023327436808373,
            1.0034175641810097
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
            384.0,
            235.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000034",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 6,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.4023327436808373,
            1.0034175641810097
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
            384.0,
            235.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00004",
          "position_m": [
            0.4598283202607212,
            0.39566622906155086,
            2.222640037536621
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
      "evidence_id": "e000035",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 6,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7393738185676924,
          0.382003556520252
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          2.4023327436808373,
          1.0034175641810097
        ]
      },
      "evidence_ids": [
        "e000034"
      ]
    },
    {
      "evidence_id": "e000036",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.x_m",
      "value": 0.027177836874104234
    },
    {
      "evidence_id": "e000037",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.y_m",
      "value": 0.0016069939273824119
    },
    {
      "evidence_id": "e000038",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 6,
      "name": "pose.yaw_rad",
      "value": 0.5805266485365677
    },
    {
      "evidence_id": "e000039",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-003.range_m",
      "value": 2.5778
    },
    {
      "evidence_id": "e000040",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 6,
      "name": "point-003.bearing_rad",
      "value": -0.1814
    },
    {
      "evidence_id": "e000041",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 6,
      "action": {
        "call_id": "call_6a6be4b310ea431c9d6d3c28",
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
      "value": 0.038018959620678076
    },
    {
      "evidence_id": "e000043",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.y_m",
      "value": 0.018507687807248718
    },
    {
      "evidence_id": "e000044",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 7,
      "name": "pose.yaw_rad",
      "value": 1.1251539587474249
    },
    {
      "evidence_id": "e000045",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 7,
      "action": {
        "call_id": "call_bca6f970a77a451bbcf45013",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0183344927160718,
            0.008185949723247831
          ],
          "yaw_delta_rad": 0.5446273102108572,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000046",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.x_m",
      "value": 0.024627711144951794
    },
    {
      "evidence_id": "e000047",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.y_m",
      "value": 0.04121012011989588
    },
    {
      "evidence_id": "e000048",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 8,
      "name": "pose.yaw_rad",
      "value": 1.6640365989994443
    },
    {
      "evidence_id": "e000049",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 8,
      "action": {
        "call_id": "call_d81725a37b52497abf9ce4ba",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.014713044204753875,
            0.021868980288937252
          ],
          "yaw_delta_rad": 0.5388826402520195,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000050",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.x_m",
      "value": 0.024627711144951794
    },
    {
      "evidence_id": "e000051",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.y_m",
      "value": 0.04121012011989588
    },
    {
      "evidence_id": "e000052",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 9,
      "name": "pose.yaw_rad",
      "value": 1.6640365989994443
    },
    {
      "evidence_id": "e000053",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 9,
      "action": {
        "call_id": "call_2661c5d9d9e948e78db5ee48",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000054",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.x_m",
      "value": 0.02518408443963946
    },
    {
      "evidence_id": "e000055",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.y_m",
      "value": 0.052996696143277025
    },
    {
      "evidence_id": "e000056",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 10,
      "name": "pose.yaw_rad",
      "value": 2.209140292369641
    },
    {
      "evidence_id": "e000057",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 10,
      "action": {
        "call_id": "call_452fa78c9ef74732a1e2cf6f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011683577104759273,
            -0.0016513484293539777
          ],
          "yaw_delta_rad": 0.5451036933701965,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000058",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 11,
      "object_id": "point-001",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000059",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.x_m",
      "value": -0.007456665569358584
    },
    {
      "evidence_id": "e000060",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.y_m",
      "value": 0.06231395500381137
    },
    {
      "evidence_id": "e000061",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 11,
      "name": "pose.yaw_rad",
      "value": 2.745450262487397
    },
    {
      "evidence_id": "e000062",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 11,
      "action": {
        "call_id": "call_02a3e11d03da4b5ab57eff92",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.026932061852275785,
            0.020661411331496758
          ],
          "yaw_delta_rad": 0.536309970117756,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000063",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.x_m",
      "value": -0.015815534613383947
    },
    {
      "evidence_id": "e000064",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.y_m",
      "value": 0.05263471138217224
    },
    {
      "evidence_id": "e000065",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 12,
      "name": "pose.yaw_rad",
      "value": -2.9854888442718943
    },
    {
      "evidence_id": "e000066",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 12,
      "action": {
        "call_id": "call_dbf5ee68f9e048f6985718fc",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.003976672012922966,
            0.01215502071095901
          ],
          "yaw_delta_rad": 0.5522462004202948,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000067",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.x_m",
      "value": -0.008962769332758552
    },
    {
      "evidence_id": "e000068",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.y_m",
      "value": 0.04848999253162976
    },
    {
      "evidence_id": "e000069",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 13,
      "name": "pose.yaw_rad",
      "value": -2.4418922666186598
    },
    {
      "evidence_id": "e000070",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 13,
      "action": {
        "call_id": "call_8e5e2ad1961c4db4820a8c1d",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.006125057387659333,
            0.005159724637930492
          ],
          "yaw_delta_rad": 0.5435965776532345,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000071",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 14,
      "object_id": "point-002",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000072",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.x_m",
      "value": -0.003943954088751013
    },
    {
      "evidence_id": "e000073",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.y_m",
      "value": 0.026684705603246605
    },
    {
      "evidence_id": "e000074",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 14,
      "name": "pose.yaw_rad",
      "value": -1.9063838819319163
    },
    {
      "evidence_id": "e000075",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 14,
      "action": {
        "call_id": "call_204feb434f77490c943c2431",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010202783888674169,
            0.019913870678590097
          ],
          "yaw_delta_rad": 0.5355083846867439,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000076",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.x_m",
      "value": -0.003943954088751013
    },
    {
      "evidence_id": "e000077",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.y_m",
      "value": 0.026684705603246605
    },
    {
      "evidence_id": "e000078",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 15,
      "name": "pose.yaw_rad",
      "value": -1.9063838819319163
    },
    {
      "evidence_id": "e000079",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 15,
      "action": {
        "call_id": "call_cddfae4cd2654116890535c3",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000080",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 16,
      "object_id": "task:B",
      "old_state": "contradicted",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000081",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 16,
      "object_id": "point-003",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000082",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.x_m",
      "value": 0.021753668994524262
    },
    {
      "evidence_id": "e000083",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.y_m",
      "value": 0.006513855241270202
    },
    {
      "evidence_id": "e000084",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 16,
      "name": "pose.yaw_rad",
      "value": -1.3375460420082894
    },
    {
      "evidence_id": "e000085",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 16,
      "action": {
        "call_id": "call_1ad3fcac3cbf4cb9bbe1644f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010582815160354819,
            0.030906877223962473
          ],
          "yaw_delta_rad": 0.5688378399236269,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000086",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.x_m",
      "value": 0.021753668994524262
    },
    {
      "evidence_id": "e000087",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.y_m",
      "value": 0.006513855241270202
    },
    {
      "evidence_id": "e000088",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 17,
      "name": "pose.yaw_rad",
      "value": -1.3375460420082894
    },
    {
      "evidence_id": "e000089",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 17,
      "action": {
        "call_id": "call_7e5f573f483347ac975ff223",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000090",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.x_m",
      "value": 0.029688417272269434
    },
    {
      "evidence_id": "e000091",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.y_m",
      "value": -0.011710083431850945
    },
    {
      "evidence_id": "e000092",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 18,
      "name": "pose.yaw_rad",
      "value": -0.7919160155897953
    },
    {
      "evidence_id": "e000093",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 18,
      "action": {
        "call_id": "call_aa114adbc3a84a5abc8a058c",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01956448488264799,
            0.003507577835130511
          ],
          "yaw_delta_rad": 0.5456300264184941,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000094",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.x_m",
      "value": 0.054119707908327555
    },
    {
      "evidence_id": "e000095",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.y_m",
      "value": 0.0015209711507060241
    },
    {
      "evidence_id": "e000096",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 19,
      "name": "pose.yaw_rad",
      "value": -0.22753892081304306
    },
    {
      "evidence_id": "e000097",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 19,
      "action": {
        "call_id": "call_d33336c88cd44173807d55b7",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.007746016993534317,
            0.02668235349900792
          ],
          "yaw_delta_rad": 0.5643770947767521,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000098",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 20,
      "observation": {
        "object_id": "point-004",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7289053975452315,
            0.38859899143529847
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
            127.0,
            282.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000099",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 20,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7289053975452315,
            0.38859899143529847
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00017",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00017",
          "pixel_uv": [
            127.0,
            282.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00017",
          "position_m": [
            -0.7596114850606778,
            0.404468453084257,
            1.2302515506744385
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
      "evidence_id": "e000100",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 20,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7393738185676924,
          0.382003556520252
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7289053975452315,
          0.38859899143529847
        ]
      },
      "evidence_ids": [
        "e000099"
      ]
    },
    {
      "evidence_id": "e000101",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.x_m",
      "value": 0.054119707908327555
    },
    {
      "evidence_id": "e000102",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.y_m",
      "value": 0.0015209711507060241
    },
    {
      "evidence_id": "e000103",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 20,
      "name": "pose.yaw_rad",
      "value": -0.22753892081304306
    },
    {
      "evidence_id": "e000104",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-004.range_m",
      "value": 1.7189
    },
    {
      "evidence_id": "e000105",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 20,
      "name": "point-004.bearing_rad",
      "value": 0.4547
    },
    {
      "evidence_id": "e000106",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 20,
      "action": {
        "call_id": "call_7a1c55af113b499ab17db5f3",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000107",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.x_m",
      "value": 0.0621289700765361
    },
    {
      "evidence_id": "e000108",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.y_m",
      "value": 0.015485917989558612
    },
    {
      "evidence_id": "e000109",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 21,
      "name": "pose.yaw_rad",
      "value": 0.32327218990148426
    },
    {
      "evidence_id": "e000110",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 21,
      "action": {
        "call_id": "call_b1b5af1ccfd0462585f700b5",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.004652598958954551,
            0.015411727470280889
          ],
          "yaw_delta_rad": 0.5508111107145273,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000111",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.x_m",
      "value": 0.05058089007395909
    },
    {
      "evidence_id": "e000112",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.y_m",
      "value": 0.024946081330722417
    },
    {
      "evidence_id": "e000113",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 22,
      "name": "pose.yaw_rad",
      "value": 0.8561647662169696
    },
    {
      "evidence_id": "e000114",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 22,
      "action": {
        "call_id": "call_b15f34bc60bd4511a591f56f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.007944682126232335,
            0.012638626036897478
          ],
          "yaw_delta_rad": 0.5328925763154855,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000115",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 23,
      "observation": {
        "object_id": "point-005",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.808891831001307,
            0.4879328252178292
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
            591.0,
            182.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000116",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 23,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.808891831001307,
            0.4879328252178292
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00019",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00019",
          "pixel_uv": [
            591.0,
            182.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00019",
          "position_m": [
            1.026941498920792,
            0.009456183231314842,
            1.1792584657669067
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
      "evidence_id": "e000117",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.x_m",
      "value": 0.05058089007395909
    },
    {
      "evidence_id": "e000118",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.y_m",
      "value": 0.024946081330722417
    },
    {
      "evidence_id": "e000119",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 23,
      "name": "pose.yaw_rad",
      "value": 0.8561647662169696
    },
    {
      "evidence_id": "e000120",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-005.range_m",
      "value": 1.8182
    },
    {
      "evidence_id": "e000121",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 23,
      "name": "point-005.bearing_rad",
      "value": -0.5987
    },
    {
      "evidence_id": "e000122",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 23,
      "action": {
        "call_id": "call_cdfbfee7f6a94c0e9fae9907",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000123",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.x_m",
      "value": 0.04161910881745167
    },
    {
      "evidence_id": "e000124",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.y_m",
      "value": 0.04223242069720239
    },
    {
      "evidence_id": "e000125",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 24,
      "name": "pose.yaw_rad",
      "value": 1.305011857159686
    },
    {
      "evidence_id": "e000126",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 24,
      "action": {
        "call_id": "call_9e59199f61f843cb85c9be5e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.007183966486516996,
            0.018097559987556446
          ],
          "yaw_delta_rad": 0.4488470909427167,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000127",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.x_m",
      "value": 0.03294623559375168
    },
    {
      "evidence_id": "e000128",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.y_m",
      "value": 0.05007374916861038
    },
    {
      "evidence_id": "e000129",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 25,
      "name": "pose.yaw_rad",
      "value": 1.750006462101766
    },
    {
      "evidence_id": "e000130",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 25,
      "action": {
        "call_id": "call_2ae577facffe460abdde50ff",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.005287922610030912,
            0.01042799293350401
          ],
          "yaw_delta_rad": 0.4449946049420799,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000131",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.x_m",
      "value": 0.03294623559375168
    },
    {
      "evidence_id": "e000132",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.y_m",
      "value": 0.05007374916861038
    },
    {
      "evidence_id": "e000133",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 26,
      "name": "pose.yaw_rad",
      "value": 1.750006462101766
    },
    {
      "evidence_id": "e000134",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 26,
      "action": {
        "call_id": "call_31cbdcb9a9064eab982f79ae",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000135",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.x_m",
      "value": 0.00037207961100117125
    },
    {
      "evidence_id": "e000136",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.y_m",
      "value": 0.0443020961521595
    },
    {
      "evidence_id": "e000137",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 27,
      "name": "pose.yaw_rad",
      "value": 2.329239228882111
    },
    {
      "evidence_id": "e000138",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 27,
      "action": {
        "call_id": "call_c144a841fd5f46d780a453eb",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00012720313625104104,
            0.03308128528175704
          ],
          "yaw_delta_rad": 0.5792327667803447,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000139",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.x_m",
      "value": 0.00037207961100117125
    },
    {
      "evidence_id": "e000140",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.y_m",
      "value": 0.0443020961521595
    },
    {
      "evidence_id": "e000141",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 28,
      "name": "pose.yaw_rad",
      "value": 2.329239228882111
    },
    {
      "evidence_id": "e000142",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 28,
      "action": {
        "call_id": "call_9ab849b9823c4ef4b2bad708",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000143",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.x_m",
      "value": 0.001971228843737719
    },
    {
      "evidence_id": "e000144",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.y_m",
      "value": 0.0540213039505231
    },
    {
      "evidence_id": "e000145",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 29,
      "name": "pose.yaw_rad",
      "value": 2.873977427826393
    },
    {
      "evidence_id": "e000146",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 29,
      "action": {
        "call_id": "call_4552736629c149599ce3ba5e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0059553672334521895,
            -0.007845628057144801
          ],
          "yaw_delta_rad": 0.5447381989442821,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000147",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 30,
      "object_id": "point-004",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000148",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.x_m",
      "value": -0.01934782570755298
    },
    {
      "evidence_id": "e000149",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.y_m",
      "value": 0.036761436107151595
    },
    {
      "evidence_id": "e000150",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 30,
      "name": "pose.yaw_rad",
      "value": -2.870679150383535
    },
    {
      "evidence_id": "e000151",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 30,
      "action": {
        "call_id": "call_22c85f77edd04eeeb53d8430",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.015996120176568512,
            0.022282936615902676
          ],
          "yaw_delta_rad": 0.5385287289696583,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000152",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.x_m",
      "value": -0.03223202823143603
    },
    {
      "evidence_id": "e000153",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.y_m",
      "value": 0.03825339825233626
    },
    {
      "evidence_id": "e000154",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 31,
      "name": "pose.yaw_rad",
      "value": -2.4265994161473308
    },
    {
      "evidence_id": "e000155",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 31,
      "action": {
        "call_id": "call_0cfaf66bca054cd0a628f657",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.012015008294306583,
            -0.004885509329316911
          ],
          "yaw_delta_rad": 0.44407973423620417,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000156",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.x_m",
      "value": -0.030682835008312623
    },
    {
      "evidence_id": "e000157",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.y_m",
      "value": 0.0177865431449677
    },
    {
      "evidence_id": "e000158",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 32,
      "name": "pose.yaw_rad",
      "value": -1.879161526576355
    },
    {
      "evidence_id": "e000159",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 32,
      "action": {
        "call_id": "call_55f72da7bb3c42c3a11f60a7",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.012248529961274283,
            0.01647014485110426
          ],
          "yaw_delta_rad": 0.5474378895709759,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000160",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 33,
      "object_id": "task:B",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000161",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 33,
      "object_id": "point-005",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000162",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.x_m",
      "value": -0.030682835008312623
    },
    {
      "evidence_id": "e000163",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.y_m",
      "value": 0.0177865431449677
    },
    {
      "evidence_id": "e000164",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 33,
      "name": "pose.yaw_rad",
      "value": -1.879161526576355
    },
    {
      "evidence_id": "e000165",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 33,
      "action": {
        "call_id": "call_bb690ff40b1c45c587cd4331",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000166",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.x_m",
      "value": -0.03620851027467177
    },
    {
      "evidence_id": "e000167",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.y_m",
      "value": 0.007550855255268998
    },
    {
      "evidence_id": "e000168",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 34,
      "name": "pose.yaw_rad",
      "value": -1.4357509212552584
    },
    {
      "evidence_id": "e000169",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 34,
      "action": {
        "call_id": "call_b215e1cd0cbc4554bb21a5cf",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0001",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01142993072638576,
            -0.0021584895910336517
          ],
          "yaw_delta_rad": 0.44341060532109644,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000170",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.x_m",
      "value": -0.03620851027467177
    },
    {
      "evidence_id": "e000171",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.y_m",
      "value": 0.007550855255268998
    },
    {
      "evidence_id": "e000172",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 35,
      "name": "pose.yaw_rad",
      "value": -1.4357509212552584
    },
    {
      "evidence_id": "e000173",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 35,
      "action": {
        "call_id": "call_9a8a9938996a459eac81ff90",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000174",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 35,
      "plan_id": "plan-0002"
    },
    {
      "evidence_id": "e000175",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.x_m",
      "value": -0.009179078199844877
    },
    {
      "evidence_id": "e000176",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.y_m",
      "value": 0.006298468803411442
    },
    {
      "evidence_id": "e000177",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 36,
      "name": "pose.yaw_rad",
      "value": -0.8723540811896002
    },
    {
      "evidence_id": "e000178",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 36,
      "action": {
        "call_id": "call_004d1f790b9149cbaafd446f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.004880099532366432,
            0.026614719586474597
          ],
          "yaw_delta_rad": 0.5633968400656579,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000179",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.x_m",
      "value": -0.009179078199844877
    },
    {
      "evidence_id": "e000180",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.y_m",
      "value": 0.006298468803411442
    },
    {
      "evidence_id": "e000181",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 37,
      "name": "pose.yaw_rad",
      "value": -0.8723540811896002
    },
    {
      "evidence_id": "e000182",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 37,
      "action": {
        "call_id": "call_6cc70b49689d424eac3679c7",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000183",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.x_m",
      "value": 0.0033915849496618153
    },
    {
      "evidence_id": "e000184",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.y_m",
      "value": 0.0024627213909460977
    },
    {
      "evidence_id": "e000185",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 38,
      "name": "pose.yaw_rad",
      "value": -0.4241226382587737
    },
    {
      "evidence_id": "e000186",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 38,
      "action": {
        "call_id": "call_9a68aee806e64d538076fba0",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011020843756174426,
            0.0071606936209134935
          ],
          "yaw_delta_rad": 0.4482314429308265,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000187",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 39,
      "observation": {
        "object_id": "point-006",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354859052592504,
            0.3821052711022028
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
            20.0,
            193.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000188",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 39,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7354859052592504,
            0.3821052711022028
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00034",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00034",
          "pixel_uv": [
            20.0,
            193.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00034",
          "position_m": [
            -1.0589940780960208,
            0.04773429066542998,
            1.1023762226104736
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
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.x_m",
      "value": 0.0033915849496618153
    },
    {
      "evidence_id": "e000190",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.y_m",
      "value": 0.0024627213909460977
    },
    {
      "evidence_id": "e000191",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 39,
      "name": "pose.yaw_rad",
      "value": -0.4241226382587737
    },
    {
      "evidence_id": "e000192",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-006.range_m",
      "value": 1.7732
    },
    {
      "evidence_id": "e000193",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 39,
      "name": "point-006.bearing_rad",
      "value": 0.6399
    },
    {
      "evidence_id": "e000194",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 39,
      "action": {
        "call_id": "call_10dc5791b93d45148ed1f3fc",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000195",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.x_m",
      "value": 0.01669514123570034
    },
    {
      "evidence_id": "e000196",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.y_m",
      "value": 0.012740982912415686
    },
    {
      "evidence_id": "e000197",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 40,
      "name": "pose.yaw_rad",
      "value": 0.02212179650610829
    },
    {
      "evidence_id": "e000198",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 40,
      "action": {
        "call_id": "call_ffaf29cad6774c3da32149c9",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.007895139345493782,
            0.01484230590153543
          ],
          "yaw_delta_rad": 0.44624443476488196,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000199",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 41,
      "observation": {
        "object_id": "point-007",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7353858588714828,
            0.7419368256821057
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
            167.0,
            251.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000200",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 41,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7353858588714828,
            0.7419368256821057
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00035",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00035",
          "pixel_uv": [
            167.0,
            251.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00035",
          "position_m": [
            -0.6955119147685257,
            0.3260924715144235,
            1.4218961000442505
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
      "evidence_id": "e000201",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.x_m",
      "value": 0.01669514123570034
    },
    {
      "evidence_id": "e000202",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.y_m",
      "value": 0.012740982912415686
    },
    {
      "evidence_id": "e000203",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 41,
      "name": "pose.yaw_rad",
      "value": 0.02212179650610829
    },
    {
      "evidence_id": "e000204",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-007.range_m",
      "value": 1.867
    },
    {
      "evidence_id": "e000205",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 41,
      "name": "point-007.bearing_rad",
      "value": 0.3791
    },
    {
      "evidence_id": "e000206",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 41,
      "action": {
        "call_id": "call_bb1bac137b6e4f058531c35a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000207",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.x_m",
      "value": 0.02989716179923289
    },
    {
      "evidence_id": "e000208",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.y_m",
      "value": 0.03496999057892763
    },
    {
      "evidence_id": "e000209",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 42,
      "name": "pose.yaw_rad",
      "value": 0.5610198850334736
    },
    {
      "evidence_id": "e000210",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 42,
      "action": {
        "call_id": "call_31bc1915504547a2b81913e7",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01369049581045566,
            0.02193154014796223
          ],
          "yaw_delta_rad": 0.5388980885273655,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000211",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.x_m",
      "value": 0.03918030174768891
    },
    {
      "evidence_id": "e000212",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.y_m",
      "value": 0.03975910344627268
    },
    {
      "evidence_id": "e000213",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 43,
      "name": "pose.yaw_rad",
      "value": 1.1082033526420505
    },
    {
      "evidence_id": "e000214",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 43,
      "action": {
        "call_id": "call_50ef44823e6a40f5808e2362",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01040820216501499,
            -0.0008840910874832889
          ],
          "yaw_delta_rad": 0.5471834676085772,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000215",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 44,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000216",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.x_m",
      "value": 0.04854014720213793
    },
    {
      "evidence_id": "e000217",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.y_m",
      "value": 0.041137855438400234
    },
    {
      "evidence_id": "e000218",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 44,
      "name": "pose.yaw_rad",
      "value": 1.549278160783874
    },
    {
      "evidence_id": "e000219",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 44,
      "action": {
        "call_id": "call_81df6ab58fba427bb60745e6",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0054108615956998144,
            -0.007760814440453166
          ],
          "yaw_delta_rad": 0.4410748081418232,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000220",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.x_m",
      "value": 0.013468771388604804
    },
    {
      "evidence_id": "e000221",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.y_m",
      "value": 0.08137809298663432
    },
    {
      "evidence_id": "e000222",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 45,
      "name": "pose.yaw_rad",
      "value": 1.006959868926231
    },
    {
      "evidence_id": "e000223",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 45,
      "action": {
        "call_id": "call_fd6a7ea59b764823beb844c8",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.03947630821068063,
            0.03592908584208251
          ],
          "yaw_delta_rad": -0.5423182918576428,
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
      "step": 46,
      "observation": {
        "object_id": "point-008",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7342863290842825,
            0.6852968235508405
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
            630.0,
            292.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000225",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 46,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7342863290842825,
            0.6852968235508405
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00039",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00039",
          "pixel_uv": [
            630.0,
            292.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00039",
          "position_m": [
            1.121288713585141,
            0.4062640266612829,
            1.1258718967437744
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
      "step": 46,
      "name": "pose.x_m",
      "value": 0.013468771388604804
    },
    {
      "evidence_id": "e000227",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.y_m",
      "value": 0.08137809298663432
    },
    {
      "evidence_id": "e000228",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 46,
      "name": "pose.yaw_rad",
      "value": 1.006959868926231
    },
    {
      "evidence_id": "e000229",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 46,
      "name": "point-008.range_m",
      "value": 1.8238
    },
    {
      "evidence_id": "e000230",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 46,
      "name": "point-008.bearing_rad",
      "value": -0.6694
    },
    {
      "evidence_id": "e000231",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 46,
      "action": {
        "call_id": "call_3aa2817ad105461389e38730",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000232",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.x_m",
      "value": 0.01109977611243453
    },
    {
      "evidence_id": "e000233",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.y_m",
      "value": 0.0777708163135438
    },
    {
      "evidence_id": "e000234",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 47,
      "name": "pose.yaw_rad",
      "value": 1.5186121110571837
    },
    {
      "evidence_id": "e000235",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 47,
      "action": {
        "call_id": "call_c58feaefdd984462a44697b1",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.004314978585959311,
            7.445412985615887e-05
          ],
          "yaw_delta_rad": 0.5116522421309528,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000236",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.x_m",
      "value": 0.008956788055405831
    },
    {
      "evidence_id": "e000237",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.y_m",
      "value": 0.08090916657759299
    },
    {
      "evidence_id": "e000238",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 48,
      "name": "pose.yaw_rad",
      "value": 1.9702442086691734
    },
    {
      "evidence_id": "e000239",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 48,
      "action": {
        "call_id": "call_5bcad0fa3d1c42f88865f99f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00302229866576606,
            0.0023037688615253934
          ],
          "yaw_delta_rad": 0.45163209761198964,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000240",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 49,
      "object_id": "point-006",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000241",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.x_m",
      "value": -0.005482218321887504
    },
    {
      "evidence_id": "e000242",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.y_m",
      "value": 0.09109506622614533
    },
    {
      "evidence_id": "e000243",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 49,
      "name": "pose.yaw_rad",
      "value": 2.4187699911380602
    },
    {
      "evidence_id": "e000244",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 49,
      "action": {
        "call_id": "call_160710ddb64346f9a9fb2348",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.014999493782575916,
            0.009340912325911346
          ],
          "yaw_delta_rad": 0.44852578246888664,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000245",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.x_m",
      "value": -0.018165774760866917
    },
    {
      "evidence_id": "e000246",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.y_m",
      "value": 0.09613471067673639
    },
    {
      "evidence_id": "e000247",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 50,
      "name": "pose.yaw_rad",
      "value": 2.9611623784265335
    },
    {
      "evidence_id": "e000248",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 50,
      "action": {
        "call_id": "call_9dac0c7a201a451fa1ae5482",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.012845671196540145,
            0.004610786444797491
          ],
          "yaw_delta_rad": 0.5423923872884733,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000249",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 51,
      "object_id": "point-007",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000250",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.x_m",
      "value": -0.046371652035522494
    },
    {
      "evidence_id": "e000251",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.y_m",
      "value": 0.09610653302338827
    },
    {
      "evidence_id": "e000252",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 51,
      "name": "pose.yaw_rad",
      "value": -2.887343639842471
    },
    {
      "evidence_id": "e000253",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 51,
      "action": {
        "call_id": "call_6dcecf8fd9404921819721cb",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.02774294257190595,
            0.00508934615299536
          ],
          "yaw_delta_rad": 0.4346792889105817,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000254",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.x_m",
      "value": -0.05194419749002484
    },
    {
      "evidence_id": "e000255",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.y_m",
      "value": 0.10612540872974593
    },
    {
      "evidence_id": "e000256",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 52,
      "name": "pose.yaw_rad",
      "value": -2.344925317544813
    },
    {
      "evidence_id": "e000257",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 52,
      "action": {
        "call_id": "call_48c91d4f8bda4d73ab8da247",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0028734678529604876,
            -0.011098392485398099
          ],
          "yaw_delta_rad": 0.542418322297658,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000258",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.x_m",
      "value": -0.05194419749002484
    },
    {
      "evidence_id": "e000259",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.y_m",
      "value": 0.10612540872974593
    },
    {
      "evidence_id": "e000260",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 53,
      "name": "pose.yaw_rad",
      "value": -2.344925317544813
    },
    {
      "evidence_id": "e000261",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 53,
      "action": {
        "call_id": "call_afdf6aabb4864e79b4075318",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000262",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.x_m",
      "value": -0.03628727592091539
    },
    {
      "evidence_id": "e000263",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.y_m",
      "value": 0.08636205663087376
    },
    {
      "evidence_id": "e000264",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 54,
      "name": "pose.yaw_rad",
      "value": -1.7829397620186653
    },
    {
      "evidence_id": "e000265",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 54,
      "action": {
        "call_id": "call_ffa7ac9663f94eb1b2782036",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.003185741274621479,
            0.02501160394169899
          ],
          "yaw_delta_rad": 0.5619855555261477,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000266",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.x_m",
      "value": -0.03716175404367774
    },
    {
      "evidence_id": "e000267",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.y_m",
      "value": 0.07585211183797706
    },
    {
      "evidence_id": "e000268",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 55,
      "name": "pose.yaw_rad",
      "value": -1.2381861285449627
    },
    {
      "evidence_id": "e000269",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 55,
      "action": {
        "call_id": "call_a5acdbd62833428c9ae3b67f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010458457664269519,
            0.0013580555296484743
          ],
          "yaw_delta_rad": 0.5447536334737029,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000270",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 56,
      "object_id": "task:B",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000271",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 56,
      "object_id": "point-008",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000272",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.x_m",
      "value": -0.007940682424422214
    },
    {
      "evidence_id": "e000273",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.y_m",
      "value": 0.07713112976692328
    },
    {
      "evidence_id": "e000274",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 56,
      "name": "pose.yaw_rad",
      "value": -0.7697234713152117
    },
    {
      "evidence_id": "e000275",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 56,
      "action": {
        "call_id": "call_3877c3254b594862911a7020",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.008332090307480486,
            0.02803717504578905
          ],
          "yaw_delta_rad": 0.4684626572297508,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000276",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.x_m",
      "value": 7.329541224028197e-05
    },
    {
      "evidence_id": "e000277",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.y_m",
      "value": 0.0708923286433246
    },
    {
      "evidence_id": "e000278",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 57,
      "name": "pose.yaw_rad",
      "value": -0.22337345322552868
    },
    {
      "evidence_id": "e000279",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 57,
      "action": {
        "call_id": "call_1189b50751d44f66a1b11224",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010096673274660404,
            0.0010971185036686574
          ],
          "yaw_delta_rad": 0.546350018089683,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000280",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 58,
      "observation": {
        "object_id": "point-009",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288757019836785,
            0.3889285043101871
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
            153.0,
            284.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000281",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 58,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288757019836785,
            0.3889285043101871
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00050",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00050",
          "pixel_uv": [
            153.0,
            284.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00050",
          "position_m": [
            -0.692434936274639,
            0.43459129634053917,
            1.296575665473938
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
      "evidence_id": "e000282",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.x_m",
      "value": 7.329541224028197e-05
    },
    {
      "evidence_id": "e000283",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.y_m",
      "value": 0.0708923286433246
    },
    {
      "evidence_id": "e000284",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 58,
      "name": "pose.yaw_rad",
      "value": -0.22337345322552868
    },
    {
      "evidence_id": "e000285",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 58,
      "name": "point-009.range_m",
      "value": 1.7579
    },
    {
      "evidence_id": "e000286",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 58,
      "name": "point-009.bearing_rad",
      "value": 0.4053
    },
    {
      "evidence_id": "e000287",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 58,
      "action": {
        "call_id": "call_3c87047b1b4749fcad22766e",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000288",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.x_m",
      "value": 0.006995001036468095
    },
    {
      "evidence_id": "e000289",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.y_m",
      "value": 0.07294145537818453
    },
    {
      "evidence_id": "e000290",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 59,
      "name": "pose.yaw_rad",
      "value": 0.22048312326552572
    },
    {
      "evidence_id": "e000291",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 59,
      "action": {
        "call_id": "call_9297eaf51553484cb3f53216",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0062958171460826655,
            0.0035315174623773435
          ],
          "yaw_delta_rad": 0.44385657649105426,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000292",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 60,
      "observation": {
        "object_id": "point-010",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7315112103171602,
            0.3821811098989973
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
            336.0,
            185.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000293",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 60,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7315112103171602,
            0.3821811098989973
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00051",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00051",
          "pixel_uv": [
            336.0,
            185.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00051",
          "position_m": [
            0.07567881840338608,
            0.025226272801128692,
            1.4299588203430176
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
      "evidence_id": "e000294",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.x_m",
      "value": 0.006995001036468095
    },
    {
      "evidence_id": "e000295",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.y_m",
      "value": 0.07294145537818453
    },
    {
      "evidence_id": "e000296",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 60,
      "name": "pose.yaw_rad",
      "value": 0.22048312326552572
    },
    {
      "evidence_id": "e000297",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 60,
      "name": "point-010.range_m",
      "value": 1.752
    },
    {
      "evidence_id": "e000298",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 60,
      "name": "point-010.bearing_rad",
      "value": -0.0431
    },
    {
      "evidence_id": "e000299",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 60,
      "action": {
        "call_id": "call_8b5a752b645f4f09898fc971",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000300",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.x_m",
      "value": 0.01868239172104597
    },
    {
      "evidence_id": "e000301",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.y_m",
      "value": 0.08901780824954056
    },
    {
      "evidence_id": "e000302",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 61,
      "name": "pose.yaw_rad",
      "value": 0.6657893007690125
    },
    {
      "evidence_id": "e000303",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 61,
      "action": {
        "call_id": "call_cf3368d7c98c45188a662456",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.014920376881491892,
            0.013131130049335327
          ],
          "yaw_delta_rad": 0.445306177503487,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000304",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.x_m",
      "value": 0.031594077710421865
    },
    {
      "evidence_id": "e000305",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.y_m",
      "value": 0.08660878103968966
    },
    {
      "evidence_id": "e000306",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 62,
      "name": "pose.yaw_rad",
      "value": 1.2041011479047725
    },
    {
      "evidence_id": "e000307",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 62,
      "action": {
        "call_id": "call_a6ac3da61b9140f5a3d3f10a",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.008666122631534535,
            -0.009869820956899512
          ],
          "yaw_delta_rad": 0.53831184713576,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000308",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 63,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000309",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.x_m",
      "value": 0.017153004727190824
    },
    {
      "evidence_id": "e000310",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.y_m",
      "value": 0.09376031035785932
    },
    {
      "evidence_id": "e000311",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 63,
      "name": "pose.yaw_rad",
      "value": 1.6584380555426124
    },
    {
      "evidence_id": "e000312",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 63,
      "action": {
        "call_id": "call_8256f90e9dc24806a837ea03",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0014984855947032423,
            0.016045046008600683
          ],
          "yaw_delta_rad": 0.45433690763784007,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000313",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.x_m",
      "value": 0.005222723504631332
    },
    {
      "evidence_id": "e000314",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.y_m",
      "value": 0.10123607207845073
    },
    {
      "evidence_id": "e000315",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 64,
      "name": "pose.yaw_rad",
      "value": 1.2227215417062047
    },
    {
      "evidence_id": "e000316",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 64,
      "action": {
        "call_id": "call_f26a1d92a68b4996b1449066",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.008491321601173331,
            0.011230141620561266
          ],
          "yaw_delta_rad": -0.4357165138364074,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000317",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.x_m",
      "value": 0.023246956434826885
    },
    {
      "evidence_id": "e000318",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.y_m",
      "value": 0.11230809008035963
    },
    {
      "evidence_id": "e000319",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 65,
      "name": "pose.yaw_rad",
      "value": 0.6840697212892062
    },
    {
      "evidence_id": "e000320",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 65,
      "action": {
        "call_id": "call_a9983bb5b46a46f3873606a9",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0002",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.016555903317881884,
            -0.013166799940968506
          ],
          "yaw_delta_rad": -0.5386518204169986,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000321",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 66,
      "observation": {
        "object_id": "point-011",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.8030046064675997,
            0.414336577286907
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
            552.0,
            244.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000322",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 66,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            2.8030046064675997,
            0.414336577286907
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00056",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00056",
          "pixel_uv": [
            552.0,
            244.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00056",
          "position_m": [
            1.5159755968576873,
            0.42056097203148746,
            2.0328361988067627
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
      "evidence_id": "e000323",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 66,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7315112103171602,
          0.3821811098989973
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          2.8030046064675997,
          0.414336577286907
        ]
      },
      "evidence_ids": [
        "e000322"
      ]
    },
    {
      "evidence_id": "e000324",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.x_m",
      "value": 0.023246956434826885
    },
    {
      "evidence_id": "e000325",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.y_m",
      "value": 0.11230809008035963
    },
    {
      "evidence_id": "e000326",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 66,
      "name": "pose.yaw_rad",
      "value": 0.6840697212892062
    },
    {
      "evidence_id": "e000327",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 66,
      "name": "point-011.range_m",
      "value": 2.7961
    },
    {
      "evidence_id": "e000328",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 66,
      "name": "point-011.bearing_rad",
      "value": -0.5758
    },
    {
      "evidence_id": "e000329",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 66,
      "action": {
        "call_id": "call_0c4cb55a1c0b4cee93ec379a",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000330",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 66,
      "plan_id": "plan-0003"
    },
    {
      "evidence_id": "e000331",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.x_m",
      "value": 0.04221240607761126
    },
    {
      "evidence_id": "e000332",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.y_m",
      "value": 0.13129299538670022
    },
    {
      "evidence_id": "e000333",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 67,
      "name": "pose.yaw_rad",
      "value": 1.125621962030872
    },
    {
      "evidence_id": "e000334",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 67,
      "action": {
        "call_id": "call_52dcadac2bd144e4b77a504e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.026695916237754018,
            0.002728179955671841
          ],
          "yaw_delta_rad": 0.4415522407416659,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000335",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 68,
      "object_id": "point-009",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000336",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.x_m",
      "value": 0.0220457751320163
    },
    {
      "evidence_id": "e000337",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.y_m",
      "value": 0.15343360102436668
    },
    {
      "evidence_id": "e000338",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 68,
      "name": "pose.yaw_rad",
      "value": 1.5882341301483835
    },
    {
      "evidence_id": "e000339",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 68,
      "action": {
        "call_id": "call_84cbd7ec38fc41278f9a2720",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011298625710055094,
            0.02773518485178311
          ],
          "yaw_delta_rad": 0.4626121681175115,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000340",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.x_m",
      "value": 0.0029355015605772037
    },
    {
      "evidence_id": "e000341",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.y_m",
      "value": 0.16661185028480913
    },
    {
      "evidence_id": "e000342",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 69,
      "name": "pose.yaw_rad",
      "value": 2.1385484314652046
    },
    {
      "evidence_id": "e000343",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 69,
      "action": {
        "call_id": "call_3d7f2293bbdd4b798a5062ad",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.013509470014386706,
            0.018877580074680683
          ],
          "yaw_delta_rad": 0.5503143013168206,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000344",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 70,
      "object_id": "point-010",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000345",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.x_m",
      "value": 0.005741056104070069
    },
    {
      "evidence_id": "e000346",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.y_m",
      "value": 0.18198085655086546
    },
    {
      "evidence_id": "e000347",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 70,
      "name": "pose.yaw_rad",
      "value": 2.6802111125306913
    },
    {
      "evidence_id": "e000348",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 70,
      "action": {
        "call_id": "call_26ee62d6505044b3bd92e297",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011449138020582483,
            -0.010629897858787067
          ],
          "yaw_delta_rad": 0.5416626810654868,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000349",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.x_m",
      "value": -0.006506581956233125
    },
    {
      "evidence_id": "e000350",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.y_m",
      "value": 0.1630258517229351
    },
    {
      "evidence_id": "e000351",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 71,
      "name": "pose.yaw_rad",
      "value": -3.040819501176629
    },
    {
      "evidence_id": "e000352",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 71,
      "action": {
        "call_id": "call_5387cf929dbb4d26802596ba",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0025285088221805464,
            0.022425509787275883
          ],
          "yaw_delta_rad": 0.5621546934722659,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000353",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.x_m",
      "value": -0.022518234718098606
    },
    {
      "evidence_id": "e000354",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.y_m",
      "value": 0.15209445224145832
    },
    {
      "evidence_id": "e000355",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 72,
      "name": "pose.yaw_rad",
      "value": -2.592199658716798
    },
    {
      "evidence_id": "e000356",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 72,
      "action": {
        "call_id": "call_9207dd6a163b431993d99aec",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.017030148593741547,
            0.009265125885020022
          ],
          "yaw_delta_rad": 0.4486198424598311,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000357",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.x_m",
      "value": -0.0343887608578652
    },
    {
      "evidence_id": "e000358",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.y_m",
      "value": 0.1342869204566751
    },
    {
      "evidence_id": "e000359",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 73,
      "name": "pose.yaw_rad",
      "value": -2.1075875873208525
    },
    {
      "evidence_id": "e000360",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 73,
      "action": {
        "call_id": "call_743943b633ea42f0a059d652",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01942223153321549,
            0.008988576159276642
          ],
          "yaw_delta_rad": 0.4846120713959454,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000361",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.x_m",
      "value": -0.036938690500317714
    },
    {
      "evidence_id": "e000362",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.y_m",
      "value": 0.12258118110565641
    },
    {
      "evidence_id": "e000363",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 74,
      "name": "pose.yaw_rad",
      "value": -1.5630027184987811
    },
    {
      "evidence_id": "e000364",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 74,
      "action": {
        "call_id": "call_ce5c3378a5264a58ac9d05ed",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011363359879276514,
            0.0037948026548813222
          ],
          "yaw_delta_rad": 0.5445848688220716,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000365",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.x_m",
      "value": -0.009947949941859149
    },
    {
      "evidence_id": "e000366",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.y_m",
      "value": 0.11726972929521587
    },
    {
      "evidence_id": "e000367",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 75,
      "name": "pose.yaw_rad",
      "value": -1.0022570510533126
    },
    {
      "evidence_id": "e000368",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 75,
      "action": {
        "call_id": "call_68fe8c15624d4a3c907248e0",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0055216436316216245,
            0.02694852589352569
          ],
          "yaw_delta_rad": 0.5607456674454685,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000369",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 76,
      "object_id": "task:B",
      "old_state": "contradicted",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000370",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 76,
      "object_id": "point-011",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000371",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.x_m",
      "value": 0.002905241841746267
    },
    {
      "evidence_id": "e000372",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.y_m",
      "value": 0.10821000601705194
    },
    {
      "evidence_id": "e000373",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 76,
      "name": "pose.yaw_rad",
      "value": -0.5560351458662964
    },
    {
      "evidence_id": "e000374",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 76,
      "action": {
        "call_id": "call_ada756a1c2e147969826d31b",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.014554703238538226,
            0.005953464415038696
          ],
          "yaw_delta_rad": 0.44622190518701643,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000375",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.x_m",
      "value": 0.018121905208427224
    },
    {
      "evidence_id": "e000376",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.y_m",
      "value": 0.12091449996967389
    },
    {
      "evidence_id": "e000377",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 77,
      "name": "pose.yaw_rad",
      "value": -0.1090996233956608
    },
    {
      "evidence_id": "e000378",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 77,
      "action": {
        "call_id": "call_d2dbc230a1884cca99b58b7e",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.006218620411302816,
            0.018822321078634966
          ],
          "yaw_delta_rad": 0.4469355224706355,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000379",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 78,
      "observation": {
        "object_id": "point-012",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7479145956059345,
            0.3818201308927221
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00067",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00067",
          "pixel_uv": [
            219.0,
            281.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000380",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 78,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7479145956059345,
            0.3818201308927221
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00067",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00067",
          "pixel_uv": [
            219.0,
            281.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00067",
          "position_m": [
            -0.44180576198873034,
            0.44620183922244905,
            1.3705612421035767
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
      "evidence_id": "e000381",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 78,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7315112103171602,
          0.3821811098989973
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7479145956059345,
          0.3818201308927221
        ]
      },
      "evidence_ids": [
        "e000380"
      ]
    },
    {
      "evidence_id": "e000382",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.x_m",
      "value": 0.018121905208427224
    },
    {
      "evidence_id": "e000383",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.y_m",
      "value": 0.12091449996967389
    },
    {
      "evidence_id": "e000384",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 78,
      "name": "pose.yaw_rad",
      "value": -0.1090996233956608
    },
    {
      "evidence_id": "e000385",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 78,
      "name": "point-012.range_m",
      "value": 1.7493
    },
    {
      "evidence_id": "e000386",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 78,
      "name": "point-012.bearing_rad",
      "value": 0.2588
    },
    {
      "evidence_id": "e000387",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 78,
      "action": {
        "call_id": "call_c2f30aca11d5415eb05e7fd3",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000388",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 79,
      "observation": {
        "object_id": "point-012",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.772913822102048,
            0.3807952714390636
          ]
        },
        "pose_covariance": null,
        "confidence": 0.239,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00068",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00068",
          "pixel_uv": [
            395.15,
            257.83
          ]
        }
      }
    },
    {
      "evidence_id": "e000389",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.x_m",
      "value": 0.025314816618093285
    },
    {
      "evidence_id": "e000390",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.y_m",
      "value": 0.13582326072867187
    },
    {
      "evidence_id": "e000391",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 79,
      "name": "pose.yaw_rad",
      "value": 0.3404318793556397
    },
    {
      "evidence_id": "e000392",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 79,
      "name": "point-012.range_m",
      "value": 1.7647
    },
    {
      "evidence_id": "e000393",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 79,
      "name": "point-012.bearing_rad",
      "value": -0.2012
    },
    {
      "evidence_id": "e000394",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 79,
      "action": {
        "call_id": "call_94d7b8386102415bac9a06b2",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0055268308270272955,
            0.015603309358138188
          ],
          "yaw_delta_rad": 0.4495315027513005,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000395",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 80,
      "observation": {
        "object_id": "point-013",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.5644271928668174,
            0.6707092282798046
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
            386.0,
            177.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000396",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 80,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            3.5644271928668174,
            0.6707092282798046
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00068",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00068",
          "pixel_uv": [
            386.0,
            177.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00068",
          "position_m": [
            0.6809175959497902,
            -0.025598405862774065,
            3.192317247390747
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
      "evidence_id": "e000397",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 80,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7315112103171602,
          0.3821811098989973
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          3.5644271928668174,
          0.6707092282798046
        ]
      },
      "evidence_ids": [
        "e000396"
      ]
    },
    {
      "evidence_id": "e000398",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.x_m",
      "value": 0.025314816618093285
    },
    {
      "evidence_id": "e000399",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.y_m",
      "value": 0.13582326072867187
    },
    {
      "evidence_id": "e000400",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 80,
      "name": "pose.yaw_rad",
      "value": 0.3404318793556397
    },
    {
      "evidence_id": "e000401",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-013.range_m",
      "value": 3.5793
    },
    {
      "evidence_id": "e000402",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-013.bearing_rad",
      "value": -0.1904
    },
    {
      "evidence_id": "e000403",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-012.range_m",
      "value": 1.7647
    },
    {
      "evidence_id": "e000404",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 80,
      "name": "point-012.bearing_rad",
      "value": -0.2012
    },
    {
      "evidence_id": "e000405",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 80,
      "action": {
        "call_id": "call_8d0e5c32957e4ff1bb2f538e",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000406",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.x_m",
      "value": 0.014800213534716939
    },
    {
      "evidence_id": "e000407",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.y_m",
      "value": 0.1675699650333526
    },
    {
      "evidence_id": "e000408",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 81,
      "name": "pose.yaw_rad",
      "value": 0.9212007868534482
    },
    {
      "evidence_id": "e000409",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 81,
      "action": {
        "call_id": "call_eaf97d11dd2b4bf98ddc985f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0006888651754179357,
            0.03343554361723281
          ],
          "yaw_delta_rad": 0.5807689074978084,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000410",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 82,
      "observation": {
        "object_id": "point-014",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7339286944445838,
            0.6625421118502557
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00069",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00069",
          "pixel_uv": [
            617.0,
            304.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000411",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 82,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7339286944445838,
            0.6625421118502557
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00069",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00069",
          "pixel_uv": [
            617.0,
            304.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00069",
          "position_m": [
            1.0653067700465366,
            0.4458174550278784,
            1.1164026260375977
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
      "evidence_id": "e000412",
      "kind": "target_relocated",
      "source": "task_label_rgbd_tracking",
      "step": 82,
      "object_id": "task:B",
      "old_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7315112103171602,
          0.3821811098989973
        ]
      },
      "new_pose": {
        "frame": "episode_start",
        "position_m": [
          1.7339286944445838,
          0.6625421118502557
        ]
      },
      "evidence_ids": [
        "e000411"
      ]
    },
    {
      "evidence_id": "e000413",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.x_m",
      "value": 0.014800213534716939
    },
    {
      "evidence_id": "e000414",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.y_m",
      "value": 0.1675699650333526
    },
    {
      "evidence_id": "e000415",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 82,
      "name": "pose.yaw_rad",
      "value": 0.9212007868534482
    },
    {
      "evidence_id": "e000416",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 82,
      "name": "point-014.range_m",
      "value": 1.789
    },
    {
      "evidence_id": "e000417",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 82,
      "name": "point-014.bearing_rad",
      "value": -0.6408
    },
    {
      "evidence_id": "e000418",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 82,
      "action": {
        "call_id": "call_b8195020c29e482abec36726",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000419",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.x_m",
      "value": 0.005673723562498602
    },
    {
      "evidence_id": "e000420",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.y_m",
      "value": 0.18205247719946738
    },
    {
      "evidence_id": "e000421",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 83,
      "name": "pose.yaw_rad",
      "value": 1.4718798481826165
    },
    {
      "evidence_id": "e000422",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 83,
      "action": {
        "call_id": "call_f2197dc923e947368e42ccb2",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.006012548666191429,
            0.016027639763587887
          ],
          "yaw_delta_rad": 0.5506790613291686,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000423",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.x_m",
      "value": -0.010594594712750543
    },
    {
      "evidence_id": "e000424",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.y_m",
      "value": 0.1836157926074886
    },
    {
      "evidence_id": "e000425",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 84,
      "name": "pose.yaw_rad",
      "value": 1.9103499526356447
    },
    {
      "evidence_id": "e000426",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 84,
      "action": {
        "call_id": "call_c7bcc8b9b3d648bf880d24fc",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -5.090830182215723e-05,
            0.016343180318241838
          ],
          "yaw_delta_rad": 0.43847010445302814,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000427",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.x_m",
      "value": -0.02943323980818353
    },
    {
      "evidence_id": "e000428",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.y_m",
      "value": 0.18213472979622913
    },
    {
      "evidence_id": "e000429",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 85,
      "name": "pose.yaw_rad",
      "value": 2.36099523975099
    },
    {
      "evidence_id": "e000430",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 85,
      "action": {
        "call_id": "call_cfbebc6110d34111a48adb1c",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.004878017436420913,
            0.01825631512580101
          ],
          "yaw_delta_rad": 0.45064528711534546,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000431",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.x_m",
      "value": -0.04643708854363482
    },
    {
      "evidence_id": "e000432",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.y_m",
      "value": 0.19282154892994224
    },
    {
      "evidence_id": "e000433",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 86,
      "name": "pose.yaw_rad",
      "value": 1.9230134653340172
    },
    {
      "evidence_id": "e000434",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 86,
      "action": {
        "call_id": "call_b8dbbd5ffdd94554b88f977b",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.019601477366483655,
            0.004372763435864513
          ],
          "yaw_delta_rad": -0.43798177441697295,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000435",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.x_m",
      "value": -0.07147331599662629
    },
    {
      "evidence_id": "e000436",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.y_m",
      "value": 0.2165672786704239
    },
    {
      "evidence_id": "e000437",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 87,
      "name": "pose.yaw_rad",
      "value": 2.458200980181224
    },
    {
      "evidence_id": "e000438",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 87,
      "action": {
        "call_id": "call_33e183d5be5f4f6e91cc8eca",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.03092497281268538,
            0.015307462968127338
          ],
          "yaw_delta_rad": 0.5351875148472063,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000439",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.x_m",
      "value": -0.09879893513197881
    },
    {
      "evidence_id": "e000440",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.y_m",
      "value": 0.2037529411309373
    },
    {
      "evidence_id": "e000441",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 88,
      "name": "pose.yaw_rad",
      "value": 2.921266037890462
    },
    {
      "evidence_id": "e000442",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 88,
      "action": {
        "call_id": "call_7929b7c6adce400aa07456e4",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.013097943047754785,
            0.02719081822277535
          ],
          "yaw_delta_rad": 0.4630650577092381,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000443",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 89,
      "object_id": "point-012",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000444",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.x_m",
      "value": -0.11351457704677055
    },
    {
      "evidence_id": "e000445",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.y_m",
      "value": 0.19085942905868358
    },
    {
      "evidence_id": "e000446",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 89,
      "name": "pose.yaw_rad",
      "value": -2.823769708094789
    },
    {
      "evidence_id": "e000447",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 89,
      "action": {
        "call_id": "call_5fa5bbd1bb344665b4832940",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.011542051902071625,
            0.01579790519061347
          ],
          "yaw_delta_rad": 0.5381495611943352,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000448",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 90,
      "object_id": "point-013",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000449",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.x_m",
      "value": -0.12796610717316687
    },
    {
      "evidence_id": "e000450",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.y_m",
      "value": 0.178074398898292
    },
    {
      "evidence_id": "e000451",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 90,
      "name": "pose.yaw_rad",
      "value": -2.3272229092804637
    },
    {
      "evidence_id": "e000452",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 90,
      "action": {
        "call_id": "call_bf97e1ad528f4a37a6c0e50f",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.017723081259749782,
            0.007628637483625037
          ],
          "yaw_delta_rad": 0.4965467988143253,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000453",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.x_m",
      "value": -0.1276415905091133
    },
    {
      "evidence_id": "e000454",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.y_m",
      "value": 0.1553059966318073
    },
    {
      "evidence_id": "e000455",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 91,
      "name": "pose.yaw_rad",
      "value": -1.880544611974724
    },
    {
      "evidence_id": "e000456",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 91,
      "action": {
        "call_id": "call_cd60de9e68f74cdda3cd83bd",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.016336579205739502,
            0.01586258593950918
          ],
          "yaw_delta_rad": 0.44667829730573994,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000457",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 92,
      "object_id": "task:B",
      "old_state": "contradicted",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000458",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 92,
      "object_id": "point-014",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000459",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.x_m",
      "value": -0.10099355535486487
    },
    {
      "evidence_id": "e000460",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.y_m",
      "value": 0.14393100174354131
    },
    {
      "evidence_id": "e000461",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 92,
      "name": "pose.yaw_rad",
      "value": -1.3062884713889815
    },
    {
      "evidence_id": "e000462",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 92,
      "action": {
        "call_id": "call_6de625f2c385413e85057b69",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0027108375692057457,
            0.028847177434950536
          ],
          "yaw_delta_rad": 0.5742561405857423,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000463",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.x_m",
      "value": -0.11174718425308218
    },
    {
      "evidence_id": "e000464",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.y_m",
      "value": 0.13461868723256748
    },
    {
      "evidence_id": "e000465",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 93,
      "name": "pose.yaw_rad",
      "value": -0.7627874510535329
    },
    {
      "evidence_id": "e000466",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 93,
      "action": {
        "call_id": "call_678c3b0a16f547779463bde8",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0061770770076646185,
            -0.01281418962218249
          ],
          "yaw_delta_rad": 0.5435010203354484,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000467",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.x_m",
      "value": -0.08583286134549066
    },
    {
      "evidence_id": "e000468",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.y_m",
      "value": 0.13812998374531518
    },
    {
      "evidence_id": "e000469",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 94,
      "name": "pose.yaw_rad",
      "value": -0.2237611908025609
    },
    {
      "evidence_id": "e000470",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 94,
      "action": {
        "call_id": "call_19bc84dc9ca94990a8f6cc52",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01630770491022448,
            0.02044358323583214
          ],
          "yaw_delta_rad": 0.5390262602509717,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000471",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 95,
      "observation": {
        "object_id": "point-015",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.882980351193795,
            0.3793671784950846
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00081",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00081",
          "pixel_uv": [
            184.0,
            270.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000472",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 95,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.882980351193795,
            0.3793671784950846
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00081",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00081",
          "pixel_uv": [
            184.0,
            270.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00081",
          "position_m": [
            -0.6708624384053115,
            0.44806679465446997,
            1.5435734987258911
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
      "evidence_id": "e000473",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.x_m",
      "value": -0.08583286134549066
    },
    {
      "evidence_id": "e000474",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.y_m",
      "value": 0.13812998374531518
    },
    {
      "evidence_id": "e000475",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 95,
      "name": "pose.yaw_rad",
      "value": -0.2237611908025609
    },
    {
      "evidence_id": "e000476",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 95,
      "name": "point-015.range_m",
      "value": 1.9835
    },
    {
      "evidence_id": "e000477",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 95,
      "name": "point-015.bearing_rad",
      "value": 0.3457
    },
    {
      "evidence_id": "e000478",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 95,
      "action": {
        "call_id": "call_0dd620352e5045e4b93f4f7c",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000479",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.x_m",
      "value": -0.08365791734551321
    },
    {
      "evidence_id": "e000480",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.y_m",
      "value": 0.12464376325201977
    },
    {
      "evidence_id": "e000481",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 96,
      "name": "pose.yaw_rad",
      "value": -0.7565206219066699
    },
    {
      "evidence_id": "e000482",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 96,
      "action": {
        "call_id": "call_77637fff890749a3bd473304",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.005113295637691221,
            -0.012667388535857999
          ],
          "yaw_delta_rad": -0.5327594311041093,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000483",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.x_m",
      "value": -0.07201222681746851
    },
    {
      "evidence_id": "e000484",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.y_m",
      "value": 0.12462225296677067
    },
    {
      "evidence_id": "e000485",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 97,
      "name": "pose.yaw_rad",
      "value": -0.3028302193082128
    },
    {
      "evidence_id": "e000486",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 97,
      "action": {
        "call_id": "call_87f527da7a864dff94d8c907",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00848384420410982,
            0.007977904366922058
          ],
          "yaw_delta_rad": 0.45369040259845717,
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
      "step": 98,
      "observation": {
        "object_id": "point-016",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7289218991869801,
            0.38980959013163663
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00083",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00083",
          "pixel_uv": [
            133.0,
            272.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000488",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 98,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7289218991869801,
            0.38980959013163663
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00083",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00083",
          "pixel_uv": [
            133.0,
            272.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00083",
          "position_m": [
            -0.7935923410539264,
            0.3936047804154863,
            1.3266359567642212
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
      "evidence_id": "e000489",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.x_m",
      "value": -0.07201222681746851
    },
    {
      "evidence_id": "e000490",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.y_m",
      "value": 0.12462225296677067
    },
    {
      "evidence_id": "e000491",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 98,
      "name": "pose.yaw_rad",
      "value": -0.3028302193082128
    },
    {
      "evidence_id": "e000492",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 98,
      "name": "point-016.range_m",
      "value": 1.8204
    },
    {
      "evidence_id": "e000493",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 98,
      "name": "point-016.bearing_rad",
      "value": 0.4491
    },
    {
      "evidence_id": "e000494",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 98,
      "action": {
        "call_id": "call_b08d177ffa4c40d3a5d678d7",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000495",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.x_m",
      "value": -0.06230521464766343
    },
    {
      "evidence_id": "e000496",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.y_m",
      "value": 0.1411234316536022
    },
    {
      "evidence_id": "e000497",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 99,
      "name": "pose.yaw_rad",
      "value": 0.14754761721210832
    },
    {
      "evidence_id": "e000498",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 99,
      "action": {
        "call_id": "call_d36cadf725bd46508eb9ccf0",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.004344278750494795,
            0.01864516627594095
          ],
          "yaw_delta_rad": 0.45037783652032104,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000499",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 100,
      "observation": {
        "object_id": "point-017",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.728840642044429,
            0.3861067169094535
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00084",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00084",
          "pixel_uv": [
            324.0,
            183.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000500",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 100,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.728840642044429,
            0.3861067169094535
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00084",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00084",
          "pixel_uv": [
            324.0,
            183.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00084",
          "position_m": [
            0.021463410765673457,
            0.016693763928857134,
            1.48702871799469
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
      "evidence_id": "e000501",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.x_m",
      "value": -0.06230521464766343
    },
    {
      "evidence_id": "e000502",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.y_m",
      "value": 0.1411234316536022
    },
    {
      "evidence_id": "e000503",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 100,
      "name": "pose.yaw_rad",
      "value": 0.14754761721210832
    },
    {
      "evidence_id": "e000504",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 100,
      "name": "point-017.range_m",
      "value": 1.8078
    },
    {
      "evidence_id": "e000505",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 100,
      "name": "point-017.bearing_rad",
      "value": -0.0116
    },
    {
      "evidence_id": "e000506",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 100,
      "action": {
        "call_id": "call_3a43858c73d24617b1fb6ac7",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000507",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.x_m",
      "value": -0.053938713297895756
    },
    {
      "evidence_id": "e000508",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.y_m",
      "value": 0.15434028674080943
    },
    {
      "evidence_id": "e000509",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 101,
      "name": "pose.yaw_rad",
      "value": 0.6910820483856667
    },
    {
      "evidence_id": "e000510",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 101,
      "action": {
        "call_id": "call_119d3e30af3948628eb58296",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010218643237011233,
            0.011843265327880858
          ],
          "yaw_delta_rad": 0.5435344311735584,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000511",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.x_m",
      "value": -0.05208922257622901
    },
    {
      "evidence_id": "e000512",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.y_m",
      "value": 0.16016144386113243
    },
    {
      "evidence_id": "e000513",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 102,
      "name": "pose.yaw_rad",
      "value": 1.2316573904253447
    },
    {
      "evidence_id": "e000514",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 102,
      "action": {
        "call_id": "call_f6ab5151440e4d7ca25cc807",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0003",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.005135376335980223,
            0.0033067198304169887
          ],
          "yaw_delta_rad": 0.5405753420396779,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000515",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 102,
      "plan_id": "plan-0004"
    },
    {
      "evidence_id": "e000516",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 103,
      "object_id": "task:B",
      "old_state": "confirmed",
      "state": "predicted",
      "unobserved_steps": 3
    },
    {
      "evidence_id": "e000517",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.x_m",
      "value": -0.06430980429618206
    },
    {
      "evidence_id": "e000518",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.y_m",
      "value": 0.1955989010461573
    },
    {
      "evidence_id": "e000519",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 103,
      "name": "pose.yaw_rad",
      "value": 0.7925879894375826
    },
    {
      "evidence_id": "e000520",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 103,
      "action": {
        "call_id": "call_30d634e112854df1a2b076fb",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.029353507273452838,
            0.02331367838977521
          ],
          "yaw_delta_rad": -0.43906940098776204,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000521",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 104,
      "observation": {
        "object_id": "point-018",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8590894632132973,
            0.566667624794196
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00087",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00087",
          "pixel_uv": [
            588.0,
            179.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000522",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 104,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.8590894632132973,
            0.566667624794196
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00087",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00087",
          "pixel_uv": [
            588.0,
            179.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00087",
          "position_m": [
            1.111903756923816,
            -0.0020705842773255418,
            1.291088581085205
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
      "evidence_id": "e000523",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.x_m",
      "value": -0.06430980429618206
    },
    {
      "evidence_id": "e000524",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.y_m",
      "value": 0.1955989010461573
    },
    {
      "evidence_id": "e000525",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 104,
      "name": "pose.yaw_rad",
      "value": 0.7925879894375826
    },
    {
      "evidence_id": "e000526",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 104,
      "name": "point-018.range_m",
      "value": 1.9588
    },
    {
      "evidence_id": "e000527",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 104,
      "name": "point-018.bearing_rad",
      "value": -0.602
    },
    {
      "evidence_id": "e000528",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 104,
      "action": {
        "call_id": "call_a44fc26c91874f93ab4511e6",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000529",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 105,
      "object_id": "point-015",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000530",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.x_m",
      "value": -0.06430980429618206
    },
    {
      "evidence_id": "e000531",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.y_m",
      "value": 0.1955989010461573
    },
    {
      "evidence_id": "e000532",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 105,
      "name": "pose.yaw_rad",
      "value": 0.7925879894375826
    },
    {
      "evidence_id": "e000533",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 105,
      "name": "point-018.range_m",
      "value": 1.9588
    },
    {
      "evidence_id": "e000534",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 105,
      "name": "point-018.bearing_rad",
      "value": -0.602
    },
    {
      "evidence_id": "e000535",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 105,
      "action": {
        "call_id": "call_2d4fe6e748ee4cafae9dee0b",
        "tool": "get_geometry",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000536",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.x_m",
      "value": -0.07083253954324412
    },
    {
      "evidence_id": "e000537",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.y_m",
      "value": 0.19031917347583022
    },
    {
      "evidence_id": "e000538",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 106,
      "name": "pose.yaw_rad",
      "value": 1.3481805618048674
    },
    {
      "evidence_id": "e000539",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 106,
      "action": {
        "call_id": "call_2763565e439f46b59040e804",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.008339066421525496,
            0.0009389193455900998
          ],
          "yaw_delta_rad": 0.555592572367285,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000540",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.x_m",
      "value": -0.07384893787471859
    },
    {
      "evidence_id": "e000541",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.y_m",
      "value": 0.19151383536898184
    },
    {
      "evidence_id": "e000542",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 107,
      "name": "pose.yaw_rad",
      "value": 1.79989627518117
    },
    {
      "evidence_id": "e000543",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 107,
      "action": {
        "call_id": "call_960f34bf8d94472692910f1c",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.0004992163232361315,
            0.0032057228507288713
          ],
          "yaw_delta_rad": 0.45171571337630256,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000544",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 108,
      "object_id": "point-016",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000545",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.x_m",
      "value": -0.07384893787471859
    },
    {
      "evidence_id": "e000546",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.y_m",
      "value": 0.19151383536898184
    },
    {
      "evidence_id": "e000547",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 108,
      "name": "pose.yaw_rad",
      "value": 1.79989627518117
    },
    {
      "evidence_id": "e000548",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 108,
      "action": {
        "call_id": "call_32a78df8cb784a02a2768130",
        "tool": "observe",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000549",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.x_m",
      "value": -0.08860576234404811
    },
    {
      "evidence_id": "e000550",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.y_m",
      "value": 0.1975306143453776
    },
    {
      "evidence_id": "e000551",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 109,
      "name": "pose.yaw_rad",
      "value": 2.2629358943469033
    },
    {
      "evidence_id": "e000552",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 109,
      "action": {
        "call_id": "call_d211f040b21f47aeb161b5ef",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.009210858508126652,
            0.013004829226586238
          ],
          "yaw_delta_rad": 0.4630396191657331,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000553",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 110,
      "object_id": "point-017",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000554",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.x_m",
      "value": -0.10090554616292463
    },
    {
      "evidence_id": "e000555",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.y_m",
      "value": 0.20043723211372402
    },
    {
      "evidence_id": "e000556",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 110,
      "name": "pose.yaw_rad",
      "value": 2.7073156217638474
    },
    {
      "evidence_id": "e000557",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 110,
      "action": {
        "call_id": "call_88596c5d7b3448e89a2b0639",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010087301755511695,
            0.007614423952973342
          ],
          "yaw_delta_rad": 0.4443797274169441,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000558",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.x_m",
      "value": -0.10737741825635078
    },
    {
      "evidence_id": "e000559",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.y_m",
      "value": 0.1812144039824489
    },
    {
      "evidence_id": "e000560",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 111,
      "name": "pose.yaw_rad",
      "value": -3.109282312591661
    },
    {
      "evidence_id": "e000561",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 111,
      "action": {
        "call_id": "call_28cac3581b2b4838a57b0e64",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.0022169772357514238,
            0.02016152924989495
          ],
          "yaw_delta_rad": 0.4665873728240779,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000562",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.x_m",
      "value": -0.131895298719047
    },
    {
      "evidence_id": "e000563",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.y_m",
      "value": 0.18457383552459916
    },
    {
      "evidence_id": "e000564",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 112,
      "name": "pose.yaw_rad",
      "value": -2.668323738335165
    },
    {
      "evidence_id": "e000565",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 112,
      "action": {
        "call_id": "call_562e0b3d6acf4f468352a41d",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.024396558261929106,
            -0.004149721393268904
          ],
          "yaw_delta_rad": 0.44095857425649587,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000566",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.x_m",
      "value": -0.1286399674478852
    },
    {
      "evidence_id": "e000567",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.y_m",
      "value": 0.15860906449641474
    },
    {
      "evidence_id": "e000568",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 113,
      "name": "pose.yaw_rad",
      "value": -2.207824182637156
    },
    {
      "evidence_id": "e000569",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 113,
      "action": {
        "call_id": "call_9ebfa04e4f98484b9ebbb413",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.00893718377092105,
            0.02459457790806408
          ],
          "yaw_delta_rad": 0.46049955569800893,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000570",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 114,
      "object_id": "task:B",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000571",
      "kind": "belief_state_changed",
      "source": "memory_rules",
      "step": 114,
      "object_id": "point-018",
      "old_state": "unknown",
      "state": "stale",
      "unobserved_steps": 10
    },
    {
      "evidence_id": "e000572",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.x_m",
      "value": -0.13213264643220554
    },
    {
      "evidence_id": "e000573",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.y_m",
      "value": 0.1370335448090726
    },
    {
      "evidence_id": "e000574",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 114,
      "name": "pose.yaw_rad",
      "value": -1.7625754371802813
    },
    {
      "evidence_id": "e000575",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 114,
      "action": {
        "call_id": "call_a36cecfa697a48eca8488913",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.019421328227470232,
            0.01002566038459663
          ],
          "yaw_delta_rad": 0.4452487454568752,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000576",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.x_m",
      "value": -0.13711137436264811
    },
    {
      "evidence_id": "e000577",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.y_m",
      "value": 0.12738344518102016
    },
    {
      "evidence_id": "e000578",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 115,
      "name": "pose.yaw_rad",
      "value": -1.318807721801009
    },
    {
      "evidence_id": "e000579",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 115,
      "action": {
        "call_id": "call_ff20920ad8ee40668d083388",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.010422155134799459,
            -0.0030480874303207795
          ],
          "yaw_delta_rad": 0.4437677153792725,
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
      "step": 116,
      "name": "pose.x_m",
      "value": -0.12186602595031967
    },
    {
      "evidence_id": "e000581",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.y_m",
      "value": 0.13625508137548892
    },
    {
      "evidence_id": "e000582",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 116,
      "name": "pose.yaw_rad",
      "value": -0.8625649725480976
    },
    {
      "evidence_id": "e000583",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 116,
      "action": {
        "call_id": "call_c10d5dc71a7f4bf3a5ca711b",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            -0.004790330196190224,
            0.0169758450037623
          ],
          "yaw_delta_rad": 0.4562427492529113,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000584",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.x_m",
      "value": -0.10371363354366789
    },
    {
      "evidence_id": "e000585",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.y_m",
      "value": 0.1316228284145037
    },
    {
      "evidence_id": "e000586",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 117,
      "name": "pose.yaw_rad",
      "value": -0.32488762217033057
    },
    {
      "evidence_id": "e000587",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 117,
      "action": {
        "call_id": "call_d713cc6c124545dcb7eab0d5",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.015326235480223289,
            0.010773746961218751
          ],
          "yaw_delta_rad": 0.5376773503777672,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000588",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 118,
      "observation": {
        "object_id": "point-019",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7431237530184007,
            0.38200652915516187
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00099",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00099",
          "pixel_uv": [
            129.0,
            272.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000589",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 118,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7431237530184007,
            0.38200652915516187
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00099",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00099",
          "pixel_uv": [
            129.0,
            272.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00099",
          "position_m": [
            -0.8287686880290569,
            0.40242049156266546,
            1.3563491106033325
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
      "evidence_id": "e000590",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.x_m",
      "value": -0.10371363354366789
    },
    {
      "evidence_id": "e000591",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.y_m",
      "value": 0.1316228284145037
    },
    {
      "evidence_id": "e000592",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 118,
      "name": "pose.yaw_rad",
      "value": -0.32488762217033057
    },
    {
      "evidence_id": "e000593",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 118,
      "name": "point-019.range_m",
      "value": 1.8637
    },
    {
      "evidence_id": "e000594",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 118,
      "name": "point-019.bearing_rad",
      "value": 0.4596
    },
    {
      "evidence_id": "e000595",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 118,
      "action": {
        "call_id": "call_608dd246b08a4eb4a4675d38",
        "tool": "track_point",
        "status": "succeeded"
      }
    },
    {
      "evidence_id": "e000596",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.x_m",
      "value": -0.08491613033242727
    },
    {
      "evidence_id": "e000597",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.y_m",
      "value": 0.14496089750037075
    },
    {
      "evidence_id": "e000598",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 119,
      "name": "pose.yaw_rad",
      "value": 0.12384347185088797
    },
    {
      "evidence_id": "e000599",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 119,
      "action": {
        "call_id": "call_6b540fc029c8495097667a89",
        "tool": "turn",
        "status": "succeeded",
        "error_code": null,
        "plan_id": "plan-0004",
        "subgoal_id": "scan_A",
        "motion_feedback": {
          "translation_start_frame_m": [
            0.01355659979369853,
            0.01864051544216136
          ],
          "yaw_delta_rad": 0.44873109402121836,
          "source": "tool_result.measured.simulator_ground_truth_delta",
          "navigation_measurement": false
        },
        "stuck": false
      }
    },
    {
      "evidence_id": "e000600",
      "kind": "observation_confirmed",
      "source": "rgbd_optical_flow",
      "step": 120,
      "observation": {
        "object_id": "point-020",
        "category": "unclassified_landmark",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288048201410928,
            0.38353183834067883
          ]
        },
        "pose_covariance": null,
        "confidence": 1.0,
        "source": "rgbd_optical_flow",
        "frame_id": "frame-00100",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00100",
          "pixel_uv": [
            317.0,
            183.0
          ]
        }
      }
    },
    {
      "evidence_id": "e000601",
      "kind": "observation_confirmed",
      "source": "task_label_rgbd_tracking",
      "step": 120,
      "observation": {
        "object_id": "task:B",
        "category": "task_target",
        "pose": {
          "frame": "episode_start",
          "position_m": [
            1.7288048201410928,
            0.38353183834067883
          ]
        },
        "pose_covariance": null,
        "confidence": 0.95,
        "source": "task_label_rgbd_tracking",
        "frame_id": "frame-00100",
        "anchor_node": null,
        "visual_feature": {
          "image_id": "frame-00100",
          "pixel_uv": [
            317.0,
            183.0
          ]
        },
        "task_label": "B",
        "label_description": "绿方块",
        "camera_pose": {
          "frame": "current_camera_optical",
          "image_id": "frame-00100",
          "position_m": [
            -0.012096744867433333,
            0.016935442814406666,
            1.5085567235946655
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
      "evidence_id": "e000602",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.x_m",
      "value": -0.08491613033242727
    },
    {
      "evidence_id": "e000603",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.y_m",
      "value": 0.14496089750037075
    },
    {
      "evidence_id": "e000604",
      "kind": "measurement",
      "source": "simulated_proprioception",
      "step": 120,
      "name": "pose.yaw_rad",
      "value": 0.12384347185088797
    },
    {
      "evidence_id": "e000605",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 120,
      "name": "point-020.range_m",
      "value": 1.8294
    },
    {
      "evidence_id": "e000606",
      "kind": "measurement",
      "source": "rgbd_optical_flow",
      "step": 120,
      "name": "point-020.bearing_rad",
      "value": 0.007
    },
    {
      "evidence_id": "e000607",
      "kind": "action_executed",
      "source": "execution_feedback",
      "step": 120,
      "action": {
        "call_id": "call_9a02c437508442e9af294f8b",
        "tool": "track_point",
        "status": "succeeded"
      }
    }
  ]
}
```

## 操作经验

## 程序工具
