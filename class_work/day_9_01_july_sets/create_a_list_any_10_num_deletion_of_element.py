# Program to create a list of 10 numbers and delete an element
# from the position entered by the user using pop()


'''----------------------coding----------------------'''
# Create an empty list
num = []

# Input 10 numbers
for i in range(10):
    n = int(input("Enter a number: "))
    num.append(n)

# Display the original list
print("\nOriginal List:", num)

# Ask the user to enter the position to delete
position = int(input("Enter the position to delete (1-10): "))

# Check if the position is valid
if position >= 1 and position <= len(num):
    deleted = num.pop(position - 1)   # Delete the element

    print("Deleted Element:", deleted)
    print("Updated List:", num)
else:
    print("Invalid Position!")

    '''------------------output------------------
    Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 5
Enter a number: 4
Enter a number: 6
Enter a number: 8
Enter a number: 9
Enter a number: 7
Enter a number: 10

Original List: [1, 2, 3, 5, 4, 6, 8, 9, 7, 10]
Enter the position to delete (1-10): 5
Deleted Element: 4
Updated List: [1, 2, 3, 5, 6, 8, 9, 7, 10]

 '''