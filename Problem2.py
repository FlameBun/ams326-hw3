import numpy

width, height = 1, 1 / numpy.sqrt(2) # Width and height of rectangle
total_points = 25000 # Number of sampled points in rectangle
total_iterations = 10000 # Number of iterations of Metropolis Method

# Sample 25000 points in the rectangle whose center is (x_center, y_center) and is rotated by alpha
def sample_rectangle(x_center, y_center, alpha):
    # Sample 25000 points in rectangle, assuming rectangle's center is origin and its angled by 0 radians
    x_sample = numpy.random.uniform(-width / 2, width / 2, total_points)
    y_sample = numpy.random.uniform(-height / 2, height / 2, total_points)

    # Rotate sample points by alpha about origin
    x_rotation = x_sample * numpy.cos(alpha) - y_sample * numpy.sin(alpha)
    y_rotation = x_sample * numpy.sin(alpha) + y_sample * numpy.cos(alpha)

    # Translate sample points such that their center is (x_center, y_center)
    x_translate = x_rotation + x_center
    y_translate = y_rotation + y_center

    return x_translate, y_translate

# Given that the rectangle's center is (x_center, y_center) and that it's rotated by alpha,
# estimate the percentage of the rectangle that cuts the area of the rose.
def estimate_percentage(x_center, y_center, alpha):
    # Sample 25000 points in rectangle
    x_sample, y_sample = sample_rectangle(x_center, y_center, alpha)

    # Determine percentage of sample points in rectangle that lie inside rose
    points_inside = (x_sample**2 + y_sample**2)**3 <= 4 * x_sample**2 * y_sample**2
    percentage = sum(points_inside) / total_points

    return percentage

init_x_center, init_y_center, init_alpha = numpy.random.uniform(-1, 1), numpy.random.uniform(-1, 1), numpy.random.uniform(0, numpy.pi) # Initial center position and angle of rectangle
init_percentage = estimate_percentage(init_x_center, init_y_center, init_alpha) # Initial percentage of rectangle that cuts area of rose
x_center, y_center, alpha = init_x_center, init_y_center, init_alpha # Center position and angle of rectangle
percentage = init_percentage # Percentage of rectangle that cuts area of rose
for i in range(0, total_iterations):
    # Create new state by randomly picking between x_center, y_center, and alpha and changing its value by small amount
    new_x_center, new_y_center, new_alpha = x_center, y_center, alpha
    random_val = numpy.random.randint(0, 3) # Random integer on [0, 3)
    if random_val == 0:
        new_x_center += numpy.random.uniform(-0.1, 0.1)
    elif random_val == 1:
        new_y_center += numpy.random.uniform(-0.1, 0.1)
    else:
        new_alpha += numpy.random.uniform(-0.4, 0.4)

    # Choose best state between previous state and new state
    new_percentage = estimate_percentage(new_x_center, new_y_center, new_alpha)
    if new_percentage > percentage:
        percentage = new_percentage
        x_center, y_center, alpha = new_x_center, new_y_center, new_alpha

print("--- Initial Rectangle State ---")
print(f"Center: ({init_x_center}, {init_y_center})")
print(f"Angle: {init_alpha} Radians")
print(f"Area of Rose Cutted: {width * height * init_percentage}\n")

print("--- Final Rectangle State After Metropolis Method (Best Estimated Center Position and Angle of Rectangle That Cuts the Most Area of the Rose) ---")
print(f"Center: ({x_center}, {y_center})")
print(f"Angle: {alpha} Radians")
print(f"Area of Rose Cutted: {width * height * percentage}")
