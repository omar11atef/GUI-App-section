import tkinter as tk
from tkinter import messagebox

# Function to compute GCD using Successive Difference method
def last_num(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b

def calculate_GCD(event=None):
    try:
        # Get the numbers from the user input
        first_number = int(entry_first_number.get())
        second_number = int(entry_second_number.get())
        
        # Calculate the GCD using Successive Difference method
        gcd_result = last_num(first_number, second_number)
        
        # Update the GCD result on the button
        button_gcd_result.config(text=f"GCD: {gcd_result}", bg='green', fg='white')
        
        # Clear the input fields after calculation
        entry_first_number.delete(0, tk.END)
        entry_second_number.delete(0, tk.END)
    
    except ValueError:
        # Show an error message if the user doesn't input a valid integer
        messagebox.showerror("Input Error", "Please enter valid numbers for both fields.")

def check_gcd_result():
    first_number = int(entry_first_number.get())
    second_number = int(entry_second_number.get())
    
    # Calculate the GCD using Successive Difference method
    gcd_result = last_num(first_number, second_number)
    
    # Check if the GCD result is found
    if gcd_result == 1:
        button_gcd_result.config(text="Not Found (GCD = 1)", bg='red', fg='white')
    else:
        button_gcd_result.config(text=f"GCD Result: {gcd_result}", bg='green', fg='white')

def navigate_up(event):
    entry_first_number.focus_set()  # Focus back to the first number input

def navigate_down(event):
    entry_second_number.focus_set()  # Focus to the second number input

# Set up the main window
root = tk.Tk()
root.title("GCD Calculator")

# Label for the message about the Successive Difference method
label_message = tk.Label(root, text="Calculate GCD by using: Successive Difference", font=('Arial', 14))
label_message.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# First number entry and label
label_first_number = tk.Label(root, text="First Number:")
label_first_number.grid(row=1, column=0, padx=10, pady=10)

entry_first_number = tk.Entry(root)
entry_first_number.grid(row=1, column=1, padx=10, pady=10)

# Second number entry and label
label_second_number = tk.Label(root, text="Second Number:")
label_second_number.grid(row=2, column=0, padx=10, pady=10)

entry_second_number = tk.Entry(root)
entry_second_number.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate GCD using Successive Difference method
button_gcd = tk.Button(root, text="Calculate GCD", command=calculate_GCD)
button_gcd.grid(row=3, column=0, padx=10, pady=10)

# Button to display the GCD result (larger button)
button_gcd_result = tk.Button(root, text="GCD Result", command=check_gcd_result, width=20, height=3)
button_gcd_result.grid(row=3, column=1, padx=10, pady=10)

# Bind the Enter key to trigger the Calculate GCD button
root.bind('<Return>', calculate_GCD)

# Bind the Up arrow key to focus on the First Number input field
root.bind('<Up>', navigate_up)

# Bind the Down arrow key to focus on the Second Number input field
root.bind('<Down>', navigate_down)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Function to compute GCD using Successive Difference method
def last_num(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b

def calculate_GCD(event=None):
    try:
        # Get the numbers from the user input
        first_number = int(entry_first_number.get())
        second_number = int(entry_second_number.get())
        
        # Calculate the GCD using Successive Difference method
        gcd_result = last_num(first_number, second_number)
        
        # Update the GCD result on the button
        button_gcd_result.config(text=f"GCD: {gcd_result}", bg='green', fg='white')
        
        # Clear the input fields after calculation
        entry_first_number.delete(0, tk.END)
        entry_second_number.delete(0, tk.END)
    
    except ValueError:
        # Show an error message if the user doesn't input a valid integer
        messagebox.showerror("Input Error", "Please enter valid numbers for both fields.")

def check_gcd_result():
    first_number = int(entry_first_number.get())
    second_number = int(entry_second_number.get())
    
    # Calculate the GCD using Successive Difference method
    gcd_result = last_num(first_number, second_number)
    
    # Check if the GCD result is found
    if gcd_result == 1:
        button_gcd_result.config(text="Not Found (GCD = 1)", bg='red', fg='white')
    else:
        button_gcd_result.config(text=f"GCD Result: {gcd_result}", bg='green', fg='white')

def navigate_up(event):
    entry_first_number.focus_set()  # Focus back to the first number input

def navigate_down(event):
    entry_second_number.focus_set()  # Focus to the second number input

# Set up the main window
root = tk.Tk()
root.title("GCD Calculator")
root.config(background="#668C99")
# Label for the message about the Successive Difference method
label_message = tk.Label(root, text="Calculate GCD by using: Successive Difference", font=('Arial', 14))
label_message.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# First number entry and label
label_first_number = tk.Label(root, text="First Number:")
label_first_number.grid(row=1, column=0, padx=10, pady=10)

entry_first_number = tk.Entry(root)
entry_first_number.grid(row=1, column=1, padx=10, pady=10)

# Second number entry and label
label_second_number = tk.Label(root, text="Second Number:")
label_second_number.grid(row=2, column=0, padx=10, pady=10)

entry_second_number = tk.Entry(root)
entry_second_number.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate GCD using Successive Difference method
button_gcd = tk.Button(root, text="Calculate GCD", command=calculate_GCD)
button_gcd.grid(row=3, column=0, padx=10, pady=10)

# Button to display the GCD result (larger button)
button_gcd_result = tk.Button(root, text="GCD Result", command=check_gcd_result, width=20, height=3)
button_gcd_result.grid(row=3, column=1, padx=10, pady=10)

# Bind the Enter key to trigger the Calculate GCD button
root.bind('<Return>', calculate_GCD)

# Bind the Up arrow key to focus on the First Number input field
root.bind('<Up>', navigate_up)

# Bind the Down arrow key to focus on the Second Number input field
root.bind('<Down>', navigate_down)

# Run the application
root.mainloop()