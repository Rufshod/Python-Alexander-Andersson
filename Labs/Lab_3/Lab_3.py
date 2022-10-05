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
    def get_x_pos(self) -> int | float:
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
    def get_y_pos(self) -> int | float:
        """Getter for y_pos"""
        return self._y_pos

# y Position setter

    @y_pos.setter
    def y_pos(self, value: int | float) -> int | float:
        if not isinstance(value, (int, float)): # checks if the type in y_pos is int or float
            raise TypeError(f"y Position must be an int or float, not {type(value).__name__}")
        # if not 0 <= value <= 1000: TODO, SETTING THIS FOR LATER IF NEEDED.
        self._y_pos = value

x = Shape(1,2)

# + __init__(self, x_pos ,y_pos)
#+ __repr__()
#+ __str__()

#+ __lt__(self, other) <
#+ __gt__(self, other) >
#+ __le__(self, other) <=
#+ __ge__(self, other) >=
#+ translation(x, y) -> Shape

#- in_object(self, point) -> bool:

# x_pos: int = 0
# y_pos: int = 0

# area = None
# omkrets = None


#Circle class

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