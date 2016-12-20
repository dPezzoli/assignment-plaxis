"""
This module provides a hierarchy of 2D-shapes. These, in particular,
differentiate in polygons and non-polygons. Non-polygons are conic sections
and are defined with a center point. A polygon, on the other hand, may consist
of a closed polyline which has no center point (the centroid would not provide
a handful parametrization term for such polygons). However, regular polygons
may be advantageously defined using their center point. 
Besides, this module provide a class able to detect whether two of the modelled
shapes do overlap each other.
"""

import math
from abc import ABCMeta, abstractmethod, abstractproperty


def sqr(x):
    return x * x


class Shape2D:
    """
    Abstract class defining a generic two-dimensional shape
    """

    __metaclass__ = ABCMeta

    @abstractproperty
    def area(self):
        pass

    @abstractmethod
    def get_bounding_box(self):
        """
        :return: the min and max coordinates points of this shape, which define
        the axis aligned bounding box ((min_x, min_y), (max_x, max_y))
        """


class NonPolygon(Shape2D):
    """
    Class defining a non-polygonal 2d shape
    """

    __metaclass__ = ABCMeta

    @abstractproperty
    def center(self):
        pass


class Polygon(Shape2D):
    """
    Class defining a polygonal 2d shape. These kind of shapes are defined by a
    centre point.
    """

    __metaclass__ = ABCMeta


class Circle(NonPolygon):
    """
    Class defining a circle
    """

    def __init__(self, center, radius):
        """
        :param center: the center of the circle
        :param radius: the radius of the circle
        """
        # Check radius positiveness
        if radius <= 0:
            raise ValueError("Please provide a positive radius value")
        # Initialize attributes
        self._center = center
        self._radius = radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    @abstractmethod
    def get_bounding_box(self):
        """
        :return: the min and max coordinates points of this shape, which define
        the axis aligned bounding box ((min_x, min_y), (max_x, max_y))
        """
        return \
            ((self._center[0] - self._radius, self._center[1] - self._radius),
             (self._center[0] + self._radius, self._center[1] + self._radius))

    def evenly_distribute_points_along_circumference(self, number_of_points):
        """
        :param number_of_points: The number of points to be distributed along
               the circumference. Possible values are the multiples of four;
               this ensures the circle extremes are included
        :return: A list of points along the circumference
        """
        points = []

        if number_of_points % 4 != 0:
            raise ValueError("The number of points must be a multiple of four")

        angular_step_size = 2 * math.pi / number_of_points

        for i in range(number_of_points):
            points.append((self.center[0] +
                           self._radius * math.sin(angular_step_size * i),
                           (self.center[1] +
                            self._radius * math.cos(angular_step_size * i))
                           ))

        return points


class Rectangle(Polygon):
    """
    Class defining a Rectangle
    """

    def __init__(self, center, half_width, half_height):
        # Check rectangle dimensions positiveness
        if half_height <= 0:
            raise ValueError("Please provide a positive half_height value")
        elif half_width <= 0:
            raise ValueError("Please provide a positive half_width value")
        # Initialize attributes
        self._half_width = half_width
        self._half_height = half_height
        self._center = center

    @classmethod
    def from_min_max_points(cls, min_point, max_point):
        """
        Initialize from min and max points
        """
        half_width = (max_point[0] - min_point[0]) / 2
        half_height = (max_point[1] - min_point[1]) / 2
        center = (min_point[0] + half_width, min_point[1] + half_height)
        return cls(center, half_width, half_height)

    @property
    def area(self):
        return self._half_height * self._half_width * 4

    @property
    def half_width(self):
        return self._half_width

    @property
    def half_height(self):
        return self._half_height

    @property
    def center(self):
        return self._center

    @abstractmethod
    def get_bounding_box(self):
        """
        :return: the min and max coordinates points of this shape, which define
        the axis aligned bounding box ((min_x, min_y), (max_x, max_y))
        """
        return ((self._center[0] - self._half_width,
                 self._center[1] - self._half_height),
                (self._center[0] + self._half_width,
                 self._center[1] + self._half_height))


class OverlappingShapesDetector:
    """
    Class providing utilities to determine whether 2d-shapes overlap each other
    """

    @staticmethod
    def do_these_two_shapes_overlap(first_shape, second_shape):
        """
        :return: True if the two given shapes overlap
        """
        if type(first_shape) == Rectangle:
            if type(second_shape) == Rectangle:
                return (OverlappingShapesDetector.
                        __do_these_two_rectangles_overlap(first_shape,
                                                          second_shape))
            if type(second_shape) == Circle:
                return (OverlappingShapesDetector.
                        __does_the_circle_overlap_the_rectangle(second_shape,
                                                                first_shape))
        elif type(first_shape) == Circle:
            if type(second_shape) == Circle:
                return (OverlappingShapesDetector.
                        __do_these_two_circles_overlap(first_shape,
                                                       second_shape))
            if type(second_shape) == Rectangle:
                return (OverlappingShapesDetector.
                        __does_the_circle_overlap_the_rectangle(first_shape,
                                                                second_shape))

    @staticmethod
    def __do_these_two_rectangles_overlap(first_rectangle, second_rectangle):
        """
        :return: True if the two given rectangles overlap
        """
        max_length_width = (first_rectangle.half_width +
                            second_rectangle.half_width)
        max_length_height = (first_rectangle.half_height +
                             second_rectangle.half_height)

        if (abs(first_rectangle.center[0] - second_rectangle.center[0]) <
                max_length_width and
                abs(first_rectangle.center[1] - second_rectangle.center[1]) <
                max_length_height):
            return True

        return False

    @staticmethod
    def __do_these_two_circles_overlap(first_circle, second_circle):
        """
        :return: True if the two given circles overlap
        """
        if (sqr(first_circle.center[0] - second_circle.center[0]) +
                sqr(first_circle.center[1] - second_circle.center[1]) <
                sqr(first_circle.radius + second_circle.radius)):
            return True

        return False

    @staticmethod
    def __does_the_circle_overlap_the_rectangle(circle, rectangle):
        """
        :return: True if the given circle overlaps the given rectangle
        """
        # Step 1: point-in-circle test for a set of points composed by the
        #         rectangle corners and the rectangle center
        corners = [(rectangle.center[0] - rectangle.half_width,
                    rectangle.center[1] - rectangle.half_height),
                   (rectangle.center[0] - rectangle.half_width,
                    rectangle.center[1] + rectangle.half_height),
                   (rectangle.center[0] + rectangle.half_width,
                    rectangle.center[1] - rectangle.half_height),
                   (rectangle.center[0] + rectangle.half_width,
                    rectangle.center[1] + rectangle.half_height),
                   (rectangle.center[0], rectangle.center[1])]
        for corner_x, corner_y in corners:
            if sqr(corner_x - circle.center[0]) + \
                    sqr(corner_y - circle.center[1]) < sqr(circle.radius):
                return True

        # Step 2: point-in-rectangle test using a set of points evenly
        #         distributed along the circumference (we use 360 points)
        points = circle.evenly_distribute_points_along_circumference(360)
        for point_x, point_y in points:
            if (rectangle.center[0] - rectangle.half_width < point_x <
                rectangle.center[0] + rectangle.half_width and
                rectangle.center[1] - rectangle.half_height < point_y <
                    rectangle.center[1] + rectangle.half_height):
                return True

        return False

