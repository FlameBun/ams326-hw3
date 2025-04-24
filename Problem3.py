import matplotlib.pyplot as plot
import math

# Constants
a = 100
w = 44
v0 = 88
k = w / v0
step = -0.00001 # Step size for Euler's method

# dy/dx for a specific x and y
def dy_dx(x, y):
    return (y / x) - k * math.sqrt(1 + (y / x)**2)

# Initialize x, y, and y_prime (dy/dx)
x = a
y = 0
y_prime = dy_dx(x, y)

x_values = [x]
y_values = [y]

while x + step >= 0:
    # Calculate y at next step
    new_y = y_prime * step + y
    y_values.append(new_y)
    x_values.append(x + step)
    
    # Transition to new x, y, and y_prime (dy/dx)
    x += step
    y = new_y
    y_prime = dy_dx(x, y)

# Print initial point and every 50000th trajectory point in TrajectoryPoints.txt
with open("TrajectoryPoints.txt", "w") as file:
    print(f"({x_values[0]}, {y_values[0]})", file=file)
    for i in range(len(x_values)):
        if (i + 1) % 50000 == 0:
            print(f"({x_values[i]}, {y_values[i]})", file=file)

# Plot plane's trajectory
print("**Point Format (x, y)")
print(f"Initial Point: ({x_values[0]}, {y_values[0]})")
print(f"Final Point: ({x_values[len(x_values) - 1]}, {y_values[len(y_values) - 1]})")
plot.plot(x_values, y_values)
plot.title("Plane Trajectory")
plot.xlabel("x")
plot.ylabel("y")
plot.grid(True)
plot.show()