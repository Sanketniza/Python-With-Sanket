#  Performed all the operations on Dictionary 

#  1. clear
#  2. copy
#  3. fromkeys
#  4. get
#  5. items
#  6. keys
#  7. pop
#  8. popitem
#  9. setdefault
#  10. update
#  11. values


d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# type
print(type(d))
print('\n')

# copy
d.copy()
print(d)
print('\n')

# fromkeys
d.fromkeys({1, 2, 3, 4, 5})
print(d)
print('\n')

# get
print(d.get(1))
print('\n')

# items
print(d.items())
print('\n')

# keys
print(d.keys())
print('\n')

# pop
d.pop(1)
print(d)
print('\n')

# popitem
d.popitem()
print(d)
print('\n')

# setdefault
d.setdefault(6)
print(d)
print('\n')

# update
d.update({7: 'f'})
print(d)
print('\n')

# values
print(d.values())
print('\n')


# clear
d.clear()
print(d)
print('\n')