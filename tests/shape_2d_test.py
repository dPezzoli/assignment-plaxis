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
        self.circle_b = shapes_2d.Circle((0, 0), 5.0)
        self.circle_c = shapes_2d.Circle((6, 0), 2.0)
        self.circle_d = shapes_2d.Circle((0, 8), 4.0)
        self.circle_e = shapes_2d.Circle((0, -5), 5.0)
        self.circle_f = shapes_2d.Circle((-9, 0), 4.0)
        self.circle_g = shapes_2d.Circle((10 * math.sin(math.pi/4),
                                          10 * math.sin(math.pi/4)), 4.99)
        self.circle_h = shapes_2d.Circle((10 * math.sin(math.pi/4),
                                          10 * math.sin(math.pi/4)), 5.01)
        self.circle_i = shapes_2d.Circle((15 * math.sin(math.pi/4),
                                          15 * math.sin(math.pi/4)), 9.99)
        self.circle_l = shapes_2d.Circle((15 * math.sin(math.pi/4),
                                          15 * math.sin(math.pi/4)), 10.01)
        self.rectangle_a = shapes_2d.Rectangle((0, 0), 3.5, 3.9)
        self.rectangle_b = shapes_2d.Rectangle((4, 0), 0.1, 7.0)
        self.rectangle_c = shapes_2d.Rectangle((16, 2), 2, 1)
        self.rectangle_d = shapes_2d.Rectangle((11, 2), 2, 1)
        self.rectangle_e = shapes_2d.Rectangle((0, 0), 3.5, 3.9)
        self.rectangle_f = shapes_2d.Rectangle((12, 2), 2, 1)
        self.rectangle_g = shapes_2d.Rectangle((12.001, 2), 2, 1)
        self.rectangle_h = shapes_2d.Rectangle((17.5, 3.5), 2, 1)

    #
    # Tests using circles -----------------------------------------------------

    def test_intersection_perfectly_overlapping_circles(self):
        """
        Test do_these_two_shapes_overlap method with two perfectly overlapping
        circles
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.circle_b))

    def test_intersection_overlapping_circles_one_unit_positive_x(self):
        """
        Test do_these_two_shapes_overlap method with two circles which overlap
        by one unit at the positive x-axis
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.circle_c))

    def test_intersection_overlapping_circles_one_unit_positive_y(self):
        """
        Test do_these_two_shapes_overlap method with two circles which overlap
        by one unit at the positive y-axis
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.circle_c))

    def test_intersection_offset_circle_by_radius_negative_y(self):
        """
        Test do_these_two_shapes_overlap method with two circles which overlap
        by the radius extension. The two triangles have same radius. One circle
        center is the axis origin and the other is obtained shifting the first
        along negative y-axis by a value equal to the radius (the center of one
        circle is located along the circumference of the other).
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_b,
                                                    self.circle_e))

    def test_intersection_not_overlapping_circles_one_unit_negative_x(self):
        """
        Test do_these_two_shapes_overlap method with two circles which touch at
        negative y-axis. If only one point along the circumference is shared by
        the triangles, there is no intersection.
        """
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_a,
                                                     self.circle_f))

    def test_intersection_not_overlapping_circles_first_quadrant(self):
        """
        Test do_these_two_shapes_overlap method with two circles which touch
        along the bisecting line of the first quadrant. If only one point along
        the circumference is shared by the triangles, there is no intersection.
        """
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_a,
                                                     self.circle_g))

    def test_intersection_overlapping_circles_first_quadrant(self):
        """
        Test do_these_two_shapes_overlap method with two circles which overlap
        along the bisecting line of the first quadrant.
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.circle_h))

    def test_intersection_not_overlapping_circles_third_quadrant(self):
        """
        Test do_these_two_shapes_overlap method with two circles which touch
        along the bisecting line of the third quadrant. If only one point along
        the circumference is shared by the triangles, there is no intersection.
        """
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.circle_a,
                                                     self.circle_g))

    def test_intersection_overlapping_circles_third_quadrant(self):
        """
        Test do_these_two_shapes_overlap method with two circles which overlap
        along the bisecting line of the third quadrant.
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.circle_a,
                                                    self.circle_h))

    #
    # Tests using rectangles --------------------------------------------------

    def test_intersection_perfectly_overlapping_rectangles(self):
        """
        Test do_these_two_shapes_overlap method with two rectangles which
        perfectly overlap each other.
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.rectangle_a,
                                                    self.rectangle_e))

    def test_intersection_not_overlapping_rectangles(self):
        """
        Test do_these_two_shapes_overlap method with two rectangles which
        overlap each other. In this case, one very thin rectangle is involved.
        """
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.rectangle_b,
                                                     self.rectangle_c))

    def test_intersection_not_overlapping_rectangles_thin(self):
        """
        Test do_these_two_shapes_overlap method with two rectangles which
        overlap each other. In this case, the rectangles are not intersecting.
        """
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.rectangle_a,
                                                     self.rectangle_b))

    def test_intersection_not_overlapping_rectangles_offset(self):
        """
        Test do_these_two_shapes_overlap method with two rectangles which
        overlap each other. In this case, one rectangle is obtained
        offsetting the first one.
        """
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.rectangle_b,
                                                     self.rectangle_d))

    def test_intersection_not_overlapping_rectangles_shared_edge(self):
        """
        Test do_these_two_shapes_overlap method with two rectangles which
        overlap each other. In this case, one rectangle is obtained
        offsetting the first one. The two rectangles share one edge (not
        overlapping)
        """
        self.assertFalse(shapes_2d.OverlappingShapesDetector.
                         do_these_two_shapes_overlap(self.rectangle_c,
                                                     self.rectangle_f))

    def test_intersection_slightly_overlapping_rectangles(self):
        """
        Test do_these_two_shapes_overlap method with two rectangles which
        overlap each other. The rectangles are obtained by offset.
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.rectangle_c,
                                                    self.rectangle_g))

    def test_intersection_overlapping_rectangles_corner(self):
        """
        Test do_these_two_shapes_overlap method with two rectangles which
        overlap each other. The rectangles overlap in one corner.
        """
        self.assertTrue(shapes_2d.OverlappingShapesDetector.
                        do_these_two_shapes_overlap(self.rectangle_c,
                                                    self.rectangle_h))


if __name__ == "__main__":
    unittest.main()
