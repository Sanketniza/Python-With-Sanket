# Function with no parameters and no return value

def say_hello():
    print("Hello, World!")

say_hello()  # Output: Hello, World!
print('\n')
print("-------------------------------------------------------")

# Function with parameters and no return value
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
print('\n')
print("-------------------------------------------------------")

# Function with parameters and a return value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
print('\n')
print("-------------------------------------------------------")

# Function with default parameters
def greet_with_default(name="World"):
    print(f"Hello, {name}!")

greet_with_default()  # Output: Hello, World!
print('\n')
print("-------------------------------------------------------")

# Function with variable-length arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print('\n')
print("-------------------------------------------------------")

# Function with keyword arguments
def print_info(name, age, **kwargs):
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="New York", country="USA")
# Output:
# Name: Bob, Age: 30
# city: New York
# country: USA
print('\n')
print("-------------------------------------------------------")

# Function with a generator
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up_to(5):
    print(number)  # Output: 1 2 3 4 5
    print('\n')
print("-------------------------------------------------------")

# Function with a decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print('\n')
print("-------------------------------------------------------")

multiply = lambda x, y: x * y
print(multiply(4, 5))  # Output: 20
print('\n')
print("-------------------------------------------------------")

# Function with a nested function
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(3))  # Output: 8



