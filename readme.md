# Plaxis assignment | Collision detection

This project consists of two main modules:
  - [shape_2d]
  - [car]

The _shape_2d_ module provides a class hierarchy describing 2D-shapes, while _car_ contains the class _Car_. The 2D-shapes serve to construct _Car_ objects that, later, may be tested for mutual collision.

In _assignment_app_ a function for constructing _Car_ objects out of given user specifications is provided. Besides, the module implements a routine to check the cars mutual overlapping and to print the possible colliding cars.

##### Cars specifications
To create _Car_ objects using the function _make_cars_ provided in the module _assignment_app_ a set of car specifications must be given. This consists of a list where the first entry specifies the car's name and the following ones the characteristics of the underlying 2D-shapes.

Specifically, this input parameter takes the form:
```
cars_specs[i] = (car_name, car_shapes_specs)
car_shapes_specs[i] = (shape_type, shape_specs)
```
where ```shape_type``` is either *Rectangle* or *Circle*

### Run the application
In order to run the application that checks for collisions, the user may modify the smoke-test in _assignment_app.py_ and/or directly run this file with:
```sh
$ python3  assignment_app.py
```

Otherwise, _Car_ objects might be interactively created and grouped in a list that, later, will be used to feed the routine _get_intersections_ provided within _assignment_app.py_ (see unit-tests in [car_test] for more details).



[shape_2d]: <https://gitlab.com/soulRebel/collidingCars/blob/master/src/shapes_2d.py>

[car]: <https://gitlab.com/soulRebel/collidingCars/blob/master/src/car.py>

[car_test]: <https://gitlab.com/soulRebel/collidingCars/blob/master/tests/car_test.py>

