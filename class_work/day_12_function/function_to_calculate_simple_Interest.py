# Function to calculate Simple Interest



'''---------------------------coding---------------------------'''


def simple_interest(principal, rate, time):
    # Calculate Simple Interest
    si = (principal * rate * time) / 100
    return si

# Take input from the user
p = float(input("Enter Principal: "))
r = float(input("Enter Rate (%): "))
t = float(input("Enter Time (years): "))

# Call the function
interest = simple_interest(p, r, t)

# Display the result
print("Simple Interest =", interest)




'''---------------------------output---------------------------Enter Principal: 10000
Enter Rate (%): 12
Enter Time (years): 5
Simple Interest = 6000.0
'''