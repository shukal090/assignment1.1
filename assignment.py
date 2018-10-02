
#Q.1- Take an input year from user and decide whether it is a leap year or not. 

n=int(input("enter the year"))
'''
a year divisible by 4 is a leap year
'''
if (n%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")

    
#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
n=int(input("enter the length"))
m=int(input("enter the breath"))
'''
if length is equalthen it is a square otherwise rectangle
'''
if(n==m):
    print("it is area of square")

else:
    print("it is area of rectangle")

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

num1=int(input ("enter the first age "))
num2=int(input("enter the second age"))
num3=int(input("enter the third age"))
if(num1>=num2)and(num1>=num3):
    print("num1 is oldest")
elif(num2>=num1)and(num2>num3):
    print("num2 is oldest")
elif(num3>=num1)and(num3>=num2):
    print("num3 is oldest")
elif(num1<=num2)and(num1<=num3):
    print("num1 is youngest")
elif(num2<=num1)and(num2<=num3):
    print("num2 is youngest")
elif(num3<=num1)and(num3<=num2):
    print("num3 isyoungest")     

else:
    print("all are equal")

another

num1=int(input ("enter the first age "))
num2=int(input("enter the second age"))
num3=int(input("enter the third age"))
old=max(num1,num2,num3)
young=min(num1,num2,num3)
print("oldest is :",old)
print("youngest is:",young)

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.


age=input("enter the age")
sex=input("enter the sex,(M or F)")
marry=input("enterthe married status,(Y or N)")

if (sex=="F"):
    print("she will work in urban only")
elif (sex=="M")and(age<=20)and(age>=40):
    print("he will work anywhere")
elif (sex=="M")and(age<=40)and(age>=60):
    print("he will work in urban only")
else:
    print("error")          

    
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 

q=int(input("enter the quantity"))
c=q*100
if c >1000:
    discount=(q*100)*.10
    c-=discount
    print("the price is:",c)
else:
    print("the price is :",c)


#  Q.1- Take 10 integers from user and print it on screen.

sum=[]
for i in range(10):
    x=int(input("enter the no"))
    sum.insert(i,x)
    i+=1
print(sum)    

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while True:
    print("infinite")

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list. 
m = list(map(int,input().split()))
m_square = []
for i in m:
    m_square.append(i**2)
print(m_square)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately 
n = ["messi",1,2,3.2,8.4,"ronaldo"]
n_int = []
n_float = []
n_string = []
for i in n:
    if type(i)==int:
        n_int.append(i)
    elif type(i)==float:
        n_float.append(i)
    else:
        n_string.append(i)
print(n_int)
print(n_float)
print(n_string)

#Q.5- Using range(1,101), make a list containing only prime numbers
num = []
for i in range(1,101):
    flag = False
    for j in range(2,i):
        if i%j==0:
            flag = True
    if not flag:
        num.append(i)
print(num)

#Q.6- Print the following patterns:
*
**
***
****

n = 6
for i in range(1,6):
    print(" "*n+"* "*i)
    n-= 1
    
#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.     


l = list(map(int,input("Enter list elements: ").split()))
element = int(input("Enter the element to search: "))
if element in l:
    print("Element found")
    del l[l.index(element)]
print(l)

    
