number = 987

while number > 9:
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
    number = sum

print(number)