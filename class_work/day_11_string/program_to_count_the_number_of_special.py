# Program to count the number of special characters in a sentence



'''------------------------------CODING----------------------------------'''

# Take input from the user
sentence = input("Enter a sentence: ")

# Variable to store the count of special characters
special_count = 0

# Traverse each character in the sentence
for ch in sentence:

    # Check if the character is not a letter, digit, or space
    if not (ch.isalpha() or ch.isdigit() or ch.isspace()):
        special_count += 1

# Display the result
print("Number of Special Characters:", special_count)


'''--------------------------------------output-------------------------------------



Enter a sentence: fgnggfrdcw@#$%&^%$#@

Number of Special Characters: 10'''