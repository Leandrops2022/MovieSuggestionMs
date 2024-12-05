from typing import Optional, List

from src.movies.domain.mood import MoodEnum
from src.movies.infrastructure.movie_repository import MovieRepository
from sqlalchemy.orm import Session
from src.movies.domain.movie import Movie

class MovieService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.movie_repository = MovieRepository(db_session)

    def map_mood_to_genre(self, mood: str) -> list[str]:

        mood_to_genre_mapping = {
            "happy": ["Comédia", "Animação", "Musical"],  # Uplifting and fun genres
            "sad": ["Comédia", "Drama", "Romance"],  # Comforting and emotional genres
            "excited": ["Ação", "Aventura", "Ficção científica"],  # High-energy genres
            "romantic": ["Romance", "Drama", "Musical"],  # Emotional and love-focused genres
            "bored": ["Comédia", "Aventura", "Animação"],  # Engaging and light-hearted genres
            "angry": ["Ação", "Comédia", "Crime"],  # Intense or humorous genres to release tension
            "relaxed": ["Drama", "Documentário", "Comédia"],  # Calming and soothing genres
            "nostalgic": ["História", "Família", "Comédia"],  # Comforting and nostalgic genres
            "scared": ["Comédia", "Drama", "Romance"],  # Light-hearted genres to reduce fear
            "adventurous": ["Aventura", "Fantasia", "Ficção científica"],  # Explorative and thrilling genres
        }

        return mood_to_genre_mapping.get(mood.lower(), ["comedia"])

    def get_random_movie_by_mood(self, mood: str) -> Optional[Movie]:
        genre = self.map_mood_to_genre(mood)
        return self.movie_repository.get_random_by_genre(genre)
