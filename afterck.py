import tkinter as tk
from tkinter import messagebox
import math

# Prime Checker Function
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Combined Prime Check and Factor Calculation
def check_number2():
    try:
        m = int(entry_prime.get())  # Get input from "ENTER Check Number"
        
        # Check if the number is prime
        if is_prime(m):
            prime_result = "Prime"
        else:
            prime_result = "Not Prime"
        
        # Update the result in the "OUTPUT / RESULT" field
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"{prime_result}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

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

# Adjusted function to handle both Prime Check and Factorization
def check_number():
    try:
        m = int(entry_prime.get())  # Get input from "ENTER Check Number"
        
        # Calculate factors
        factors = get_factors (m)
        
        # Update the result in the "OUTPUT / RESULT" field
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"Factors: {factors}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")



# Modulus Calculation with Quotient and Remainder
def calculate_modulus(event=None):  # Add event parameter to handle Enter key
    """Calculates q (quotient) and r (remainder), and handles errors for negative m."""
    global m, n, q, r
    try:
        # Get values for m and n from the entry fields
        m = int(entry_first.get())
        n = int(entry_second.get())

        # Validate values
        if m < 0:
            raise ValueError("m cannot be negative. Enter a positive value for m.")
        if n <= 0:
            raise ValueError("n must be greater than 0.")

        # Calculate quotient (q) and remainder (r)
        q = m // n
        r = m - q * n

        # Update the result field
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"{m} = {q}({n}) + {r}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")

def calculate_mod_method(method):
    try:
        m = int(entry_first.get())
        n = int(entry_second.get())
        
        # Check if m is positive and show error if so
        
        if method == "method1":
            #Calculating modulus for negative m by : m+n
            result = m
            if m < 0:
                while result < 0:
                    result += n
                if result == 0:  # Special condition to handle exact multiples
                    result += n
                
                    
        elif method == "method2":
            # Updated logic for method2: By rneg= n - rnag
            result = m
            if m < 0:
                q = int(-m / n)
                r = -m - (q * n)
                a = n - r
                q = int((m - a) / n)
                result = f"{m} = {q}({n}) + {a}"
        
        elif method == "method3":
            # By : m = -q*n+r
            q = -(m // n)
            r = m + q * n
            result = r
            

        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

        


# GCD Calculation
def calculate_gcd(method):
    try:
        m = int(entry_first.get())
        n = int(entry_second.get())

        if method == "gcd1":
            while n:
                m, n = n, m % n
        elif method == "gcd2":
            # Function to compute GCD using the prime factors method
            def get_factors(num):
                factors = []
                for i in range(1, int(num**0.5) + 1):
                    if num % i == 0:
                        factors.append(i)
                        if i != num // i:  # To avoid adding square roots twice
                            factors.append(num // i)
                return factors

            def gcd(a, b):
                # Get the factors of both numbers
                factors_a = get_factors(a)
                factors_b = get_factors(b)

                # Find the common factors
                common_factors = list(set(factors_a) & set(factors_b))

                # Return the greatest common factor
                return max(common_factors)

            m = gcd(m, n)
            

        elif method == "gcd3":
            # Function to compute GCD using the Successive Difference method
            def last_num(a, b):
                while a != b:
                    if a > b:
                        a = a - b
                    else:
                        b = b - a
                return b

            m = last_num(m, n)

        elif method == "gcd4":
            # Function to compute GCD using a Algorithm 
            def compute_GCD(a, b):
                if b == 0:
                    return a
                else:
                    return compute_GCD(b, a % b)

            m = compute_GCD(m, n)

        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"GCD: {m}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

# LCM Calculation
def calculate_lcm(method):
    try:
        m = int(entry_first.get())
        n = int(entry_second.get())

        if method == "lcm1":
            # Function to compute GCD using the Euclidean Algorithm
            def gcd(a, b):
                while b != 0:
                    a, b = b, a % b
                return a

            # Function to compute LCM using the formula: LCM = (a * b) / GCD(a, b)
            def lcm(a, b):
                return abs(a * b) // gcd(a, b)

            lcm_value = lcm(m, n)
            

        elif method == "lcm2":
            # Function to compute LCM (Least Common Multiple) using the 'Tree' method
            def compute_LSM(a, b):
                if b > a:
                    hight = a
                else:
                    hight = b
                value = hight  # To calculate the next index
                while True:
                    if hight % a == 0 and hight % b == 0:
                        return hight
                    else:
                        hight = hight + value  # Go to the next index

            lcm_value = compute_LSM(m, n)
            

        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"LCM is: {lcm_value}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

# Tkinter GUI Design
root = tk.Tk()
root.title("Math Operations")
root.geometry("900x600")
root.config(bg="#425cbd")

# Input Fields
tk.Label(root, text="Enter Check Number", fg="red", font=("Arial", 12)).place(x=550, y=50)
entry_prime = tk.Entry(root, font=("Arial", 14), width=10)
entry_prime.place(x=550, y=80)

tk.Label(root, text="Enter First Number", fg="black", font=("Arial", 12)).place(x=550, y=150)
entry_first = tk.Entry(root, font=("Arial", 14), width=10)
entry_first.place(x=550, y=180)

tk.Label(root, text="Enter Second Number", fg="black", font=("Arial", 12)).place(x=550, y=250)
entry_second = tk.Entry(root, font=("Arial", 14), width=10)
entry_second.place(x=550, y=280)

tk.Label(root, text="OUTPUT / RESULT", fg="black", font=("Arial", 12)).place(x=550, y=350)
result_entry = tk.Entry(root, font=("Arial", 14), width=15 )
result_entry.place(x=550, y=380)

# Buttons
buttons = [
    ("Check Number", check_number2),
    ("factors", check_number),
    ("pos mod", calculate_modulus),
    ("neg mod1", lambda: calculate_mod_method("method1")),
    ("neg mod2", lambda: calculate_mod_method("method2")),
    ("neg mod3", lambda: calculate_mod_method("method3")),
    ("GCD1", lambda: calculate_gcd("gcd1")),
    ("GCD2", lambda: calculate_gcd("gcd2")),
    ("GCD3", lambda: calculate_gcd("gcd3")),
    ("GCD4", lambda: calculate_gcd("gcd4")),
    ("LCM1", lambda: calculate_lcm("lcm1")),
    ("LCM2", lambda: calculate_lcm("lcm2")),
]

# Render Buttons
for i, (text, command) in enumerate(buttons):
    tk.Button(root, text=text, bg="yellow", font=("Arial", 10), width=15, command=command).place(x=50, y=50 + i * 40)

root.mainloop()
