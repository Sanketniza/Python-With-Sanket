
#  This tell the version of py
import sys
print(sys.version)
print("--------------------------------------------")

# Hello World
print("Hello World")

# Python Indentation
if 5 > 2:
    print("Hello")

# this code will not run, because the indentation is wrong
""" if 5 > 2:
print("Five is greater than two!") """

#* py variable
x = 5
print(x)
y = "kya baat hai , bole to kya baat "
print(y , "chuu be")
print("--------------------------------------------")

#* Variables
# ? Variables are containers for storing data values.
# ? Variables do not need to be declared with any particular type, and can even change type after they have been set.

a = 5  # int
b = 5.0  # float
c = "Hello"  # string
d = True  # boolean
e = None  # None
f = type(a )  # type
print("kya baat hai : ",a)
print("kya baat hai : ",b)
print("kya baat hai : ",c)
print("kya baat hai : ",d)
print("kya baat hai : ",e)
print("kya baat hai : ",f)
print("--------------------------------------------")

#* Casting
# -> If you want to declered a variable with a specific data type , you can use the casting operator.

a = int(3)
b =float(3.0)
c = str(3)
d = bool(3)
print("values :" , a , b , c , d)
print("--------------------------------------------")

#* Geting the type of a variable
# -> You can use the type() function to get the type of a variable.
type(a) 
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("--------------------------------------------")

#* Single or Double Quotes?
# ^String variables can be declared either by using single or double quotes:

s1 = 'single quotes'
s2 = "double quotes"
print(s1)
print(s2)
print("--------------------------------------------")

# Case Sensitivity
# -> Python is case sensitive.
# -> You can use either upper or lower case letters to declare a variable.

name = "sanket"
Name = "sanket" #Name will not overwrite a
Aa = "sanket"
print(name)
print(Name)
print(Aa)
print("--------------------------------------------")

#* python variable
#^ A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

myvar = "John"
my_var = "John"
_my_var = "John"
print(_my_var)
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print("--------------------------------------------")

# * multi word variable name 

# ^ camel case
myVariable = "John"
# ^ snake case
my_variable = "John"
# ^ Pascal case
MyVariable = "John"
print("--------------------------------------------")

#* many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)  #output: Orange
print(y)  #output: Banana
print(z)  #output: Cherry  

x = y = z = "Orange"
print(x) #output: Orange
print(y) #output: Orange
print(z) #output: Orange
print("--------------------------------------------")


#* Unpack a Collection
# -> If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0]) #output: Apple
print(fruits[1]) #output: Banana
print(fruits[2] , "\n") #output: Cherry

x, y, z = fruits
print(x) 
print(y)
print(z)
print("--------------------------------------------")

#* Python - Output Variables

a = 5
print(a , "\n")

b = 333
print(b , a , "\n")
print(a + b )

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# print(a + x)  #error
print("--------------------------------------------")

#* Global Variables
# -> Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

x = "sanket"
def name(): 
    print(x)

name()
print("\n")

def print_x():
    global x
    print(x)
print_x()

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print("--------------------------------------------")

# function with default parameters

def greeting(): 
    print("Hello, World!")
    
greeting()  # Output: Hello, World!
print('\n')
print("-------------------------------------------------------")

def greeting(name="World"):
    print(f"Hello, {name}!")

greeting()  # Output: Hello, World!
print('\n')
print("-------------------------------------------------------")

def greeting(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")

greeting("Alice")  # Output: Hello, Alice! You are 30 years old.
print('\n')
print("-------------------------------------------------------")

def greeting(name, age=30, city="New York"):
    print(f"Hello, {name}! You are {age} years old and from {city}.")

greeting("Bob", age=25)  # Output: Hello, Bob! You are 25 years old and from New York.
print('\n')
print("-------------------------------------------------------")

# function with variable-length arguments

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print('\n')
print("-------------------------------------------------------")

def print_info(name, age, **kwargs):
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="New York", country="USA")
# Output:
# Name: Bob, Age: 30
# city: New York
# country: USA
print('\n')
print("-------------------------------------------------------")

# function with a generator

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up_to(5):
    print(number)  # Output: 1 2 3 4 5
    print('\n')
print("-------------------------------------------------------")