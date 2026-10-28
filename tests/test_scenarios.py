"""Public scene catalog capabilities are independent of the API provider."""

from go2_demo.scenarios import get_scenario, list_scenarios


def test_public_task_catalog_has_distinct_goals_and_honest_unsupported_cases():
    scenarios = list_scenarios()
    assert len({item.task_id for item in scenarios}) == 16
    assert sum(item.supported for item in scenarios if item.category != "baseline") == 13
    assert {item.category for item in scenarios} == {"baseline", "go_to", "distinguish", "go_avoid", "go_through", "crawl"}
    assert all(not item.supported and item.unsupported_reason for item in scenarios if item.category == "crawl")
    assert get_scenario("go_to_blue_ball").target.kind == "sphere"
    assert get_scenario("go_to_green_cube").target.color == "green"
