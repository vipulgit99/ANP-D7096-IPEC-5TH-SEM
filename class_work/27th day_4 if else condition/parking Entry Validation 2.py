# Parking Entry Validation Program

# Take parking pass status as input
parking_pass = int(input("Enter parking pass (1 = Valid Pass, 0 = No Pass): "))

# Validate the input
if parking_pass != 0 and parking_pass != 1:
    print("Invalid Input")

# Check if the parking pass is valid
elif parking_pass == 1:
    print("Entry Allowed")

# If there is no valid parking pass
else:
    print("Entry Denied")



    

'''output
 Enter parking pass (1 = Valid Pass, 0 = No Pass): 1
Entry Allowed'''