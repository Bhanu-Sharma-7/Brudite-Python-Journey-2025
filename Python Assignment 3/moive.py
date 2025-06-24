import requests
import csv

API_KEY = "9c0de57c"
BASE_URL = "http://www.omdbapi.com/"
CSV_FILE = "movie.csv"

def fetch_movie_data(title):
    params = {"t": title, "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params).json()

    if response.get("Response") == "True":
        return {
            "Title": response.get("Title", "N/A"),
            "Year": response.get("Year", "N/A"),
            "Genre": response.get("Genre", "N/A"),
            "IMDB_Rating": response.get("imdbRating", "N/A")
        }
    else:
        print("Movie not found!")
        return None

def save_to_csv(data):
    fieldnames = ["Title", "Year", "Genre", "IMDB_Rating"]
    try:
        with open(CSV_FILE, "x", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
    except FileExistsError:
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(data)

def main():
    title = input("Enter movie name: ")
    data = fetch_movie_data(title)
    if data:
        save_to_csv(data)
        print("Saved to movie.csv")

if __name__ == "__main__":
    main()
