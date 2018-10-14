# Q.1 Create a function to calculate the area of a sphere by taking radius from user.
r=float(input("enter the radius"))
a=4*3.14*r**2
print(a)

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
m1=int(input("enterthe maximum value"))
for n in range(2,limit +1):
    sum=0
    for x in range(1,n):
        if not n%x:
            sum +=x
        if sum==n:
            print(n,"is perfect number")       

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user. 
num=int(input("enter the no"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)
#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion. 
def power(x,y):
    if(y==1):
        return(x)
    if(y!=1):
        return(x*power(x,y-1))
x=int(input("Enter base: "))
y=int(input("Enter exponential value: "))
print("Result:",power(x,y))

