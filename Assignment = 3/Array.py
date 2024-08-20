# Operation on Array in python


#  Performed all the operations on Array
#  1. append
#  2. clear
#  3. copy
#  4. count
#  5. extend
#  6. index
#  7. insert
#  8. pop
#  9. remove
#  10. reverse
#  11. sort


import array

a = array.array('i', [1, 2, 3, 14, 5, 6, 7, 8, 9, 10])

# type
print(type(a))
print('\n')

# append
a.append(11)
print(a)
print('\n')


# # copy
# a.copy()
# print(a)
# print('\n')

# count
a.count(1)
print(a)
print('\n')

# extend
a.extend([12, 13, 14])
print(a)
print('\n')

# index
a.index(1)
print(a)
print('\n')

# insert
a.insert(0, 0)
print(a)
print('\n')

# pop
a.pop(0)
print(a)
print('\n')

# remove
a.remove(1)
print(a)
print('\n')

# reverse
a.reverse()
print(a)
print('\n')

