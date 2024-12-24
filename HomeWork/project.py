import matplotlib.pyplot as plt

# Data for the lines
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]  # Line 1 (y = x^2)
y2 = [1, 2, 3, 4, 5]    # Line 2 (y = x)
y3 = [25, 16, 9, 4, 1]  # Line 3 (y = reverse of x^2)

# Plot the lines
plt.plot(x, y1, label='y = x^2', color='blue', linestyle='-')
plt.plot(x, y2, label='y = x', color='red', linestyle='--')
plt.plot(x, y3, label='y = reverse(x^2)', color='green', linestyle='-.')

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines on the Same Plot")

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)  # Add a grid for better readability
plt.show()
