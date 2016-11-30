"""
Unit tests for car module
"""

import unittest
from src import car, shapes_2d


class TestCar(unittest.TestCase):
    """
    Tests for the class Circle
    """

    def setUp(self):
        """
        Define a fixture for the tests
        """
        self.shapes_first_car = []
        self.shapes_first_car.append(shapes_2d.Rectangle((3, 2), 1, 1))
        self.shapes_first_car.append(shapes_2d.Rectangle((4, 1), 3, 1))
        self.shapes_first_car.append(shapes_2d.Circle((1, 0), 1))
        self.shapes_first_car.append(shapes_2d.Circle((6, 0), 1))
        self.first_car = car.Car("Ferrari", self.shapes_first_car)

        self.shapes_second_car = []
        self.shapes_second_car.append(shapes_2d.Rectangle((11, 3), 2, 2))
        self.shapes_second_car.append(shapes_2d.Rectangle((12, 1), 2, 1))
        self.shapes_second_car.append(shapes_2d.Rectangle((14, 2), 1, 1))
        self.shapes_second_car.append(shapes_2d.Circle((10, 1), 2))
        self.shapes_second_car.append(shapes_2d.Circle((15, 0), 1))
        self.second_car = car.Car("Fiat", self.shapes_second_car)

        self.shapes_third_car = []
        self.shapes_third_car.append(shapes_2d.Rectangle((5, 6), 2, 1))
        self.shapes_third_car.append(shapes_2d.Circle((3, 5), 1))
        self.shapes_third_car.append(shapes_2d.Circle((7, 5), 1))
        self.third_car = car.Car("Lamborghini", self.shapes_third_car)

        self.shapes_fourth_car = []
        self.shapes_fourth_car.append(shapes_2d.Rectangle((8, 4), 2, 1))
        self.shapes_fourth_car.append(shapes_2d.Circle((6, 3), 1))
        self.shapes_fourth_car.append(shapes_2d.Circle((10, 3), 1))
        self.fourth_car = car.Car("Maserati", self.shapes_fourth_car)

    def test_compute_bounding_box(self):
        """
        Tests min max coordinates of axis aligned bounding boxes
        """
        box_first_car = self.first_car.compute_bounding_box()
        self.assertEqual(box_first_car[0], [0, -1])
        self.assertEqual(box_first_car[1], [7, 3])

        box_second_car = self.second_car.compute_bounding_box()
        self.assertEqual(box_second_car[0], [8, -1])
        self.assertEqual(box_second_car[1], [16, 5])

        box_third_car = self.third_car.compute_bounding_box()
        self.assertEqual(box_third_car[0], [2, 4])
        self.assertEqual(box_third_car[1], [8, 7])

        box_fourth_car = self.fourth_car.compute_bounding_box()
        self.assertEqual(box_fourth_car[0], [5, 2])
        self.assertEqual(box_fourth_car[1], [11, 5])

    def test_collides(self):
        """
        Tests cars collisions
        """
        self.assertFalse(self.first_car.collides(self.second_car))
        self.assertFalse(self.second_car.collides(self.third_car))
        self.assertFalse(self.third_car.collides(self.first_car))
        self.assertFalse(self.first_car.collides(self.fourth_car))
        self.assertTrue(self.second_car.collides(self.fourth_car))
        self.assertTrue(self.third_car.collides(self.fourth_car))
        self.assertTrue(self.fourth_car.collides(self.second_car))

if __name__ == "__main__":
    unittest.main()
