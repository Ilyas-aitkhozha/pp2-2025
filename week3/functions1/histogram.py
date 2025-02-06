def Histogram(list):
    for x in list:
        print('*' * x)

if __name__ == "__main__":
    histogram = list(map(int,(input("Enter integers: ").split())))
    Histogram(histogram)