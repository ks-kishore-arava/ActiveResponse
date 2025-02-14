from typing import Optional
from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects.postgresql import JSON


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    payload: str = Field(sa_column=Column(JSON))
