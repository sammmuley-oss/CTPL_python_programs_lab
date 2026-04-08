class shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print("No function defined for area in shape class")

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
c = circle(5)
print("Area of circle:", c.area())
r = rectangle(4, 6)
print("Area of rectangle:", r.area())
