import math
import matplotlib.pyplot as plt

# Get user inputs
weight = float(input("Enter plane weight (grams): "))
launch_angle_deg = float(input("Enter launch angle (degrees): "))
initial_speed = float(input("Enter initial speed (m/s): "))

g = 9.81  # gravity (m/s^2)
launch_angle_rad = math.radians(launch_angle_deg)

flight_time = (2 * initial_speed * math.sin(launch_angle_rad)) / g
flight_distance = ((initial_speed ** 2) * math.sin(2 * launch_angle_rad)) / g

print(f"Estimated flight time: {flight_time:.2f} seconds")
print(f"Estimated flight distance: {flight_distance:.2f} meters")

num_points = 100
t_vals = [i * flight_time / num_points for i in range(num_points + 1)]
x_vals = [initial_speed * math.cos(launch_angle_rad) * t for t in t_vals]
y_vals = [initial_speed * math.sin(launch_angle_rad) * t - 0.5 * g * t ** 2 for t in t_vals]

plt.plot(x_vals, y_vals)
plt.title("Paper Plane Flight Trajectory")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()