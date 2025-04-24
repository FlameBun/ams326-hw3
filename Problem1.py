import matplotlib.pyplot as plot
import random
import math

num_lines = 10000 # Number of parallel lines of distance 1
num_tosses = 4444444 # Number of tosses for experiment
diameter_prob = {} # Dictionary of each diameter and their probabilities for crossing 1, 2, and 3 lines
diameters = [1/10, 2/10, 3/10, 4/10, 5/10, 6/10, 7/10, 8/10, 9/10, 10/10, 15/10, 20/10, 30/10]

# Calculate the probabilities for crossing 1, 2, and 3 lines for the specified diameter
def calc_prob(diameter):
    radius = diameter / 2

    # Initialize dictionary of probabilities for this disc
    diameter_prob[diameter] = {}

    # Number of times this disc crosses at least 1, 2, 3, and 4 lines in 4444444 tosses
    crossed1, crossed2, crossed3, crossed4 = 0, 0, 0, 0

    for i in range(0, num_tosses):
        center_pos = random.uniform(1, num_lines)   # Center of disc
        top_edge_pos = center_pos + radius          # Top edge of disc
        bottom_edge_pos = center_pos - radius       # Bottom edge of disc

        if center_pos.is_integer(): # Center of disc is directly on top of a line
            num_lines_crossed = 1
            top = center_pos + 1    # Position of next top line
            bottom = center_pos - 1 # Position of next bottom line
        else: # Center of disc is not on top of a line
            num_lines_crossed = 0
            top = math.ceil(center_pos)     # Position of top line closest to center of disc
            bottom = math.floor(center_pos) # Position of bottom line closest to center of disc

        # Determine number of lines top-half of disc crossed
        while top <= top_edge_pos:
            num_lines_crossed += 1
            top += 1 # Next top line

        # Determine number of lines bottom-half of disc crossed
        while bottom >= bottom_edge_pos:
            num_lines_crossed += 1
            bottom -= 1 # Next bottom line

        if num_lines_crossed >= 1:
            crossed1 += 1
        if num_lines_crossed >= 2:
            crossed2 += 1
        if num_lines_crossed >= 3:
            crossed3 += 1
        if num_lines_crossed >= 4:
            crossed4 += 1

    # Calculate probabilities of this disc crossing at least 1, 2, 3, and 4 lines
    diameter_prob[diameter][1] = crossed1 / num_tosses
    diameter_prob[diameter][2] = crossed2 / num_tosses
    diameter_prob[diameter][3] = crossed3 / num_tosses
    diameter_prob[diameter][4] = crossed4 / num_tosses

    print(f"Diameter: {diameter}")
    print(f"P(1 Line) = {diameter_prob[diameter][1]}")
    print(f"P(2 Line) = {diameter_prob[diameter][2]}")
    print(f"P(3 Line) = {diameter_prob[diameter][3]}")
    print(f"P(4 Line) = {diameter_prob[diameter][4]}\n")

# Calculate probabilities of discs of each diameter crossing at least 1, 2, 3, and 4 lines
prob_1_line, prob_2_line, prob_3_line, prob_4_line = [], [], [], []
for diameter in diameters:
    calc_prob(diameter)
    prob_1_line.append(diameter_prob[diameter][1])
    prob_2_line.append(diameter_prob[diameter][2])
    prob_3_line.append(diameter_prob[diameter][3])
    prob_4_line.append(diameter_prob[diameter][4])

# Plot probabilities as a function of diameter for crossing at least 1, 2, 3, and 4 lines
plot.plot(diameters, prob_1_line, label="P(1 Line)", color="red", linestyle="solid", marker="o")
plot.plot(diameters, prob_2_line, label="P(2 Line)", color="green", linestyle="dashed", marker="^")
plot.plot(diameters, prob_3_line, label="P(3 Line)", color="blue", linestyle="dotted", marker="s")
plot.plot(diameters, prob_4_line, label="P(4 Line)", color="orange", linestyle="dashdot", marker="x")
plot.legend()
plot.xlabel("Diameter d")
plot.ylabel("Probability P(d)")
plot.grid(True)
plot.show()
