

#Q.1- Reverse the whole lst using list methods.

lst=['messi','ronaldo',10,34,'neymar']
lst.reverse()
print(lst)

#Q.2- Print all the uppercase letters from a string.

s=("Pep Guardiola is Best Football Manager")
for i in s:
    if i==i.upper():
        print(i,end=',')

#Q.3- Split the user input on comma's and store the values in a list as integers.
x=list(map(int,input("enter no of elements").split(",")))
print(x)

#Q.4- Check whether a string is palindromic or not.

s=input("enter the string")
if s[::-1]==s:
    print("itis palidrome:")
else:
    print("itis not palidrome")


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)  

