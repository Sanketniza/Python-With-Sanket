import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.barh(categories, values, color='lightblue')

plt.title("Horizontal Bar Chart Example")
plt.xlabel("Values")
plt.ylabel("Categories")

plt.show()
