def s_numbs(n):
    for i in range(1, n+1):
        yield (i*i)

n = int(input("enter number u want to squares up: "))


for num in s_numbs(n):
    print(num)