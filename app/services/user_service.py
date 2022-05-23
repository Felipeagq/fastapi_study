
from app.models.user_model import User 
from app.schemas import user_schema
from fastapi import HTTPException, status

from app.services.auth_service import get_password_hash

def create_user(
    user:user_schema.UserRegister
):
    get_user = User.filter((User.email == user.email) | (User.username == user.username))
    if get_user:
        msg = "Email is already register"
        if get_user.username == user.username:
            msg = "username is already register"
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= msg
        )
    
    db_user = User(
        username = user.username,
        email = user.email,
        password = get_password_hash(user.password)
    )
    
    db_user.save()
    
    return user_schema.User(
        id= db_user.id,
        username= db_user.username,
        email= db_user.email
    )