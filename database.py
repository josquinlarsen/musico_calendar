from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///calendar.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Event model
class Event(Base):
    """
    Event table in database
    """

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    event_name = Column(String, index=True)
    location = Column(String, index=True)
    duration = Column(String, index=True)
    notes = Column(String, index=True)


# Create the database table
Base.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
