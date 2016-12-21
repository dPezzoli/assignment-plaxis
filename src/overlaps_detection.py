"""
This module provides utilities to detect overlapping shapes. Here, a function
to assess the intersection of two Car objects is also implemented
"""

from src import shapes_2d


def do_these_cars_collide(first_car, second_car):
    """
    :param first_car: the first car against which the collision state is
                      determined
    :param second_car: the second car against which the collision state is
                       determined
    :return: True if self collides with the given car; False otherwise
    """

    shapes_compound = shapes_2d.CompositeShape(first_car.shapes)
    other_shapes_compound = shapes_2d.CompositeShape(second_car.shapes)

    return OverlappingShapesDetector.do_these_two_shapes_overlap(
        shapes_compound,
        other_shapes_compound)


class OverlappingShapesDetector:
    """
    Class providing utilities to determine whether 2d-shapes overlap each other
    """

    @staticmethod
    def do_these_two_shapes_overlap(first_shape, second_shape):
        """
        :return: True if the two given shapes overlap
        """
        if (type(first_shape) == shapes_2d.CompositeShape or
                type(second_shape) == shapes_2d.CompositeShape):
            if type(first_shape) == shapes_2d.CompositeShape:
                first_composite = first_shape
                second_composite = shapes_2d.CompositeShape([second_shape])
            else:
                first_composite = second_shape
                second_composite = shapes_2d.CompositeShape([first_shape])
            return OverlappingShapesDetector.\
                __do_these_two_composite_shapes_overlap(
                    first_composite,
                    second_composite)

        elif type(first_shape) == shapes_2d.Rectangle:
            if type(second_shape) == shapes_2d.Rectangle:
                return (OverlappingShapesDetector.
                        __do_these_two_rectangles_overlap(first_shape,
                                                          second_shape))
            if type(second_shape) == shapes_2d.Circle:
                return (OverlappingShapesDetector.
                        __does_the_circle_overlap_the_rectangle(second_shape,
                                                                first_shape))
        elif type(first_shape) == shapes_2d.Circle:
            if type(second_shape) == shapes_2d.Circle:
                return (OverlappingShapesDetector.
                        __do_these_two_circles_overlap(first_shape,
                                                       second_shape))
            if type(second_shape) == shapes_2d.Rectangle:
                return (OverlappingShapesDetector.
                        __does_the_circle_overlap_the_rectangle(first_shape,
                                                                second_shape))

    @staticmethod
    def __do_these_two_composite_shapes_overlap(first_compound,
                                                second_compound):
        """
        :return: True if the two given composite shapes overlap
        """
        # 1) Check on bounding boxes: if they don't overlap, the two cars don't
        #    collide.

        bounding_box = first_compound.get_bounding_box()
        other_bounding_box = second_compound.get_bounding_box()

        # Make two rectangles to check intersection.
        box = shapes_2d.Rectangle.from_min_max_points(bounding_box[0],
                                                      bounding_box[1])
        other_box = shapes_2d.Rectangle.from_min_max_points(
            other_bounding_box[0],
            other_bounding_box[1])

        if OverlappingShapesDetector.do_these_two_shapes_overlap(box,
                                                                 other_box):
            # 2) Check all the underlying shapes.
            for i in range(len(first_compound.shapes)):
                for j in range(len(second_compound.shapes)):
                    if OverlappingShapesDetector.do_these_two_shapes_overlap(
                            first_compound.shapes[i],
                            second_compound.shapes[j]):
                        return True
        return False

    @staticmethod
    def __do_these_two_rectangles_overlap(first_rectangle, second_rectangle):
        """
        :return: True if the two given rectangles overlap
        """
        max_length_width = (first_rectangle.half_width +
                            second_rectangle.half_width)
        max_length_height = (first_rectangle.half_height +
                             second_rectangle.half_height)

        if (abs(first_rectangle.center[0] - second_rectangle.center[0]) <
                max_length_width and
                abs(first_rectangle.center[1] - second_rectangle.center[1]) <
                max_length_height):
            return True

        return False

    @staticmethod
    def __do_these_two_circles_overlap(first_circle, second_circle):
        """
        :return: True if the two given circles overlap
        """
        if (shapes_2d.sqr(first_circle.center[0] - second_circle.center[0]) +
                shapes_2d.sqr(first_circle.center[1] - second_circle.center[1])
                < shapes_2d.sqr(first_circle.radius + second_circle.radius)):
            return True

        return False

    @staticmethod
    def __does_the_circle_overlap_the_rectangle(circle, rectangle):
        """
        :return: True if the given circle overlaps the given rectangle
        """
        # Step 1: point-in-circle test for a set of points composed by the
        #         rectangle corners and the rectangle center
        corners = [(rectangle.center[0] - rectangle.half_width,
                    rectangle.center[1] - rectangle.half_height),
                   (rectangle.center[0] - rectangle.half_width,
                    rectangle.center[1] + rectangle.half_height),
                   (rectangle.center[0] + rectangle.half_width,
                    rectangle.center[1] - rectangle.half_height),
                   (rectangle.center[0] + rectangle.half_width,
                    rectangle.center[1] + rectangle.half_height),
                   (rectangle.center[0], rectangle.center[1])]
        for corner_x, corner_y in corners:
            if shapes_2d.sqr(corner_x - circle.center[0]) + \
                    shapes_2d.sqr(corner_y - circle.center[1]) < \
                    shapes_2d.sqr(circle.radius):
                return True

        # Step 2: point-in-rectangle test using a set of points evenly
        #         distributed along the circumference (we use 360 points)
        points = circle.evenly_distribute_points_along_circumference(360)
        for point_x, point_y in points:
            if (rectangle.center[0] - rectangle.half_width < point_x <
                rectangle.center[0] + rectangle.half_width and
                rectangle.center[1] - rectangle.half_height < point_y <
                    rectangle.center[1] + rectangle.half_height):
                return True

        return False
