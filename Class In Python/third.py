# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
       
p1= Person("Ram",22)
print(f"Name:{p1.name}")
print(f"Age:{p1.age}")



