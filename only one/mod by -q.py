
import tkinter as tk
from tkinter import messagebox

def calculate_modulus(event=None):  # Add event parameter to handle Enter key
    """Calculates modulus with the custom logic for negative m."""
    try:
        # Get values for m and n from the entry fields
        m = int(entry_first_number.get())
        n = int(entry_second_number.get())

        # Check if m is positive
        if m > 0:
            raise ValueError("m cannot be positive. Enter a negative value for m.")
        if n <= 0:
            raise ValueError("n must be greater than 0.")

        # Custom modulus calculation logic
        q = m // n
        r = m - (q * n)

        # Update the result on the button
        result_button.config(text=f"{m} = {q}({n}) + {r}")
        result_button.config(bg="yellow")  # Change button color to blue

        # Clear input fields for new input
        entry_first_number.delete(0, tk.END)
        entry_second_number.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        result_button.config(text="Error", bg="lightgray")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")
        result_button.config(text="Error", bg="lightgray")

def focus_first_number(event):
    """Set focus on the First Number input field."""
    entry_first_number.focus_set()

def focus_second_number(event):
    """Set focus on the Second Number input field."""
    entry_second_number.focus_set()

# Main window setup
root = tk.Tk()
root.title("Modulus Checker")
root.geometry("500x250")
root.config(background="#438abc")

# Add Message at the Top
tk.Label(root, text="Calculate the Mod negative by used: m = -q * n + r", 
        font=("Arial", 12), fg="blue").pack(pady=10)

# Widgets
frame = tk.Frame(root)
frame.pack(expand=True)

# Input Fields
tk.Label(frame, text="First Number (m):").grid(row=0, column=0, padx=5, pady=5)
entry_first_number = tk.Entry(frame)
entry_first_number.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Second Number (n):").grid(row=1, column=0, padx=5, pady=5)
entry_second_number = tk.Entry(frame)
entry_second_number.grid(row=1, column=1, padx=5, pady=5)

# Calculate Button
button1 = tk.Button(frame, text="Calculate Modulus", command=calculate_modulus)
button1.grid(row=2, column=0, pady=20, padx=10)

# Result Button (Next to Calculate Button)
result_button = tk.Button(frame, text="Result will be shown here", bg="lightgray", width=30)
result_button.grid(row=2, column=1, pady=20, padx=10)

# Bind Enter Key to the Calculate Button
root.bind('<Return>', calculate_modulus)

# Bind Up Arrow to focus on First Number
root.bind('<Up>', focus_first_number)

# Bind Down Arrow to focus on Second Number
root.bind('<Down>', focus_second_number)

# Run the application
root.mainloop()