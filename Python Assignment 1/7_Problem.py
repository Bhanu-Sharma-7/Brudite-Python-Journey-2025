"""

7. Write a Python program to check if a string is an anagram of another string.
    string1 = "listen", string2 = "silent"
    Output: True

"""

# Input strings
str1 = "bhanu"
str2 = "uahbn"

# Check if sorted characters of both strings are equal
if sorted(str1) == sorted(str2):
    print("It is an Anagram")
else:
    print("It is not an Anagram")