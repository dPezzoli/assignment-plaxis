"""
Computes for a list of cars, which of them intersect each other.
Note: the cars are currently approximated by rectangles or circles.
"""

from src import car
from src import shapes_2d


def get_intersections(cars):
    """
    :param cars: The list of cars to be tested
    :return: A list of intersecting cars pairs
    """
    result = []

    for i in range(len(cars)):
        for j in range(len(cars)):
            if i < j and cars[i].collides(cars[j]):
                result.append((cars[i], cars[j]))
    return result
