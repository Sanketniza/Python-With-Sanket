import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color='lightgreen')

plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()
