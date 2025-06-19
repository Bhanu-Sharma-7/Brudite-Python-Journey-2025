num, sum = 128, 0

for i in range(num - 1):
    if num % (i + 1) == 0:
        sum = sum + i + 1

if sum == num:     
    print("The given number is perfact number")