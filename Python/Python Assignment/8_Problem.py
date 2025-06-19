a, b = 4, 6

max = a if a > b else b

while True:
    if max % a == 0 and max % b == 0:
        ans = max
        break
    else:
        max += 1

print(ans)