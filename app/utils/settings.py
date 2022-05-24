import os
from dotenv import load_dotenv
from pydantic import BaseSettings, AnyHttpUrl
from typing import Any,List,Optional,Union

import logging

load_dotenv()

class Settings(BaseSettings):


    # Logs
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
        filename="./logs",
        level=logging.INFO,
        format=LOG_FORMAT,
        filemode="a"
    )
    @staticmethod
    async def log(request,response):
        import json
        body = None
        await request.body()
        if request._body:
            body = json.loads(request._body)
        _log = {
        "path":request.url._url,
        "request": body,
        "response":response
    }
        logging.info(_log)

    # Name, version and base path
    PROJECT_NAME: str = "ESTUDIO"
    PROJECT_VERSION: str = "v0.0.0"
    API_V1_STR: str = "/api/v1"
    
    # basic security
    SECRET_KEY: str = os.getenv("SECRET_KEY") or os.urandom(12).hex()
    TOKEN_EXPIRE_MINUTES: int = os.getenv("TOKEN_EXPIRE_MINUTES") or 60
    ALGORITHM: str = "HS256"

    # Postgres general credential
    _PG_NAME: str = os.getenv("PG_NAME") or None
    _PG_USER: str = os.getenv("PG_USER") or None
    _PG_PASSWORD: str = os.getenv("PG_PASSWORD") or None
    _PG_HOST: str = os.getenv("PG_HOST") or None
    _PG_PORT:str = os.getenv("PG_PORT") or None
    
    # mongo general credential
    _MG_NAME: str = os.getenv("MG_NAME") or None
    _MG_USER: str = os.getenv("MG_USER") or None
    _MG_PASSWORD: str = os.getenv("MG_PASSWORD") or None
    _MG_HOST: str = os.getenv("MG_HOST") or None
    _MG_PORT:str = os.getenv("MG_PORT") or None
    
    # Database URI Construction
    SQLALCHEMY_DATABASE_URL: str = f"postgresql://{_PG_USER}:{_PG_PASSWORD}@{_PG_HOST}:{_PG_PORT}"
    logging.warning(SQLALCHEMY_DATABASE_URL)
    MONGO_DATABASE_URL: str = f"mongodb://{_MG_USER}:{_MG_PASSWORD}{_MG_HOST}:{_MG_PORT}/"
    logging.warning(MONGO_DATABASE_URL)

    # CROS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

settings = Settings()