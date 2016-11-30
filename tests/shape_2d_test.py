"""
Unit tests for the shapes_2d module
"""

import math
import unittest
from src import shapes_2d


class TestCircle(unittest.TestCase):
    """
    Tests for the class Circle
    """

    def setUp(self):
        """
        Define a fixture for the tests
        """
        self.circle_a = shapes_2d.Circle((0, 0), 1.0)
        self.circle_b = shapes_2d.Circle((3, 0), 1.8)
        self.circle_c = shapes_2d.Circle((0, 4), 3.0)
        self.circle_d = shapes_2d.Circle((0, -2), 1.1)

    def test_area(self):
        area_a = self.circle_a.area
        self.assertEqual(area_a, math.pi)

        area_c = self.circle_c.area
        self.assertEqual(area_c, math.pi * 9)

    def test_center(self):
        center_d = self.circle_d.center
        self.assertEqual(center_d, (0, -2))

    def test_get_min_coordinates(self):
        min_b = self.circle_b.get_min_coordinates()
        self.assertEqual(min_b, (1.2, -1.8))

    def test_get_max_coordinates(self):
        max_b = self.circle_b.get_max_coordinates()
        self.assertEqual(max_b, (4.8, 1.8))

    def test_evenly_distribute_points_along_circumference(self):
        points = self.circle_c.evenly_distribute_points_along_circumference(12)
        self.assertEqual(points[0], (0, 7))
        self.assertEqual(points[3], (3, 4))
        self.assertAlmostEquals(points[6][0], 0)
        self.assertEqual(points[6][1], 1)
        self.assertEqual(points[9][0], -3)
        self.assertAlmostEquals(points[9][1], 4)


class TestRectangle(unittest.TestCase):
    """
    Tests for the class Rectangle
    """

    def setUp(self):
        """
        Define a fixture for the tests
        """
        self.rectangle_a = shapes_2d.Rectangle((0, 0), 3.16, 1.2)
        self.rectangle_b = shapes_2d.Rectangle((3, 0), 1.0, 4.0)

    def test_from_min_max_points(self):
        rectangle = shapes_2d.Rectangle.from_min_max_points((-1, -1), (3, 5))
        self.assertEqual(rectangle.get_min_coordinates(), (-1, -1))
        self.assertEqual(rectangle.get_max_coordinates(), (3, 5))

    def test_area(self):
        area_a = self.rectangle_a.area
        self.assertEqual(area_a, 15.168)

        area_b = self.rectangle_b.area
        self.assertEqual(area_b, 16)

    def test_center(self):
        center_b = self.rectangle_b.center
        self.assertEqual(center_b, (3, 0))

    def test_get_min_coordinates(self):
        min_b = self.rectangle_a.get_min_coordinates()
        self.assertEqual(min_b, (-3.16, -1.2))

    def test_get_max_coordinates(self):
        max_b = self.rectangle_a.get_max_coordinates()
        self.assertEqual(max_b, (3.16, 1.2))


class TestOverlappingShapesDetector(unittest.TestCase):
    """
    Tests for the class OverlappingShapesDetector
    """

    def setUp(self):
        """
        Define a fixture for the tests
        """
        # Get some shapes to check for collision
        self.circle_a = shapes_2d.Circle((0, 0), 5.0)
        self.circle_b = shapes_2d.Circle((6, 0), 1.0)
        self.circle_c = shapes_2d.Circle((6, 0), 1.01)
        self.circle_d = shapes_2d.Circle((0, 4), 3.0)
        self.circle_e = shapes_2d.Circle((-9, 4), 0.1)
        self.rectangle_a = shapes_2d.Rectangle((0, 0), 3.5, 3.9)
        self.rectangle_b = shapes_2d.Rectangle((4, 0), 0.1, 7.0)
        self.rectangle_c = shapes_2d.Rectangle((3, 9), 8.4, 0.2)
        self.rectangle_d = shapes_2d.Rectangle((4, 1), 6.0, 0.1)
        self.rectangle_e = shapes_2d.Rectangle((16, 2), 2, 1)

    def test_do_these_two_shapes_overlap(self):
        """
        Test the possible collision cases
        """
        # Test intersection circles
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_a,
                                                     self.circle_b))
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_a,
                                                     self.circle_e))
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_b,
                                                     self.circle_e))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.circle_c))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_d,
                                                    self.circle_a))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_b,
                                                    self.circle_c))

        # Test intersection rectangles
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.rectangle_a,
                                                     self.rectangle_b))
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.rectangle_c,
                                                     self.rectangle_b))
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.rectangle_e,
                                                     self.rectangle_c))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.rectangle_a,
                                                    self.rectangle_d))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.rectangle_b,
                                                    self.rectangle_d))

        # Test intersection circle-rectangle
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_e,
                                                     self.rectangle_c))
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_a,
                                                     self.rectangle_e))
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_c,
                                                     self.rectangle_a))
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_c,
                                                     self.rectangle_b))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.rectangle_b))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.rectangle_a))
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_d,
                                                    self.rectangle_d))

if __name__ == "__main__":
    unittest.main()


