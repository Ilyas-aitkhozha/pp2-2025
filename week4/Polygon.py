import math

parametrs = list(map(float, input("Put your number of sides and input the length of the side: ").split()))
apothem = parametrs[1] / (2 * math.tan(math.radians(180/parametrs[0])))
print(round((parametrs[0] * parametrs[1] * apothem) / 2))
