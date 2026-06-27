'''Secure Vault Access Problem Statement A digital vault can only be opened 
if the user enters the correct security code. Write a Python program that accept
s the entered security code. If the entered code is 7890, display: "Access Granted to
 the Vault." Otherwise, do nothing. Sample Input 7890 Sample Output Access Granted to t
 he Vault'''


'''-----------------------------coding-----------------------'''



code = int(input("Enter the security code: "))

if code == 7890:
    print("Access Granted to the Vault.")
else:
    print("Access Denied.")