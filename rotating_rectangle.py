import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Rectangle dimensions
width = 4
height = 2
vectors = [
    np.array([width / 2, height / 2]),
    np.array([-width / 2, height / 2]),
    np.array([-width / 2, -height / 2]),
    np.array([width / 2, -height / 2]),
]

colors = ['r', 'g', 'b', 'm']

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True, which='both')

quivers = [ax.quiver(0, 0, v[0], v[1], color=c, angles='xy', scale_units='xy', scale=1) for v, c in zip(vectors, colors)]

# Create the rectangle outline
rectangle_line, = ax.plot([], [], 'k-', linewidth=2, label='Rectangle')

# Store reference to animation globally
ani = None

def update(frame):
    """
    Updates the plot for each frame of the animation.
    """
    global ani
    
    angle = np.deg2rad(frame)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])

    rotated_vectors = []
    for i, v in enumerate(vectors):
        rotated_vector = np.dot(rotation_matrix, v)
        rotated_vectors.append(rotated_vector)
        quivers[i].set_UVC(rotated_vector[0], rotated_vector[1])

    # Update rectangle outline by connecting the rotated corner points
    # Close the rectangle by adding the first point at the end
    x_coords = [rv[0] for rv in rotated_vectors] + [rotated_vectors[0][0]]
    y_coords = [rv[1] for rv in rotated_vectors] + [rotated_vectors[0][1]]
    rectangle_line.set_data(x_coords, y_coords)

    # Stop animation after completing one full rotation (360 degrees)
    if frame >= 360:
        ani.event_source.stop()

    return quivers + [rectangle_line]

# Create the animation with exactly 360 degrees of rotation
# Using frames from 0 to 360 with step size 2 (181 frames total)
ani = FuncAnimation(fig, update, frames=np.arange(0, 361, 2), 
                   blit=False, interval=50, repeat=False)

plt.show()