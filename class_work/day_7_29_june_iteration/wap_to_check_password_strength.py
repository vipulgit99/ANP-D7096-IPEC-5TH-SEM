# WAP to Check Password Strength

while True:
    # Accept password from the user
    password = input("Enter Password: ")

    # Check the length of the password
    if len(password) >= 8:
        print("Password Accepted.")
        break      # Exit the loop
    else:
        print("Password too short.")


'''---------------------------------output---------------------------------'''


     '''  Enter Password: vipul
          Password too short.
           Enter Password: vipul@123
           Password Accepted.'''