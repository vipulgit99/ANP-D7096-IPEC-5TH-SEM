# Initialize variables
deposit = 0
withdrawal = 0
balance = 0

while True:
    # Accept transaction amount
    amount = int(input("Enter Transaction Amount (0 to Stop): "))

    # Stop if user enters 0
    if amount == 0:
        break

    # Check for deposit
    if amount > 0:
        deposit += amount

    # Check for withdrawal
    else:
        withdrawal += abs(amount)

    # Update balance
    balance += amount

# Display the summary
print("Total Deposit =", deposit)
print("Total Withdrawal =", withdrawal)
print("Final Balance =", balance)




'''------------------------output------------------------


                          Enter Number of Employees: 10
Enter Salary: 1000
Enter Salary: 2000
Enter Salary: 3000
Enter Salary: 40000
Enter Salary: 500001
Enter Salary: 600000
Enter Salary: 50000
Enter Salary: 2000
Enter Salary: 5000000
Enter Salary: 8000000
Highest Salary = 8000000
Lowest Salary = 1000
Average Salary = 1419800.1
Employees Earning More Than ₹50,000 = 4'''