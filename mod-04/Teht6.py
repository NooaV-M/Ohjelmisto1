import random
import math

target_point_number = int(input("Enter number of points to generate:"))
current_point_number = 0
points_in_circle = 0


while current_point_number < target_point_number:

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        points_in_circle += 1

    current_point_number += 1

print(f"Pi approximated value:\n{4*points_in_circle/target_point_number}")