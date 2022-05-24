from os import access
from fastapi import FastAPI, Request
import uvicorn
from app.utils.settings import settings
import logging
from starlette.middleware.cors import CORSMiddleware

# from app.routes.user_router import router as user_router

app = FastAPI(
    title="Estudio",
    version="v0.0.0"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )


@app.get("/")
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
        reload=True,
        # log_level= "debug",
        access_log=False,
        use_colors=True
    )