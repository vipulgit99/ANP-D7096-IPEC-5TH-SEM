# Accept the number of houses
n = int(input("Enter Number of Houses: "))

# Read units consumed by the first house
units = int(input("Enter Units Consumed: "))
total = units
highest = units
lowest = units

# Read units for remaining houses
for i in range(2, n + 1):
    units = int(input("Enter Units Consumed: "))
    total += units

    if units > highest:
        highest = units

    if units < lowest:
        lowest = units

# Calculate average
average = total / n

# Display results
print("Total Units Consumed =", total)
print("Average Units Consumed =", average)
print("Highest Consumption =", highest)
print("Lowest Consumption =", lowest)



'''-------------------------output-------------------------'''
'''Enter Number of Houses: 2
Enter Units Consumed: 500
Enter Units Consumed: 1000
Total Units Consumed = 1500
Average Units Consumed = 750.0
Highest Consumption = 1000
Lowest Consumption = 500
'''_