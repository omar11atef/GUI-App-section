import tkinter as tk
import math 

def is_prime(n):
    if n== 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Function to check the number and update the second button
def check_number(event = None):                                                             
    try:
        # Get the number from the entry box
        number = int(entry_box.get())
        
        # Check if the number is prime
        if is_prime(number):
            result_button.config(text="THAT IS PRIME", bg="green")
        else:
            result_button.config(text="NOT PRIME", bg="red")
    except ValueError:
        result_button.config(text="INVALID INPUT", bg="yellow")
    
    # Clear the entry box after checking
    entry_box.delete(0, tk.END)

# Function to reset the result button and clear the input box
def reset_fields():
    entry_box.delete(0, tk.END)
    result_button.config(text="Result", bg="lightgrey")

# Create the main window
root = tk.Tk()
root.title("Prime Number Checker")
root.geometry("300x250")  # Set the window size
root.resizable(False, False)  # Disable window resizing
root.config(background="blue")
# Centering the layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Text Box (Input)
entry_box = tk.Entry(root, font=("Helvetica", 14), width=10)
entry_box.grid(row=1, column=0, sticky="e", padx=10)
# Enter Run the Buttom check box
entry_box.bind("<Return>", check_number)
# First Button - Check Prime
check_button = tk.Button(root, text="Check Prime", font=("Helvetica", 12), command=check_number)
check_button.grid(row=1, column=1, sticky="w", padx=10)
# Second Button - Result
result_button = tk.Button(root, text="Result", font=("Helvetica", 12), bg="lightgrey", width=15)
result_button.grid(row=2, column=0, columnspan=2, pady=10)
# Reset Button - To clear fields
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_fields)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)
# Run the main loop
root.mainloop()