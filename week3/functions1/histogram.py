def Histogram(list):
    for x in list:
        print('*' * x)


histogram = list(map(int,(input("Enter integers: ").split())))
Histogram(histogram)