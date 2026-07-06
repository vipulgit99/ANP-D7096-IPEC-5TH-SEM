# WAP to input a sentence and count the number of vowels present in it





'''------------------------------CODING----------------------------------'''



# Take input from the user

sentence = input("Enter a sentence: ")

# Initialize vowel counter
vowels = 0

# Traverse each character in the sentence
for x in sentence:

    # Check if the character is a vowel
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or
        x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
        

        vowels=vowels+1

# Display the total number of vowels
print("Number of vowels =", vowels)



'''------------------------------OUTPUT----------------------------------




Enter a sentence: vipul chauhan
Number of vowels = 5
'''