"""
5. Write a Python program to find the factorial of a number using a for loop.

"""

def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number n.
    Args:
        n (int): The number to calculate factorial for.
    Returns:
        int: Factorial of n.
    """
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Take user input and print the factorial
num = int(input("Enter a number to find factorial: "))
print(factorial(num))