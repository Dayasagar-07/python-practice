# abstraction:it is the process of hiding implementation details and exposing only the essential functionalities to the user
# abstract base class(ABC):is used to achieve data abstraction by defining a common interface for it subclasses
# abstract classess are created using abc module and @abstractmethod decorator
'''from abc import ABC,abstractmethod
class Greet(ABC):
    @abstractmethod
    def sayhello(self):
        pass
class English(Greet):
    def sayhello(self):
        return "hello"
obj=English()
print(obj.sayhello())'''        

# component of abstraction:
# abstract method:abstract method are method declaration without any body inside an abstract class.the subclasses are forced to override this method by providing their own implementation

# concrete method:these are fully implementend method inside abstract class.subclass can inherit and use directly without overriding

'''from abc import ABC,abstractmethod
class Greet(ABC):
    @abstractmethod
    def sayhello(self):    
        pass
    def sayby(self):
        return "by"
class English(Greet):
    def sayhello(self):
        return "hello"
obj=English()
print(obj.sayhello(),obj.sayby())'''  

# abstract properties:these works like abstrsct method but used for property.this property are declared with @property decorator.subclass are must implement thih property
from abc import ABC,abstractmethod
class Greet(ABC):
    @property
    @abstractmethod
    def sayhello(self):
        pass
class English(Greet):
    @property
    def sayhello(self):
        return "hello"
obj=English()
print(obj.sayhello)        