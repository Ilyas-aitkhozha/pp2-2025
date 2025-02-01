import math

def prime(x):
    if x <=1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def filter_prime(num):
    pr_num = []
    for x in num:
        if prime(x):
            pr_num.append(x)
    return pr_num




list = [1, 2, 5, 4, 8, 10, 14, 19, 21, 20, 23, 31, 32]
print(filter_prime(list))