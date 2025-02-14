from prefect import task
from application.database import get_session
from application.models import Event


@task
def take_action(event_id):
    session = get_session()
    event = session.get(Event, event_id)
    if event is None:
        return {"error": "Event not found"}
    return event.payload
