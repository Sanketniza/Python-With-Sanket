
# 61. Write function to compute gcd, lcm of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(12, 18))
print(lcm(12, 18))

# ---------------------------------------------------------------------------------------------

# 62. Write a program to implement Merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(arr))

# ---------------------------------------------------------------------------------------------

# 63. Write a program to implement Selection sort.

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))

# ---------------------------------------------------------------------------------------------

# 64. Write a program to implement Insertion sort.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([12, 11, 13, 5, 6]))

# ---------------------------------------------------------------------------------------------

""" 
65.
a) Write a Pandas program to convert a dictionary to a Pandas series.
b) Write a Pandas program to convert the first column of a DataFrame as a Series.
c) Write a Pandas program to convert a given Series to an array.
d) Write a Pandas program to sort a given Series """

import pandas as pd

# Dictionary
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

# Convert to Pandas Series
series = pd.Series(data)

print("Pandas Series from Dictionary:")
print(series)

# ===========
import pandas as pd

# Create a DataFrame
data = {'Column1': [10, 20, 30, 40], 'Column2': [50, 60, 70, 80]}
df = pd.DataFrame(data)

# Convert the first column to a Series
series_from_column = df['Column1']

print("Series from the first column of DataFrame:")
print(series_from_column)

# ===========

import pandas as pd

# Create a Series
series = pd.Series([1, 2, 3, 4, 5])

# Convert to an array
array = series.to_numpy()

print("Array from Series:")
print(array)

# ===========

import pandas as pd

# Create a Series
series = pd.Series([50, 20, 30, 10, 40])

# Sort the Series
sorted_series = series.sort_values()

print("Sorted Series:")
print(sorted_series)

# ----------------------------------------------------------------------------------

""" 66. Write a Python programming to display a bar chart of the popularity of programming
Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 """

import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create the bar chart
plt.bar(languages, popularity, color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])

# Add titles and labels
plt.title("Popularity of Programming Languages")
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")

# Show the plot
plt.show()

# ----------------------------------------------------------------------------------

""" 67. Write a Python programming to display a horizontal bar chart of the popularity of
programming Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 """

import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create the horizontal bar chart
plt.barh(languages, popularity, color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])

# Add titles and labels
plt.title("Popularity of Programming Languages")
plt.xlabel("Popularity (%)")
plt.ylabel("Programming Languages")

# Show the plot
plt.show()

# ----------------------------------------------------------------------------------

""" 68. Write a Python program to create bar plot of scores by group and gender. Use multiple X
values on the same chart for men and women.
Sample Data:
Means (men) = (22, 30, 35, 35, 26)
Means (women) = (25, 32, 30, 35, 29) """

import matplotlib.pyplot as plt
import numpy as np

# Sample data
groups = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Define the positions for the bars
x = np.arange(len(groups))  # Group positions
width = 0.35  # Width of the bars

# Create the bar plot
plt.bar(x - width/2, means_men, width, label='Men', color='blue')
plt.bar(x + width/2, means_women, width, label='Women', color='orange')

# Add titles and labels
plt.title("Scores by Group and Gender")
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.xticks(x, groups)  # Set group names as x-ticks
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------------------

""" 
69. Write a Python programming to create a pie chart of the popularity of programming
Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 """

import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create the pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=140, colors=['blue', 'orange', 'green', 'red', 'purple', 'brown'])

# Add title
plt.title("Popularity of Programming Languages")

# Display the chart
plt.show()

# ----------------------------------------------------------------------------------

""" 70. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics
and Science. Use marks of 10 students.
Sample data:
Test Data:
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] """

import matplotlib.pyplot as plt

# Sample data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create the scatter plot
plt.scatter(math_marks, science_marks, color='blue', label='Marks')

# Add labels and title
plt.title("Comparison of Mathematics and Science Marks")
plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")
plt.xticks(marks_range)
plt.yticks(marks_range)

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)  # Add grid for better readability
plt.show()

# ----------------------------------------------------------------------------------

# 71. Write a Python NLTK program to split the text sentence/paragraph into a list of words

import nltk
from nltk.tokenize import word_tokenize

# Ensure the NLTK tokenizer data is downloaded (only required once)
nltk.download('punkt')

# Sample text
text = "Natural Language Processing with Python is interesting. Let's tokenize this text!"

# Tokenize the text into words
words = word_tokenize(text)

# Print the list of words
print("List of words:", words)

# ----------------------------------------------------------------------------------

# 72. Write a Python NLTK program to tokenize words, sentence wise.

import nltk
from nltk.tokenize import sent_tokenize

# Ensure the NLTK tokenizer data is downloaded (only required once)
nltk.download('punkt')

# Sample text
text = "Natural Language Processing with Python is interesting. Let's tokenize this text!"

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Print the list of sentences
print("List of sentences:", sentences)  

# ----------------------------------------------------------------------------------

# 73. Write a Python program to plot two or more lines on same plot with suitable legends of each line

import matplotlib.pyplot as plt

# Data for the lines
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]  # Line 1 (y = x^2)
y2 = [1, 2, 3, 4, 5]    # Line 2 (y = x)
y3 = [25, 16, 9, 4, 1]  # Line 3 (y = reverse of x^2)

# Plot the lines
plt.plot(x, y1, label='y = x^2', color='blue', linestyle='-')
plt.plot(x, y2, label='y = x', color='red', linestyle='--')
plt.plot(x, y3, label='y = reverse(x^2)', color='green', linestyle='-.')

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines on the Same Plot")

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)  # Add a grid for better readability
plt.show()

