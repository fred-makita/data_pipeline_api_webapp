"""Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

# # Create a database engine that establishes the connection with our SQLite database (movies.db).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Define SessionLocal, which allows creating sessions to interact with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base, which will serve as the base class for our SQLAlchemy models.
Base = declarative_base()

# # Optional: to perform a check of the database connection.

# # (Can be useful for debugging or initial configuration.).
""" if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Database connection successful.")
    except Exception as e:
        print(f"Connection error : {e}") """
