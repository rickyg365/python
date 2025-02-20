import cv2
import numpy as np


def create_dummy_img(width: int, height: int, data_type=np.uint8):
    return np.zeros((width, height), dtype=data_type)

def add_circle(drawing_surface: np.array, x, y, radius):
    return cv2.circle(drawing_surface, (x, y), radius, (255,), -1)


custom_kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])


blank_canvas = create_dummy_img(50, 50)

canvas = add_circle(blank_canvas, 25, 25, 10)
cv2.imwrite("original.png", canvas)

dst = cv2.filter2D(canvas, -1, custom_kernel)
cv2.imwrite("filtered.png", dst)
