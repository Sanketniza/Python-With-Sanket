#  Performed all the operations on Tuple
#  1. count
#  2. index


t = (1, 2, 3, 4, 5, 16, 7, 8, 9, 10)
# type
print(type(t))
print('\n')

# count
t.count(1)
print(t)
print('\n')

# index
t.index(1)
print(t)
print('\n')

# conversion of tuple to list
l = list(t)
print(type(l))
print(l)
print('\n')

# conversion of list to tuple
t = tuple(l)
print(type(t))
print(t)

# example
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple) 
