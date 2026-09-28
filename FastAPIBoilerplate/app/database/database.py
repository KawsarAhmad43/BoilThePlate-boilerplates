from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
# using os to get the database URL from environment variables (Docker will pass this to us)

# Default to localhost if running outside docker, but in docker it will be 'db'
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_USER = os.getenv("DB_USER", "student")
DB_PASSWORD = os.getenv("DB_PASSWORD", "secret123")
DB_NAME = os.getenv("DB_NAME", "student_db")

# Connection string for MySQL using pymysql
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

# Engine is what actually connects to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal will be used to create individual database sessions for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database models to inherit from
Base = declarative_base()

# Dependency to get the DB session in our routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
