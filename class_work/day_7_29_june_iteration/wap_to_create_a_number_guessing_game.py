# WAP to Create a Number Guessing Game

# Store the secret number
secret_number = 37

while True:
    try:
        # Accept the guessed number from the user
        guess = int(input("Enter your guess: "))

        # Check whether the guess is correct
        if guess == secret_number:
            print("Correct Guess!")
            break      # Exit the loop

        # Check if the guess is too low
        elif guess < secret_number:
            print("Too Low!")

        # Otherwise, the guess is too high
        else:
            print("Too High!")

    except ValueError:
        # Handle invalid input
        print("Invalid Input! Please enter an integer only.")



        '''---------------------------output---------------------------'''
        '''Enter your guess: 80
Too High!
Enter your guess: 30
Too Low!
Enter your guess: 37
Correct Guess!'''