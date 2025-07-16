"""

2.  Write a function that reads a text file and returns its lines.
    - Use with open(...) as f:
    - Catch and handle FileNotFoundError with a user-friendly message.
    - From main(), prompt user for file name, call read_lines, then print line count

"""

def read_lines(filename: str):
    """
    Reads all lines from the given file and returns them as a list.
    Handles FileNotFoundError gracefully.
    Args:
        filename (str): The name of the file to read.
    Returns:
        list: List of lines from the file, or empty list if file not found.
    """
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("File is not found.")
        return []

if __name__ == "__main__":
    # Prompt user for filename and print the number of lines in the file
    filename = input("Enter filename: ")
    lines = read_lines(filename)
    print(f"Line count: {len(lines)}")