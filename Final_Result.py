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
concated_String = a+b

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

for i in range(5, 0, -1):
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

-------------------------------------------------------------------------------------------------------

#21. 
    #a) Write a Program for checking whether the given number is a even number or not.  
    #b) Using for loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4, ..1/10.  
    #c) Write a program using for loop that loops over a sequence. What is sequence?     
    #d) Write a program using a while loop that asks the    user for a number, and prints a countdown from that 
    #number to zero.
#Even
a=int(input("Enter the number:"))
if a%2==0:
    print("Even number")
else:
    print("Odd Number") 
#B.Decimal
for i in range(2,11):
    print(f"1/{i} = {1/i:.6f}")
#C.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
#string
word = "hello"
for letter in word:
    print(letter)
#D.
num = int(input("Enter a number: "))
while num >= 0:
    print(num)
    num -= 1  
#------------------------------------------------------
#22. 
    #a) Find the sum of all the primes below two million.  
    #b) Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting 
    #with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 By considering the terms in the 
    #Fibonacci sequence whose values do not exceed four million, find the sum of the even valued terms.  
    #c) Write a program to count the numbers of characters in the given string and store them in a dictionary 
    #data structure  
    #d)  Write a program to use split and join methods in the   given string and trace a birthday with a 
    #dictionary data structure.
#a.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
sum_primes = 0
for x in range(2, 2000000):
    if is_prime(x):
        sum_primes += x
print(sum_primes)
#b.
a, b = 1, 2
sum_even_fibs = 0
while a <= 4000000:
    if a % 2 == 0:
        sum_even_fibs += a
    a, b = b, a + b
print(sum_even_fibs)
#c
string = "hello"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
#d
birthday_str = "John:1990-05-22, Alice:1985-12-14"
birthday_list = birthday_str.split(", ")
birthday_dict = {}
for item in birthday_list:
    name, date = item.split(":")
    birthday_dict[name] = date
print(birthday_dict)
#------------------------------------------------------
#23. 
    #a) Write a program to combine two lists into a dictionary.  
    #b) Write a program to count frequency of characters in a given file. Can you use character frequency to 
    #tell whether the given file is a Python program file, C program file or a text file? 
#a.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)
#b.
filename = "example.txt"
with open(filename, 'r') as file:
    content = file.read()
    char_count = {}
    for char in content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
print(char_count)
#--------------------------------------
#24. 
      #a) Write a program to print each line of a file in reverse order.  
      #b) Write a program to compute the number of characters, words and lines in a file.
#a
filename = "example.txt"
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())
#b
filename = "example.txt"
with open(filename, 'r') as file:
    content = file.read()
    lines = content.splitlines()
    words = content.split()
    num_lines = len(lines)
    num_words = len(words)
    num_chars = len(content)
print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}")
#--------------------------------------------
#25. 
    #a) Write a function ball _collide that takes two balls as parameters and computes if they are colliding. 
    #Your function should return a Boolean representing whether or not the balls are colliding. Hint: Represent 
    #a ball on a plane as a tuple of (x, y, r), r being the radius. If (distance between two balls centers) <= (sum 
    #of their radii) then (they are colliding)   
    #b) Find mean, median, mode for the given set of numbers in a list
#a
import math
def ball_collide(ball1, ball2):
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= (r1 + r2)
ball1 = (0, 0, 5)
ball2 = (3, 4, 5)
print(ball_collide(ball1, ball2))
#b
from statistics import mean, median, mode
numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]
mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)
print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")
#----------------------------------------------------
#26. 
     #a) Write a function nearly_ equal to test whether two strings are nearly equal. Two strings a and b are 
     #nearly equal when a can be generated by a single mutation on b.  
     #b) Write a function dups to find all duplicates in the list.  
     #c) Write a function unique to find all the unique elements of a list.
#a
def nearly_equal(a, b):
    if len(a) != len(b):
        return False
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            if count > 1:
                return False
    return count == 1
