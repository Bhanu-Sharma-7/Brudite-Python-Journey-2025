"""

2.  Write a program that accepts a string as input from the user and calculates the number of digits and letters.
    Input: Hello123
    Output: Alphabets: 5 & Number : 3

"""

userWord = "Bhanu7"

alpha = 0
num = 0

for userInput in userWord:
    if userInput.isalpha():
        alpha += 1
    if userInput.isdigit():
        num += 1

print(f"Your Alpha is {alpha} & Number is {num}")
    