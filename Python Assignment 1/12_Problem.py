"""

12. Write a Python program to reverse a number using a while loop.
    Sample Input: num = 12345
    Sample Output: revnum = 54321

"""

number = 123

rev = 0

while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10

print(rev)