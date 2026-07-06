'''Employee Information System Problem Statement: Create
 a dictionary where: • Employee ID is the key. 
   • Value is another dictionary containing:  o Name 
     o Department  o Salary  Perform the following 
     operations: • Display all employee details.  • Search for
       an employee using Employee ID.  • Increase the salary
         of all employees by 10%.  • Display employees belonging 
         to a specific department entered by the user'''


'''------------------------------CODING----------------------------------'''






# Employee Information System

# Create an empty dictionary
employees = {}

# Input details of 3 employees
for i in range(3):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    # Store details in nested dictionary
    employees[emp_id] = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }

# Display all employee details
print("\nEmployee Details")
for emp_id, details in employees.items():
    print("\nEmployee ID:", emp_id)
    print("Name:", details["Name"])
    print("Department:", details["Department"])
    print("Salary:", details["Salary"])

# Search employee using Employee ID
search_id = input("\nEnter Employee ID to Search: ")

if search_id in employees:
    print("\nEmployee Found")
    print("Name:", employees[search_id]["Name"])
    print("Department:", employees[search_id]["Department"])
    print("Salary:", employees[search_id]["Salary"])
else:
    print("Employee Not Found")

# Increase salary by 10%
for emp_id in employees:
    employees[emp_id]["Salary"] = employees[emp_id]["Salary"] * 1.10

print("\nEmployee Details After 10% Salary Increase")
for emp_id, details in employees.items():
    print(emp_id, ":", details)

# Display employees of a specific department
dept = input("\nEnter Department Name: ")

print("\nEmployees in", dept, "Department")

found = False

for emp_id, details in employees.items():
    if details["Department"].lower() == dept.lower():
        print("Employee ID:", emp_id)
        print("Name:", details["Name"])
        print("Salary:", details["Salary"])
        print()
        found = True

if found == False:
    print("No Employee Found")



    '''---------------------output---------------------Enter Employee ID: 101
Enter Employee Name: Amit
Enter Department: IT
Enter Salary: 50000

Enter Employee ID: 102
Enter Employee Name: Neha
Enter Department: HR
Enter Salary: 40000

Enter Employee ID: 103
Enter Employee Name: Rahul
Enter Department: IT
Enter Salary: 60000

Employee Details

Employee ID: 101
Name: Amit
Department: IT
Salary: 50000

Employee ID: 102
Name: Neha
Department: HR
Salary: 40000

Employee ID: 103
Name: Rahul
Department: IT
Salary: 60000

Enter Employee ID to Search: 102

Employee Found
Name: Neha
Department: HR
Salary: 40000

Employee Details After 10% Salary Increase
101 : {'Name': 'Amit', 'Department': 'IT', 'Salary': 55000.0}
102 : {'Name': 'Neha', 'Department': 'HR', 'Salary': 44000.0}
103 : {'Name': 'Rahul', 'Department': 'IT', 'Salary': 66000.0}

Enter Department Name: IT

Employees in IT Department
Employee ID: 101
Name: Amit
Salary: 55000.0

Employee ID: 103
Name: Rahul
Salary: 66000.0'''