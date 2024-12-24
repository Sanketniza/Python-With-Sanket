
a = (1,2,3 , 'sanket' , 'omkar')

print(a)
print(a[0])
print(a[1])
print(a[3])


y = list(a)
y.append("orange")
a = tuple(y)

print(a)

for x in a:
    print(x)
    
    