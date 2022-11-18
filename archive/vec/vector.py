from dataclasses import dataclass
from __future__ import annotations


"Îî Ĵĵ K̂k̂"

@dataclass
class Vector2D:
    x: int
    y: int

    def __str__(self):
        txt = f"< {self.x}, {self.y} >"  # î ĵ
        return txt
    
    def __add__(self, other: Vector2D):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)
    
    def __mul__(self, other: int | float):
        return Vector2D(other*self.x, other*self.y)
    
    def __rmul__(self, other: int | float):
        return Vector2D(other*self.x, other*self.y)

    def dot(self, other: Vector2D):
        x = self.x*other.x
        y = self.y*other.y
        return Vector2D(x, y)
    
    def cross(self, other: Vector2D):
        return


@dataclass
class Vector3D:
    x: int
    y: int
    z: int

    def __str__(self):
        txt = f"< {self.x}, {self.y}, {self.z} >"  # î ĵ k
        return txt

    def __add__(self, other: Vector3D):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3D(x, y, z)
    
    def __mul__(self, other: int | float):
        return Vector3D(other*self.x, other*self.y, other*self.z)
    
    def __rmul__(self, other: int | float):
        return Vector3D(other*self.x, other*self.y, other*self.z)

    def dot(self, other: Vector3D):
        x = self.x*other.x
        y = self.y*other.y
        z = self.z*other.z
        return Vector3D(x, y, z)
    
    def cross(self, other: Vector3D):
        return


if __name__ == '__main__':
    # 2D
    vec_2d = Vector2D(1, 1)
    
    # 3D
    vec_3d = Vector3D(1, 2, 1)

    # Display
    display_txt = f"""
2D Vector: {vec_2d*2}

3D Vector: {3*vec_3d}"""

    print(display_txt)
    
