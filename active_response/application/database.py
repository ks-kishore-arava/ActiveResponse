import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session


engine = create_engine(os.environ.get('DATABASE_CONNECTION_URL',
                                      'sqlite:///./test.db'), echo=True)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def get_db():
    async with async_session() as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
