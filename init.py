# __init__:it is a constructor which is automatically called when an object is created
class Person:
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")
dayasagar=Person("daya",50000,"python")
print(dayasagar.name,dayasagar.salary,dayasagar.language)

# class:it is a collection of object. classes are blueprint for creating object. a class defines a set of attributes or methods that the created object can have

class Dog:
    species="canines"
    def __init__(self,name,age):
        self.name=name
        self.age=age
sagardaya=Dog("nalu",20)
print(sagardaya.name,sagardaya.age,sagardaya.species)

# constructor:it is a special method in python and its automatically called when an object is created
# parametarized constructor:it passes an argument
# default constructor:no parameter is passed

class Person:
    def __init__(self):
        print("i am creating an object")        