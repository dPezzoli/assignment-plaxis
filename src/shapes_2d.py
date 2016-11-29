"""
This module provides a hierarchy of 2D-shapes. These, in particular,
differentiate in polygons and non-polygons. Non-polygons are conic sections
and are defined with a center point. A polygon, on the other hand, may consist
of a closed polyline which has no center point (the centroid would not provide
a handful parametrization term for such polygons). However, regular polygons
may be advantageously defined using their center point. Shapes have the ability
to detect intersection with other shapes.
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

