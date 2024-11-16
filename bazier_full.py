import numpy as np
import matplotlib.pyplot as plt

# Path with points [x, y, heading]
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

# Helper function to compute intermediate control points for Bézier curve
def compute_intermediate_control_points(p1, p2, dist_factor=2.5):
    x1, y1, heading1 = p1
    x4, y4, heading4 = p2

    # Euclidean distance between points
    ecl_dist = np.sqrt((x4 - x1)**2 + (y4 - y1)**2)
    dist = ecl_dist / dist_factor
    
    # Calculate control points
    x2 = x1 + (dist) * np.cos(np.radians(heading1))  
    y2 = y1 + (dist) * np.sin(np.radians(heading1))  

    x3 = x4 + (dist) * np.cos(np.radians(heading4 + 180))  
    y3 = y4 + (dist) * np.sin(np.radians(heading4 + 180))  

    return [x2, y2], [x3, y3]

# Bézier curve function
def cubic_bezier(t, points):
    """Compute a cubic Bézier curve point."""
    P1 = np.array(points[0])
    P2 = np.array(points[1])
    P3 = np.array(points[2])
    P4 = np.array(points[3])
    
    return (1 - t)**3 * P1 + \
           3 * (1 - t)**2 * t * P2 + \
           3 * (1 - t) * t**2 * P3 + \
           t**3 * P4

# Generate the full Bézier path for the entire path
control_points = []
for i in range(len(path) - 2):
    p1 = path[i]
    p2 = path[i + 1]

    
    # Compute intermediate control points for Bézier
    control_point1, control_point2 = compute_intermediate_control_points(p1, p2)
    
    # Append the control points to the list
    control_points.append([p1[:2], control_point1, control_point2, p2[:2]])

# Generate Bézier curve points
t_values = np.linspace(0, 1, num=100)
curve_points = []

for segment in control_points:
    for t in t_values:
        curve_points.append(cubic_bezier(t, segment))

curve_points = np.array(curve_points)

# Plot the Bézier curve
plt.figure(figsize=(10, 8))

# Plot the full path
plt.plot(curve_points[:, 0], curve_points[:, 1], label="Full Bézier Curve Path", color="blue")

# Plot control points
for segment in control_points:
    segment_points = np.array(segment)
    
# Plot control polygons
for segment in control_points:
        segment_points = np.array(segment)
        plt.scatter(segment_points[:,0], segment_points[:,1], color="red", marker="o")
        plt.plot(segment_points[:,0], segment_points[:,1], '--', color="gray")

plt.title("Full Path - Cubic Bézier Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
