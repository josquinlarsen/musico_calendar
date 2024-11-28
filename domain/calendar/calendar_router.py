from fastapi import FastAPI, APIRouter, HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
from domain.calendar.calendar_schema import EventCreate, EventUpdate, EventResponse
from database import get_db
from models import Event


router = APIRouter()


@router.post("/calendar/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):

    check_date = db.query(Event).filter_by(date=event.date).first()
    if check_date:
        raise HTTPException(
            status_code=400,
            detail=f"I'm sorry, {event.date} is taken. Please reschedule",
        )

    db_event = Event(
        date=event.date,
        event_type=event.event_type,
        location=event.location,
        duration=event.duration,
        notes=event.notes,
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


@router.get("/calendar/", response_model=list[EventResponse])
def read_events(db: Session = Depends(get_db)):
    #  can set a limit parameter and limit query.
    events = db.query(Event).all()
    return events


@router.get("/calendar/{event_id}", response_model=EventResponse)
def read_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.put("/calendar/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    check_date = db.query(Event).filter_by(date=event.date).first()
    if check_date and check_date.id != event_id:
        raise HTTPException(
            status_code=400,
            detail=f"I'm sorry, {event.date} is taken. Please reschedule",
        )

    db_event.date = event.date
    db_event.event_type = event.event_type
    db_event.location = event.location
    db_event.duration = event.duration
    db_event.notes = event.notes

    db.commit()
    db.refresh(db_event)
    return db_event


@router.delete("/calendar/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(db_event)
    db.commit()
    return {"detail": "Event deleted successfully"}


# -----------------------------------------------------------------------
#            Utilities
# -----------------------------------------------------------------------

