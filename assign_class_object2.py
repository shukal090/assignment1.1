
#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class. 
class Circle():
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        return self.radius**2*3.14
    def getCircumference(self):
        return 2*self.radius*3.14

newCircle=Circle(2)
print(newCircle.getArea())
print(newCircle.getCircumference())

#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
      
    print(self.name)
    print(self.roll)
  def setAge(self,age):
    self.age=age
  def setMarks(self,marks):
    self.marks = marks
newStudent=Student()
print(newStudent.display())
print(newStudent.setAge())
print(newStudent.setMarks())

#Q.3- Create a Temprature class and create two methods:
class Temprature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)
newTemperature=Temperature(34)
print(newTemperature.convertFahrenhiet())
print(newTemperature.convertCelsius)

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .

#
    

    
        
    
