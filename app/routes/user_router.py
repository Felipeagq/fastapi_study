from fastapi import APIRouter, Body, Depends, status
from app.schemas import user_schema

from app.utils.db import get_db

router = APIRouter()

@router.post(
    "/signup",
    tags=["Users"],
    status_code=status.HTTP_201_CREATED,
    response_model= user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a User"
)
def create_user(
    user: user_schema.UserRegister = Body(...)
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