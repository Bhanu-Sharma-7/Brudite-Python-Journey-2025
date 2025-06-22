"""
4.  Write a Python program to find the sum of all odd numbers between two given numbers.
    Start = 1, stop = 10
    Sum of odd numbers: 25

"""

ans, start, stop = 0, 1, 10
for i in range(stop):
    if i % 2 != 0:
        ans = ans + i

print(ans)