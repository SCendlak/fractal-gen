import tkinter as tk
from tkinter import ttk

from classes.fractal_app import FractalApp

if __name__ == "__main__":
    root = tk.Tk()
    app = FractalApp(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (root.quit(), root.destroy()))
    quit_btn = ttk.Button(root, text="Quit", command=lambda: (root.quit(), root.destroy()))
    quit_btn.grid(row=4, column=1, padx=5, pady=5)

    root.mainloop()
