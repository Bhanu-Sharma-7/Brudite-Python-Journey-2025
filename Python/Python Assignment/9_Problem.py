lst = [1, 2, 1]

dictionary = {}

for i in lst:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
        
for key, value in dictionary.items():
    print(f"{key} -> {value}")