class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class employee(person):
    def __init__(self, name, age, employee_id, department):
        self.employee_id = employee_id
        self.department = department
    
    def display_employee(self):
        self.display_person()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}") 

class manager(employee):
    def __init__(self, name, age, employee_id, department, team_size):    
        self.team_size = team_size
    
    def display_manager(self):
        self.display_employee()
        print(f"Team Size: {self.team_size}")

e = employee("Sarthak", 30, "1234", "Sales")
e.display_employee()

m = manager("Jane", 40, "456", "Marketing", 10)
m.display_manager()