"""

9. Write a Python program to count the frequency of each element in a list.
    Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
    Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}

"""

lst = [1, 2, 1]

dictionary = {}

for i in lst:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
        
for key, value in dictionary.items():
    print(f"{key} -> {value}")