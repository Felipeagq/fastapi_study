from datetime import datetime, timedelta
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException,status
from app.utils.settings import settings
from app.schemas import token_schema

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.models.user_model import User

password_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="api/v1/login")

def verify_password(
    plain_password:str,
    hashed_password:str
):
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(plain_password:str):
    return password_context.hash(plain_password)


def get_user(username:str):
    return User.filter((User.email == username) | (User.username == username)).first()


def authenticate_user(
    username:str,
    password:str
):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(
    data:dict,
    expires_delta:Optional[timedelta]=None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({
        "exp":expire
    })
    encode_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encode_jwt

def generate_token(
    username:str,
    password:str
):
    user = authenticate_user(username,password)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate":"Bearer"}
        )
    access_token_expire = timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    return create_access_token(
        data={"sub":user.username},
        expires_delta=access_token_expire
    )


async def get_current_user(
    token:str = Depends(oauth2_schema)
):
    credentials_exception = HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate":"Bearer"}
    )
    
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = token_schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user