import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Path data: x, y, heading
path = [
    [20, 20, 20], [31.449902934592444, 24.167423853428893, 20.0],
    [39.9234730112761, 30.893575286672355, 83.73175064999998],
    [43.53144920827289, 41.885315907862406, 40.21544658999997],
    [50.89348385342818, 50.97382941376945, 78.60171349999996],
    [56.251197100714954, 60.11813735600124, 12.337086579999948],
    [66.77857631991273, 58.89431312118713, -53.92754034000005],
    [71.51508428168064, 48.33962949496109, -97.44384440000005],
    [73.57900381270089, 37.71970769125345, -33.71209375000004],
    [84.01566344991362, 34.87038521663486, 30.019656899999973],
    [94.56586029795415, 40.96637121180517, 30.019656899999973],
    [103.42041798953639, 48.60819298085757, 68.40592380999999],
    [104.01532323875318, 59.41044231568807, 132.13767445999997],
    [99.84538230847431, 69.15390430927641, 65.87304753999996],
    [102.54624813387443, 80.5339726595416, 104.25931444999998],
    [99.54501632126221, 92.34330398661857, 104.25931444999998],
    [96.54378450864999, 104.15263531369553, 104.25931444999998],
    [96.06832594001844, 115.71160556502544, 60.74301038999997],
    [103.68258927860913, 124.42130406337822, 17.226706329999956],
    [115.32071956908202, 128.02985254271093, 17.226706329999956],
    [126.9588498595549, 131.63840102204364, 17.226706329999956],
    [138.4777080097785, 132.71160232498843, -26.289597730000054],
    [149.40213506042232, 127.31488180221922, -26.289597730000054],
    [160.32656211106615, 121.91816127945, -26.289597730000054]
]

# Separate x, y, heading
x, y, heading = zip(*path)

# Parameter t (based on point indices)
t = np.linspace(0, len(x) - 1, len(x))

# Create cubic splines
spline_x = CubicSpline(t, x)
spline_y = CubicSpline(t, y)
spline_heading = CubicSpline(t, heading)

# Generate parameterized points
t_fine = np.linspace(0, len(x) - 1, 500)  # Higher resolution for smooth curve
x_fine = spline_x(t_fine)
y_fine = spline_y(t_fine)

# Calculate heading direction vectors for arrows
heading_radians = np.radians(heading)  # Convert heading to radians
dx = np.cos(heading_radians)  # X components of arrows
dy = np.sin(heading_radians)  # Y components of arrows

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(x_fine, y_fine, '-', label='Cubic Spline Interpolation', color='blue')
plt.scatter(x, y, color='red', label='Original Points')

# Add arrows for heading direction with reduced width
plt.quiver(x, y, dx, dy, angles='xy', scale_units='xy', scale=0.15, width=0.004, color='green', label='Heading Direction')

plt.title('cubic spline Parameterized Path with Heading Directions')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()
