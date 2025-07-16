def show_the_data(path: str, number: int) -> None:
    """
    Display the first 'number' lines from the file at 'path'.
    Handles file not found error gracefully.
    """
    try:
        with open(path, 'r') as f:
            for _ in range(number):
                user_data = f.readline()
                if not user_data:
                    break  # Stop if end of file is reached
                print(user_data.strip())  # Print each line without extra newline
    except FileNotFoundError:
        print(f"File not found: {path}")


def store_data(data, name: str, score: int) -> None:
    # Append a tuple of (name, score) to the data list
    data.append((name, score))


def save_data(path: str, name: str, score: int) -> None:
    # Save the player's name and score to the specified file
    with open(path, "a") as f:
        f.write(f"Player name is {name}, and score is {score}\n")


if __name__ == "__main__":
    path = "demo.csv"
    data = []
    close_program = True
    while close_program:
        print("1. Show the top N scores")
        print("2. Add a new score")
        print("3. Exit")
        try:
            choice = int(input("Enter what you want to do: "))
            match choice:
                case 1:
                    number = int(input("top N scores: "))
                    show_the_data(path, number)
                case 2:
                    name = input("Enter the Name: ")
                    try:
                        score = int(input("Enter the Score: "))
                        store_data(data, name, score)
                        save_data(path, name, score)
                        print(data)
                    except ValueError:
                        print("Error - Input must be a number")
                case 3:
                    close_program = False
        except ValueError:
            print("Enter a integer")
