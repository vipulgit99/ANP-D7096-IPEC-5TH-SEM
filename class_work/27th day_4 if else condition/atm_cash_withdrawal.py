#-------------------------------------------------------------------------------

'''ATM Cash Withdrawal  Problem Statement A customer can withdraw money only 
if the requested amount does not exceed the available balance. Accept the account
 balance and withdrawal amount. • If withdrawal amount is less than or equal to balance, 
display: Transaction Successful • Otherwise display: Insufficient Balance 
Sample Input 5000 4500 Sample Output Transaction Successful '''

#-------------------------------------------------------------------------------


#-----------------------------coding----------------------




# ATM Cash Withdrawal Program
# This program checks whether the withdrawal amount
# is less than or equal to the available account balance.

# Accept account balance
balance = float(input("Enter Account Balance: "))

# Validate account balance
if balance < 0:
    print("Account Balance cannot be negative.")

else:
    # Accept withdrawal amount
    withdraw_amount = float(input("Enter Withdrawal Amount: "))

    # Validate withdrawal amount
    if withdraw_amount < 0:
        print("Withdrawal Amount cannot be negative.")

    # Check if withdrawal is possible
    elif withdraw_amount <= balance:
        print("Transaction Successful")

    # Insufficient balance
    else:
        print("Insufficient Balance")



        #-------------------------------output---------------------------------
        '''Enter Account Balance: 5000
           Enter Withdrawal Amount: 4500
           Transaction Successful'''
        
        #-----------------------------------------------------------------------