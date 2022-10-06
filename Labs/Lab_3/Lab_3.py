#TODO
from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
#TODO 
#Shape class
class Shape:
    """The Super class named Shape"""
    def __init__(self, x_pos: int | float, y_pos: int | float) -> None:
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
        if not isinstance(value, (int, float)): # checks if the type in x_pos is int or float
            raise TypeError(f"x Position must be an int or float, not {type(value).__name__}")
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
        if not isinstance(value, (int, float)): # checks if the type in y_pos is int or float
            raise TypeError(f"y Position must be an int or float, not {type(value).__name__}")
        # if not 0 <= value <= 1000: TODO, SETTING THIS FOR LATER IF NEEDED.
        self._y_pos = value


# -------------------- Overloading Operators, Shape Class  -------------------- # PLACEHOLDER CODE


# __eq__(self, other) ==
    def __eq__(self, other: Shape) -> bool:
        """Checks Equality between Shapes""" # TODO ADD AREA CHECKER
        if type(self) == other:
            return True
        else:
            return False

#+ __lt__(self, other) <
    def __lt__(self, other: Shape) -> bool:
        """Checks less than between Shapes""" # TODO ADD AREA CHECKER
        if type(self) < other:
            return True
        else:
            return False

#+ __gt__(self, other) >
    def __gt__(self, other: Shape) -> bool:
        """Checks greater than between Shapes""" # TODO ADD AREA CHECKER
        if type(self) > other:
            return True
        else:
            return False

#+ __le__(self, other) <=
    def __le__(self, other: Shape) -> bool:
        """Checks less or equal between Shapes""" # TODO ADD AREA CHECKER
        if type(self) <= other:
            return True
        else:
            return False

#+ __ge__(self, other) >=
    def __ge__(self, other: Shape) -> bool:
        """Checks greator or equal between Shapes""" # TODO ADD AREA CHECKER
        if type(self) >= other:
            return True
        else:
            return False


#+ translation(x, y) -> Shape
    def translation(self, x_value: float | int, y_value: float | int,): # This should add the x and or y to self.x or self.y
        self.x_pos += x_value
        self.y_pos += y_value





#+ __repr__()
    def __repr__(self) -> str:
        """When print function is called, returns the x position and y position of the shape"""
        return f"The shape's position is x = {self.x_pos}, y = {self.y_pos}"
#+ __str__()


a = Shape(10,20)
print(a)
a.translation(10,0)
print(a)

#- in_object(self, point) -> bool:

# x_pos: int = 0
# y_pos: int = 0

# area = None
# omkrets = None


#Circle class

class Circle(Shape):


# - radie: float = 1
# x_pos: float = 0
# y_pos: float = 0

# Radie Getter
# @property 
#def radie(self):


# Radie Setter 
    #def(self, radie, xpos, ypos)

# def is_unit_circle(self) -> bool:
    # if unit is circle
        # return True
        # else:
        # return false
        # EXAMPLE



# def calc_area(self) -> float:
    # radie ** Pi.

# def calc_circumfurence(self) -> float:
    #calculating circum
    #return circum_answer.


#Rectangle class

# @property getter

# @width.setter

# @height.getter

# def is_square(self) -> bool:
    # h*w/2 = x**2
    
# def calc_area(self) > float:
    #h**2 + w**2

# CALC CIRCUM?????