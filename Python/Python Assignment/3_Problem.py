Physics = 78
Chemistry = 90
Biology = 78
Mathematics = 99
Computer = 100

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