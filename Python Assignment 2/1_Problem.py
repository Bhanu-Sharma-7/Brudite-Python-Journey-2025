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
    squares = []
    for convert in number:
        squares.append(convert * convert)
    return squares


print(compute_squares([1, 2, 3]))
print(compute_squares([2, 3, 4]))