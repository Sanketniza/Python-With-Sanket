#   Write a Python program to calculate the sum of the first n positive integers.  


n = int(input("Enter the n numbers :- "))
total_sum = 0
for i in range(1,n+1):
  total_sum+= i
print(total_sum)