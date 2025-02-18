def squares(a, b):
    for i in range(a, b + 1):
        yield i * i  
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for num in squares(a, b):
    print(num)