# ----------------------------------------------------------------------------------

# 74. Write a program to create registration page for student management system.

import tkinter as tk
from tkinter import messagebox
import re

# Define a class for Student
class Student:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

# Function to validate phone number
def is_valid_phone(phone):
    # Check if the phone number is exactly 10 digits and starts with a number > 7
    return bool(re.match(r"^[8-9][0-9]{9}$", phone))

# Function to validate email
def is_valid_email(email):
    # Check if the email ends with '@gmail.com'
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email))

# Function to register a student
def register_student():
    # Get the input data from the user
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()

    # Validate the email and phone number
    if not is_valid_email(email):
        messagebox.showwarning("Input Error", "Email must be a valid Gmail address!")
        return
    if not is_valid_phone(phone):
        messagebox.showwarning("Input Error", "Phone number must be exactly 10 digits and start with a number greater than 7!")
        return

    if name and email and phone:
        student = Student(name, email, phone)
        
        # Save student data to a file
        with open("students.txt", "a") as file:
            file.write(f"{student.name}, {student.email}, {student.phone}\n")
        
        messagebox.showinfo("Success", f"Student {student.name} has been successfully registered!")
        # Clear the input fields
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to display all registered students
def display_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if not students:
                messagebox.showinfo("No Students", "No students registered yet.")
            else:
                student_list = "\n".join([student.strip() for student in students])
                messagebox.showinfo("Registered Students", student_list)
    except FileNotFoundError:
        messagebox.showinfo("No Students", "No students have been registered yet.")

# Create main window
root = tk.Tk()
root.title("Student Registration System")
root.geometry("400x300")

# Create labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)

entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)

entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

label_phone = tk.Label(root, text="Phone:")
label_phone.pack(pady=5)

entry_phone = tk.Entry(root, width=30)
entry_phone.pack(pady=5)

# Create Register and Display buttons
button_register = tk.Button(root, text="Register Student", width=20, command=register_student)
button_register.pack(pady=10)

button_display = tk.Button(root, text="Display Registered Students", width=20, command=display_students)
button_display.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# ----------------------------------------------------------------------------------


# 75. Write a program to create calculator which perform basic arithmetic operations.

import tkinter as tk
from tkinter import messagebox

# Function to handle button click events
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, current + value)  # Add the button value to the entry field

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, str(result))  # Display the result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")  # Show error for invalid input

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for displaying the input/output
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button labels and create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create buttons dynamically and place them in the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=evaluate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: click_button(t))
    button.grid(row=row, column=col)

# Create clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the Tkinter event loop
root.mainloop()

# ----------------------------------------------------------------------------------

#  76. Write a program to create login page using Django.

# ----------------------------------------------------------------------------------

# 77. Write a program to display name and set the background color of web page using Django

# ----------------------------------------------------------------------------------

# 78.78. Create a GUI for performing basic arithmetic operations on two numbers

import tkinter as tk
from tkinter import messagebox

# Function to perform arithmetic operations
def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation.get() == "Add":
            result = num1 + num2
        elif operation.get() == "Subtract":
            result = num1 - num2
        elif operation.get() == "Multiply":
            result = num1 * num2
        elif operation.get() == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Radio buttons for operation selection
operation = tk.StringVar()
operation.set("Add")  # Default operation

radio_add = tk.Radiobutton(root, text="Add", variable=operation, value="Add")
radio_add.grid(row=2, column=0, padx=10, pady=10)

radio_subtract = tk.Radiobutton(root, text="Subtract", variable=operation, value="Subtract")
radio_subtract.grid(row=2, column=1, padx=10, pady=10)

radio_multiply = tk.Radiobutton(root, text="Multiply", variable=operation, value="Multiply")
radio_multiply.grid(row=3, column=0, padx=10, pady=10)

radio_divide = tk.Radiobutton(root, text="Divide", variable=operation, value="Divide")
radio_divide.grid(row=3, column=1, padx=10, pady=10)

# Button to perform the operation
button_calculate = tk.Button(root, text="Calculate", command=perform_operation)
button_calculate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()


# ----------------------------------------------------------------------------------

# 79. Create a GUI for checking the valid mobile number using regular expression. Accept mobile number from the user

import tkinter as tk
from tkinter import messagebox
import re

# Function to check the mobile number validity
def check_valid_mobile():
    mobile_number = entry_mobile.get()
    
    # Regular expression to validate mobile number
    pattern = r'^[789]\d{9}$'
    
    if re.match(pattern, mobile_number):
        messagebox.showinfo("Valid", "The mobile number is valid.")
    else:
        messagebox.showerror("Invalid", "The mobile number is invalid. It should start with 7, 8, or 9 and contain 10 digits.")

# Create the main window
root = tk.Tk()
root.title("Mobile Number Validator")

# Create and place the widgets
label_mobile = tk.Label(root, text="Enter mobile number:")
label_mobile.grid(row=0, column=0, padx=10, pady=10)

entry_mobile = tk.Entry(root)
entry_mobile.grid(row=0, column=1, padx=10, pady=10)

# Button to validate the mobile number
button_validate = tk.Button(root, text="Validate", command=check_valid_mobile)
button_validate.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()

# ----------------------------------------------------------------------------------

# 80. Create a GUI for validating email id. Accept email id from the user.


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

# ----------------------------------------------------------------------------------

