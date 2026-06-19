# polymorphism:manyforms and allows the same method,function/operator to be behave differently on the object and data it works with
# compile time polymorphism(method overloading)
# run time polymorphism(methodoverriding)it means the behaviour of method is decided while program is running, based on the object calling it

class Animal:
    def sound(self):
        return "some generic sound"
class Dog(Animal):
    def sound(self):
        return "bark" 
class Cat(Animal):
    def sound(self):
        return "meow"
dayasagar=[Dog(),Cat()]
for i in dayasagar:
    print(i.sound())

class Vehicle:
    def start(self):
        raise NotImplementedError("most implementend this")
class Car(Vehicle):
    def start(self):
        return "car started" 
class Bike(Vehicle):
    def start(self):
        return "bike started"
sagardaya=[Car(),Bike()]
for i in sagardaya:
    print(i.start())

class Area:
    def area(self):
        raise NotImplementedError("most implemented this")
class Rectangle(Area):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Area):      
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius*self.radius*3.141
majhi=[Rectangle(3,4),Circle(5)]
for i in majhi:
    print(i.area())   

# payment system
class Payment:
    def payment(self):
        raise NotImplementedError("most implemented this")
class CreditCard(Payment):
    def payment(self):
        return "paid 1000 using credit card"  
class UPI(Payment):
    def payment(self):
        return "paid 1000 using UPI"
class Cash(Payment):
    def payment(self):
        return "paid 1000 using cash"       
dsm=[CreditCard(),UPI(),Cash()]    
for i in dsm:
    print(i.payment()) 

# Notification system
 def payment(self):
        raise NotImplementedError("most implemented this")
class CreditCard(Payment):
    def payment(self):
        return "paid 1000 using credit card"  
class UPI(Payment):
    def payment(self):
        return "paid 1000 using UPI"
class Cash(Payment):
    def payment(self):
        return "paid 1000 using cash"       
dsm=[CreditCard(),UPI(),Cash()]    
for i in dsm:
    print(i.payment())

 # login system
 def payment(self):
        raise NotImplementedError("most implemented this")
class CreditCard(Payment):
    def payment(self):
        return "paid 1000 using credit card"  
class UPI(Payment):
    def payment(self):
        return "paid 1000 using UPI"
class Cash(Payment):
    def payment(self):
        return "paid 1000 using cash"       
dsm=[CreditCard(),UPI(),Cash()]    
for i in dsm:
    print(i.payment()) 

