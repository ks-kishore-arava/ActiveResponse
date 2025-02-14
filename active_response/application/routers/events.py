from fastapi import APIRouter, Depends
from sqlmodel import Session
from application.models import Event
from application.database import get_session

from prefect.deployments import run_deployment


router = APIRouter()


@router.post("/events")
def create_item(event_json: dict, session: Session = Depends(get_session)):
    event = Event(payload=event_json)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


@router.get("/events/{event_id}")
def read_item(event_id: int):
    run_deployment(name="take_action",
                   work_queue_name='actions',
                   parameters={"event_id": event_id})
