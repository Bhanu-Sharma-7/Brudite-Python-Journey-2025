"""
2. Write a program that accepts a string as input from the user and calculates the number of digits and letters.
   Input: Hello123
   Output: Alphabets: 5 & Number : 3
"""

def count_alpha_num(text: str) -> None:
    """
    This function takes a string and counts how many alphabets (letters)
    and how many digits (numbers) are present in it. It prints the result.
    """
    alpha_count = 0  # To count letters
    digit_count = 0  # To count numbers

    # Loop through each character in the string
    for char in text:
        if char.isalpha():
            alpha_count += 1  # If character is a letter
        elif char.isdigit():
            digit_count += 1  # If character is a digit

    print(f"Alphabets: {alpha_count} & Numbers: {digit_count}")

# Example usage:
user_input = "Bhanu7"  # You can replace this with input("Enter a string: ")
count_alpha_num(user_input)
    