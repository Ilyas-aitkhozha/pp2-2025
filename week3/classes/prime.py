import math
def filter_prime(p_numbs):
    is_prime = filter(lambda x: x > 1 and all(x%i != 0 for i in range(2, int(math.sqrt(x))+ 1)),p_numbs)
    return list(is_prime)

p_numbs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(filter_prime(p_numbs))