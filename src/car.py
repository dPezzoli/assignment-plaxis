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
