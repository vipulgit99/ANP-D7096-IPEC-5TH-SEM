'''Problem 1: Student Management System Problem Statement
 Create a class named Student to store and display a student's details. '''



#==============================coding part========================




# Define the Student class to manage student details
class Student:
    def __init__(self):
        # Initialize instance variables to store student data
        self.student_id = None
        self.name = None
        self.course = None
        self.marks = None

    # Method to take input for student details from the user
    def accept_data(self):
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Name: ")
        self.course = input("Enter Course: ")
        # Convert marks input to a float for numerical comparison
        self.marks = float(input("Enter Marks: "))

    # Method to print all the collected student details
    def display_data(self):
        print("\nStudent Details")
        print(f"Student ID: {self.student_id}")
        print(f"Name : {self.name}")
        print(f"Course: {self.course}")
        print(f"Marks : {self.marks}")

    # Method to evaluate if the student passed or failed
    def check_result(self):
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")

# --- Program Execution ---
# 1. Create an object (instance) of the Student class
student_obj = Student()

# 2. Call the methods sequentially using the object
student_obj.accept_data()
student_obj.display_data()
student_obj.check_result()




#============================output=================
'''Enter Student ID: 858601
Enter Name: vipul chauhan
Enter Course: B.tech
Enter Marks: 78

Student Details
Student ID: 858601
Name : vipul chauhan
Course: B.tech
Marks : 78.0
Result: Pass




Enter Student ID: 773964
Enter Name: anshika mishra
Enter Course: B.tech
Enter Marks: 30

Student Details
Student ID: 773964
Name : anshika mishra
Course: B.tech
Marks : 30.0
Result: Fail'''


