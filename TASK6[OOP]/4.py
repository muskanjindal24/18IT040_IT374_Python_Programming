from abc import ABC, abstractmethod
class Shapes(ABC):  
    @abstractmethod   
    def getNoOfsides(Self):
        pass

class Rectangle(Shapes): 
    def getNoOfsides(self):
        return 4

class Triangle(Shapes):  
    def getNoOfsides(self):
        return 3
      
class Circle(Shapes):  
    def getNoOfsides(self):
        return 0

a=Rectangle()
print("Number of Wheels in a rectangle:",a.getNoOfsides())
b=Triangle()
print("Number of Wheels in a triangle:",b.getNoOfsides())
c=Circle()
print("Number of sides in a circle:",c.getNoOfsides())