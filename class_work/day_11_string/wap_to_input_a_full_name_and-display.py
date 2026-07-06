# WAP to input a full name and display the first name
# without using any library function
'''------------------------------CODING----------------------------------'''




# Take full name as input from the user
name = input("Enter your full name: ")

# Initialize an empty string to store the first name
first_name = ""

# Traverse each character of the name
for ch in name:

    # Stop when a space is encountered
    if ch == " ":
        break

    # Add the character to first_name
    first_name += ch

# Display the first name
print("First Name =", first_name)



'''---------------------------output----------------------------------


Enter your full name: dipu vipu
First Name = dipu'''