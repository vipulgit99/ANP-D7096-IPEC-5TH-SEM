# WAP to Verify ATM PIN

# Store the correct PIN
correct_pin = 4589

while True:
    try:
        # Accept PIN from the user
        pin = int(input("Enter PIN: "))

        # Check if the entered PIN is correct
        if pin == correct_pin:
            print("Access Granted")
            break   # Exit the loop
        else:
            print("Incorrect PIN")

    except ValueError:
        # Handle invalid input
        print("Invalid Input! Please enter a 4-digit numeric PIN.")