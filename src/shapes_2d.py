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


class CompositeShape(Shape2D):
    """
    Class defining a 2d-compound
    """

    def __init__(self, shapes):
        """
        :param shapes: list of 2d-shapes that within this 2d-compound
        """
        # Check radius positiveness
        self._shapes = shapes

    @property
    def area(self):
        sum_shapes_area = 0
        for shape in self._shapes:
            sum_shapes_area += shape.area

        return sum_shapes_area

    def get_bounding_box(self):
        """
        :return: the min and max coordinates points of this shape, which define
        the axis aligned bounding box ((min_x, min_y), (max_x, max_y))
        """
        min_coordinates = [math.inf, math.inf]
        max_coordinates = [-math.inf, -math.inf]

        for shape in self._shapes:

            shape_bounding_box = shape.get_bounding_box()

            shape_min_coordinates = shape_bounding_box[0]
            if shape_min_coordinates[0] < min_coordinates[0]:
                min_coordinates[0] = shape_min_coordinates[0]
            if shape_min_coordinates[1] < min_coordinates[1]:
                min_coordinates[1] = shape_min_coordinates[1]

            shape_max_coordinates = shape_bounding_box[1]
            if shape_max_coordinates[0] > max_coordinates[0]:
                max_coordinates[0] = shape_max_coordinates[0]
            if shape_max_coordinates[1] > max_coordinates[1]:
                max_coordinates[1] = shape_max_coordinates[1]

        return min_coordinates, max_coordinates


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

    def get_bounding_box(self):
        """
        :return: the min and max coordinates points of this shape, which define
        the axis aligned bounding box ((min_x, min_y), (max_x, max_y))
        """
        return ((self._center[0] - self._half_width,
                 self._center[1] - self._half_height),
                (self._center[0] + self._half_width,
                 self._center[1] + self._half_height))
