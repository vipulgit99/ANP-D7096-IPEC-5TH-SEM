# WAP to create a tuple of 15 numbers entered by the user
# and display all the odd numbers present in the tuple.

# Create an empty list to store the input numbers
num = []

# Take 15 numbers as input from the user
for i in range(15):
    n = int(input("Enter number: "))   # Input a number
    num.append(n)                      # Add the number to the list

# Convert the list into a tuple
t = tuple(num)

# Display the tuple
print("\nTuple is:")
print(t)

# Display all odd numbers present in the tuple
print("\nOdd numbers are:")

# Traverse each element of the tuple
for i in t:

    # Check whether the current number is odd
    if i % 2 != 0:
        print(i, end=" ")   # Display the odd number


        '''------------------------output------------------------


        Enter number: 50
Enter number: 60
Enter number: 65
Enter number: 45
Enter number: 85
Enter number: 78
Enter number: 65
Enter number: 12
Enter number: 32
Enter number: 25
Enter number: 85
Enter number: 45
Enter number: 65
Enter number: 25
Enter number: 36

Tuple is:
(50, 60, 65, 45, 85, 78, 65, 12, 32, 25, 85, 45, 65, 25, 36)

Odd numbers are:
65 45 85 65 25 85 45 65 25 '''