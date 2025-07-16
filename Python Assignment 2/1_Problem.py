"""

1.  Turn the following snippet into a function:
    numbers = [1,2,3,4,5]
    squares = []
    for n in numbers:
        squares.append(n*n)
    print(squares)
    Requirements:
    - Create def compute_squares(nums: list[int]) -> list[int]
    - Add a docstring and type hints
    - Call it on at least two different lists

"""

from typing import List

def compute_squares(number: List[int]) -> List[int]:
    """
    Return a list of squares of the given numbers.
    Args:
        number (List[int]): List of integers to be squared.
    Returns:
        List[int]: List containing squares of the input numbers.
    """
    # Using list comprehension for concise and efficient code
    return [x * x for x in number]

# Example usage
print(compute_squares([1, 2, 3]))  # Output: [1, 4, 9]
print(compute_squares([2, 3, 4]))  # Output: [4, 9, 16]