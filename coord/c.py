import os

import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass


sin = np.sin
cos = np.cos

asin = np.arcsin
acos = np.arccos

# MOstly a class used for viewing not necesseraly data storage
@dataclass
class Coordinate:
    x: float
    y: float

    def __str__(self) -> str:
        txt = f"{self.x}, {self.y}"
        return txt

    def export(self):
        return self.x, self.y


@dataclass
class PolarCoordinate:
    r: float
    theta: float

    def __str__(self) -> str:
        txt = f"{self.r}, {self.theta} deg"
        return txt
    
    def export(self):
        return self.r, self.theta
    

def reg_to_polar(x: float, y: float):
    '''
         /|
        / |
       /  |
    0 ____| y
       x
    SOH
    CAH
    TOA
    '''
    radius = (x**2 + y**2)**(1/2)
    thetax = acos(x/radius) 
    thetay = asin(y/radius)

    print(thetax, thetay)

    return radius, thetax

def polar_to_reg(radius: float, theta: float):
    x = cos(theta) * radius
    y = sin(theta) * radius

    return x, y


def main():
    # X Coordinates
    x_coords = np.linspace(0, 1/2, 10)

    f = lambda x: x**2
    f1 = lambda x: x**2 + x
    f2 = lambda x: x**2 + x + 1
    
    # Y Coordinates
    f_x = [f(a) for a in x_coords]
    f1_x = [f1(b) for b in x_coords]
    f2_x = [f2(c) for c in x_coords]

    f_f_x = [f(a) for a in f_x]
    f_f_f_x = [f(a) for a in f_f_x]

    # Plot Title
    plt.title('Sample Graph')

    # Label X-axis and Y-axis
    plt.xlabel('Raw Data')
    plt.ylabel('Parsed Data')

    plt.plot(x_coords, f_x, color='red', label="function")
    plt.plot(x_coords, f_f_x, color='green', label="function function")
    plt.plot(x_coords, f_f_f_x, color='blue', label="function function function")

    # plt.plot(x_coords, f1_x, color='green', label="function 1")
    # plt.plot(x_coords, f2_x, color='blue', label="function 2")
    
    plt.legend()
    plt.show()

    print(f"Ratio: {(f_f_f_x[-1] - f_f_x[-1]) / (f_f_x[-1] - f_x[-1])}")
    return

if __name__ == '__main__':
    main()
