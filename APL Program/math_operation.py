import tkinter as tk
from tkinter import messagebox
import re

# Function to check the email validity
def check_valid_email():
    email = entry_email.get()
    
    # Regular expression to validate email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        messagebox.showinfo("Valid", "The email ID is valid.")
    else:
        messagebox.showerror("Invalid", "The email ID is invalid. Please enter a valid email address.")

# Create the main window
root = tk.Tk()
root.title("Email ID Validator")

# Create and place the widgets
label_email = tk.Label(root, text="Enter email ID:")
label_email.grid(row=0, column=0, padx=10, pady=10)

entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=10)

# Button to validate the email ID
button_validate = tk.Button(root, text="Validate", command=check_valid_email)
button_validate.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
