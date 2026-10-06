from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="GDG MKU Backend Starter")


class Event(BaseModel):
    title: str
    venue: str


# no database yet, events just live in this list
# restart the server and they're gone. we fix that in session 2
events = [
    {"id": 1, "title": "Backend Kickoff", "venue": "TBC"},
]


@app.get("/")
def home():
    return {"message": "backend journey starter is running"}


@app.get("/events")
def list_events():
    return events


@app.get("/events/{event_id}")
def get_event(event_id: int):
    for e in events:
        if e["id"] == event_id:
            return e
    raise HTTPException(status_code=404, detail="event not found")


@app.post("/events", status_code=201)
def create_event(event: Event):
    new_event = {"id": len(events) + 1, **event.model_dump()}
    events.append(new_event)
    return new_event
