"""
This module provides an implementation of a car class.
"""

import math
from src import shapes_2d


class Car:
    """
    Class defining a car. Each car is composed by a bunch of 2D shapes. This
    class provides a method to detect if 'self' collides with another car.
    """

    def __init__(self, name, shapes):
        self._name = name
        self._shapes = shapes

    @property
    def shapes(self):
        return self._shapes

    @property
    def name(self):
        return self._name

    def compute_bounding_box(self):
        """
        :return: The min and max coordinates points of this car axis aligned
                 bounding box
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

    def collides(self, car):
        """
        :param car: a second car against which the collision state is
                    determined
        :return: True if self collides with the given car; False otherwise
        """
        # 1) Check on bounding boxes: if they don't overlap, the two cars don't
        #    collide.

        bounding_box = self.compute_bounding_box()
        other_bounding_box = car.compute_bounding_box()

        # Make two rectangles to check intersection.
        box = shapes_2d.Rectangle.from_min_max_points(bounding_box[0],
                                                      bounding_box[1])
        other_box = shapes_2d.Rectangle.from_min_max_points(
                                                        other_bounding_box[0],
                                                        other_bounding_box[1])

        if shapes_2d.OverlappingShapesDetector.do_these_two_shapes_overlap(
                box, other_box):
            # 2) Check all the underlying shapes.
            for i in range(len(self._shapes)):
                for j in range(len(car.shapes)):
                    if shapes_2d.OverlappingShapesDetector. \
                            do_these_two_shapes_overlap(self._shapes[i],
                                                        car.shapes[j]):
                        return True
        return False
