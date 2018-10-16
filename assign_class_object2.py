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
class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    def setAge(self):
        self.age = int(input("Enter Age: "))
    def setMarks(self):
        self.marks = int(input("Enter Marks: "))
    def display(self):
        print("Name :"+self.name,"Age :"+str(self.age),"Roll No. :"+str(self.roll_no),"Marks :"+str(self.marks),sep="\n")
student1 = Student("Shukal",10)
student1.setAge()
student1.setMarks()
student1.display()
#Q.3- Create a Temprature class and create two methods:

class Temperature:
    def __init__(self,temp):
        self.temperature = temp
    def convertFahrenheit(self):
        print((self.temperature*(9/5))+32)
    def convertCelcius(self):
        print((self.temperature-32)*5/9)
temp = int(input("Enter Temperature: "))
obj = Temperature(temp)
obj.convertFahrenheit()
obj.convertCelcius()
#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
class MovieDetails:
    def __init__(self,artist,year,ratings):
        self.artistName = artist
        self.year = year
        self.ratings = ratings
        self.movieName = ""
    def Add(self):
        self.movieName = input("Enter movie name: ")
    def Display(self):
        print("Movie Name: "+self.movieName,"Artist Name: "+self.artistName,"Year :"+str(self.year),"Ratings :"+str(self.ratings),sep="\n")
obj = MovieDetails("Akshey",2017,7.6)
obj.Add()
obj.Display()
#Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    def __init__(self,animal_attribute=4):
        self.animal_attribute = animal_attribute
class Tiger(Animal):
    def display(self):
        print(self.animal_attribute)
obj = Tiger()
obj.display()    
#Q.6- What will be the output of following code.
A B
A B

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area
class Shape:
    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.t = ()
    def setValues(self):
        self.length = int(input("Enter Length: "))
        self.breadth = int(input("Enter Breadth: "))
    def Area(self):
        if self.length==self.breadth:
            print("Area of square:",self.length*self.breadth)
        else:
            print("Area of rectangle: ",self.length*self.breadth)
class Square(Shape):
    def __init__(self):
        self.setValues()
        self.Area()
class Rectangle(Shape):
    def __init__(self):
        self.setValues()
        self.Area()
num1 = Square()
num2= Rectangle()        
    


