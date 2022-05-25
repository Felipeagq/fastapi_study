
from fastapi import APIRouter, Body, Depends, status, Request

from app.schemas import user_schema
from typing import Optional

from app.db.postgres.pg_core import get_db
from app.db.postgres.pg_crud import PostgresDatabase
from app.models.user_model import User
from sqlalchemy.orm import Session
from app.utils.settings import settings



router = APIRouter()

@router.post(
    "/signup",
    tags=["Users"],
    status_code=status.HTTP_201_CREATED,
    summary="Create a User"
)
async def create_user(
    request:Request,
    user: user_schema.UserRegister = Body(...),
    db:Session = Depends(get_db)
):
    """
    Create a user in the app

    Args:
        user (user_schema.UserRegister, optional): _description_. Defaults to Body(...).
            - emai
            - username
            - password
    
    Return 
    - user info
    """
    to_create_user = User(
        email = user.email,
        username = user.username,
        password = user.password
    )
    response = to_create_user
    # db.add(to_create_user)
    # db.commit()
    # db.refresh(to_create_user)
    await settings.log(request,to_create_user.__dict__)
    PostgresDatabase.create(db=db,entity=to_create_user)
    return user_schema.User(
        username=to_create_user.username,
        email= to_create_user.email,
        id = to_create_user.id
    )




@router.get(
    "/user/{usernma}",
    tags=["Users"],
    status_code= status.HTTP_200_OK,
    summary="Get user info by username"
)
async def get_user(
    request:Request,
    username:Optional[str] = None,
    db:Session = Depends(get_db)
):
    q = PostgresDatabase.read(
        db=db,
        entity = User,
        param=username
    )
    await settings.log(request,q)
    return q