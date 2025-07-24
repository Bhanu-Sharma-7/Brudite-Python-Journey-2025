import requests
import csv
import sys
from typing import Dict, Optional

class MovieDataFetcher:
    """
    A class to fetch and store movie data from OMDB API.
    
    Attributes:
        base_url (str): The base URL for OMDB API
        api_key (str): The API key for authentication
        csv_filename (str): Name of the CSV file to store data
    """
    
    def __init__(self, api_key: str, csv_filename: str = "movie_data.csv"):
        """
        Initialize the MovieDataFetcher with API key and CSV filename.
        
        Args:
            api_key: OMDB API key
            csv_filename: Output CSV filename (default: 'movie_data.csv')
        """
        self.base_url = "http://www.omdbapi.com/"
        self.api_key = api_key
        self.csv_filename = csv_filename
        self._initialize_csv()

    def _initialize_csv(self) -> None:
        """Initialize CSV file with headers if it doesn't exist."""
        try:
            with open(self.csv_filename, 'x', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Title", "Year", "Genre", "Director", "IMDB Rating"])
        except FileExistsError:
            pass

    def _fetch_movie_data(self, movie_name: str) -> Optional[Dict]:
        """
        Fetch movie data from OMDB API.
        
        Args:
            movie_name: Name of the movie to search
            
        Returns:
            Dictionary containing movie data or None if not found
        """
        params = {
            "t": movie_name,
            "apikey": self.api_key,
            "type": "movie"
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def save_movie_data(self, movie_name: str) -> bool:
        """
        Save movie data to CSV file.
        
        Args:
            movie_name: Name of the movie to search and save
            
        Returns:
            True if data was saved successfully, False otherwise
        """
        data = self._fetch_movie_data(movie_name)
        
        if not data or data.get("Response") == "False":
            print(f"Movie '{movie_name}' not found or error occurred.")
            return False
        
        fields = [
            data.get("Title", "N/A"),
            data.get("Year", "N/A"),
            data.get("Genre", "N/A"),
            data.get("Director", "N/A"),
            data.get("imdbRating", "N/A")
        ]
        
        try:
            with open(self.csv_filename, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
            return True
        except IOError as e:
            print(f"Error writing to file: {e}")
            return False

def main():
    """Main function to run the movie data fetcher."""
    print("=== Movie Data Fetcher ===")
    
    # In production, use environment variables for API keys
    API_KEY = "9c0de57c"  # Replace with your actual API key
    
    fetcher = MovieDataFetcher(api_key=API_KEY)
    
    while True:
        try:
            movie_name = input("\nEnter a movie name (or 'quit' to exit): ").strip()
            if movie_name.lower() in ('quit', 'exit'):
                break
                
            if not movie_name:
                print("Please enter a valid movie name.")
                continue
                
            if fetcher.save_movie_data(movie_name):
                print(f"Data for '{movie_name}' saved successfully!")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

if __name__ == "__main__":
    main()