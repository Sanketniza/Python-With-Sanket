import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values)

plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Values")

plt.show()
