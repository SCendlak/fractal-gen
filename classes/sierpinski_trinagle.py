import matplotlib.pyplot as plt
from tkinter import BOTH, Canvas

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Polygon


def draw_triangle(ax, depth, x, y, size):
    if depth == 0:
        points = [(x, y), (x+size, y), (x+size/2, y+size)]
        triangle = Polygon(points, closed=True, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(triangle)
    else:
        draw_triangle(ax, depth-1, x, y, size/2)
        draw_triangle(ax, depth-1, x + size/2, y, size/2)
        draw_triangle(ax, depth-1, x + size/4, y + size/2, size/2)


def display_sierpinski_triangle(max_depth: int, master_canvas: Canvas):
    print("generating sierpinski triangle for: " + str(max_depth) + " depth")
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    draw_triangle(ax, max_depth, 0, 0, 1)
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    canvas = FigureCanvasTkAgg(fig, master=master_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)


if __name__ == '__main__':
    print("needs to be run as main")
# display_sierpinski_triangle(3)