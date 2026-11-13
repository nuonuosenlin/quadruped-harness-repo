# 记忆库 · memory v1

## 现场状态

规则生成；对象来源与判定证据见 JSON。ledger 为只追加账本，旧计划保留但非活跃。

```json
{
  "world": {
    "step": 0,
    "revision": 1,
    "active_plan_id": "plan-0001"
  },
  "pose": null,
  "objects": [],
  "active_beliefs": [],
  "invalidated": [],
  "events": [],
  "topology": null,
  "confidence_thresholds": {
    "confirmed": 0.8,
    "predicted_after_steps": 3,
    "unknown_after_steps": 6,
    "stale_after_steps": 10,
    "relocation_distance_m": 0.5
  },
  "measurements": {},
  "plans": [
    {
      "subgoals": [
        {
          "subgoal_id": "explore",
          "description": "change viewpoint",
          "preconditions": [],
          "completion": [],
          "active": true,
          "status": "待做",
          "evidence_ids": []
        }
      ],
      "branches": [],
      "recovery": "stop",
      "plan_id": "plan-0001",
      "active": true
    }
  ],
  "ledger": [
    {
      "evidence_id": "e000001",
      "kind": "plan_registered",
      "source": "planning_harness",
      "step": 0,
      "plan_id": "plan-0001"
    }
  ]
}
```

## 操作经验

## 程序工具
