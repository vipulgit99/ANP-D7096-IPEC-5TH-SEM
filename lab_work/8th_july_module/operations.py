# -----------------------------------------
# File Name : main.py
# Purpose   : Menu-driven Geometry Calculator
#             using the twodfigures module.
# -----------------------------------------

# Import the user-defined module
import twodfigures

# Infinite loop to keep the program running
while True:

    # Display the main menu
    print("\n===== GEOMETRY CALCULATOR =====")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    # Take user's choice
    choice = int(input("Enter your choice: "))

    # Exit the program
    if choice == 5:
        print("Thank You!")
        break

    # Display operation menu
    print("\nSelect Operation")
    print("1. Area")
    print("2. Perimeter")

    # Take operation choice
    operation = int(input("Enter your choice: "))

    # -----------------------------
    # Square
    # -----------------------------
    if choice == 1:
        side = float(input("Enter side: "))

        if operation == 1:
            area = twodfigures.square_area(side)
            print("Area of Square =", area)

        elif operation == 2:
            perimeter = twodfigures.square_perimeter(side)
            print("Perimeter of Square =", perimeter)

    # -----------------------------
    # Circle
    # -----------------------------
    elif choice == 2:
        radius = float(input("Enter radius: "))

        if operation == 1:
            area = twodfigures.circle_area(radius)
            print("Area of Circle =", area)

        elif operation == 2:
            circumference = twodfigures.circle_perimeter(radius)
            print("Circumference of Circle =", circumference)

    # -----------------------------
    # Triangle
    # -----------------------------
    elif choice == 3:

        if operation == 1:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            area = twodfigures.triangle_area(base, height)
            print("Area of Triangle =", area)

        elif operation == 2:
            a = float(input("Enter first side: "))
            b = float(input("Enter second side: "))
            c = float(input("Enter third side: "))

            perimeter = twodfigures.triangle_perimeter(a, b, c)
            print("Perimeter of Triangle =", perimeter)

    # -----------------------------
    # Rectangle
    # -----------------------------
    elif choice == 4:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        if operation == 1:
            area = twodfigures.rectangle_area(length, breadth)
            print("Area of Rectangle =", area)

        elif operation == 2:
            perimeter = twodfigures.rectangle_perimeter(length, breadth)
            print("Perimeter of Rectangle =", perimeter)

    # -----------------------------
    # Invalid Choice
    # -----------------------------
    else:
        print("Invalid Choice")

        '''------------------------output------------------------
        
        
        
        ===== GEOMETRY CALCULATOR =====
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice: 1

Select Operation
1. Area
2. Perimeter
Enter your choice: 1
Enter side: 25
Area of Square = 625.0

===== GEOMETRY CALCULATOR =====
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice: 5
Thank You!'''