# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
print('\n')
print("-------------------------------------------------------")

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(4, 5))  # Output: 20
print('\n')
print("-------------------------------------------------------")

# Lambda function to calculate the square of a number
square = lambda x: x ** 2
print(square(3))  # Output: 9
print('\n')
print("-------------------------------------------------------")

# Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print('\n')
print("-------------------------------------------------------")

# Lambda function to convert a string to uppercase
to_uppercase = lambda s: s.upper()
print(to_uppercase("hello"))  # Output: HELLO
print('\n')
print("-------------------------------------------------------")

# Lambda function to calculate the length of a string
length = lambda s: len(s)
print(length("hello"))  # Output: 5
print('\n')
print("-------------------------------------------------------")

# Lambda function to reverse a string
reverse = lambda s: s[::-1]
print(reverse("hello"))  # Output: olleh
print('\n')
print("-------------------------------------------------------")

# Lambda function to check if a number is positive
is_positive = lambda x: x > 0
print(is_positive(5))  # Output: True
print('\n')
print("-------------------------------------------------------")

# Lambda function to calculate the factorial of a number
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
print(factorial(5))  # Output: 120
print('\n')
print("-------------------------------------------------------")

# Lambda function to calculate the average of a list of numbers
average = lambda nums: sum(nums) / len(nums)
print(average([1, 2, 3, 4, 5]))  # Output: 3.0
print('\n')
print("-------------------------------------------------------")
