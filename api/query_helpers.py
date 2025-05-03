"""SQLAlchemy Query Functions for MovieLens API"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import Optional

import models

# --- Movies ---


def get_movie(db: Session, movie_id: int):
    """Récupère un film par son ID."""
    return db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genre: str = None):
    """Récupère une liste de films avec filtres optionnels."""
    query = db.query(models.Movie)

    if title:
        query = query.filter(models.Movie.title.ilike(f"%{title}%"))
    if genre:
        query = query.filter(models.Movie.genres.ilike(f"%{genre}%"))

    return query.offset(skip).limit(limit).all()

# --- Ratings ---


def get_rating(db: Session, user_id: int, movie_id: int):
    """Récupère une évaluation en fonction du couple (userId, movieId)."""
    return db.query(models.Rating).filter(
        models.Rating.userId == user_id,
        models.Rating.movieId == movie_id
    ).first()


def get_ratings(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None, min_rating: float = None):
    """Récupère une liste d'évaluations avec filtres optionnels."""
    query = db.query(models.Rating)

    if movie_id:
        query = query.filter(models.Rating.movieId == movie_id)
    if user_id:
        query = query.filter(models.Rating.userId == user_id)
    if min_rating:
        query = query.filter(models.Rating.rating >= min_rating)

    return query.offset(skip).limit(limit).all()

# --- Tags ---


def get_tag(db: Session, user_id: int, movie_id: int, tag_text: str):
    """Récupère un tag par userId, movieId et le texte du tag."""
    return (
        db.query(models.Tag)
        .filter(
            models.Tag.userId == user_id,
            models.Tag.movieId == movie_id,
            models.Tag.tag == tag_text
        )
        .first()
    )


def get_tags(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    movie_id: Optional[int] = None,
    user_id: Optional[int] = None
):
    """Retrieve a list of tags with optional filters."""
    query = db.query(models.Tag)

    if movie_id is not None:
        query = query.filter(models.Tag.movieId == movie_id)
    if user_id is not None:
        query = query.filter(models.Tag.userId == user_id)

    return query.offset(skip).limit(limit).all()


# --- Likns ---
def get_link(db: Session, movie_id: int):
    """Returns the associated IMDB and TMDB links for a specific movie."""
    return db.query(models.Link).filter(models.Link.movieId == movie_id).first()


def get_links(db: Session, skip: int = 0, limit: int = 100):
    """Returns a paginated list of IMDB and TMDB links for movies."""
    return db.query(models.Link).offset(skip).limit(limit).all()

# --- Analytical queries ---


def get_movie_count(db: Session):
    """Returns the total number of movies."""
    return db.query(models.Movie).count()


def get_rating_count(db: Session):
    """Returns the total number of ratings."""
    return db.query(models.Rating).count()


def get_tag_count(db: Session):
    """Returns the total number of tags."""
    return db.query(models.Tag).count()


def get_link_count(db: Session):
    """Returns the total number of links."""
    return db.query(models.Link).count()
