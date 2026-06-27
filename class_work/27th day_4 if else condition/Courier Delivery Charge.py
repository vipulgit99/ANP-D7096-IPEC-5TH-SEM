



'''Courier Delivery Charge Problem Statement A co
urier company calculates delivery charges based on the package weight. • W
eight up to 2 kg → ₹50  • Weight greater than 2 kg and up to 5 kg → ₹100  • Weight grea
ter than 5 kg → ₹180  Write a Python program to disp
lay the delivery charge. Sample Input 4 Sample Output Delivery Charge = ₹100 '''



'''---------------------------------coding ---------------------------------'''



# Courier Delivery Charge Calculator

# Take package weight as input from the user
weight = float(input("Enter the package weight (in kg): "))

# Validate the weight
if weight <= 0:
    print("Invalid Weight")

# Check if weight is up to 2 kg
elif weight <= 2:
    print("Delivery Charge = ₹50")

# Check if weight is greater than 2 kg and up to 5 kg
elif weight <= 5:
    print("Delivery Charge = ₹100")

# If weight is greater than 5 kg
else:
    print("Delivery Charge = ₹180")