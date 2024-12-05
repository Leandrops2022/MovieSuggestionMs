from typing import Optional
from src.movies.domain.movie import Movie
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import Session
from sqlalchemy import or_

class MovieRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_random_by_genre(self, genres: list[str]) -> Optional[Movie]:
        genre_filters = [Movie.genres.like(f"%{genre}%") for genre in genres]

        movie = (
            self.db_session.query(Movie)
            .filter(
                or_(*genre_filters),
                Movie.nota > 7,
                Movie.quantidade_de_votos > 2000)
            .order_by(func.rand())
            .limit(1)
            .first()
        )

        return movie


