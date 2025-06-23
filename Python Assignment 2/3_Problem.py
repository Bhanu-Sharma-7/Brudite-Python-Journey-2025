def show_the_data(path: str, number: int) -> None:
    for i in range(number):
        with open(path, 'r') as f:
            user_data = f.readline()
            print(user_data)

def store_data(data, name: str, score: int) -> None:
    data.append((name, score))

def save_data(path: str, name: str, score: int) -> None:
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
