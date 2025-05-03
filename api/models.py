"""SQLAlchemy models"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
# Allows foreign key relationships between tables.
from sqlalchemy.orm import relationship
from database import Base


class Movie(Base):
    __tablename__ = "movies"
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genres = Column(String)

    # Adding the relationship
    ratings = relationship(
        "Rating", back_populates="movie", cascade="all, delete")
    tags = relationship("Tag", back_populates="movie", cascade="all, delete")
    link = relationship("Link", back_populates="movie",
                        uselist=False, cascade="all, delete")


class Rating(Base):
    __tablename__ = "ratings"
    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    rating = Column(Float)
    timestamp = Column(Integer)

    # Adding the relationship
    movie = relationship("Movie", back_populates="ratings")


class Tag(Base):
    __tablename__ = "tags"

    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    tag = Column(String, primary_key=True)
    timestamp = Column(Integer)

    # Adding the relationship
    movie = relationship("Movie", back_populates="tags")


class Link(Base):
    __tablename__ = "links"

    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    imdbId = Column(String)
    tmdbId = Column(Integer)

    # Adding the relationship
    movie = relationship("Movie", back_populates="link")
