'''class person:
    def __init__(self):
        self.name = "sarthak"
        self.age = 18
class student(person):  
    def display(self):
        roll_no = int(input("Enter the roll number: "))
        print(f"{self.name} is {self.age} years old and has roll number {roll_no}")

s=student()
s.display() '''

class shape:
    pass   
class circle(shape):
    def __init__(self):
        self.r = float(input("Enter the radius: "))

    def area(self):
        self.c = 3.14 * self.r * self.r
        print(f"Area of circle is {self.c}")
class rectangle(shape):
    def __init__(self):
        self.l = int(input("Enter the length: "))
        self.b = int(input("Enter the breadth: "))

    def area(self):
        self.a = self.l * self.b
        print(f"The area of the rectangle is {self.a}")



c1 = circle()
c1.area()

r1 = rectangle()
r1.area()
