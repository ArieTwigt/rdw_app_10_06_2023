from math import pow, pi
from typing import Tuple, Union


def calc_circle(diameter: float,
                rounding: int=2, 
                double_up: bool=False 
                ) -> Tuple[float, float]: 
    """
    Calculates the size of a circle.

    Inputs:
    * diameter

    Returns
    * size of the circle
    * radius of the circle
    
    """

    # calculate the radius
    radius = diameter / 2

    # calculate the size
    size = pow(radius, 2) * pi

    # round the size
    size_rounded = round(size, rounding)

    # double it?
    if double_up:
        print("Doubling it")
        size_rounded *= 2

    return size_rounded, radius



def calc_contents(length: Union[float, int], 
                  height: Union[float, int], 
                  width: Union[float, int]
                  ) -> Union[float, int]:
    """
    Method for calculating the contents of a box

    Inputs:
    * length: length of the box
    * width
    * height

    Returns:
    * Size of the box
    """

    # calculate the
    size = length * width * height

    return size