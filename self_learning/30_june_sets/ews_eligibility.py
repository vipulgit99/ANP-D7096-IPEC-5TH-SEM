
'''create a record of 15 person along with there name and salary
 display the name of person who are eligible for ews category a
   person will be considered in ews category if the the salary 
   is below 5 lakh per annum '''

'''------------------------code starts here------------------------'''






 # Create two blank lists to store names and annual salaries
name = []
salary = []

# Loop to enter details of 15 persons
for i in range(15):

    # Input the name of the person
    n = input("Enter Name of Person " + str(i + 1) + ": ")

    # Validation loop for salary
    while True:

        # Input annual salary
        s = int(input("Enter Annual Salary: "))

        # Check if salary is valid (not negative)
        if s >= 0:
            break          # Exit the loop if salary is valid
        else:
            print("Invalid Salary! Please enter a positive salary.")

    # Store the name and salary in their respective lists
    name.append(n)
    salary.append(s)

# Display the heading
print("\nPersons Eligible for EWS Category")

# Variable to count eligible persons
count = 0

# Check each person's salary
for i in range(15):

    # A person is eligible for EWS if salary is below ₹5,00,000 per annum
    if salary[i] < 500000:

        # Increase the count
        count = count + 1

        # Display serial number, name, and salary of eligible person
        print(count, ".", name[i], "-", salary[i])



        '''---------------------output---------------------
Enter Name of Person 1: a
Enter Annual Salary: 800000
Enter Name of Person 2: b
Enter Annual Salary: 900000
Enter Name of Person 3: c
Enter Annual Salary: 40000
Enter Name of Person 4: d
Enter Annual Salary: 8009
Enter Name of Person 5: e
Enter Annual Salary: 100000
Enter Name of Person 6: f
Enter Annual Salary: 456123
Enter Name of Person 7: g
Enter Annual Salary: 10000000
Enter Name of Person 8: i
Enter Annual Salary: 20000
Enter Name of Person 9: j
Enter Annual Salary: 60000
Enter Name of Person 10: k
Enter Annual Salary: 800000
Enter Name of Person 11: l
Enter Annual Salary: 7856
Enter Name of Person 12: m
Enter Annual Salary: 9054563
Enter Name of Person 13: n
Enter Annual Salary: 7965
Enter Name of Person 14: o
Enter Annual Salary: 500000
Enter Name of Person 15: p
Enter Annual Salary: 99

Persons Eligible for EWS Category
1 . c - 40000
2 . d - 8009
3 . e - 100000
4 . f - 456123
5 . i - 20000
6 . j - 60000
7 . l - 7856
8 . n - 7965
9 . p - 99'''