# TODO
from __future__ import annotations
from turtle import circle

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
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
        """Checks Equality (==) between Shapes""" #Should i fix so that it checks position aswell?
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
    ):  # This will add the values to self.x or self.y
        """Translation method is used in order to change the values of the x, y position for"""
        self.x_pos += x_value
        self.y_pos += y_value

    # + __repr__()
    def __repr__(self) -> str:
        """Representation of the shapes positional values"""
        return f"Shape's position x = {self.x_pos}, y = {self.y_pos}"

    # + __str__()
    def __str__(self) -> str:
        """When print function is called, returns the x position and y position of the shape"""
        return f"The shape's position is x = {self.x_pos}, y = {self.y_pos}"


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
        """Radius of the Circle object"""
        return self._c_radius  # Getter

    @c_radius.setter
    def c_radius(self, value: (float | int)):  # Setter
        if not isinstance(
            value, (float, int)
        ):  # Checks to see if the value is float or int
            raise TypeError(f"Radius must be float or int, not {type(value).__name__}")
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
       # if not isinstance((x, y), (float, int)):
            #raise TypeError("X or Y must be int or float")
        if math.hypot(x - self.x_pos, y - self.y_pos ) <= self.c_radius:  # uses the hypot module from math in order to calculate the euclidian distance
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

#Placeholder plot code
    def plot(self, color="r"):
        fig, ax = plt.subplots()
        circle1 = plt.Circle(
            (self.x_pos, self.y_pos), self.c_radius, color=color, alpha=0.5
        )
        ax.add_patch(circle1)
        ax.autoscale()
        ax.set_aspect(1)
        plt.show()



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

    # -------------------- Setter for Rectangle Class + # TODO Error Handling -------------------- #

    @r_height.setter
    def r_height(self, value: float | int):
        if not isinstance(
            value, (float, int)
        ):  # Checks to see if the value is float or int
            raise TypeError(f"Height must be float or int, not {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"The value of height must be positive, not {value}")

        self._r_height = value

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
    def perimiter(self) -> float | int:
        """Method used to see the perimiter of the rectangle"""
        return (self.r_height + self.r_width) * 2

    # -------------------- Is Point Inside - Rectangle -------------------- #
    @property
    def point_inside_rectangle(self) -> bool:
        """Method to see if the point is inside the rectangle shape"""

#Placeholder code to print rectangle:
    def plotter(self) -> None:
        #define matplotlib figure and axis
        fig, ax = plt.subplot()
        #add rectangle to plot
        ax.add_patch(Rectangle((self.x_pos, self.y_pos), self.r_height, self.r_width))
        plt.show()

    # -------------------- Representation and String __Methods__ Rectangle -------------------- #
    def __repr__(self) -> str:
        """String representation of class Rectangle"""
        return f"Rectangle = x = {self.x_pos}, y = {self.y_pos}, height = {self.r_height}, width = {self.r_width}."

    def __str__(self) -> str:
        """Override string function"""
        return f"The Rectangle's position is x: {self.x_pos}, y: {self.y_pos}. The height and width is: {self.r_height}, {self.r_width}. Area: {self.area}, Perimiter: {self.perimiter}."


#r = Rectangle(1,1,1,1)
#print(r)
#print(r.is_square)

c1 = Circle(1,1,1)
c2 = Circle(1,1,3)
c3 = Circle(1,2,2)

r1 = Rectangle(1,1,2,4)
r1.plotter()

#c1.plot()
#c2.plot("b")


#print(c)
#print(c.is_unit_circle)

#c.translation(1,2)
#print(c)

