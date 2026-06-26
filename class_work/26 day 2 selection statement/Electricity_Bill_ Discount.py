# ------------------------------------------------------------
# Program Name : Electricity Bill Discount
# Description  : This program accepts the electricity bill
#                amount from the user. If the bill amount is
#                ₹5000 or more, a 10% discount is applied.
#                Otherwise, no discount is given.
# ------------------------------------------------------------

# Take the electricity bill amount as input from the user
bill_amount = float(input("Enter the electricity bill amount: "))

# Check whether the bill amount is eligible for discount
if bill_amount >= 5000:
    # Calculate 10% discount
    discount = bill_amount * 0.10

    # Calculate the final bill amount after discount
    final_bill = bill_amount - discount

    # Display the result
    print("Discount Applied!")
    print("Final Bill Amount: ₹", final_bill)

else:
    # No discount is applicable
    print("No Discount Applied!")
    print("Final Bill Amount: ₹", bill_amount)