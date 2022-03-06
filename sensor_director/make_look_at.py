import numpy as np

# https://github.com/stemkoski/three.py
def make_look_at(position, target, up):

    forward = np.subtract(target, position)
    forward = np.divide(forward, np.linalg.norm(forward))

    right = np.cross(forward, up)

    # if forward and up vectors are parallel, right vector is zero;
    #   fix by perturbing up vector a bit
    if np.linalg.norm(right) < 0.001:
        epsilon = np.array([0.001, 0, 0])
        right = np.cross(forward, up + epsilon)

    right = np.divide(right, np.linalg.norm(right))

    up = np.cross(right, forward)
    up = np.divide(up, np.linalg.norm(up))

    return np.array(
        [
            [right[0], up[0], -forward[0], position[0]],
            [right[1], up[1], -forward[1], position[1]],
            [right[2], up[2], -forward[2], position[2]],
            [0, 0, 0, 1],
        ]
    )
