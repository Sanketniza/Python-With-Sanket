# Write a Python program to calculate the sum of the first n positive odd numbers.

n = int(input("Enter the n numbers :- "))
total_sum = 0
for i in range(1,n+1):
   if i%2==0:
     print()
   else:
      print(i)
      total_sum+=i
print("The sum of odd numbers is :- ")
print(total_sum)