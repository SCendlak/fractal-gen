import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import BOTH, Canvas


def mandelbrot(re, im, max_iter):
    c = complex(re, im)
    z = 0.0j
    for i in range(max_iter):
        z = z ** 2 + c  # cant use math.pow cause z is complex number type
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i
    return max_iter


def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    # using linear space to space data evenly on plot
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    fractal = np.empty((height, width))

    for i, re in enumerate(real):
        for j, im in enumerate(imag):
            fractal[j, i] = mandelbrot(re, im, max_iter)

    return fractal


def display_mandelbrot(max_iteration: int, master_canvas: Canvas):
        print("generating mandelbrot set for: "+str(max_iteration)+" iterations")
        xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
        width, height = 600, 400

        fractal = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iteration)

        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        ax.imshow(fractal, extent=(xmin, xmax, ymin, ymax), cmap="inferno")
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=master_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)
