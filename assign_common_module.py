# Q.1- Print the current day using Datetime module.
from datetime import date
import calender
my_date=date.today()
print(calendar.day_name[my_date.weekday()])
#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
import time

total_breaks=1
break_count=0

while(break_count<total_breaks):
    print("this program started on time"+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=P5N6-yrMIGU")
    break_count +=1

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os
path=r'D:\python'
files=os.listdir(path)
i=1
for file in files:
    os.rename(os.path.join(path,file),
              os.path.join(path,str(i)+'.jpg'))
   
    i=i+1

