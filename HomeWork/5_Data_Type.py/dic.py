
a = {
    
    "sanket" : 234,
    "banana" : 324,
     34 : 34,
}

print(a)
print(type(a))
print(a["banana"])

a[934] = 435
print(a)

a.update({"banana" : 23423})
print(a)

a.pop(34)
print(a)

a.popitem()
print(a)

a.clear()
print(a , type(a) , len(a))