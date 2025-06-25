import requests
import csv

def movie_data(movieName: str, base_url: str) -> None:
    params = {
        "t": movieName,
        "apikey": "9c0de57c"
    }

    response = requests.get(url=base_url, params=params)
    data = response.json()

    # Check if movie was found
    if data.get("Response") == "False":
        print("Movie not found.")
        return

    # Fields to store
    fields = [
        data.get("Title", ""),
        data.get("Year", ""),
        data.get("Genre", ""),
        data.get("Director", ""),
        data.get("imdbRating", "")
    ]

    # Write to CSV
    with open("bhanu.csv", "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    
    print("Movie data saved successfully.")

def starting_point():
    movieName = input("Enter a movie name: ")
    base_url = "http://www.omdbapi.com/"
    movie_data(movieName, base_url)

if __name__ == "__main__":
    starting_point()
