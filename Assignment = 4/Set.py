#  Performed all the operations on set
#  1. add
#  2. clear
#  3. copy
#  4. difference
#  5. discard
#  6. intersection
#  7. isdisjoint
#  8. issubset
#  9. issuperset
#  10. pop
#  11. remove
#  12. symmetric_difference
#  13. union



s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# type
print(type(s))
print('\n')

# add
s.add(11)
print(s)
print('\n')
 
# copy
s.copy()
print(s)
print('\n')

# difference
s.difference({1, 2, 3, 4, 5})
print(s)
print('\n')

# discard
s.discard(11)
print(s)
print('\n')

# intersection
s.intersection({1, 2, 3, 4, 5})
print(s)
print('\n')

# isdisjoint
s.isdisjoint({1, 2, 3, 4, 5})
print(s)
print('\n')

# issubset
s.issubset({1, 2, 3, 4, 5})
print(s)
print('\n')

# issuperset
s.issuperset({1, 2, 3, 4, 5})
print(s)
print('\n')

# pop
s.pop()
print(s)
print('\n')

# symmetric_difference
s.symmetric_difference({1, 2, 3, 4, 5})
print(s)
print('\n')

# union
s.union({1, 2, 3, 4, 5})
print(s)
print('\n')




# clear
s.clear()
print(s)
print('\n')