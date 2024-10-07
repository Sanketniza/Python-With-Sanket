
#* Python data types
# ^ Python has 6 basic data types:

# Text Type:str
# Numeric Types:int, float, complex
# Sequence Types:list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = 4 # int
x = int(4) # int
x = 4.0 # float
y = 4.0 # float
y = "Hello" # str
y = str("Hello") # str
z = True # bool
z = None # None
w = [1, 2, 3, "sanket", 5] # list
print(type(w)) # list
j = list([1, 2, 3, "sanket", 5]) # list
w = (1, "kya", 3, 4, 5) # tuple
w = range(1, 10) # range
w = {1: "omkar", 2: "sanket", 3: 9} # dict
w = set([1, 2, 3, 4, 5]) # set
w = frozenset([1, 2, 3, 4, 5]) # frozenset
print("--------------------------------------------")

#* Python Numbers
x = 1    # int
print(type(x)) # int
y = 2.8  # float
z = 1j   # complex

# Type Conversion
# -> You can convert from one type to another with the int(), float(), and complex() methods:

a = 3
b = 34.3
c = 3j

d = int(b)  # converting int float
e = float(a)
f = complex(d, e)
print(d, e, f)
print("--------------------------------------------")

#* py random number
import random
print(random.randrange(1, 10)) # print a random number between 1 and 10
print(random.randint(1, 10)) # print a random number between 1 and 10
print(random.choice([1, 2, 3, 4, 5])) # print a random number from the list
print(random.choice(["a", "b", "c", "d", "e"])) # print a random string from the list
print("--------------------------------------------")

#* py string

a = "hello " 
print(len(a)) # print the length of the string
b = 'hello'
c = " 'hello ' " 
d = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(d)              

a = "Hello, World!"
print(a[1]) # print the second character = e
b = a[1:4] # print the second to fourth character = el
c = a[1:] # print the second to the end of the string = ello, World!
print(b)
print(c)
print("------------------------------------------")          

#* looping through a string
for i in "Hello, World!":
    print(i)
print("------------------------------------------")

#* Check String
# -> To check if a certain phrase or character is present in a string, we can use the keyword in.

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

sanket = "hello my name is sanket"
if "sanket" in sanket:
    print("sanket is present in the string")
else:
    print("sanket is not present in the string")
    
sanket = "hello my name is sanket"
if "sanket" not in sanket:
    print("sanket is not present in the string")
else:
    print("sanket is present in the string")
print("------------------------------------------")

#* Python - Slicing Strings

# -> Specify the start index and the end index, separated by a colon, to return a part of the string.
txt = "The best things in life are free!"
print(txt[0:9]) # print the first four characters


x = "The best things in life are free!"
print(x[:4])  #  -> Slice From the Start
print(x[4:])  # -> Slice From the End

b = "Hello, World!"
print(b[-5:-2])  # -> Slice From the End
print("------------------------------------------")

#*  Python - Modify Strings

txt = "The best Things in life are fr-ee!"
txt = txt.upper()  # -> Convert to Uppercase
print(txt)
txt = txt.lower()  # -> Convert to Lowercase
print(txt)
txt = txt.title()  # -> Convert to Titlecase
print(txt)
txt = txt.strip()  # -> Remove Whitespace
print(txt)
txt = txt.replace("life", "love")  # -> Replace a Character
print(txt)
txt = txt.replace("life", "love", 1)  # -> Replace the first occurrence of a Character
print(txt)
txt = txt.replace("life", "love", 2)  # -> Replace the second occurrence of a Character
print(txt)
print("------------------------------------------")