# Accept the number of students
n = int(input("Enter Number of Students: "))

# Read marks of the first student
marks = int(input("Enter Marks: "))
highest = marks
lowest = marks
total = marks

# Initialize counters
pass_count = 0
distinction_count = 0

# Check first student's result
if marks >= 40:
    pass_count += 1

if marks >= 75:
    distinction_count += 1

# Read marks of remaining students
for i in range(2, n + 1):
    marks = int(input("Enter Marks: "))
    total += marks

    if marks > highest:
        highest = marks

    if marks < lowest:
        lowest = marks

    if marks >= 40:
        pass_count += 1

    if marks >= 75:
        distinction_count += 1

# Calculate average
average = total / n

# Display results
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Average Marks =", average)
print("Number of Students Passed =", pass_count)
print("Number of Students with Distinction =", distinction_count)




'''----------------------output----------------------



Enter Number of Students: 5
Enter Marks: 50
Enter Marks: 0
Enter Marks: 100
Enter Marks: 600
Enter Marks: 90
Highest Marks = 600
Lowest Marks = 0
Average Marks = 168.0
Number of Students Passed = 4
Number of Students with Distinction = 3'''