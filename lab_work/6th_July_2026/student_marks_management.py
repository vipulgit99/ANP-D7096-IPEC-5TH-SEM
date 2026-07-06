'''Problem Statement: Create a dictionary to store the marks
 of 5 students, where the key is the student's name and the 
 value is their marks. Perform the following operations: 
 • Display all student names and marks.  • Add a new student 
 with marks.  • Update the marks of an existing student. 
   • Delete a student by name.  • Display the student who 
   scored the highest marks.  #  Student Marks Management'''



'''------------------------------CODING----------------------------------'''

# Create an empty dictionary
students = {}

# Input details of 5 students
for i in range(5):
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    students[name] = marks
# Display all students and marks
print("\nStudent Records")
for name, marks in students.items():
    print(name, ":", marks)

# Add a new student
new_name = input("\nEnter New Student Name: ")
new_marks = int(input("Enter Marks: "))
students[new_name] = new_marks

print("\nAfter Adding New Student")
for name, marks in students.items():
    print(name, ":", marks)

# Update marks of an existing student
update_name = input("\nEnter Student Name to Update Marks: ")

if update_name in students:
    new_marks = int(input("Enter New Marks: "))
    students[update_name] = new_marks
    print("Marks Updated Successfully")
else:
    print("Student Not Found")

# Delete a student
delete_name = input("\nEnter Student Name to Delete: ")

if delete_name in students:
    del students[delete_name]
    print("Student Deleted Successfully")
else:
    print("Student Not Found")

# Display final records
print("\nFinal Student Records")
for name, marks in students.items():
    print(name, ":", marks)

# Display student with highest marks
highest_marks = max(students.values())

for name, marks in students.items():
    if marks == highest_marks:
        print("\nHighest Scorer")
        print(name, ":", marks)





        '''------------------------output------------------------
        
        
        
        
        
        
        
        Enter Student Name: vipul chauhan
Enter Marks: 100
Enter Student Name: dipanshu sharma
Enter Marks: 99
Enter Student Name: anshika mishra
Enter Marks: 98
Enter Student Name: lokesh mishra
Enter Marks: 97
Enter Student Name: utkarsh singh
Enter Marks: 96

Student Records
vipul chauhan : 100
dipanshu sharma : 99
anshika mishra : 98
lokesh mishra : 97
utkarsh singh : 96

Enter New Student Name: tripti mishra
Enter Marks: 95

After Adding New Student
vipul chauhan : 100
dipanshu sharma : 99
anshika mishra : 98
lokesh mishra : 97
utkarsh singh : 96
tripti mishra : 95

Enter Student Name to Update Marks: anshika mishra
Enter New Marks: 100
Marks Updated Successfully

Enter Student Name to Delete: lokesh mishra
Student Deleted Successfully

Final Student Records
vipul chauhan : 100
dipanshu sharma : 99
anshika mishra : 100
utkarsh singh : 96
tripti mishra : 95

Highest Scorer
vipul chauhan : 100

Highest Scorer
anshika mishra : 100'''