print(nearly_equal("hello", "hallo"))  
print(nearly_equal("hello", "hella"))  
print(nearly_equal("hello", "world")) 
#b
def dups(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
print(dups([1, 2, 3, 4, 5, 5, 6, 7, 8, 1])) 
#c
def unique(lst):
    return list(set(lst))
print(unique([1, 2, 3, 4, 5, 5, 6, 7, 8, 1]))
#----------------------------------------------
#27. 
     #a) Write a function cumulative_product to compute cumulative product of a list of numbers.  
     #b) Write a function reverse to reverse a list. Without using the reverse function.
#a
def cumulative_product(lst):
    result = []
    product = 1
    for num in lst:
        product *= num
        result.append(product)
    return result

print(cumulative_product([1, 2, 3, 4]))
#b
def reverse(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst
print(reverse([1, 2, 3, 4]))
#-------------------------------------------
#28. Create a Regular Expression and implement the following  
    #a) Recognize the following strings: “bat,” “bit,” “but,” “hat,” “hit,” or “hut.” 
    #b) Match any pair of words separated by a single space, i.e., first and last names.  
    #c) Match any word and single letter separated by a comma and single space, as in last name, first initial. 
#a
import re
pattern = r"b[aiu]t|h[it|ut]"
strings = ["bat", "bit", "but", "hat", "hit", "hut", "cat", "hot"]

for string in strings:
    if re.match(pattern, string):
        print(f"{string} matches")
    else:
        print(f"{string} does not match")
#b
import re
pattern = r"\b\w+\s\w+\b"
strings = ["John Doe", "Alice Smith", "Robert", "Tom"]
for string in strings:
    if re.match(pattern, string):
        print(f"{string} matches")
    else:
        print(f"{string} does not match")
#c
import re
pattern = r"\b\w+, [A-Za-z]\b"
strings = ["Smith, J", "Doe, A", "Johnson, ", "Lee, R"]
for string in strings:
    if re.match(pattern, string):
        print(f"{string} matches")
    else:
        print(f"{string} does not match")
#------------------------------------------------------
# 29. Write a python program to simulate the banking operations using Class.
class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
#--------------------------------------------------------------
#30. Write a python program to demonstrate the Queue / Stack operations using Class.
#Queue
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    def dequeue(self):
        if len(self.queue) > 0:
            removed_item = self.queue.pop(0)
            print(f"Dequeued: {removed_item}")
        else:
            print("Queue is empty!")
    def display(self):
        print("Queue:", self.queue)
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
#stack
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    def dequeue(self):
        if len(self.queue) > 0:
            removed_item = self.queue.pop(0)
            print(f"Dequeued: {removed_item}")
        else:
            print("Queue is empty!")
    def display(self):
        print("Queue:", self.queue)
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
#-----------------------------------------------------
#31. 
    #a) WAP to add two numbers in python  
    #b) WAP to declare variables and display types of respective variables  
    #c) WAP to demonstrate type casting in python  
    #d) WAP to demonstrate Logical operators 
#a.
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
sum=a+b
print(sum)
#b.
n1 = input("Enter the value of n1: ")
if n1.isdigit():
    print("Type of n1: Number")
elif n1.isalpha():
    print("Type of n1: Alphabet")
else:
    print("Type of n1: Mixed or Special Characters")
#c.
a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
print(float(a))
print(complex(b))
print(f'"{str(c)}"')
#d.
a = True
b = False
print(a and b) 
print(a or b)   
print(not a)
#----------------------------------------------
#32.
    #a) WAP to Calculate length of string  
    #b) WAP to make string from 1st two and last two characters from given string.  
    #c) WAP to concatenate two strings 
#a.
a="DYPCET"
print(len(a))
#b.
s = input("Enter a string: ")
result = s[:2] + s[-2:]
print(result)
#C.
a="Hello"
b="World"
c=a+ " " +b
print(c)
#-------------------------------------------------
#33.
      #a) WAP to find out greatest of 3 numbers  
      #b)  WAP to find whether given number is odd or even  
      #c)  Write a C program to check whether a character is uppercase or lowercase alphabet.  
      #d)  WAP to find whether given input is number or character 
#a.
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
c=int(input("Enter the number:-"))
if a>b and b>c:
    print("a is greater")
elif b>c and b>a:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("!!!")
#b
d=int(input("Enter the number:-"))
if d%2==0:
    print("Even number")
else:
    print("Odd number")
#c
char=input("enter the character::===")
if char>='A' and char<='Z':
    print("uppercase")
elif char>='a' and char<='z':
    print("lowercase")
elif char>='0' and char<='9':
    print("digit")
else:
    print("special symbos")  
#d
n1=input("Enter the value of n1:")

if n1.isdigit():
    print("number")

elif n1.isalpha():
    print("Alphabet")
#----------------------------------
#34.
    #a) WAP to display even numbers from 1-10  
    #b) WAP to add odd numbers from 1-10  
    #c) Write a Python program to get the Fibonacci series between 0 to 50.  
    #d) Write a Python program to remove the characters which have odd index values of a given string. 
#a
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
#b
sum_odd = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum_odd += i
print("Sum of odd numbers:", sum_odd)
#c
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
#d
s = input("Enter a string: ")
result = "".join([s[i] for i in range(len(s)) if i % 2 == 0])
print("Resulting string:", result)
#------------------------------------------
#35.
    #a) Write a Python script to sort (ascending and descending) a dictionary by value  
    #b)  Write a Python script to check if a given key already exists in a dictionary.  
    #c)  Write a Python script to merge two Python dictionaries 
#a
my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 15}
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)

