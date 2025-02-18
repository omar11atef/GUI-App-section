import tkinter as tk
import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_factors(num):
    factors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return sorted(factors)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def show_output(output):
    output_field.delete(0, tk.END)
    output_field.insert(0, str(output))

def button_prime():
    try:
        num = int(check_number_field.get())
        result = "Prime" if is_prime(num) else "Not Prime"
        show_output(result)
    except ValueError:
        show_output("Invalid Input")

def button_factors():
    try:
        num = int(check_number_field.get())
        result = get_factors(num)
        show_output(result)
    except ValueError:
        show_output("Invalid Input")

def button_mod1():
    try:
        m = int(check_number_field.get())
        n = int(check_number_field2.get())
        if m > 0 and n > 0:
            q = m // n
            r = m - q * n
            result = f"{m}={q}({n})+{r}"
        else:
            result = "Enter Positive Values"
        show_output(result)
    except ValueError:
        show_output("Invalid Input")

def button_mod2():
    try:
        m = int(check_number_field.get())
        n = int(check_number_field2.get())
        if m < 0 and n > 0:
            while m < 0:
                m += n
                if m == 0:
                    m += n
                    break
            result = f"Value: {m}"
        else:
            result = "Wrong"
        show_output(result)
    except ValueError:
        show_output("Invalid Input")

def button_mod3():
    try:
        m = int(check_number_field.get())
        n = int(check_number_field2.get())
        if m < 0 and n > 0:
            q = int(-m / n)
            r = -m - (q * n)
            a = n - r
            q = int((m - a) / n)
            result = f"{m}={q}({n})+{a}"
        else:
            result = "Invalid Input"
        show_output(result)
    except ValueError:
        show_output("Invalid Input")

def button_mod4():
    try:
        m = int(check_number_field.get())
        n = int(check_number_field2.get())
        if m > 0 and n > 0:
            q = m // n
            r = m - q * n
            result = f"{m}={q}({n})+{r}"
        else:
            result = "Enter Positive Values"
        show_output(result)
    except ValueError:
        show_output("Invalid Input")

def button_gsd1():
    try:
        def get_factors(num):
            factors = []
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.append(i)
                    factors.append(num // i)
            return factors

        def gcd(a, b):
            factors_a = get_factors(a)
            factors_b = get_factors(b)
            common_factors = list(set(factors_a) & set(factors_b))
            return max(common_factors)

        num1 = int(check_number_field.get())
        num2 = int(check_number_field2.get())
        result = gcd(num1, num2)
        show_output(f"GSD: {result}")
    except ValueError:
        show_output("Invalid Input")

def button_gsd2():
    try:
        def compute_GSD(a, b):
            if b == 0:
                return a
            else:
                return compute_GSD(b, a % b)

        n1 = int(check_number_field.get())
        n2 = int(check_number_field2.get())
        result = compute_GSD(n1, n2)
        show_output(f"GSD: {result}")
    except ValueError:
        show_output("Invalid Input")

def button_gsd3():
    try:
        def last_num(a, b):
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return b

        num1 = int(check_number_field.get())
        num2 = int(check_number_field2.get())
        result = last_num(num1, num2)
        show_output(f"GSD: {result}")
    except ValueError:
        show_output("Invalid Input")

def button_gsd4():
    try:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        a = int(check_number_field.get())
        b = int(check_number_field2.get())
        gcd_value = gcd(a, b)
        show_output(f"GSD: {gcd_value}")
    except ValueError:
        show_output("Invalid Input")

def button_lsm1():
    try:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        a = int(check_number_field.get())
        b = int(check_number_field2.get())
        gcd_value = gcd(a, b)
        lcm_value = lcm(a, b)
        show_output(f"GCD: {gcd_value}, LCM: {lcm_value}")
    except ValueError:
        show_output("Invalid Input")

def button_lsm2():
    try:
        def compute_LSM(a, num2):
            hight = max(a, num2)
            value = hight
            while True:
                if hight % a == 0 and hight % num2 == 0:
                    return hight
                else:
                    hight += value

        n1 = int(check_number_field.get())
        n2 = int(check_number_field2.get())
        result = compute_LSM(n1, n2)
        show_output(f"LSM: {result}")
    except ValueError:
        show_output("Invalid Input")

def create_button(window, text, row, col, command):
    button = tk.Button(window, text=text, command=command)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    return button

# Create the main window
window = tk.Tk()
window.title("Mathematics Utility")
window.geometry("300x400")

# Input fields
check_number_field = tk.Entry(window)
check_number_field2 = tk.Entry(window)
check_number_field.grid(row=0, column=1, padx=5, pady=5)
check_number_field2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(window, text="Check Number").grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text="Check Number2").grid(row=1, column=0, padx=5, pady=5)

output_field = tk.Entry(window)
output_field.grid(row=3, column=1, padx=5, pady=5)
tk.Label(window, text="Output").grid(row=3, column=0, padx=5, pady=5)

# Buttons
create_button(window, "Prime", 4, 0, button_prime)
create_button(window, "Mod1", 5, 0, button_mod1)
create_button(window, "Mod2", 6, 0, button_mod2)
create_button(window, "Mod3", 7, 0, button_mod3)
create_button(window, "Mod4", 8, 0, button_mod4)
create_button(window, "LSM1", 9, 0, button_lsm1)

create_button(window, "Factors", 4, 1, button_factors)
create_button(window, "GSD1", 5, 1, button_gsd1)
create_button(window, "GSD2", 6, 1, button_gsd2)
create_button(window, "GSD3", 7, 1, button_gsd3)
create_button(window, "GSD4", 8, 1, button_gsd4)
create_button(window, "LSM2", 9, 1, button_lsm2)

window.mainloop()
