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


def make_cars(cars_specs):
    """
    Builds a set of cars as specified in the input parameter:
        * cars_specs[i] = (car_name, car_shapes_specs)
        * car_shapes_specs[i] = (shape_type, shape_specs)
            - shape_type: rectangle => shape_specs: ((center_x, center_y),
                                                      half_width, half_height)
            - shape_type: circle => shape_specs: ((center_x, center_y), radius)
    :param cars_specs: The specifications for building the cars
    :return: A list of cars
    """
    cars = []

    for car_specs in cars_specs:
        car_name = car_specs[0]
        car_shapes_specs = car_specs[1]
        car_shapes = []
        if car_shapes_specs[0] == "rectangle":
            print("make a rectangle")
            car_shapes.append(shapes_2d.Rectangle(car_shapes_specs[1][0],
                                                  car_shapes_specs[1][1],
                                                  car_shapes_specs[1][2]))
        elif car_shapes_specs[0] == "circle":
            print("make a circle")
            car_shapes.append(shapes_2d.Circle(car_shapes_specs[1][0],
                                               car_shapes_specs[1][1]))
        cars.append(car.Car(car_name, car_shapes))
    return cars
