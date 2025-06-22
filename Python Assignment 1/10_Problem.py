"""

10. Write a Python program to reverse the order of words in a given sentence.
    Input_sentence = “Hello, World! Welcome to Python programming.”
    Output after reverse = “programming. Python to Welcome
    World! Hello,”


"""

string = "Bhanu Sharma"
word = string.split()
reverse = word[::-1]
print(reverse)

getter = ''.join(reverse)

print(getter)