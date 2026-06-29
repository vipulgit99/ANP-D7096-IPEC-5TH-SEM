# Correct username and password
correct_username = "admin"
correct_password = "python123"

# Allow only 3 login attempts
for attempt in range(1, 4):

    print("Attempt", attempt)

    # Accept username and password
    username = input("Username: ")
    password = input("Password: ")

    # Check credentials
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")

# Lock account after 3 unsuccessful attempts
if attempt == 3 and (username != correct_username or password != correct_password):
    print("Account Locked")





    '''------------------------------output------------------------------


    Attempt 1
Username: admin
Password: vipul123
Invalid Credentials
Attempt 2
Username: admim1232
Password: python321
Invalid Credentials
Attempt 3
Username: admin
Password: python1234
Invalid Credentials
Account Locked




Attempt 1
Username: admin
Password: python123
Login Successful'''


