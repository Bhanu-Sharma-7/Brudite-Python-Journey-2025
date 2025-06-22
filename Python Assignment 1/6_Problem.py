"""

6.  Write a Python program to check if a given number is a perfect number. A Perfect number is a positive integer 
    that is equal to the sum of its proper divisors. For instance, 6 has divisors 1, 2, and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
    Input: 5
    Output: No
    
"""

num, sum = 128, 0

for i in range(num - 1):
    if num % (i + 1) == 0:
        sum = sum + i + 1

if sum == num:     
    print("The given number is perfact number")