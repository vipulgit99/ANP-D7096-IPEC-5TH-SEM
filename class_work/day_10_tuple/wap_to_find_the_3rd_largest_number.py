# WAP to find the 3rd largest number from a list of 20 numbers given by the user.

# Create an empty list


'''---------------------coding---------------------'''


num = []

# Input 20 numbers from the user
for i in range(20):
    n = int(input("Enter Number: "))
    num.append(n)

# Display the original list
print("\nOriginal List:")
print(num)

# Sort the list in ascending order
num.sort()

# Display the sorted list
print("\nSorted List:")
print(num)

# Display the 3rd largest number
print("\nThird Largest Number =", num[-3])



'''---------------------output---------------------


Enter Number: 80
Enter Number: 30
Enter Number: 40
Enter Number: 90
Enter Number: 20
Enter Number: 25
Enter Number: 45
Enter Number: 95
Enter Number: 85
Enter Number: 48
Enter Number: 47
Enter Number: 42
Enter Number: 12
Enter Number: 32
Enter Number: 2
Enter Number: 15
Enter Number: 85
Enter Number: 65
Enter Number: 95
Enter Number: 85

Original List:
[80, 30, 40, 90, 20, 25, 45, 95, 85, 48, 47, 42, 12, 32, 2, 15, 85, 65, 95, 85]

Sorted List:
[2, 12, 15, 20, 25, 30, 32, 40, 42, 45, 47, 48, 65, 80, 85, 85, 85, 90, 95, 95]

Third Largest Number = 90

'''