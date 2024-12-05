from fastapi import FastAPI
import uvicorn
from src.movies.presentation.movie_controller import router as movies_router

app = FastAPI()

app.include_router(movies_router, prefix="/api/v1", tags=["Movies"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)