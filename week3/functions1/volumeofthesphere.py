
import math
def Volume_of_the_sphere(radius):
    return (4/3)*math.pi*pow(radius,3)

radius = float(input("Enter your radius: "))
print(Volume_of_the_sphere(radius))