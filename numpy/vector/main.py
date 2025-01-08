import numpy as np
import matplotlib.pyplot as plt


vector = lambda x, y: np.array([x, y])

# Data
v1 = vector(3, 4)
v2 = vector(4, 5)
v3 = vector(1, 2)

sf = 2

vs = sf * v3



# angle between 2 vectors
# dot_product = np.dot(v1, v2)
# angle = np.arccos(dot_product / (np.linalg.norm(v1)) * np.linalg.norm(v2))

# Cross Product
# cross_product = np.cross(v1, v2)

# Vector Normalization
mag = np.linalg.norm(v1)
v_norm = v1/mag


# Vector Projection  V -> U
projection = lambda vec1, vec2: (np.dot(vec1, vec2)/ np.dot(vec2, vec2)) * vec2

u = vector(3, 4)
v = vector(1, 2)
proj_v_on_u = projection(v, u)


# Plot
TITLE = "Vector Projection"

LOWER_X_BOUND = 0
LOWER_Y_BOUND = 0
UPPER_X_BOUND = 8
UPPER_Y_BOUND = 8

FIGURE_HEIGHT = 8
FIGURE_WEIGHT = 6


plt.figure(figsize=(FIGURE_HEIGHT, FIGURE_WEIGHT))

# plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='b', label='Original')
# plt.quiver(0, 0, vs[0], vs[1], angles='xy', scale_units='xy', scale=1, color='r', label='Scaled')
make_quiver = lambda vec, angle='xy', scale_units='xy', scale=1, color='b', label='': plt.quiver(0, 0, vec[0], vec[1], angles=angle, scale_units=scale_units, scale=scale, color=color, label=label)

make_quiver(v, color='b', label='v')
make_quiver(u, color='r', label='u')
make_quiver(proj_v_on_u, color='g', label='proj_v_on_u')


plt.legend()

plt.xlim(LOWER_X_BOUND, UPPER_X_BOUND)
plt.ylim(LOWER_Y_BOUND, UPPER_Y_BOUND)

# plt.axis('equal')
plt.grid()

plt.title(TITLE)
plt.show()








