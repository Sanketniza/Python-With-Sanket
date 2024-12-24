# 41 Write a Python class to reverse a string word by word. Input string : 'hello .py' Expected Output : 
# '.py hello'
class ReverseString:
    @staticmethod
    def reverse_words(input_string):
        return ' '.join(input_string.split()[::-1])

# Example usage
input_string = 'hello .py'
output = ReverseString.reverse_words(input_string)
print(output)
# ------------------------------------------------------------------------------------

# 42 Create a list and perform the following methods 1) insert()   2) remove()
    # 4) len()   5) pop() (6) clear() 
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)  
print("After insert:", my_list)
my_list.remove(3)  
print("After remove:", my_list)
print("Length of list:", len(my_list))
popped_element = my_list.pop()  
print("Popped element:", popped_element)
print("After pop:", my_list)
my_list.clear()
print("After clear:", my_list)

# ---------------------------------------------------------------------------------------
# 43. Create a dictionary and apply the following methods                  
    #  1) Print the dictionary items                  
    #  2) access items                   
    #  3) use get()                 
    #   4)change values  
    #   5)uselen()

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Dictionary items:", my_dict)
print("Access an item (name):", my_dict['name'])
print("Using get() (age):", my_dict.get('age'))
my_dict['city'] = 'Los Angeles'
print("After changing value (city):", my_dict)
print("Length of dictionary:", len(my_dict))
# -----------------------------------------------------------------------------------------

# 44. Create a tuple and perform the following methods  
    # 1) Add items   2)len() 3)check for item in tuple  4)Acess items

my_tuple = (1, 2, 3, 4)
my_tuple += (5,)
print("After adding items:", my_tuple)
print("Length of tuple:", len(my_tuple))
print("Is 3 in tuple?", 3 in my_tuple)
print("Access item at index 2:", my_tuple[2])
# -------------------------------------------------------------------------------------------
# 45
# a) Write a python program to add two numbers.                         
# b) Write a python program to print a number is positive/negative using if-else. 
# c) Write a python program to find largest number among three numbers. 
# d) Write a python Program to read a number and display corresponding day using if_elif_else? 

# a) Add two numbers
num1, num2 = 5, 10
print("Sum:", num1 + num2)

# b) Check if a number is positive or negative
num = -3
if num >= 0:
    print("Positive")
else:
    print("Negative")

# c) Find the largest among three numbers
a, b, c = 10, 20, 15
if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)
day_num = 3
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid day number")
# ---------------------------------------------------------------------------------------

# 46. Write a program to create a menu with the following options 
# 1. TO PERFORM ADDITITON  
# 2. TO PERFORM SUBTRACTION  
# 3. TO PERFORM MULTIPICATION  
# 4. TO PERFORM DIVISION  
# Accepts users input and perform the operation accordingly. Use functions with arguments.

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def menu():
    print("1. TO PERFORM ADDITION")
    print("2. TO PERFORM SUBTRACTION")
    print("3. TO PERFORM MULTIPLICATION")
    print("4. TO PERFORM DIVISION")

