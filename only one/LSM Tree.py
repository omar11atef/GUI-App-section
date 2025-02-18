import tkinter as tk
from tkinter import messagebox

# Function to compute LSM (Least Common Multiple) using the 'Tree' method
def compute_LSM(a, num2):
    if num2 > a:
        hight = a
    else:
        hight = num2
    value = hight  # To calculate the next index
    while True:
        if hight % a == 0 and hight % num2 == 0:
            return hight
        else:
            hight = hight + value  # Go to the next index

def calculate_LSM(event=None):
    try:
        # Get the numbers from the user input
        first_number = int(entry_first_number.get())
        second_number = int(entry_second_number.get())

        # Call the compute_LSM function to calculate the LSM
        lsm_value = compute_LSM(first_number, second_number)

        # Display the result on the LSM result button
        button_lsm_result.config(text=f"LSM: {lsm_value}", bg='blue', fg='white')

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
root.title("LSM Calculator")
root.config(background="#3770C8")

# Label for the message about the LSM method
label_message = tk.Label(root, text="Calculate LSM by using: Tree", font=('Arial', 14))
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

# Button to calculate LSM
button_calculate_LSM = tk.Button(root, text="Calculate LSM", command=calculate_LSM)
button_calculate_LSM.grid(row=3, column=0, padx=10, pady=10)

# Button to display the LSM result
button_lsm_result = tk.Button(root, text="LSM Result", width=20, height=2)
button_lsm_result.grid(row=3, column=1, padx=10, pady=10)

# Bind the Enter key to trigger the Calculate LSM button
root.bind('<Return>', calculate_LSM)

# Bind the Up arrow key to focus on the First Number input field
root.bind('<Up>', navigate_up)

# Bind the Down arrow key to focus on the Second Number input field
root.bind('<Down>', navigate_down)

# Run the application
root.mainloop()
