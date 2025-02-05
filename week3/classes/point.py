import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return (self.x, self.y)
    def move(self, moving_point):
        self.x += moving_point
        self.y += moving_point
    def dist(self, secondpoint):
        dx = self.x - secondpoint.x
        dy = self.y - secondpoint.y
        return math.sqrt(dx**2 + dy**2)
    
x1 = float(input("enter x coordinate for the first point: "))    
y1 = float(input("enter y coordinate for the first point: "))  
p1 = Point(x1, y1)
x2 = float(input("enter x coordinate for the second point: "))  
y2 = float(input("enter y coordinate for the second point: "))  
p2 = Point(x2, y2)
print("First point:", p1.show())
print("Second point:", p2.show())
print("Distance:", p1.dist(p2))
moving_point = float(input("How much do u want to move the point? "))
p1.move(moving_point)
p2.move(moving_point)
print("First point after moving",p1.show())
print("Second point after moving", p2.show())
