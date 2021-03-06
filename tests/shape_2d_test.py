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

    def get_bounding_box(self):
        bounding_box_b = self.circle_b.get_bounding_box
        self.assertEqual(bounding_box_b, ((1.2, -1.8), (4.8, 1.8)))

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
        rectangle_bounding_box = rectangle.get_bounding_box()
        self.assertEqual(rectangle_bounding_box[0], (-1, -1))
        self.assertEqual(rectangle_bounding_box[1], (3, 5))

    def test_area(self):
        area_a = self.rectangle_a.area
        self.assertEqual(area_a, 15.168)

        area_b = self.rectangle_b.area
        self.assertEqual(area_b, 16)

    def test_center(self):
        center_b = self.rectangle_b.center
        self.assertEqual(center_b, (3, 0))

    def get_bounding_box(self):
        bounding_box_a = self.rectangle_a.get_bounding_box()
        self.assertEqual(bounding_box_a, ((-3.16, -1.2), (3.16, 1.2)))


if __name__ == "__main__":
    unittest.main()
