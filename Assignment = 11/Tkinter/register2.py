import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x500")

fields = ["Name", "Email", "Password"]
entries = {}

# Create input fields for Name, Email, and Password
for i, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=i, column=0, padx=10, pady=5)
    entries[field] = tk.Entry(root, show="*" if field == "Password" else None)
    entries[field].grid(row=i, column=1)

# Function to validate the name (only alphabets)
def is_valid_name(name):
    return name.isalpha()

# Function to validate the email (must be in the format user@gmail.com)
def is_valid_email(email):
    # Validate if email has the format "username@gmail.com"
    email_regex = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(email_regex, email))

# Function to validate the password (at least 8 characters, 1 uppercase, 1 lowercase, 1 number, 1 special char)
def is_valid_password(password):
    if len(password) >= 8:
        if (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in password)):
            return True
    return False

# Register function to validate inputs and show appropriate messages
def register():
    name = entries["Name"].get()
    email = entries["Email"].get()
    password = entries["Password"].get()

    # Validate Name
    if not is_valid_name(name):
        messagebox.showwarning("Invalid Name", "Name must contain only alphabets.")
        return

    # Validate Email
    if not is_valid_email(email):
        messagebox.showwarning("Invalid Email", "Please enter a valid email address in the format: username@gmail.com.")
        return

    # Validate Password
    if not is_valid_password(password):
        messagebox.showwarning("Invalid Password", 
                               "Password must be at least 8 characters long and contain an uppercase letter, lowercase letter, number, and special character.")
        return
    
    # If all validations pass, show success message
    messagebox.showinfo("Success", "Registration Successful!")

# Register Button
tk.Button(root, text="Register", command=register).grid(row=3, columnspan=2, pady=10)

root.mainloop()
