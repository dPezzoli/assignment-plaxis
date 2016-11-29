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


class Shape2D:
    """
    Abstract class defining a generic two-dimensional shape
    """

    __metaclass__ = ABCMeta

    @abstractproperty
    def area(self):
        pass

    @abstractmethod
    def get_min_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the shape bounding box minimum
                 point (min 'x' and min 'y')
        """

    @abstractmethod
    def get_max_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the shape bounding box maximum
                 point (min 'x' and min 'y')
        """


class NonPolygon(Shape2D):
    """
    Class defining a non-polygonal 2d shape
    """

    __metaclass__ = ABCMeta

    @abstractproperty
    def area(self):
        pass

    @abstractproperty
    def center(self):
        pass

    @abstractmethod
    def get_min_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the non-polygon shape bounding box
                 minimum point (min 'x' and min 'y')
        """

    @abstractmethod
    def get_max_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the non-polygon shape bounding box
                 maximum point (min 'x' and min 'y')
        """


class Polygon(Shape2D):
    """
    Class defining a polygonal 2d shape. These kind of shapes are defined by a
    centre point.
    """

    __metaclass__ = ABCMeta

    @abstractproperty
    def area(self):
        pass

    @abstractmethod
    def get_min_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the polygon bounding box minimum
                 point (min 'x' and min 'y')
        """

    @abstractmethod
    def get_max_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the polygon bounding box maximum
                 point (min 'x' and min 'y')
        """


class Circle(NonPolygon):
    """
    Class defining a circle
    """

    def __init__(self, center, radius):
        """
        :param center: the center of the circle
        :param radius: the radius of the circle
        """
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

    def get_min_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the circle bounding box minimum
                 point (min 'x' and min 'y')
        """
        return [self._center[0] - self._radius, self._center[1] - self._radius]

    def get_max_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the circle bounding box maximum
                 point (min 'x' and min 'y')
        """
        return [self._center[0] + self._radius, self._center[1] + self._radius]


class Rectangle(Polygon):
    """
    Class defining a Rectangle
    """

    def __init__(self, center, half_width, half_height):
        self.center = center
        self.half_width = half_width
        self.half_height = half_height

    @property
    def area(self):
        return self.half_height * self.half_width * 4

    def get_min_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the rectangle bounding box minimum
                 point (min 'x' and min 'y')
        """
        return (self.center[0] - self.half_width,
                self.center[1] - self.half_height)

    def get_max_coordinates(self):
        """
        :return: 2D-Cartesian coordinates of the rectangle bounding box maximum
                 point (min 'x' and min 'y')
        """
        return (self.center[0] + self.half_width,
                self.center[1] + self.half_height)


