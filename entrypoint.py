from os import access
from fastapi import FastAPI, Request
import uvicorn
from app.utils.settings import settings
import logging

# from app.routes.user_router import router as user_router

app = FastAPI(
    title="Estudio",
    version="v0.0.0"
)

@app.get("/hola")
async def hello_check(request:Request):

    response = {
        "title":app.title,
        "version":app.version
    }
    await settings.log(request,response)
    return response

@app.post("/")
async def hello_check(request:Request):
    
    response = {
        "title":app.title,
        "version":app.version
    }
    await settings.log(request,response)
    return response
  

# app.include_router(user_router,prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="0.0.0.0",
        port=5000,
        workers=1,
        reload=False,
        # log_level= "debug",
        access_log=False,
        use_colors=True
    )