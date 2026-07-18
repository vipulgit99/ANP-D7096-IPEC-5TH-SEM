'''Problem 2: Bank Account System Problem Statement 
Create a simple Bank Account class that allows users
 to deposit and withdraw money. '''




#=====================coding part=======================================

# Define the BankAccount class for banking operations
class BankAccount:
    def __init__(self):
        # Initialize instance variables for the account details
        self.account_number = None
        self.customer_name = None
        self.balance = 0.0

    # Method to accept initial account details from the user
    def accept_details(self):
        self.account_number = input("Enter Account Number: ")
        self.customer_name = input("Enter Customer Name: ")
        self.balance = float(input("Enter Initial Balance: "))

    # Method to add money to the existing balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful.")

    # Method to deduct money after checking for sufficient funds
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    # Method to display current account summary and balance
    def display_balance(self):
        print("\nAccount Details")
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.balance}")

# --- Program Execution ---
# 1. Create an object of the BankAccount class
account = BankAccount()

# 2. Setup the account details
account.accept_details()

# 3. Prompt user for deposit amount and execute the operation
dep_amount = float(input("Enter Deposit Amount: "))
account.deposit(dep_amount)

# 4. Prompt user for withdrawal amount and execute the operation
with_amount = float(input("Enter Withdrawal Amount: "))
account.withdraw(with_amount)

# 5. Display the final updated balance sheet
account.display_balance()





#=====================================output======================================


'''Enter Account Number: 8586015440
Enter Customer Name: vipul chauhan
Enter Initial Balance: 100000 
Enter Deposit Amount: 500000
Deposit Successful.
Enter Withdrawal Amount: 400000
Withdrawal Successful.

Account Details
Account Number: 8586015440
Customer Name: vipul chauhan
Current Balance: 200000.0




Enter Account Number: 8586015440
Enter Customer Name: vipul chauhan 
Enter Initial Balance: 100000
Enter Deposit Amount: 500000
Deposit Successful.
Enter Withdrawal Amount: 700000
Insufficient Balance.

Account Details
Account Number: 8586015440
Customer Name: vipul chauhan
Current Balance: 600000.0'''