import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    _DB_NAME: str = os.getenv("DB_NAME")
    _DB_USER: str = os.getenv("DB_USER")
    _DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    _DB_HOST: str = os.getenv("DB_HOST")
    _DB_PORT:str = os.getenv("DB_PORT")
    
    PROJECT_NAME: str = "ESTUDIO"
    PROJECT_VERSION: str = "v0.0.0"
    API_V1_STR: str = "/api/v1"
    
    SECRET_KEY: str = os.getenv("SECRET_KEY") or os.urandom(12).hex()
    TOKEN_EXPIRE_MINUTES: int = os.getenv("TOKEN_EXPIRE_MINUTES") or 60
    ALGORITHM: str = "HS256"
    

settings = Settings()