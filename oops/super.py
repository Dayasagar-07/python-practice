# super:it is used to call method from a parent class inside a child class,it allows to extend/override inherited methods while still reusing the parent functionalities
class Parent:
    def func(self):
        print("it is a parent class")
class Child(Parent):
    def func(self):
        super().func()
        print("it is a child class")
obj=Child()
obj.func()             

class Employee:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
class Manager(Employee):
    def __init__(self, name, age, email,id):
        super().__init__(name, age, email)   
        self.id=id
obj2=Manager("daya",22,"daya@56gmail.com",3)       
print(obj2.name,obj2.age)    
           