
'''Problem Statement 1: Student Grade Calculator Write
 a Python program that defines a function calculate_grade(marks).
   The function should: • Accept marks (0–100) as a parameter. 
     • Return the grade according to the following criteria:
         o 90 and above → A+ 
           o 75–89 → A  
           o 60–74 → B 
             o 40–59 → C  
             o Below 40 → Fail 
               The main program should: 
               • Accept marks of 5 students. 
               • Call the function for each student. 
               • Display the marks and corresponding grade.  '''




'''---------------------------coding---------------------------'''







# Function to calculate grade based on marks
def calculate_grade(marks):
    # Check the grade according to the given criteria
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# Main program

# Repeat the process for 5 students
for i in range(1, 6):

    # Take marks as input from the user
    marks = float(input(f"Enter marks of Student {i}: "))

    # Call the function to calculate the grade
    grade = calculate_grade(marks)

    # Display the marks and corresponding grade
    print("Marks:", marks)
    print("Grade:", grade)
    print("----------------------")




    '''----------------output---------------------------------
    
    Enter marks of Student 1: 100
Marks: 100.0
Grade: A+
----------------------
Enter marks of Student 2: 52
Marks: 52.0
Grade: C
----------------------
Enter marks of Student 3: 45
Marks: 45.0
Grade: C
----------------------
Enter marks of Student 4: 30
Marks: 30.0
Grade: Fail
----------------------
Enter marks of Student 5: 80
Marks: 80.0
Grade: A
----------------------
'''