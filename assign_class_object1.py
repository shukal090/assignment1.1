#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop. 
d={'messi':10,'ronaldo':7,'becham':9}
for number_key,values in d.items():
    print(number_key,"corresponds to",d[number_key])
#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject.
student = {
            "Ram":{"Maths":85,"Science":80,"English":83},
            "Sham":{"Maths":59,"Science":70,"English":75}
          }
studentName = input("Enter the name of student: ")
if studentName in student:
    print(studentName)
    for key,value in student[studentName].items():
        print(key,value)
else:
    print("Student not found")

