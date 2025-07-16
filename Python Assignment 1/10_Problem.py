"""

10. Write a Python program to reverse the order of words in a given sentence.
    Input_sentence = “Hello, World! Welcome to Python programming.”
    Output after reverse = “programming. Python to Welcome
    World! Hello,”


"""

# Input string
string = "Bhanu Sharma"

# Split the string into words
word = string.split()

# Reverse the list of words
reverse = word[::-1]
print(reverse)  # Output: ['Sharma', 'Bhanu']

# Join the reversed words with a space to form the reversed sentence
getter = ' '.join(reverse)

print(getter)  # Output: Sharma Bhanu