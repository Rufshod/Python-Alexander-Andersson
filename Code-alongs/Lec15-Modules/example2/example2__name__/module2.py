import numpy as np


def newline():
    """Prints a newline"""
    return print("\n")

def trigonometric_identity(angle: float) -> float:
    """Calculates trig identity
    
    param: 
    angle: angle in radians
    
    return trignometric one
    """
    print("Running trigonometric_identity()")
    return np.cos(angle) ** 2 + np.sin(angle) **2

if __name__ == "__main__": # if statment to tell if we run directly from main file or if we imported it
    print("Running directly from module2.py")
    print(trigonometric_identity(1337))
else:
    print("You have imported trigonometric_identity from module2.py")