"""

3.  Write a Python program to input marks for five subjects Physics, Chemistry, Biology, Mathematics, and Computer.
    Calculate the percentage and grade according to the following:
    Percentage >= 90% : Grade A
    Percentage >= 80% : Grade B
    Percentage >= 70% : Grade C
    Percentage >= 60% : Grade D
    Percentage >= 40% : Grade E
    Percentage < 40% : Grade F

"""

Physics = int(input("Enter Your Physics Number: "))
Chemistry = int(input("Enter Your Chemistry Number: "))
Biology = int(input("Enter Your Biology Number: "))
Mathematics = int(input("Enter Your Mathematics Number: "))
Computer = int(input("Enter Your Computer Number: "))

percentage = ((Physics + Chemistry + Biology + Mathematics + Computer) / 500) * 100

if percentage >= 90 and percentage <= 100:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
elif percentage < 40 and percentage > 0:
    print("Grade F")