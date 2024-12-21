# 1. Write a program to demonstrate different number data types in Python.


# Integer
integer_num = 10
print("Integer:", integer_num)

# Float
float_num = 10.5
print("Float:", float_num)

# Complex
complex_num = 3 + 5j
print("Complex:", complex_num)

# Type checking
print("Type of integer_num:", type(integer_num))
print("Type of float_num:", type(float_num))
print("Type of complex_num:", type(complex_num))

# -----------------------------------------------------------------------------------

# 2. Write a program to perform different Arithmetic Operations on numbers in Python.

# Input numbers
num1 = 20
num2 = 10

# Arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # Floating-point division
floor_division = num1 // num2  # Integer division
modulus = num1 % num2
exponentiation = num1 ** num2

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

# -----------------------------------------------------------------------------------

# 3. Write a program to create, concatenate and print a string and accessing sub-string from a given string.

# Creating a string
my_string = "Hello, World!"

# Concatenating strings
concatenated_string = my_string + " Welcome to the Python programming language."

# Accessing a sub-string
sub_string = my_string[0:5]

# Printing the results
print("Original String:", my_string)
print("Concatenated String:", concatenated_string)
print("Sub-string:", sub_string)

# -----------------------------------------------------------------------------------

# 4. Write a python script to print the current date in the following format “Sun May 29 02:26:23 IST 2017”

import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time
formatted_datetime = current_datetime.strftime("%a %b %d %H:%M:%S %Z %Y")

# Print the formatted date and time
print("Current Date and Time:", formatted_datetime)

# -----------------------------------------------------------------------------------

# 5. Write a program to create, append, and remove lists in python.

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Appending an element to the list
my_list.append(6)

# Removing an element from the list
my_list.remove(3)

# Printing the list
print("List:", my_list)

# -----------------------------------------------------------------------------------

# 6. Write a program to demonstrate working with tuples in python.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Printing the tuple
print("Tuple:", my_tuple)

# -----------------------------------------------------------------------------------

# 6. Write a program to demonstrate working with dictionaries in python.

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Printing the dictionary
print("Dictionary:", my_dict)

# -----------------------------------------------------------------------------------

# 7. Write a python program to find largest of three numbers.

# Input numbers
num1 = 10
num2 = 20
num3 = 30

# Finding the largest number
largest_num = max(num1, num2, num3)

# Printing the result
print("Largest number:", largest_num)

# -----------------------------------------------------------------------------------

# 8. Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [ Formula : c/5 = f-32/9 ]

# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the result
print(f"{celsius}°C is equivalent to {fahrenheit}°F")

# -----------------------------------------------------------------------------------
# 9. Write a Python program to construct the following pattern, using a nested for loop
# *
# * *
# * * *
# * * * *
# * * * * *
# ** *
# **
# *

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# -----------------------------------------------------------------------------------
# 10. Write a Python script that prints prime numbers less than 20  

for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# -----------------------------------------------------------------------------------
# 11. Write a python program to find factorial of a number using Recursion  

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# -----------------------------------------------------------------------------------

# 12. Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides).

# Input lengths of the sides of triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if the triangle is a right triangle
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")

# -----------------------------------------------------------------------------------
# 13. Write a python program to define a module to find Fibonacci Numbers and import the module to another program.


# fibonacci_module.py

# Step 1: Create a Module (fibonacci_module.py)
""" def fibonacci(n):
   Generate a Fibonacci sequence up to n
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# main_program.py
# Step 2: Main Program to Import the Module (main_program.py)
# Import the Fibonacci module
import modules.fibonacci_module  # Adjust the path accordingly

# Get input from the user
n = int(input("Enter a number to generate Fibonacci sequence up to: "))

# Call the fibonacci function from the module
fib_sequence = modules.fibonacci_module.fibonacci(n)

# Display the Fibonacci sequence
print(f"Fibonacci sequence up to {n}: {fib_sequence}") """


# ---------------------------------------------------------------------------

# 14. Write a python program to define a module and import a specific function in that module to another program.

print("14 -----------------------------------")
# Import the specific function from the module
from math_operations import add

# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Use the imported function
result = add(num1, num2)

# Display the result
print(f"The sum of {num1} and {num2} is: {result}")

# ---------------------------------------------------------------------------
# 15. Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second file.

print("15 -----------------------------------")
# copyfile.py

# Prompt user for file names
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

try:
    # Open the source file and read its contents
    with open(input.txt, 'r') as src:
        content = src.read()
    
    # Write the content to the destination file
    with open(output.txt, 'w') as dest:
        dest.write(content)
    
    print(f"Contents of '{input.txt}' have been copied to '{output.txt}'.")
except FileNotFoundError:
    print(f"Error: '{input.txt}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# ---------------------------------------------------------------------------   
