# WAP to Generate Multiplication Table up to 20

while True:
    try:
        # Accept a number from the user
        num = int(input("Enter Number: "))

        # Display multiplication table
        print("\nMultiplication Table of", num)

        for i in range(1, 21):
            print(num, "x", i, "=", num * i)

        # Exit the loop after successful execution
        break

    except ValueError:
        # Handle invalid input
        print("Invalid Input! Please enter an integer only.")

        '''---------------------------output---------------------------'''

    '''Enter Number: 21

Multiplication Table of 21
21 x 1 = 21
21 x 2 = 42
21 x 3 = 63
21 x 4 = 84
21 x 5 = 105
21 x 6 = 126
21 x 7 = 147
21 x 8 = 168
21 x 9 = 189
21 x 10 = 210
21 x 11 = 231
21 x 12 = 252
21 x 13 = 273
21 x 14 = 294
21 x 15 = 315
21 x 16 = 336
21 x 17 = 357
21 x 18 = 378
21 x 19 = 399
21 x 20 = 420'''