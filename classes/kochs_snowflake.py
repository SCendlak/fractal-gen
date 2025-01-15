import matplotlib.pyplot as plt
import numpy as np
from tkinter import BOTH, Canvas

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def koch_snowflake(max_depth, scale=10):
    """
    Return two lists x, y of point coordinates of the Koch snowflake.

    Parameters
    ----------
    max_depth : int
        The recursion depth.
    scale : float
        The extent of the snowflake (edge length of the base triangle).
    """
    def _koch_snowflake_complex(max_depth):
        if max_depth == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            start_point = _koch_snowflake_complex(max_depth - 1)
            end_point = np.roll(start_point, shift=-1)
            connection_vector = end_point - start_point

            new_points = np.empty(len(start_point) * 4, dtype=np.complex128)
            new_points[::4] = start_point
            new_points[1::4] = start_point + connection_vector / 3
            new_points[2::4] = start_point + connection_vector * ZR
            new_points[3::4] = start_point + connection_vector / 3 * 2
            return new_points

    points = _koch_snowflake_complex(max_depth)
    x, y = points.real, points.imag
    return x, y


def display_koch_snowflake(max_depth: int, master_canvas: Canvas):
    print("generating koch snowflake for: " + str(max_depth) + " depth")
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    x, y = koch_snowflake(max_depth)
    ax.axis('equal')
    ax.fill(x, y)
    canvas = FigureCanvasTkAgg(fig, master=master_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)


if __name__ == '__main__':
    x, y = koch_snowflake(max_depth=5)

    plt.figure(figsize=(6, 4))
    plt.axis('equal')
    plt.fill(x, y)
    plt.show()