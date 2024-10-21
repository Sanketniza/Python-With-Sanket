
# File Handling

# 1. open a file
# 2. read a file
# 3. write a file
# 4. close a file


# create a file
file = open("test.txt", "w")

# open a file
file = open("test.txt", "w")

# write a file
file.write("Hello, World!")

# close a file
file.close()

# read a file
file = open("test.txt", "r")
print(file.read())
file.close()

# append a file
file = open("test.txt", "a")
file.write("Hello, World!")
file.close()

# file size
file = open("test.txt", "r")
# print(file.size())
file.close()

# readline
file = open("test.txt", "r")
print(file.readline())
file.close()

# ! Remove and passing file name in remove function
import os
os.remove("test.txt")

#  Make directory
os.mkdir("test")

# Remove directory
os.rmdir("test")

# getcwd
print(os.getcwd())

# chdir
# os.chdir("C:\\Users\\HP\\Desktop")


# create a file in current directory
file = open("test.txt", "w")
file.write("Hello, World!")
file.close()

# create empty file 
open("test.txt", "w").close()

# ! read a file
file = open("test.txt", "r")
print(file.read())
file.close()


# read the data from the file
with open("test.txt", "r") as file:
    print(file.read())


