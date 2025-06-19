userWord = "Bhanu7"

alpha = 0
num = 0

for userInput in userWord:
    if userInput.isalpha():
        alpha += 1
    if userInput.isdigit():
        num += 1

print(f"Your Alpha is {alpha} & Number is {num}")
    