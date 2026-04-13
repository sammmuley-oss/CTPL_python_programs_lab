class student:
    def __new__(cls,name,*args,**kwargs):
        print("creating instance using __new__")
        return super().__new__(cls)

    def __init__(self,*args,**kwargs):
        print("initializing instance using __init__")
        self.name=args[0] if args else kwargs.get('name')
    
    def __str__(self):
        return f"student name is {self.name}"
    
s1=student("LEXII")
print(s1)

s2=student(name="SZA") #using keyword argument
print(s2)