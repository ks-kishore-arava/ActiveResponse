from prefect import flow
from application.prefect.tasks.action import take_action


@flow
def take_action_flow(event_id):
    take_action.submit(event_id=event_id)
