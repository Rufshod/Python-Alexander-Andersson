from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import math
import os

os.system("cls||clear")


# Shape class
class Shape:
    """The Super class named Shape"""

    def __init__(self, x_pos: int | float = 1, y_pos: int | float = 1) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    # x Position getter
    @property
    def x_pos(self) -> int | float:
        """X position for the Shape"""
        return self._x_pos

    # y Position getter
    @property
    def y_pos(self) -> int | float:
        """Y position for the Shape"""
        return self._y_pos

    # x Position setter

    @x_pos.setter
    def x_pos(self, value: int | float) -> int | float:
        if not isinstance(
            value, (int, float)
        ):  # checks if the type in x_pos is int or float
            raise TypeError(
                f"x Position must be an int or float, not {type(value).__name__}"
            )

        self._x_pos = value  # Sets the x value

    # y Position setter

    @y_pos.setter
    def y_pos(self, value: int | float) -> int | float:
        if not isinstance(
            value, (int, float)
        ):  # checks if the type in y_pos is int or float
            raise TypeError(
                f"y Position must be an int or float, not {type(value).__name__}"
            )

        self._y_pos = value  # Sets the y value

    # -------------------- Overloading Operators, Shape Class  -------------------- #

    # __eq__(self, other) ==
    def __eq__(self, other) -> bool:
        """Checks Equality (==) between Shapes"""
        return self.area == other.area

    # + __lt__(self, other) <
    def __lt__(self, other) -> bool:
        """Checks less than (<) between Shapes"""
        if self.area < other.area:
            return True
        else:
            return False

    # + __gt__(self, other) >
    def __gt__(self, other) -> bool:
        """Checks greater than (>) between Shapes"""
        if self.area > other.area:
            return True
        else:
            return False

    # + __le__(self, other) <=
    def __le__(self, other) -> bool:
        """Checks less or equal (<=) between Shapes"""
        if self.area <= other.area:
            return True
        else:
            return False

    # + __ge__(self, other) >=
    def __ge__(self, other) -> bool:
        """Checks greator or equal (>=) between Shapes"""
        if self.area >= other.area:
            return True
        else:
            return False

    # + translation(x, y) -> Shape
    def translation(
        self,
        x_value: float | int,
        y_value: float | int,
    ):  # This will add the values to self.x or self.y
        """Translation method is used in order to change the values of the x, y position for"""
        if not isinstance(x_value, (int, float)):
            raise TypeError(
                f"x_value must be float or int. Not {type(x_value).__name__}"
            )
        self.x_pos += x_value
        if not isinstance(y_value, (int, float)):
            raise TypeError(
                f"y_value must be float or int. Not {type(y_value).__name__}"
            )
        self.y_pos += y_value

    # + __repr__()
    def __repr__(self) -> str:
        """Representation of the shapes positional values"""
        return f"Shape's position x = {self.x_pos}, y = {self.y_pos}"

    # + __str__()
    def __str__(self) -> str:
        """When print function is called, returns the x position and y position of the shape"""
        return f"The shape's position is x = {self.x_pos}, y = {self.y_pos}"

    # --------------------------------------- Circle Class --------------------------------------- #


