import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Sample data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 2, 4, 0])

# Create a cubic spline interpolation
cs = CubicSpline(x, y)

# Generate new x values for a smoother curve
x_new = np.linspace(0, 4, 100)
y_new = cs(x_new)

# Plot the original polygon and the interpolated curve
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_new, y_new, label='Cubic Spline')
plt.legend()
plt.show()