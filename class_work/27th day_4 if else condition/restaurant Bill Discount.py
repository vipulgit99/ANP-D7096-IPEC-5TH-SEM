


''' Restaurant Bill Discount Problem Statement A restaurant offers discounts
 based on the total bill amount. • Bill below ₹1000 → No Discount
     • ₹1000–₹2999 → 10% Discount  • ₹3000 or more → 20% Discount 
       Write a Python program to determine the applicable discount.
         Sample Input 3200 Sample Output 20% Discount Applied '''





#-----------------------------coding----------------------






# Restaurant Bill Discount Program
# This program checks the bill amount and applies the appropriate discount.

# Taking bill amount as input
bill = float(input("Enter the total bill amount (₹): "))

# Input Validation
if bill < 0:
    print("Invalid Input! Bill amount cannot be negative.")

# No Discount
elif bill < 1000:
    print("No Discount Applied.")

# 10% Discount
elif bill >= 1000 and bill < 3000:
    print("10% Discount Applied.")

# 20% Discount
else:
    print("20% Discount Applied.")



    #-------------------------------output---------------------------------

    '''Enter the total bill amount (₹): 3200

            20% Discount Applied'''
    

    #-----------------------------------------------------------------------