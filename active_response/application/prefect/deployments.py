from application.prefect.flows.action import take_action_flow
from prefect.deployments import Deployment


async def create_prefect_deployments():
    # Define the deployment
    deployment = await Deployment.build_from_flow(
        flow=take_action_flow,
        name="take_action",
        work_queue_name="actions"
    )

    # Apply the deployment
    await deployment.apply()
