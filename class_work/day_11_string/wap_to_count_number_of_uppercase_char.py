'''wap to count number of uppercase char as well
 as lowecase char in given sentence without using library function '''




'''-----------------------------coding----------------------------------'''




sentence = input("Enter a sentence: ")

upper = 0
lower = 0

# Traverse each character of the sentence
for x in sentence:

    # Check for uppercase letters (A-Z)
    if x >= 'A' and x <= 'Z':
        upper += 1

    # Check for lowercase letters (a-z)
    elif x >= 'a' and x <= 'z':
        lower += 1

# Display the result
print("Number of Uppercase letters =", upper)
print("Number of Lowercase letters =", lower) 
 




 '''-------------------------------------output-------------------------------------
 
 
 
 
 Enter a sentence: VIPUL chauhan
Number of Uppercase letters = 5
Number of Lowercase letters = 7
'''