# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link


db = SessionLocal()

# %%
# Test retrieving a few movies.

movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genre: {movie.genres}")


# %%
# Test retrieving the movies of the Action genre.
action_movies = db.query(Movie).filter(
    Movie.genres.contains("Action")).limit(5).all()

for movie in action_movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genre: {movie.genres}")


# %%
# Test retrieving a few rating
Ratings = db.query(Rating).limit(5).all()

for rating in Ratings:
    print(
        f"User ID: {rating.userId}, Movie ID: {rating.movieId}, Rate: {rating.rating}, Timestamp: {rating.timestamp}")


# %%
# Retrieve movies with an average rating of 4 or higher.
high_rated_movies = db.query(Movie.title, Rating.rating).join(
    Rating).filter(Rating.rating >= 4).limit(5).all()

print(high_rated_movies)

for title, rating in high_rated_movies:
    print(title, rating)


# %%
# Retrieval of tags associated with the movies.
tags = db.query(Tag).limit(5).all()

for tag in tags:
    print(
        f"User ID: {tag.userId}, Movie ID: {tag.movieId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")
#
#
# %%
# Test the link class
links = db.query(Link).limit(5).all()

for link in links:
    print(
        f"Movie ID: {link.movieId}, IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")


# %%
# Close the connexion to the database

db.close()
