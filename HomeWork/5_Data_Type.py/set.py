
# print hello world

a = {1,2,3,5,1,'sanket'}
print(a)
print(type(a))
print(len(a))

a.add("talekar")
print(a)

b = {"A" , 3}
a.update(b)
print(a)

a.remove(1)
print(a)

a.discard('sanket')
print(a)

a.pop()
print(a)

for x in a:
    print(x)
    
c = a.union(b)
print(c)    