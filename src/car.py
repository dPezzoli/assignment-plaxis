"""
This module provides an implementation of a car class.
"""

import math
import shapes_2d


class Car:
    """
    Class defining a car. Each car is composed by a bunch of 2D shapes. This
    class provides a method to detect if 'self' collides with another car.
    """

    def __init__(self, name, shapes):
        self.name = name
        self._shapes = shapes

    def compute_bounding_box(self):
        """
        :return: The min and max coordinates points of this car axis aligned
                 bounding box
        """
        min_coordinates = [math.inf, math.inf]
        max_coordinates = [-math.inf, -math.inf]

        for shape in self._shapes:

            shape_min_coordinates = shape.get_min_coordinates()
            if shape_min_coordinates[0] < min_coordinates[0]:
                min_coordinates[0] = shape_min_coordinates[0]
            if shape_min_coordinates[1] < min_coordinates[1]:
                min_coordinates[1] = shape_min_coordinates[1]

            shape_max_coordinates = shape.get_max_coordinates()
            if shape_max_coordinates[0] > max_coordinates[0]:
                max_coordinates[0] = shape_max_coordinates[0]
            if shape_max_coordinates[1] > max_coordinates[1]:
                max_coordinates[1] = shape_max_coordinates[1]

        return [min_coordinates, max_coordinates]

    def collides(self, car):
        """
        :param car: a second car against which the collision state is
                    determined
        :return: True if self collides with the given car; False otherwise
        """
