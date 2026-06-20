# inheritance: it is a fundamental concepts in oops that allows class(child/derived class)to inherit attributes and methods from another class(parent/base class)
class Animal:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("animal name",self.name)
class Dog(Animal):
    def sound(self):
        print(self.name,"barks")
virat=Dog("kohil") 
virat.info()
virat.sound()

# super():it is used to call methods from a super class. in perticular it is commonly used in child class __init__ methods to initialize inherited attribute
class Animal:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("animal name",self.name)
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def details(self):
        print(self.name,"is a",self.breed)
d=Dog("im aam","labrador")
d.info()
d.details()                    
    
# Types of inheritance 
# single inheritance
class Parent:
    def func1(self):
        print("parent class")
class Child(Parent):
    def func2(self):
        print("child class")
obj=Child()
obj.func1()
obj.func2()                 

# multiple inheritance
# class Mother:
#     def __init__(self,motherName):
#         self.motherName=motherName
#     def mother(self):
#         print(self.motherName)
# class Father:
#     def __init__(self,fatherName):
#         self.fatherName=fatherName
#     def father(self):
#         print(self.fatherName)       
# class Child(Father,Mother):
#     def parent(self):
#         print(self.fatherName,self.motherName)
# obj2=Child("pramod","raimat")
# obj2.father()
# obj2.mother()
# obj2.parent()     

# multilevel inheritance
class Grandfather:
    def __init__(self,grandfatherName):
        self.grandfatherName=grandfatherName
class Father(Grandfather):
    def __init__(self,fatherName,grandfatherName):
        self.fatherName=fatherName
        Grandfather.__init__(self,grandfatherName)      
class Son(Father):
    def __init__(self,sonName,fatherName, grandfatherName):
        self.sonName=sonName
        Father.__init__(self,fatherName, grandfatherName)          
    def print_name(self):
        print("grandfatherName:",self.grandfatherName)    
        print("fatherName:",self.fatherName)
        print("sonName:",self.sonName)
obj3=Son("dibyanshu","pramod","karunakar")
obj3.print_name()        

# hierarchical inheritance
class Parent:
    def func1(self):
        print("this is parent class")
class child1(Parent):
    def func2(self):
        print("this is child1")
class child2(Parent):
    def func3(self):
        print("this is child2")
obj4=child1()
obj5=child2()
obj4.func2()
obj5.func3()

# hybrid inheritance
class School:
    def func1(self):
        print("this function is in school")
class Student1(School):
    def func2(self):
        print("this function is in student1")
class Student2(School):
    def func3(self):
        print("this function is in student2")
class Student3(Student1,School):
    def func4(self):
        print("this function is in student3")
obj6=Student3()
obj6.func4()
obj6.func1()
obj6.func2()                       