import tkinter as tk
from tkinter import ttk

from .mandelbrot import display_mandelbrot
from .sierpinski_trinagle import display_sierpinski_triangle
from .kochs_snowflake import display_koch_snowflake

class FractalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Explorer")

        ttk.Label(root, text="Fractal Type:").grid(row=0, column=0, padx=5, pady=5)
        self.fractal_type = tk.StringVar(value="Mandelbrot Set")
        self.fractal_menu = ttk.Combobox(root, state="readonly", textvariable=self.fractal_type,
                                         values=["Mandelbrot Set", "Sierpinski Triangle", "Koch Snowflake"])
        self.fractal_menu.grid(row=0, column=1, padx=5, pady=5)

        self.param_frame = ttk.LabelFrame(root, text="Parameters")
        self.param_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        ttk.Label(self.param_frame, text="Max Iterations:").grid(row=0, column=0, padx=5, pady=5)
        self.max_iter = tk.IntVar(value=100)
        self.max_iter_entry = ttk.Entry(self.param_frame, textvariable=self.max_iter)
        self.max_iter_entry.grid(row=0, column=1, padx=5, pady=5)

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=2)
        self.canvas_flag = 0

        self.generate_button = ttk.Button(root, text="Generate", command=self.generate_fractal)
        self.generate_button.grid(row=3, column=0, padx=5, pady=5)

        self.clear_button = ttk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.grid(row=3, column=1, padx=5, pady=5)

    def generate_fractal(self):
        fractal_type = self.fractal_type.get()
        self.clear_canvas()
        print(fractal_type)
        if fractal_type == "Mandelbrot Set":
            temp_iter = self.max_iter.get()
            if temp_iter <= 99:
                temp_iter = 100
            display_mandelbrot(temp_iter, self.canvas)
        elif fractal_type == "Sierpinski Triangle":
            temp_iter = self.max_iter.get()
            if temp_iter >= 5:
                temp_iter = 5
            display_sierpinski_triangle(temp_iter, self.canvas)
        elif fractal_type == "Koch Snowflake":
            temp_iter = self.max_iter.get()
            if temp_iter >= 5:
                temp_iter = 5
            display_koch_snowflake(temp_iter, self.canvas)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=2)
        self.canvas_flag = 0
