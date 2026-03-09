# Catalog class - manages a collection of Content objects

from content import Content

class Catalog:
    def __init__(self):
        self.items = []  # Empty list to store Content objects
    
    def add_content(self, content):
        """Add a Content object to the catalog"""
        self.items.append(content)
        print(f"✅ Added: {content.title}")
    
    def exists(self, title):
        """Check if content with this title already exists"""
        for item in self.items:
            if item.title.lower() == title.lower():
                return True
        return False
    
    def remove_content(self, title):
        """Remove content by title"""
        for item in self.items:
            if item.title.lower() == title.lower():
                self.items.remove(item)
                print(f"❌ Removed: {item.title}")
                return
        print(f"⚠️  '{title}' not found in catalog")
    
    def search_by_genre(self, genre):
        """Find all content matching a genre"""
        results = []
        for item in self.items:
            if item.matches_genre(genre):
                results.append(item)
        return results
    
    def display_all(self):
        """Show all content in the catalog"""
        if len(self.items) == 0:
            print("Catalog is empty")
            return
        
        print(f"\n=== Catalog ({len(self.items)} items) ===")
        for item in self.items:
            print(f"- {item.title} ({item.genre}, {item.duration} min)")
    
    def save_to_file(self, filename="catalog.json"):
        """Save catalog to JSON file"""
        import json
        
        data = []
        for item in self.items:
            data.append({
                'title': item.title,
                'genre': item.genre,
                'duration': item.duration,
                'release_year': item.release_year
            })
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Saved {len(self.items)} items to {filename}")
    
    def load_from_file(self, filename="catalog.json"):
        """Load catalog from JSON file"""
        import json
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.items = []  # Clear current items
            for item_data in data:
                content = Content(
                    item_data['title'],
                    item_data['genre'],
                    item_data['duration'],
                    item_data['release_year']
                )
                self.items.append(content)
            
            print(f"📂 Loaded {len(self.items)} items from {filename}")
        except FileNotFoundError:
            print(f"⚠️  {filename} not found. Starting with empty catalog.")
    
    def search(self, **kwargs):
        """
        Advanced search with multiple filters
        Usage: catalog.search(genre="Drama", min_duration=40)
        """
        results = self.items.copy()  # Start with all items
        
        # Filter by genre if provided
        if 'genre' in kwargs:
            results = [item for item in results if item.matches_genre(kwargs['genre'])]
        
        # Filter by minimum duration
        if 'min_duration' in kwargs:
            results = [item for item in results if item.duration >= kwargs['min_duration']]
        
        # Filter by maximum duration
        if 'max_duration' in kwargs:
            results = [item for item in results if item.duration <= kwargs['max_duration']]
        
        # Filter by year
        if 'year' in kwargs:
            results = [item for item in results if item.release_year == kwargs['year']]
        
        return results
    
    def get_stats(self):
        """Generate statistics about the catalog"""
        # Step 1: Count total items
        total = len(self.items)
        
        # Step 2: Count movies vs episodes
        movie_count = 0 
        episode_count = 0
        for item in self.items:
            if item.is_movie():
                movie_count += 1
            else:
                episode_count += 1

        # Step 3: Count genres
        genres = {}
        for item in self.items:
            if item.genre in genres:
                genres[item.genre] +=1
            else:
                genres[item.genre] =1
        # Step 4: Print everything
        print("\n" + "="*40)
        print("📊 CATALOG STATISTICS")
        print("="*40)
        print(f"Total Items:    {total}")
        print(f"Movies:         {movie_count}")
        print(f"Episodes:       {episode_count}")
        print()
        print("Genre Breakdown:")
        for genre, count in genres.items():
            print(f"  {genre}: {count}")
        print("="*40)





# Test code
catalog = Catalog()
catalog.load_from_file()

# Search examples
print("\n--- All Drama shows ---")
dramas = catalog.search(genre="Drama")
for show in dramas:
    print(f"- {show.title}")

print("\n--- Movies (>80 min) ---")
movies = catalog.search(min_duration=80)
for show in movies:
    print(f"- {show.title} ({show.duration} min)")

print("\n--- Shows from 2016 ---")
shows_2016 = catalog.search(year=2016)
for show in shows_2016:
    print(f"- {show.title}")

print("\n--- Drama movies (combined filters) ---")
drama_movies = catalog.search(genre="Drama", min_duration=80)
for show in drama_movies:
    print(f"- {show.title}")


# Show statistics
catalog.get_stats()

