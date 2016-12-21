"""
Computes for a list of cars, which of them intersect each other.
Note: the cars are currently approximated by rectangles or circles.
"""

from src import car
from src import shapes_2d, overlaps_detection


def get_intersections(cars):
    """
    :param cars: The list of cars to be tested
    :return: A list of intersecting cars pairs
    """
    result = []

    for i in range(len(cars)):
        for j in range(len(cars)):
            if i < j and overlaps_detection.do_these_cars_collide(cars[i],
                                                                  cars[j]):
                result.append((cars[i], cars[j]))
    return result


def print_colliding_cars(cars_pairs):
    """
    :param cars_pairs: The list of cars pairs to be printed
    """

    if len(cars_pairs) == 0:
        print("No car is colliding")
    else:
        for intersecting_pair in cars_pairs:
            print(str(intersecting_pair[0].name) +
                  ' overlaps ' +
                  str(intersecting_pair[1].name))


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

    if len(cars_specs) == 0:
        print("The given specifications do not contain data!")
    else:
        for car_specs in cars_specs:
            car_name = car_specs[0]
            car_shapes = []
            for i in range(1, len(car_specs)):
                shape = car_specs[i]
                if shape[0].lower() == "rectangle":
                    car_shapes.append(shapes_2d.Rectangle(shape[1][0],
                                                          shape[1][1],
                                                          shape[1][2]))
                elif shape[0].lower() == "circle":
                    car_shapes.append(shapes_2d.Circle(shape[1][0],
                                                       shape[1][1]))
                else:
                    print("Could not determine the type of shape")
            cars.append(car.Car(car_name, car_shapes))
    return cars


# ============================================================================
# EXAMPLE: Here three cars are constructed from the user specifications given
#          in the_cars_specs. Later, the collision state for these cars is
#          checked and the possible colliding cars names are printed.

# Get a bunch of cars
the_cars_specs = [
    ("Fiat",
     ("rectangle", ((2, 2), 1, 1)),
     ("rectangle", ((3, 1), 3, 1)),
     ("circle", ((0, 0), 1)),
     ("circle", ((5, 0), 1))),
    ("Maserati",
     ("rectangle", ((10, 2), 1, 1)),
     ("rectangle", ((11, 1), 3, 1)),
     ("circle", ((8, 0), 1)),
     ("circle", ((13, 0), 1))),
    ("Ferrari",
     ("rectangle", ((13, 2), 1, 1)),
     ("rectangle", ((14, 1), 3, 1)),
     ("circle", ((11, 0), 1)),
     ("circle", ((17, 0), 1))),
    ("Lamborghini",
     ("rectangle", ((19, 2), 1, 1)),
     ("rectangle", ((20, 1), 3, 1)),
     ("circle", ((17, 0), 1)),
     ("circle", ((23, 0), 1))),
                 ]

# Make the cars
the_cars = make_cars(the_cars_specs)

# Get colliding cars
intersecting_cars = get_intersections(the_cars)

# Print colliding cars
print_colliding_cars(intersecting_cars)
