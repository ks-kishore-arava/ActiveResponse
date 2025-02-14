from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.ext.asyncio import AsyncSession

from application.database import get_db, create_db_and_tables
from application.routers import events
from application.prefect.deployments import create_prefect_deployments

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    create_prefect_deployments()


app.include_router(events.router)


@app.get("/")
async def read_root(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT 1")
    return {"message": "Hello World", "result": result.scalar()}
