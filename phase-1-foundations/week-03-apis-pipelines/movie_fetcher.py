import requests
import json

# Free movie API (no signup needed for basic use)
BASE_URL = "https://www.omdbapi.com/"
API_KEY = "trilogy"  # Demo key (limited requests)

def search_movie(title):
    """Search for a movie by title"""
    params = {
        'apikey': API_KEY,
        't': title  # t = title search
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        movie = response.json()
        
        if movie.get('Response') == 'True':
            return movie
        else:
            print(f"❌ Movie not found: {movie.get('Error')}")
            return None
    else:
        print(f"❌ API Error: {response.status_code}")
        return None
    
    
def save_movies_to_file(movies, filename="movies.json"):
    """Save movie data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(movies, f, indent=2)
    print(f"💾 Saved {len(movies)} movies to {filename}")

def load_movies_from_file(filename="movies.json"):
    """Load movie data from JSON file"""
    try:
        with open(filename, 'r') as f:
            movies = json.load(f)
        print(f"📂 Loaded {len(movies)} movies from {filename}")
        return movies
    except FileNotFoundError:
        print(f"⚠️  {filename} not found")
        return []

# Main program
movies_collection = []

while True:
    print("\n--- Movie Collector ---")
    print("1. Search and add movie")
    print("2. Show all movies")
    print("3. Save to file")
    print("4. Load from file")
    print("5. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        title = input("Enter movie title: ")
        movie = search_movie(title)
        if movie:
            movies_collection.append(movie)
            print(f"✅ Added: {movie['Title']}")
    
    elif choice == "2":
        if movies_collection:
            print(f"\n📚 Collection ({len(movies_collection)} movies):")
            for m in movies_collection:
                print(f"- {m['Title']} ({m['Year']}) - {m['imdbRating']}/10")
        else:
            print("Collection is empty")
    
    elif choice == "3":
        save_movies_to_file(movies_collection)
    
    elif choice == "4":
        movies_collection = load_movies_from_file()
    
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice")