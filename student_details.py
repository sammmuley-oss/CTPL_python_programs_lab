class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __del__(self):
        print(f"Student {self.name} has been deleted.")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


student1 = student("Sarthak", 20, "A")
student1.display_details()
del student1
student2 = student("Lexi", 22, "B")
student2.display_details()
del student2