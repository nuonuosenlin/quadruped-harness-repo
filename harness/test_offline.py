"""Offline checks: no network, simulator initialization, package install or secret access."""
import ast
import json
import os
from pathlib import Path
import unittest
import numpy as np
from geometry import relation_geometry, vec3, TOOLS
from text_client import TextClient
from protocol import Progress


class GeometryChecks(unittest.TestCase):
    def test_touch_adjust_bounded_progress(self):
        a, b = {'position':[0,0,0.7]}, {'position':[0.2,0,0.7]}
        touch = relation_geometry(a,b,'touch')
        adjust = relation_geometry(a,b,'adjust')
        self.assertAlmostEqual(touch['position'][0],0.08)
        self.assertAlmostEqual(adjust['position'][0],0.05)
        for relation in ('touch','adjust'):
            near = relation_geometry({'position':[0.19,0,0.7]},b,relation)
            self.assertTrue(np.allclose(near['position'],[0.19,0,0.7]))

    def test_collinear_projection_and_parallel(self):
        result = relation_geometry({'position':[1,2,3]}, {'position':[0,0,0],'axis':[0,0,2]}, 'collinear')
        self.assertTrue(np.allclose(result['position'],[0,0,3]))
        parallel = relation_geometry({'position':[1,2,3],'axis':[1,0,0]}, {'position':[0,0,0],'axis':[0,4,0]}, 'parallel')
        self.assertTrue(np.allclose(parallel['axis'],[0,1,0]))
        self.assertEqual(parallel['scope'],'geometry_only')
        with self.assertRaises(ValueError):
            relation_geometry({'position':[1,2,3]}, {'position':[0,0,0],'axis':[0,0,0]}, 'collinear')

    def test_invalid_coordinate(self):
        for point in ([1,2], [float('nan'),0,0], [float('inf'),0,0]):
            with self.assertRaises(ValueError):
                vec3(point)

    def test_transport_rejects_images_before_network(self):
        client = TextClient.__new__(TextClient)
        client.model, client.total, client.calls = 'qwen3.8-flash', 0, 0
        with self.assertRaises(ValueError):
            client.payload([{'role':'user','content':[{'type':'image_url','image_url':{'url':'test'}}]}],TOOLS)
        with self.assertRaises(ValueError):
            client.payload([{'role':'user','content':'text','images':['test']}],TOOLS)
        payload = client.payload([{'role':'system','content':'text only'}, {'role':'user','content':'point [0.1,0.2,0.3]'}],TOOLS)
        self.assertFalse(payload['enable_thinking'])
        self.assertEqual(payload['max_tokens'],384)

    def test_persistent_phase_and_legal_relation(self):
        p = Progress()
        p.validate('track_keypoint',{'bbox':[0,0,10,10],'name':'alphabet_soup_1'})
        p.record('track_keypoint',{}, {'position':[0,0,0]})
        p.validate('solve_constraint',{'keypoint_A':'eef','keypoint_B':'alphabet_soup_1','relation':'touch'})
        p.record('solve_constraint',{}, {'traj':'traj_001'})
        with self.assertRaises(ValueError):
            p.validate('execute_trajectory',{'traj':'invented'})
        p.validate('execute_trajectory',{'traj':'traj_001'})
        p.record('execute_trajectory',{}, {'traj':'traj_001'})
        self.assertEqual(p.phase,'plan')
        self.assertEqual(p.relation,'adjust')
        with self.assertRaises(ValueError):
            p.validate('solve_constraint',{'keypoint_A':'eef','keypoint_B':'alphabet_soup_1','relation':'touch'})
        solve=next(t for t in p.tools() if t['function']['name']=='solve_constraint')
        self.assertEqual(solve['function']['parameters']['properties']['relation']['enum'],['adjust'])
        # Building dynamic contracts must never mutate the shared base schemas.
        original=next(t for t in TOOLS if t['function']['name']=='solve_constraint')
        self.assertIn('touch',original['function']['parameters']['properties']['relation']['enum'])

    def test_repeat_and_no_progress_guards(self):
        p = Progress()
        self.assertIsNone(p.record('check_success',{}, {'success':False}))
        self.assertIn('REPEAT_REVIEW',p.record('check_success',{}, {'success':False}))
        p = Progress()
        p.record('solve_constraint',{}, {'error':'bad relation'})
        reason = p.record('solve_constraint',{}, {'error':'bad relation'})
        self.assertIn('same invalid call',reason)
        self.assertEqual(p.last_error['error'],'bad relation')

    def test_reduced_budget_before_network(self):
        client = TextClient.__new__(TextClient)
        client.model, client.total, client.calls = 'qwen3.8-flash', 14999, 0
        with self.assertRaisesRegex(RuntimeError,'TOKEN_REVIEW'):
            client.payload([{'role':'user','content':'test'}],[])
        client.total, client.calls = 0, 12
        with self.assertRaisesRegex(RuntimeError,'STEP_REVIEW'):
            client.payload([{'role':'user','content':'test'}],[])
        self.assertEqual(client.MAX_TOTAL_TOKENS,15000)

    def test_compile_sources_without_bytecode(self):
        for path in Path(__file__).parent.glob('*.py'):
            ast.parse(path.read_text(encoding='utf-8-sig'),filename=str(path))


if __name__ == '__main__':
    unittest.main()
