# write a program to find the student performance
# 80-100 best
# 60-79 good
# 40-59 average
# 35-39 pass
# 0-34 fail


d=int(input("Enter the students marks:-  "))
if d>=80 :
    print("The student performance is best!!")
elif d>=60 and d<=79:
      print("The student performance is good")
elif d>=40 and d<=59:
      print("The student performance is average")
elif d>=35 and d<=39:
      print("The student performance is pass")
else:
      print("student is fail")