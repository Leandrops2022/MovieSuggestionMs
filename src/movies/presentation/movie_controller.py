from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.movies.domain.mood import MoodEnum
from src.movies.infrastructure.data_sources import get_db
from src.movies.application.movie_service import MovieService

router = APIRouter()

@router.get("/movies/random/{mood}")
async def get_random_movie(mood: MoodEnum, db: Session = Depends(get_db)):
    movie_service = MovieService(db)
    movie = movie_service.get_random_movie_by_mood(mood)

    if movie:
        return movie
    raise HTTPException(status_code=404, detail="No movie found.")


