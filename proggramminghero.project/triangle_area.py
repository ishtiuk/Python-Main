import math

def triangle_area(first_angle_len, second_angle_len, third_angle_len):
    s = (first_angle_len + second_angle_len + third_angle_len) / 2
    area = math.sqrt(s * (s - first_angle_len)* (s - second_angle_len) * (s - third_angle_len))

    return area

a = float(input("Enter first side lenght: "))
b = float(input("Enter second side lenght: "))
c = float(input("Enter third side length: "))

print(triangle_area(a, b, c))

