


'''Mobile Battery Warning Problem Statement A smartphone displays a low battery
 warning only when the battery percentage falls below 15%. Write a Pytho
n program to accept the battery percentage. If the battery is below 15, display: 
connect Charger Immediately Otherwise, display nothing. Sample Input 
10 Sample Output Connect Charger Immediately'''




'''-------------------------coding starts here-------------------------'''





# Mobile Battery Warning Program

# Take battery percentage as input from the user
battery = int(input("Enter battery percentage: "))

# Validate the battery percentage
if battery < 0 or battery > 100:
    print("Invalid Battery Percentage")

# Check if battery is below 15%
elif battery < 15:
    print("Connect Charger Immediately")

# If battery is 15% or above
else:
    print("Battery Level is Normal")