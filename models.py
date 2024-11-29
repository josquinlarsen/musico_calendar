from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# Event model
class Event(Base):
    """
    Event table in database
    """

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    event_type = Column(String, index=True)
    location = Column(String, index=True)
    duration = Column(String, index=True)
    notes = Column(String, index=True)
