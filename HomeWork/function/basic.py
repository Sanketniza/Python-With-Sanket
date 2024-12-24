
def a():
    print("hello sanket how are you")
    
a()

def b(x):
    print(  x + "hello")

b("sanket ")


def c(x , y ) :
    print(x , " and " , y)
    
c("sanket" , "sanket")  


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")  

def d(x):
    return 3+x

print(d(3))

x = lambda p : 3 + 3 + p
print(x(3))

def z(x):
    return lambda y: x + y
k = z(4)
print(k(10))
