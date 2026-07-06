'''Student Subject Report Card Problem Statement:
 Create a nested dictionary to store marks of students 
 in three subjects. Example: 'Priya': {'Math': 78, 'Science':
   95, 'English': 82}, 'Ankit': {'Math': 91, 'Science': 89, 
   'English': 94} } Write a program to: • Calculate the total
     marks of each student.  • Calculate the average marks of
       each student.  • Display the topper based on total marks.
           • Display the subject-wise highest marks along with the 
           student's name.  • Display students whose average is
             greater than or equal to 85. '''


'''--------------------------------coding----------------------------------'''







# Student Subject Report Card

# Create a nested dictionary
students = {
    "Priya": {"Math": 78, "Science": 95, "English": 82},
    "Ankit": {"Math": 91, "Science": 89, "English": 94},
    "Rahul": {"Math": 85, "Science": 80, "English": 88}
}

# Display Total and Average of each student
print("Student Report Card")

topper = ""
highest_total = 0

for name, marks in students.items():

    total = marks["Math"] + marks["Science"] + marks["English"]
    average = total / 3

    print("\nStudent Name :", name)
    print("Total Marks :", total)
    print("Average Marks :", average)

    # Find topper
    if total > highest_total:
        highest_total = total
        topper = name

# Display Topper
print("\nTopper")
print(topper, "with Total Marks =", highest_total)

# Subject-wise Highest Marks
subjects = ["Math", "Science", "English"]

print("\nSubject-wise Highest Marks")

for subject in subjects:

    highest = 0
    student = ""

    for name, marks in students.items():

        if marks[subject] > highest:
            highest = marks[subject]
            student = name

    print(subject, ":", student, "-", highest)

# Display students whose average >= 85
print("\nStudents having Average >= 85")

for name, marks in students.items():

    total = marks["Math"] + marks["Science"] + marks["English"]
    average = total / 3

    if average >= 85:
        print(name, ":", average)




        '''-------------------output-------------------Student Report Card

Student Name : Priya
Total Marks : 255
Average Marks : 85.0

Student Name : Ankit
Total Marks : 274
Average Marks : 91.33

Student Name : Rahul
Total Marks : 253
Average Marks : 84.33

Topper
Ankit with Total Marks = 274

Subject-wise Highest Marks
Math : Ankit - 91
Science : Priya - 95
English : Ankit - 94

Students having Average >= 85
Priya : 85.0
Ankit : 91.33'''