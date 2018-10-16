  
#Q.1- Name and handle the exception occured in the following program.
ZeroDivisionError
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as e:
    print("not divided by zero")
#Q.2- Name and handle the exception occurred in the following program:
try:
    l = [1,2,3]
    print(l[3])
except Exception as e:
    print(e)
#Q.3- What will be the output of the following code
an exception
#Q.4- What will be the output of the following code
-5.0
a/b result in 0

#Q.5- Write a program to show and handle following exceptions
# Program to check import error
try:
    from abnddf import abc
except ImportError as e:
    print(e)

#Program to check value error
try:
    a = "abc"
    print(int(a))
except ValueError as e:
    print(e)

# Program to check Index Error
try:
    l = [1,2,3]
    print(l[3])
except IndexError as e:
    print(e)



