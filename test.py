import numpy as np
import matplotlib.pyplot as plt

# Example arrays
x = np.array([1, 2, 3])
y = np.array([4, 5])

# Create meshgrid for combinations
xx, yy = np.meshgrid(x, y)

# Flatten the grid
x_flat = xx.ravel()
y_flat = yy.ravel()

# Example z values based on some function of x and y (e.g., z = x^2 + y^2)
z = x_flat**2 + y_flat**2

# Create a scatter plot with color-coding based on z
plt.scatter(x_flat, y_flat, c=z, cmap="viridis")

# Add color bar for reference
plt.colorbar(label="z values")

# Label the axes
plt.xlabel("Array1 (x)")
plt.ylabel("Array2 (y)")
plt.title("Color-coded z values for combinations of array1 and array2")

# Show the plot
plt.show()
