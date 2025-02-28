num = int(input("enter number: "))
zaderzhka = int(input("enter miliseconds: "))

for i in range(zaderzhka * 1000): pass
print(f"Square root of {num} after {zaderzhka} milliseconds is {pow(num, 0.5)}")
