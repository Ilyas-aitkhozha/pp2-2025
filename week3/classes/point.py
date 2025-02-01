import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return (self.x, self.y)
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
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
newx1 = float(input("enter new x coordinate for the first point: "))    
newy1 = float(input("enter new y coordinate for the second point: "))  
p1.move(newx1,newy1)
newx2 = float(input("enter new x coordinate for the first point: "))    
newy2 = float(input("enter new y coordinate for the second point: "))  
p2.move(newx2,newy2)
print("new coordinates for the first point: ", p1.show())
print("new coordinates for the second point: ", p2.show())
print("Distance: ", p1.dist(p2))
