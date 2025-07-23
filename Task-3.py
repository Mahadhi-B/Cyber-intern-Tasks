import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()
    strength = 0
    criteria = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        criteria.append("Password length is less than 8 characters")

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        criteria.append("No uppercase letter")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        criteria.append("No lowercase letter")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        criteria.append("No number")

    # Check for special characters
    if re.search(r'[@$!%*?&#]', password):
        strength += 1
    else:
        criteria.append("No special character")

    # Assessing strength
    if strength == 5:
        result = "Strong Password"
    elif 3 <= strength < 5:
        result = "Moderate Password"
    else:
        result = "Weak Password"

    messagebox.showinfo("Password Strength", f"{result}\n\nIssues:\n" + "\n".join(criteria))


# Tkinter GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show='*', width=30)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

root.mainloop()