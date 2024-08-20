# ? Write a Python Program to find the greatest number among three numbers.

a =  int (input ('enter first number '))
print(a)

b = int (input ('enter second number '))
print(b)

c = int (input ('enter third number '))
print(c)

if a < b and c < b:
 print('b greater than a and c ')

elif a > b and a > c:
 print('a is greater then b and c ')
    
else:
 print('c greater then a and b ')
