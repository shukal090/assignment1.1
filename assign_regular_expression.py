#Q.1- Write a python code to find a valid email address from a text
import re
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', "shukal.jain090@yify.com")
for address in addresses: 
    print(address)



#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
import re
pattern=r"^[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$"
if re.search(pattern,"79999999999"):
    print("match 1")
if re.search(pattern,"62843513648"):
    print("match2")
    
