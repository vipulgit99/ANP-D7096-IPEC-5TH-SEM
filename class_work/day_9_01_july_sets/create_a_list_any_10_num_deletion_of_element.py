
# Program to create a list of 10 numbers and delete an element
# from the position entered by the user
'''----------------------coding----------------------'''

# Create an empty list
num = []

# Input 10 numbers
for i in range(10):
    n = int(input("Enter a number: "))
    num.append(n)

# Display the original list
print("\nOriginal List:", num)

# Ask the user for the position to delete
position = int(input("Enter the position to delete (1-10): "))

# Check whether the position is valid
if position >= 1 and position <= len(num):
    # Delete the element
    del num[position - 1]

    # Display the updated list
    print("Updated List:", num)
else:
    print("Invalid Position!")



'''---------------------output---------------------

Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
Enter a number: 6
Enter a number: 7
Enter a number: 9
Enter a number: 8
Enter a number: 10

Original List: [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]
Enter the position to delete (1-10): 4
Updated List: [1, 2, 3, 5, 6, 7, 9, 8, 10]'''
