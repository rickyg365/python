import os

from dataclasses import dataclass

import numpy as np

sine = np.sin
cos = np.cos

arcsine = np.arcsin

@dataclass
class Coordinate:
    x: int
    y: int

    def __str__(self):
        txt = f"({self.x}, {self.y})"
        return txt


@dataclass
class PolarCoordinate:
    r: int
    theta: int

    def __str__(self):
        txt = f"{self.r}, {self.theta} deg"
        return txt

def reg_polar(regular_coordinate: Coordinate):
    a = regular_coordinate.x
    b = regular_coordinate.y

    radius = (a**2 + b**2)**(1/2)
    # o, b     a, x
    theta = arcsine(b/radius)

    return PolarCoordinate(radius, theta)
    

def polar_to_reg(polar_coordinate: PolarCoordinate):
    r = polar_coordinate.r
    theta = polar_coordinate.theta

    x = cos(theta) * r
    y = sine(theta) * r

    return Coordinate(x, y)


def main():
    r_coord = Coordinate(2, 2)
    p_coord = PolarCoordinate(1, np.pi/4)

    result = f"""
Reg. Coordinates: {r_coord} -> {reg_polar(r_coord)}

Polar Coordinate: {p_coord} -> {polar_to_reg(p_coord)}

"""

    print(result)
    pass

if __name__ == '__main__':
    main()
    
