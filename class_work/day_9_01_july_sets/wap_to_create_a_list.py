'''# WAP to create a list of 20 numbers given by the user.
# Ask the user to enter any two numbers.
# If both numbers are present in the list,
# remove all duplicate values from the list.
'''




'''--------------CODING STARTS HERE-----------------'''
# Create an empty list
num = []

# Input 20 numbers
for i in range(20):
    n = int(input("Enter a number: "))
    num.append(n)

# Display the original list
print("\nOriginal List:", num)

# Input any two numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Check whether both numbers are present in the list
if n1 in num and n2 in num:

    # Create a new list to store unique elements
    unique = []

    # Remove duplicate values
    for i in num:
        if i not in unique:
            unique.append(i)

    print("\nList after removing duplicate values:")
    print(unique)

else:
    print("\nOne or both numbers are not present in the list.")


    '''--------------------OUTPUT---------------------
    
    Enter a number: 10
Enter a number: 20
Enter a number: 50
Enter a number: 60
Enter a number: 50
Enter a number: 50
Enter a number: 80
Enter a number: 60
Enter a number: 40
Enter a number: 80
Enter a number: 60
Enter a number: 20
Enter a number: 30
Enter a number: 50
Enter a number: 50
Enter a number: 70
Enter a number: 100
Enter a number: 50
Enter a number: 60
Enter a number: 90

Original List: [10, 20, 50, 60, 50, 50, 80, 60, 40, 80, 60, 20, 30, 50, 50, 70, 100, 50, 60, 90]
Enter first number: 80
Enter second number: 50

List after removing duplicate values:
[10, 20, 50, 60, 80, 40, 30, 70, 100, 90]

    
    
    
    '''
