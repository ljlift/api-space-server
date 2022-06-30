import uvicorn

from fastapi import FastAPI

from app.api import api_router
from app.core import settings

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
