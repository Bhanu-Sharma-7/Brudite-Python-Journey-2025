"""

8. Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
    number1 = 12, number2 = 18
    LCM of 12 and 18 are: 36

"""

import math

# Input numbers
a, b = 4, 6

# Calculate LCM using GCD
lcm = a * b // math.gcd(a, b)
print(lcm)  # Output: 12