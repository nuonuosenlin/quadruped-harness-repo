# Existing-scene memory demo feasibility audit

Branch: `memory-v1`. Seed: 0. 14 unchanged scenes, 40 ordered pairs.

All candidates fail universal condition (b) by an explicit positive visibility counterexample. No candidate certified; stage 2 not started. No API calls, key reads, viewer, or scene edits.

MuJoCo rays use the unchanged actual scene including furniture rotations, sign glyphs, floor and robot geometry. Letters require glyph visibility. Static poses are geometry checks, not executed policy episodes.

| Scene | First A | Second B | B visible from start (positive certificate) | Turn at A | Distance to A | Heading error | Rejection |
|---|---|---|---|---:|---:|---:|---|
| distinguish_texture_a | A | B | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_a | A | C | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_a | B | A | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_a | B | C | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_a | C | A | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_a | C | B | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_b | A | B | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_b | A | C | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_b | B | A | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_b | B | C | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_b | C | A | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_b | C | B | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_c | A | B | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_c | A | C | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_c | B | A | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_c | B | C | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_c | C | A | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| distinguish_texture_c | C | B | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_avoid_texture_cooker | cooker | red_marker | True | +0.00 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose without turning |
| go_avoid_texture_cooker | red_marker | cooker | True | +0.60 | 1.170 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_avoid_texture_drawers | drawers | red_marker | True | +0.00 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose without turning |
| go_avoid_texture_drawers | red_marker | drawers | True | +0.60 | 1.170 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_avoid_texture_fan | fan | red_marker | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_avoid_texture_fan | red_marker | fan | True | +0.60 | 1.170 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_avoid_texture_sofa | sofa | red_marker | True | +0.00 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose without turning |
| go_avoid_texture_sofa | red_marker | sofa | True | +0.60 | 1.000 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_through_green_rectangle_tunnel | gate | reference_marker | True | +0.00 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose without turning |
| go_through_green_rectangle_tunnel | reference_marker | gate | True | +0.60 | 1.000 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_through_red_triangle_tunnel | gate | reference_marker | True | +0.00 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose without turning |
| go_through_red_triangle_tunnel | reference_marker | gate | True | +0.60 | 1.000 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_through_yellow_triangle_tunnel | gate | reference_marker | True | +0.00 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose without turning |
| go_through_yellow_triangle_tunnel | reference_marker | gate | True | +0.60 | 1.000 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_to_blue_ball | blue_sphere | wrong_color_object | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_to_blue_ball | wrong_color_object | blue_sphere | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_to_green_cube | green_box | wrong_color_object | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_to_green_cube | wrong_color_object | green_box | True | +0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| go_to_red_cube | red_box | wrong_color_object | True | +0.00 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose without turning |
| go_to_red_cube | wrong_color_object | red_box | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| red_marker | red_box | blue_distractor | True | -0.60 | 1.000 | 0.000 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |
| red_marker | blue_distractor | red_box | True | +0.60 | 1.000 | 0.240 | B has unobstructed rays inside the frustum at a valid A stop pose after one permitted turn |

Support geometries and arbitrary points on the floor were not promoted to task targets. Crawl tasks remain unsupported and were excluded. The rejected blue-ball/green-cube composition was not reused.

Full evidence: candidate_preflight.json and geometry_preflight_<scene_id>.json. Each positive witness includes pose, turn, camera position, image coordinates, first-hit geometry and ray distance.

Source hashes and git status verified unchanged.
