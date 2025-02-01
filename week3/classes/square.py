class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
square = Square(6) #or i can add input to  self.length like this => self.length = int(input("whats the length?: "))
print(square.area())