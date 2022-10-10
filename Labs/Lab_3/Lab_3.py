# TODO
from __future__ import annotations
from turtle import circle
import matplotlib.pyplot as plt
import numpy as np
import math
import os

os.system("cls||clear")


# TODO
# Shape class
class Shape:
    """The Super class named Shape"""

    def __init__(self, x_pos: int | float = 1, y_pos: int | float = 1) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    # x Position getter
    @property
    def x_pos(self) -> int | float:
        """Getter for x_pos"""
        return self._x_pos

    # x Position setter

    @x_pos.setter
    def x_pos(self, value: int | float) -> int | float:
        if not isinstance(
            value, (int, float)
        ):  # checks if the type in x_pos is int or float
            raise TypeError(
                f"x Position must be an int or float, not {type(value).__name__}"
            )
        # if not 0 <= value <= 1000: TODO, SETTING THIS FOR LATER IF NEEDED.
        self._x_pos = value

    # y Position getter
    @property
    def y_pos(self) -> int | float:
        """Getter for y_pos"""
        return self._y_pos

    # y Position setter

    @y_pos.setter
    def y_pos(self, value: int | float) -> int | float:
        if not isinstance(
            value, (int, float)
        ):  # checks if the type in y_pos is int or float
            raise TypeError(
                f"y Position must be an int or float, not {type(value).__name__}"
            )
        # if not 0 <= value <= 1000: TODO, SETTING THIS FOR LATER IF NEEDED.
        self._y_pos = value

    # -------------------- Overloading Operators, Shape Class  -------------------- #

    # __eq__(self, other) ==
    def __eq__(self, other: Shape) -> bool:
        """Checks Equality (==) between Shapes"""
        return self.area == other.area

    # + __lt__(self, other) <
    def __lt__(self, other) -> bool:
        """Checks less than (<) between Shapes"""
        return self.area == other.area

    # + __gt__(self, other) >
    def __gt__(self, other) -> bool:
        """Checks greater than (>) between Shapes"""
        return self.area == other.area

    # + __le__(self, other) <=
    def __le__(self, other) -> bool:
        """Checks less or equal (<=) between Shapes"""
        return self.area == other.area

    # + __ge__(self, other) >=
    def __ge__(self, other) -> bool:
        """Checks greator or equal (>=) between Shapes"""
        return self.area == other.area

    # + translation(x, y) -> Shape
    def translation(
        self,
        x_value: float | int,
        y_value: float | int,
    ):  # This should add the x and or y to self.x or self.y
        self.x_pos += x_value
        self.y_pos += y_value

    # + __repr__()
    def __repr__(self) -> str:
        """When print function is called, returns the x position and y position of the shape"""
        return f"The shape's position is x = {self.x_pos}, y = {self.y_pos}"

    # + __str__()
    def __str__(self) -> str:
        """STR function for Superclass shape"""
        return f"The shape's position is x = {self.x_pos}, y = {self.y_pos}"


# - in_object(self, point) -> bool:

# x_pos: int = 0
# y_pos: int = 0

# area = None
# omkrets = None


# Circle class


class Circle(Shape):
    """Circle class, subclass from superclass Shape"""

    def __init__(
        self,
        x_pos: (int | float) = 1,
        y_pos: (int | float) = 1,
        c_radius: (int | float) = 1,
    ) -> None:
        super().__init__(x_pos, y_pos)
        self.c_radius = c_radius

    # -------------------- Getter and Setter for Circle Class + # TODO Error Handling -------------------- #

    @property
    def c_radius(self) -> float:
        """Getter for the radius of the Circle object"""
        return self._c_radius  # Getter

    @c_radius.setter
    def c_radius(self, value: (float | int)):  # Setter
        if isinstance(value, float or int):  # TODO. CHANGE TO FLOAT AND INT
            raise TypeError(f"Radius must be float or int, not {type(value).__name__}")
        else:
            self._c_radius = value

    @property
    def area(self) -> (int | float):
        """Calculates the area of the Cricle object"""  # Check the area of Circle
        return math.pi * self._c_radius**2

    @property
    def circumference(self) -> (int | float):  # Check the Circumfurence of Cirlce
        """The Circumference of the Circle object"""
        return 2 * math.pi * self.c_radius

    @property
    def is_unit_circle(self) -> bool:
        """Method for checking if the Circle object is a unit-circle"""
        if self.c_radius == 1 and self.x_pos == 0 and self.y_pos == 0:
            return True
        else:
            return False

    ### PLACEHOLDER CODE!!!!!!!
    def __repr__(self) -> str:
        """ "Describes self as a string"""
        return f"Circle(x = {self.x_pos}, y = {self.y_pos}, radius = {self.c_radius})"

    def __str__(self) -> str:
        """Describes self as a string for printing"""
        return f"Circle in position x: {self.x_pos}, y: {self.y_pos}, with radius: {self.c_radius}, area: {self.area}, circumference: {self.circumference}"


# Rectangle class ---------------------------------------######
class Rectangle(Shape):
    """Rectangle Subclass, Super Class is Shape"""

    def __init__(
        self,
        x_pos: int | float = 1,
        y_pos: int | float = 1,
        r_height: int | float = 1,
        r_width: int | float = 1,
    ) -> None:
        super().__init__(x_pos, y_pos)
        self.r_height = r_height
        self.r_width = r_width

    # -------------------- Getter for Rectangle Class -------------------- #

    @property
    def r_height(self) -> (float | int):
        return self._r_height  # Getter for height

    @property
    def r_width(self) -> (float | int):
        return self._r_width  # Getter for width

    # -------------------- Getter for Rectangle Class + # TODO Error Handling -------------------- #

    @r_height.setter
    def r_height(self, value: float | int):
        self._r_height = value

    @r_width.setter
    def r_width(self, value: float | int):
        self._r_width = value


# def is_square(self) -> bool:
# h*w/2 = x**2

# def calc_area(self) > float:
# h**2 + w**2

# CALC CIRCUM?????
