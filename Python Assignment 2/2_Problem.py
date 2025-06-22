"""

2.  Write a function that reads a text file and returns its lines.
    - Use with open(...) as f:
    - Catch and handle FileNotFoundError with a user-friendly message.
    - From main(), prompt user for file name, call read_lines, then print line count

"""

def readLines():
    try:
        with open("./Demo.txt", "r") as f:
            fileLines = f.readlines()
            print(len(fileLines))
    except FileNotFoundError:
        print("File is not found.")

readLines()