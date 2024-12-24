#1. Write a program to demonstrate different number data types in Python. 
a=10
b=10.09
c="hello"
d=30+0j
d={"brand":"Honda"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
#--------------------------------------------------

#2. Write a program to perform different Arithmetic Operations on numbers in Python.  
a=int(input("Enter the number:"))
b=int(input("Enter the number"))

print("Addition is:-",a+b)
print("Addition is:-",a-b)
print("Addition is:-",a*b)
print("Addition is:-",a/b)
#------------------------------------------------

#3.Write a program to create, concatenate and print a string and accessing sub-string from a given string
a="Hello"
b="World"
concated_String=a+b
print("Concated String is:", concated_String)

substring=concated_String[5:]
print("Substring is",substring)
#------------------------------------------------

#4. Write a python script to print the current date in the following format “Sun May 29 02:26:23 IST 2017”  
import time
c_time=time.strftime("%a %b %d %H:%M:%S %Z %Y")
print(c_time) 
#------------------------------------------------

#5. Write a program to create, append, and remove lists in python. 6. Write a program to demonstrate working with tuples in python. 
my_list=[1,2,3,4,"Suresh"]
print("Original list",my_list)

my_list.append(5)
print("After appending",my_list)

my_list.remove(2)
print("After removing",my_list)
print(type(my_list))

print(my_list[2])

a=["cocnut" , "cheery", "banana" , " apple"]
print(a[2:5])

a[1]="Kstrwabeery"
print(a)

a.insert(1,"Samarth")
print(a)

b=["apple" , " Banana", "Cherry", "Dog"]
c=['ABCD',"EFGH","IJKL"]
b.extend(c)
print(b)
thislist=["appple", "Banana", "cherry"]
mylist=thislist.copy()
print(mylist)
#-----------------------------------------------

#6. Write a program to demonstrate working with dictionaries in python. 
student = {
    "name":"Suresh",
    "age":45,
    "course":"CSe"
}
print("orginal dict",student)

print("name",student["name"])
print("age",student["age"])

student["grade"]="a"
print("After adding",student)
#--------------------------------------------------

#7. Write a python program to find largest of three numbers.  
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
c=int(input("Enter the number:-"))

if a>b and a>c:
    print("a greater number is",a)
elif b>c and b>a:
     print("b greater number is",b)
elif c>a and c>b:
     print("c greater number is",c)
else:
    print("All are equal or zero")
#----------------------------------------------------
#8. Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [ Formula : c/5 = f-32/9 ]  
def convert_temperature(value, scale):
    if scale.lower() == 'c':
        fahrenheit = (value * 9 / 5) + 32
        return f"{value}°C = {fahrenheit}°F"
    elif scale.lower() == 'f':
        celsius = (value - 32) * 5 / 9
        return f"{value}°F = {celsius}°C"
    else:
        return "Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit."

value = float(input("Enter the temperature value: "))
scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ")
print(convert_temperature(value, scale))
#------------------------------------------------------
#9. Write a Python program to construct the following pattern, using a nested for loop 
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(2, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
#-------------------------------------------------------------
#10. Write a Python script that prints prime numbers less than 20. 
for num in range(2,20):
    is_prime=True
    for i in range(2,num):
        if num % i==0:
          is_prime=False
          break
    if is_prime:

      print(num)
#-----------------------------------------------------------------
#11. Write a python program to find factorial of a number using Recursion.  
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
num=int(input("Enter the number:"))
print(factorial(num))
#-----------------------------------------------------------------
#12. Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). 
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The triangle is a right triangle")
else:
    print("not a trianglr")
#-------------------------------------------------------------------
#13. Write a python program to define a module to find Fibonacci Numbers and import the module to another program. 
#step 1 Create the Fibonacci module (e.g., fibonacci_module.py)
# fibonacci_module.py
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while n > 0:
        fib_sequence.append(a)
        a, b = b, a + b
        n -= 1
    return fib_sequence

#step 2  Create another program to import and use the Fibonacci module (e.g., main.py)
# main.py
from fibonacci_module import fibonacci

n = int(input("Enter the number of terms for Fibonacci sequence: "))
fib_sequence = fibonacci(n)
print(f"The first {n} terms of the Fibonacci sequence are: {fib_sequence}")
#----------------------------------------------------------------
#14. Write a python program to define a module and import a specific function in that module to another program.  
#Create a module (e.g., mymodule.py)
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
#step 2:Import the function from the module into another program
# main.py
from mymodule import greet
name = input("Enter your name: ")
print(greet(name))
#------------------------------------------------------------------
#15. Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second file.  
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

try:
    with open(input_file, "r") as file1:
        content = file1.read()

    with open(output_file, "w") as file2:
        file2.write(content)

    print(f"Contents of {input_file} have been copied to {output_file}")

except FileNotFoundError:
    print(f"The file {input_file} was not found.")
#--------------------------------------
#16. Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order.  
import string
def get_unique_words(filename):

    with open(filename, 'r') as file:
        text = file.read()

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    unique_words = set(words)

    sorted_words = sorted(unique_words)

    for word in sorted_words:
        print(word)

filename = input("Enter the name of the text file: ")
get_unique_words(filename)
#-------------------------------------------
#17. Write a Python class to convert an integer to a roman numeral.  
class RomanConverter:
    def int_to_roman(self, num):
        val = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        roman = ""
        for value, symbol in val:
            while num >= value:
                roman += symbol
                num -= value
        return roman
converter = RomanConverter()
num = int(input("Enter an integer: "))
roman_numeral = converter.int_to_roman(num)
print(f"The Roman numeral for {num} is: {roman_numeral}")
#---------------------------------------
#18. Write a Python class to implement pow(x, n)  
class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def calculate(self):
        return self.x ** self.n
x = 2
n = 3
power = Power(x, n)
print(f'{x} raised to the power {n} is {power.calculate()}')

x = 2
n = -3
power = Power(x, n)
print(f'{x} raised to the power {n} is {power.calculate()}')
#------------------------------------------
#19. Write a Python class to reverse a string word by word. 
class StringReversal:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def reverse_words(self):
        return ' '.join(self.sentence.split()[::-1])

sentence = "Hello world how are you.."
reversal = StringReversal(sentence)
print(reversal.reverse_words())
#-------------------------------------
#20.   
    #a) Write a program to purposefully raise Indentation Error and correct it. 
    #b) Write a program to compute distance between two points taking input from the user (Pythagorean 
    #Theorem). 
    #c) Write a program add.py that takes 2 numbers as command line arguments and prints its sum. 
#A.
def greet():
print("Hello, World!")  
greet()
#Correct
def greet():
    print("Hello, World!") 

greet()
#B.
import math
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
#C.
import sys
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")







 

  

      
        
    



































 



