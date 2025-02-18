def belown(n):
    while n >= 0:
        yield n
        n-=1
n = int(input("enter your number: "))
for num in belown(n):
    print(num)