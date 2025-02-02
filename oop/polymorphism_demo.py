import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):    
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width
    