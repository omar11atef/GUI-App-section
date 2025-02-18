import tkinter as tk
import math 

# Function to get factors of a number
def get_factors(num): 
    factors = [] 
    for i in range(1, int(num**0.5) + 1): 
        if num % i == 0: 
            factors.append(i) 
            if i != num // i:  # Avoid duplicate factors
                factors.append(num // i)
    factors.sort()  # Sort the factors
    return factors 

# Function to check the number and update the result button
def get_factors_result(event=None):                                                             
    try:
        # Get the number from the entry box
        number = int(entry_box.get())
        
        # Get the factors of the number
        factors = get_factors(number)
        result_button.config(text=f"Factors: {factors}", bg="lightgreen")
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
root.title("Factor Finder")
root.geometry("350x250")  # Set the window size
root.resizable(False, False)  # Disable window resizing
root.config(background="blue")

# Centering the layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Text Box (Input)
entry_box = tk.Entry(root, font=("Helvetica", 14), width=10)
entry_box.grid(row=1, column=0, sticky="e", padx=10)
# Enter Key to Trigger "Get Factors"
entry_box.bind("<Return>", get_factors_result)

# First Button - Get Factors
get_factors_button = tk.Button(root, text="Get Factors", font=("Helvetica", 12), command=get_factors_result)
get_factors_button.grid(row=1, column=1, sticky="w", padx=10)

# Second Button - Result
result_button = tk.Button(root, text="Result", font=("Helvetica", 12), bg="lightgrey", width=30)
result_button.grid(row=2, column=0, columnspan=2, pady=10)

# Reset Button - To clear fields
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_fields)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
