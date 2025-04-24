from sqlmodel import Session, create_engine, SQLModel
from app.db.models.users_models import UserInDB   # Registrar la tabla en el metadata
from fastapi import Depends
from typing import Annotated
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  # Esto es app/db/
sqlite_file_name = os.path.join(base_dir, "data","datausers.db")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread":False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

sessionDep = Annotated[Session, Depends(get_session)]