class Circle(Shape):
    """Circle class, subclass from superclass Shape"""

    def __init__(
        self,
        x_pos: (
            int | float
        ) = 1,  # Set the default value to 1 for the __init__ functions
        y_pos: (int | float) = 1,
        c_radius: (int | float) = 1,
    ) -> None:
        super().__init__(x_pos, y_pos)
        self.c_radius = c_radius

    # -------------------- Getter and Setter for Circle Class -------------------- #

    @property
    def c_radius(self) -> float:
        """Radius of the Circle object"""
        return self._c_radius  # Getter

    @c_radius.setter
    def c_radius(self, value: (int | float)):  # Setter
        if not isinstance(
            value, (float, int)
        ):  # Checks to see if the value is float or int
            raise TypeError(
                f"Radius must be float or int, not {type(value).__name__}"
            )  # Error handling
        if value <= 0:
            raise ValueError(f"The value of the radius must be positive, not {value}")
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

    # -------------------- Is Point Inside - Circle Method -------------------- #

    def point_inside_circle(self, x: int | float, y: int | float) -> bool:
        """Method to see if the point is inside the circle shape"""
        if not isinstance(x, (float, int)):
            raise TypeError(
                f"x value is wrong, must be int or float. Not {type(x).__name__}"
            )
        if not isinstance(y, (float, int)):
            raise TypeError(
                f"y value is wrong, must be int or float. Not {type(y).__name__}"
            )
        if (
            math.hypot(x - self.x_pos, y - self.y_pos) <= self.c_radius
        ):  # uses the hypot module from math in order to calculate the euclidian distance
            return True
        else:
            return False

    # -------------------- Representation and String __Methods__ Circle -------------------- #
    def __repr__(self) -> str:
        """String representation of class Circle"""
        return f"Circle = x = {self.x_pos}, y = {self.y_pos}, radius = {self.c_radius}."

    def __str__(self) -> str:
        """Override string function"""
        return f"The Circle's position is x: {self.x_pos}, y: {self.y_pos}. The radius is: {self.c_radius}, Area: {self.area}, Circumference: {self.circumference}."


# --------------------------------------- Rectangle class --------------------------------------- #
class Rectangle(Shape):
    """Rectangle Subclass, Super Class is Shape"""

    def __init__(
        self,
        x_pos: int | float = 1,  # Set the default value to 1 for the __init__ functions
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

    # -------------------- Setter for Rectangle Class -------------------- #

    @r_height.setter
    def r_height(self, value: float | int):
        if not isinstance(
            value, (float, int)
        ):  # Checks to see if the value is float or int
            raise TypeError(f"Height must be float or int, not {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"The value of height must be positive, not {value}")

        self._r_height = value  # Setting the height as value

    @r_width.setter
    def r_width(self, value: float | int):
        if not isinstance(
            value, (float, int)
        ):  # Checks to see if the value is float or int
            raise TypeError(f"Height must be float or int, not {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"The value of height must be positive, not {value}")

        self._r_width = value

    # -------------------- Area Method - Rectangle -------------------- #

    @property
    def area(self) -> (int | float):
        """Calculates the area of the Rectangle"""
        return self.r_height * self.r_width

    # -------------------- Is it Square Method - Rectangle -------------------- #

    @property
    def is_square(self) -> bool:
        """Method to see if the rectangle is square"""
        if self.r_height == self.r_width:
            return True
        else:
            return False

    # -------------------- Calculate the Perimiter - Rectangle -------------------- #

    @property
    def perimiter(self) -> (float | int):
        """Method used to see the perimiter of the rectangle"""
        return (self.r_height + self.r_width) * 2

    # -------------------- Is Point Inside - Rectangle -------------------- #

    def point_inside_rectangle(self, x: float | int, y: float | int) -> bool:
        """Method to see if the point is inside the rectangle shape"""
        if not isinstance(x, (float, int)):
            raise TypeError(
                f"x value is wrong, must be int or float. Not {type(x).__name__}"
            )
        x_min = self.x_pos - self.r_width / 2
        x_max = (
            self.x_pos + self.r_width / 2
        )  # Splits the rectangle into four parts. from where the x and y position is in relation to its width and height
        if not isinstance(y, (float, int)):
            raise TypeError(
                f"y value is wrong, must be int or float. Not {type(y).__name__}"
            )
        y_min = self.y_pos - self.r_height / 2
        y_max = self.y_pos + self.r_height / 2

        if (
            x_min < x < x_max and y_min < y < y_max
        ):  # Checks to see if point is inside the rectangle
            return True
        else:
            return False

    # -------------------- Representation and String __Methods__ Rectangle -------------------- #
    def __repr__(self) -> str:
        """String representation of class Rectangle"""
        return f"Rectangle = x = {self.x_pos}, y = {self.y_pos}, height = {self.r_height}, width = {self.r_width}."

    def __str__(self) -> str:
        """Override string function"""
        return f"The Rectangle's position is x: {self.x_pos}, y: {self.y_pos}. The height and width is: {self.r_height}, {self.r_width}. Area: {self.area}, Perimiter: {self.perimiter}."
