import numpy as np
import matplotlib.pyplot as plt

# Given points with x, y, heading (angles in degrees)
point1 = [31.449902934592444, 24.167423853428893, 20.0]  # Start point
point4 = [39.9234730112761, 30.893575286672355, 83.73175064999998]  # End point

# Extract values
x1, y1, heading1 = point1
x4, y4, heading4 = point4

# Compute Euclidean distance
ecl_dist = np.sqrt((x4 - x1)**2 + (y4 - y1)**2)
dist = ecl_dist / 2.5
# Compute intermediate control points
x2 = x1 + (dist) * np.cos(np.radians(heading1))  # Convert degrees to radians
y2 = y1 + (dist) * np.sin(np.radians(heading1))  # Convert degrees to radians

x3 = x4 + (dist) * np.cos(np.radians(heading4 + 180))  # Convert degrees to radians
y3 = y4 + (dist) * np.sin(np.radians(heading4 + 180))  # Convert degrees to radians

# Control points
control_points = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])

# Bézier curve function
def cubic_bezier(t, points):
    """Compute a cubic Bézier curve point."""
    P1, P2, P3, P4 = points
    return (1-t)**3 * P1 + 3*(1-t)**2 * t * P2 + 3*(1-t) * t**2 * P3 + t**3 * P4

# Generate Bézier curve points
t_values = np.linspace(0, 1, 100)  # Parameter t from 0 to 1
curve_points = np.array([cubic_bezier(t, control_points) for t in t_values])

# Plot the Bézier curve
plt.figure(figsize=(8, 6))
plt.plot(curve_points[:, 0], curve_points[:, 1], label="Bézier Curve", color="blue")
plt.scatter(control_points[:, 0], control_points[:, 1], color="red", label="Control Points")
plt.plot(control_points[:, 0], control_points[:, 1], '--', color="gray", label="Control Polygon")
plt.title("Cubic Bézier Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