menu()
choice = int(input("Enter your choice (1-4): "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result:", addition(a, b))
elif choice == 2:
    print("Result:", subtraction(a, b))
elif choice == 3:
    print("Result:", multiplication(a, b))
elif choice == 4:
    print("Result:", division(a, b))
else:
    print("Invalid choice")
# ---------------------------------------------------------------------------------------------

# 47.   
# a) Write a python program to check whether the given string is palindrome or not. 
# b) Write a python program to find factorial of a given number using functions. 
# c) Write a Python function that takes two lists and returns True if they are equal otherwise false. 
# d) Write a program to double a given number and add two numbers using lambda()?

# a) Check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

string = "madam"
print("Palindrome:" if is_palindrome(string) else "Not a palindrome")

# b) Find factorial using functions
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = 5
print("Factorial:", factorial(num))

# c) Check if two lists are equal
def are_lists_equal(list1, list2):
    return list1 == list2

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("Lists are equal:" if are_lists_equal(list1, list2) else "Lists are not equal")

# d) Double a number and add two numbers using lambda
double = lambda x: x * 2
add = lambda x, y: x + y

num1 = 4
num2 = 5
print("Double:", double(num1))
print("Sum:", add(num1, num2))
# ------------------------------------------------------------------------------------------
# 48
# a) Write a python program to open and write “hello world” into a file? 
# b) Write a python program to write the content “hi python programming” for the existing file. 

# a) Write "hello world" into a file
with open("file.txt", "w") as file:
    file.write("hello world")

# b) Write "hi python programming" into the existing file
with open("file.txt", "a") as file:
    file.write("\nhi python programming")
# -------------------------------------------------------------------------------------------------

#  49
# a) Write a python program to get python version. 
# b) Write a python program to open a file and check what are the access permissions acquired by that 
# file using os module? 
# c) Write a python program to display a particular month of a year using calendar module. 
# d) Write a python program to print all the months of given year


# a) Get Python version
import sys
print("Python version:", sys.version)

# b) Check file access permissions using the os module
import os
file_path = "file.txt"
if os.path.exists(file_path):
    print("File exists")
    print("Readable:", os.access(file_path, os.R_OK))
    print("Writable:", os.access(file_path, os.W_OK))
    print("Executable:", os.access(file_path, os.X_OK))
else:
    print("File does not exist")

# c) Display a particular month of a year using the calendar module
import calendar
year = 2024
month = 2
print(calendar.month(year, month))

# d) Print all months of a given year
print(calendar.TextCalendar().formatyear(year))
# ------------------------------------------------------------------------------

# 50
# a) Write a python program to print date, time for today and now. 
# b) Write a python program to add some days to your present date and print the date added. 
# c) Write a python program to print date, time using date and time functions. 
# d) Write a python program which accepts the radius of a circle from user and computes the area  
# (use math module). 


# a) Print date and time for today and now
from datetime import datetime
now = datetime.now()
print("Today:", now.strftime("%Y-%m-%d"))
print("Current time:", now.strftime("%H:%M:%S"))

# b) Add some days to the present date and print the new date
from datetime import timedelta
days_to_add = 5
new_date = now + timedelta(days=days_to_add)
print("New date after adding days:", new_date.strftime("%Y-%m-%d"))

# c) Print date and time using date and time functions
print("Current date:", now.date())
print("Current time:", now.time())

# d) Compute the area of a circle using math module
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print("Area of the circle:", area)
# ------------------------------------------------------------------------------------

# 53
# a) Write a python program to concatenate the dataframes with two different objects. 
# b) Write a python code to read a csv file using pandas module and print the first and last five lines  
# of a file. 
# suggestion install pandas
import pandas as pd
# Create two dataframes
data1 = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
data2 = {'Name': ['Charlie', 'David'], 'Age': [35, 40]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# Concatenate the dataframes
df_concatenated = pd.concat([df1, df2], ignore_index=True)
print(df_concatenated)

import pandas as pd
# Read the CSV file
df = pd.read_csv('file.csv')
# Print the first and last five rows
print("First five rows:")
print(df.head())
print("\nLast five rows:")
print(df.tail())
# --------------------------------------------------------------------------------

# 54.Write Python program to perform following operations on Lists: a) Create list b) Access list  c) Update 
# list (Add item, Remove item) d) Delete list. 

my_list = [1, 2, 3, 4, 5]
print("Created list:", my_list)
print("Access item at index 2:", my_list[2])
my_list.append(6)
print("List after adding item:", my_list)
my_list.remove(3)
print("List after removing item 3:", my_list)
del my_list
print("List deleted successfully")
# -----------------------------------------------------------------------------------------

# 55. Write a program in Python to demonstrate following operations:

# a) Method overloading
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
calc = Calculator()
print("Sum of 2 numbers:", calc.add(10, 20)) 
print("Sum of 3 numbers:", calc.add(10, 20, 30)) 

#  b) Method  overriding. 
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
animal = Animal()
dog = Dog()
animal.sound() 
dog.sound()     
# ----------------------------------------------------------------------------------

# 56. Write a program in Python to demonstrate following operations: a) Simple inheritance b) Multiple 
# inheritance. 
# a)simple inheritance
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
dog = Dog()
dog.speak()  
dog.bark()  

# b) Multiple inheritance. 

class Animal:
    def speak(self):
        print("Animal speaks")
class Bird:
    def fly(self):
        print("Bird flies")
class Eagle(Animal, Bird):
    def hunt(self):
        print("Eagle hunts")
eagle = Eagle()
eagle.speak()  #
eagle.fly()    
eagle.hunt()  



# --------------------------------------------------------------------------------------

# 57. Write a program to compute distance between two points taking input from the user Write a program 
# add.py that takes 2 numbers as command line arguments and prints its sum. 

import math
x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance between the points:", distance)

import sys
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
sum_result = num1 + num2
print("Sum:", sum_result)

# --------------------------------------------------------------------------------------

# 58. Write a Program for checking whether the given number is an even number or not. Using a for loop. 
number = int(input("Enter a number: "))
for i in range(1):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is not an even number.")

# ---------------------------------------------------------------------------------------------------
# 59. Write a program to count the numbers of characters in the string and store them in a dictionary data 
# structure Write a program to use split and join methods in the string and trace a birthday of a person with 
# a dictionary data structure. 

input_string = input("Enter a string: ")
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Character count:", char_count)

birthday_str = input("Enter the birthday (dd-mm-yyyy): ")
birthday_parts = birthday_str.split('-')
birthday_dict = {
    "Day": birthday_parts[0],
    "Month": birthday_parts[1],
    "Year": birthday_parts[2]
}
print("Birthday Information:", birthday_dict)
birthday_reconstructed = '-'.join(birthday_parts)
print("Reconstructed Birthday:", birthday_reconstructed)

# --------------------------------------------------------------------------------
#60 Function to print each line of a file in reverse order
def print_lines_reverse(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print("\nLines in reverse order:")
            for line in reversed(lines):
                print(line.strip())  
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
def compute_file_stats(file_name):
    try:
        with open(file_name, 'r') as file:
            num_lines = 0
            num_words = 0
            num_chars = 0
            for line in file:
                num_lines += 1
                num_chars += len(line)  
                num_words += len(line.split())  
            print(f"\nNumber of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
file_name = input("Enter the file name: ")
print_lines_reverse(file_name)

compute_file_stats(file_name)
#----------------------------------------------------------------------------------------------------