#b.
my_dict = {'a': 10, 'b': 20, 'c': 5}
key = input("Enter key to check: ")
if key in my_dict:
    print(f"Key '{key}' exists.")
else:
    print(f"Key '{key}' does not exist.")
#c
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}
merged_dict = dict1.copy()
merged_dict.update(dict2)
print("Merged Dictionary:", merged_dict)
#------------------------------------------
#36.
    #a)  Write a Python program to add an item in a tuple.  
    #b)  Write a Python program to create a tuple with different data types 
#a
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4,)
print(my_tuple)
#b
my_tuple = (1, "hello", 3.14, True)
print(my_tuple)
#------------------------------------------------
#37.
    #a)  Write a Python program to sum all the items in a list  
    #b)  Write a Python program to get the largest number from a list. 
    #c) Write a Python program to add member(s) in a set.  
#a
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print(total)
#b
my_list = [1, 2, 3, 4, 5]
largest = max(my_list)
print(largest)
#c
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
print(my_set)
#----------------------------------------------------
#38.
    #a)  Write a Python program to reverse the order of the items in the array  
    #b)  Write a Python program to create an array of 5 integers and display the array items. Access 
    #individual element through indexes.
#a
import array
my_array = array.array('i', [1, 2, 3, 4, 5])
my_array.reverse()
print(my_array)
#b
import array
my_array = array.array('i', [10, 20, 30, 40, 50])
print(my_array)
print(my_array[0])
print(my_array[1])
print(my_array[2])
print(my_array[3])
print(my_array[4])
#------------------------------------------------------------
#39.
    #a) Write a Python function to find the Max of three numbers.  
    #b)  Write a Python program to reverse a string. Sample String : "1234abcd" Expected Output : 
    #"dcba4321"  
    #c)  Write a Python function to calculate the factorial of a number (a non-negative integer). The 
    #function accepts the number as an argument.
#a.
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(max_of_three(10, 20, 30))
#b.
def reverse_string(s):
    return s[::-1]

print(reverse_string("1234abcd"))
#c.
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))
#------------------------------------------------
#40.
      #a) Write a Python program to read an entire text file 
      #b) Write a Python program to append text to a file and display the text.  
      #c) Write a Python program to read last n lines of a file 
#a
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#b.
with open("example.txt", "a") as file:
    file.write("\nThis is the appended text.")  
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#c.
def read_last_n_lines(filename, n):
    with open(filename, "r") as file:
        lines = file.readlines()
        return lines[-n:]
filename = "example.txt"
n = 3
last_lines = read_last_n_lines(filename, n)
for line in last_lines:
    print(line.strip())


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
    
day_num = int(input("enter a no : "))

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

