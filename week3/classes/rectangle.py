class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.length =  length
        self.width = width
    
    def area(self):
        return self.length * self.width
rectangle = Rectangle(6, 8)
#or u can use inputs from the user 
#length = int(input("enter a length: "))
#width = int(input("enter a width: "))
#rect = Rectangle(length, width)
