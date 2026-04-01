class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = 0
        self.marks = 0

    def input_data(self):
        self.name = input("Enter the name: ")
        self.roll_number = int(input("Enter the roll number: "))
        self.marks = int(input("Enter the marks obtained: "))

    def display_data(self):
        print("\nStudent Details\n")
        print("Student name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


students = []

n = int(input("Enter the no. of students: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    s = Student()
    s.input_data()
    students.append(s)

print("\n--------All Student Records---------\n")

for s in students:
    s.display_data()
