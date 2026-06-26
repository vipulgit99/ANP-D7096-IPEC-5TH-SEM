# Program: Parking Fee Waiver
# Description:
# This program checks whether a customer gets a parking fee waiver
# based on the purchase amount.
# If the purchase amount is ₹2000 or more, the parking fee is waived.
# Otherwise, a parking fee of ₹100 is charged.

# Taking purchase amount as input from the user
purchase_amount = float(input("Enter the purchase amount: ₹"))

# Checking the purchase amount
if purchase_amount >= 2000:
    print("Parking Fee Waived!")
    print("Parking Fee: ₹0")
else:
    print("Parking Fee Applicable!")
    print("Parking Fee: ₹100")