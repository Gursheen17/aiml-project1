import tkinter as tk
from tkinter import messagebox
import math

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Error", "Coefficient 'a' cannot be zero!")
            return

        D = (b**2) - (4*a*c)

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            result = f"Discriminant: {D}\nRoots are Real and Different\nx1 = {x1:.2f}\nx2 = {x2:.2f}"

        elif D == 0:
            x = -b / (2*a)
            result = f"Discriminant: {D}\nRoots are Real and Equal\nx = {x:.2f}"

        else:
            real = -b / (2*a)
            imag = math.sqrt(-D) / (2*a)
            result = f"Discriminant: {D}\nRoots are Complex\nx1 = {real:.2f} + {imag:.2f}i\nx2 = {real:.2f} - {imag:.2f}i"

        label_result.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


# GUI Window
root = tk.Tk()
root.title("Quadratic Equation Solver")
root.geometry("400x400")
root.config(bg="#dbeafe")  # pastel blue background

# Title
tk.Label(root, text="Quadratic Equation Solver",
         font=("Arial", 16, "bold"),
         bg="#dbeafe", fg="#1e3a8a").pack(pady=10)

# Input fields
frame = tk.Frame(root, bg="#dbeafe")
frame.pack(pady=10)

tk.Label(frame, text="a:", font=("Arial", 12), bg="#dbeafe").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(frame, font=("Arial", 12), bg="#eff6ff")
entry_a.grid(row=0, column=1)

tk.Label(frame, text="b:", font=("Arial", 12), bg="#dbeafe").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(frame, font=("Arial", 12), bg="#eff6ff")
entry_b.grid(row=1, column=1)

tk.Label(frame, text="c:", font=("Arial", 12), bg="#dbeafe").grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(frame, font=("Arial", 12), bg="#eff6ff")
entry_c.grid(row=2, column=1)

# Button
tk.Button(root, text="Solve",
          font=("Arial", 12, "bold"),
          bg="#93c5fd", fg="#1e3a8a",
          activebackground="#60a5fa",
          command=solve_quadratic).pack(pady=15)

# Result label
label_result = tk.Label(root, text="",
                        font=("Arial", 12),
                        bg="#dbeafe",
                        fg="#1e3a8a",
                        justify="left")
label_result.pack(pady=10)

# Footer
tk.Label(root, text="THANK YOU!",
         font=("Arial", 10, "italic"),
         bg="#dbeafe",
         fg="#1e3a8a").pack(side="bottom", pady=10)

root.mainloop()