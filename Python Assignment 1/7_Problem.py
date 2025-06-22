"""

7. Write a Python program to check if a string is an anagram of another string.
    string1 = "listen", string2 = "silent"
    Output: True

"""

str1 = "bhanu"
str2 = "uahbn"

sorted(str1)
sorted(str2)

if len(str1) == len(str2):
    print("It is an Anagrams")