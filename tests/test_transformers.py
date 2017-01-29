import unittest

from pycg3d.cg3d_point import CG3dPoint
from pycg3d.cg3d_plane import CG3dPlane3P
from pycg3d import cg3d_transformer


class TestTransformers(unittest.TestCase):
    def test_mirror_point_to_plane(self):
        p1 = CG3dPoint(1.0, 0.0, 0.0)
        plane = CG3dPlane3P(
                    CG3dPoint(0.0, 0.0, 0.0),
                    CG3dPoint(0.0, 1.0, 0.0),
                    CG3dPoint(0.0, 0.0, 1.0),
                )
        mirror = cg3d_transformer.CG3dMirrorTF(plane)
        p2 = p1.transform(mirror)

        self.assertEqual(p2, CG3dPoint(-1.0, 0.0, 0.0))