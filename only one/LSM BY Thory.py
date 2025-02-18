import tkinter as tk
from tkinter import messagebox

# Function to compute GCD using Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute LCM using the formula: LCM = (a * b) / GCD(a, b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def calculate_LSM(event=None):
    try:
        # Get the numbers from the user input
        first_number = int(entry_first_number.get())
        second_number = int(entry_second_number.get())
        
        # Calculate the GCD and LCM
        gcd_value = gcd(first_number, second_number)
        lcm_value = lcm(first_number, second_number)
        
        # Display the results on the buttons
        button_gcd_result.config(text=f"GCD: {gcd_value}", bg='green', fg='white')
        button_lcm_result.config(text=f"LCM: {lcm_value}", bg='blue', fg='white')
        
        # Clear the input fields after calculation
        entry_first_number.delete(0, tk.END)
        entry_second_number.delete(0, tk.END)
    
    except ValueError:
        # Show an error message if the user doesn't input a valid integer
        messagebox.showerror("Input Error", "Please enter valid numbers for both fields.")

def navigate_up(event):
    entry_first_number.focus_set()  # Focus back to the first number input

def navigate_down(event):
    entry_second_number.focus_set()  # Focus to the second number input

# Set up the main window
root = tk.Tk()
root.title("LCM and GCD Calculator")
root.config(background="#7EA956")

# Label for the message about the LCM method
label_message = tk.Label(root, text="Calculate LCM by using: a*b / gcd(a,b)", font=('Arial', 14))
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

# Button to calculate GCD and LCM using the formula
button_calculate = tk.Button(root, text="Calculate LCM and GCD", command=calculate_LSM)
button_calculate.grid(row=3, column=0, padx=10, pady=10)

# Button to display the GCD result
button_gcd_result = tk.Button(root, text="GCD Result", width=20, height=2)
button_gcd_result.grid(row=3, column=1, padx=10, pady=10)

# Button to display the LCM result
button_lcm_result = tk.Button(root, text="LCM Result", width=20, height=2)
button_lcm_result.grid(row=4, column=0, padx=10, pady=10)

# Bind the Enter key to trigger the Calculate LCM and GCD button
root.bind('<Return>', calculate_LSM)

# Bind the Up arrow key to focus on the First Number input field
root.bind('<Up>', navigate_up)

# Bind the Down arrow key to focus on the Second Number input field
root.bind('<Down>', navigate_down)

# Run the application
root.mainloop()