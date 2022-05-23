from fastapi import FastAPI
import uvicorn
from app.utils.settings import settings

from app.routes.user_router import router as user_router

app = FastAPI(
    title="Estudio",
    version="v0.0.0"
)

@app.get("/")
def hello_check():
    return {
        "title":app.title,
        "version":app.version
    }

app.include_router(user_router,prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="0.0.0.0",
        port=5000,
        workers=1,
        reload=True,
        log_level= "info",
        use_colors=True
    )