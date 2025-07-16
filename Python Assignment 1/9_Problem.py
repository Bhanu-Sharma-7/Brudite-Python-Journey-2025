"""

9. Write a Python program to count the frequency of each element in a list.
    Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
    Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}

"""

from collections import Counter

# Input list
lst = [1, 2, 1]

# Use Counter to count frequency of each element
frequency = Counter(lst)
for key, value in frequency.items():
    print(f"{key} -> {value}")