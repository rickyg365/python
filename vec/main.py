import os
from dataclasses import dataclass

from vector import Vector2D, Vector3D


def main():

    vec1_2d = Vector2D(1, 1)
    vec2_2d = Vector2D(-1, -1)
    vec3_2d = Vector2D(2, 2)

    vec1_3d = Vector3D(1, 1, 1)
    vec2_3d = Vector3D(-1, -1, -1)
    vec3_3d = Vector3D(2, 2, 2)


    print(f"""
2D Vectors
1. {vec1_2d}
2. {vec2_2d}
3. {vec3_2d}

3D Vectors
1. {vec1_3d}
2. {vec2_3d}
3. {vec3_3d}


2d sums
1 + 3 = {vec3_2d + vec1_2d}
2 + 3 = {vec2_2d + vec3_2d}

3d sums
1 + 1 = {vec1_3d + vec1_3d}
2 + 3 = {vec2_3d + vec3_3d}
""")

    return

if __name__ == '__main__':
    main()
