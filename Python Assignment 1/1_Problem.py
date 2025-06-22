"""

1.  Write a program in Python to perform the following
    operation:
    If a number is divisible by 3 it should print “SKILLBREW” as a string
    If a number is divisible by 5 it should print “BRUDITE” as a string
    If a number is divisible by both 3 and 5 it should print “BRUDITE - NIRVANA” as a string.

"""

n = 15

if n % 3 == 0 and n % 5 == 0:
    print("Brudite - Nirvana")
elif n % 3 == 0:
    print("SkillBrew")
elif n % 5 == 0:
    print("Brudite")