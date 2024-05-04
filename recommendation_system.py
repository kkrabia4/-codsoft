# Hardcoded dataset of movies and their genres
movies = {
    'The Shawshank Redemption': ['Drama'],
    'The Godfather': ['Drama', 'Crime'],
    'The Dark Knight': ['Action', 'Crime', 'Drama'],
    'Pulp Fiction': ['Crime', 'Drama'],
    'The Lord of the Rings: The Return of the King': ['Adventure', 'Drama', 'Fantasy'],
    'Forrest Gump': ['Drama', 'Romance'],
    'Inception': ['Action', 'Adventure', 'Sci-Fi'],
    'The Matrix': ['Action', 'Sci-Fi'],
    'Interstellar': ['Adventure', 'Drama', 'Sci-Fi'],
    'The Silence of the Lambs': ['Crime', 'Drama', 'Thriller']
}

def recommend_movies(preferred_genres):
    recommended_movies = []
    for movie, genres in movies.items():
        if any(genre in genres for genre in preferred_genres):
            recommended_movies.append(movie)
    return recommended_movies

def main():
    print("Welcome to the Movie Recommendation System!")
    print("Here are the available genres:")
    print("Drama, Crime, Action, Adventure, Fantasy, Romance, Sci-Fi, Thriller")

    preferred_genres = input("Enter your preferred genres (separated by commas): ").split(',')
    preferred_genres = [genre.strip().capitalize() for genre in preferred_genres]

    recommended_movies = recommend_movies(preferred_genres)

    if recommended_movies:
        print("\nHere are some movie recommendations for you:")
        for movie in recommended_movies:
            print(movie)
    else:
        print("\nSorry, no movies found matching your preferences.")

if __name__ == "__main__":
    main()
