def farenheitToCelcius(F):
    return (5 / 9) * (F - 32)
F = float(input("Enter farenheit temperature: "))
print(farenheitToCelcius(F))