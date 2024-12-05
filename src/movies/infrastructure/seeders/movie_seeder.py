from faker import Faker
from sqlalchemy.orm import Session
from src.movies.domain.movie import Movie

fake = Faker()

def seed_movies(db: Session, num_movies: int = 100):
    for _ in range(num_movies):
        movie = Movie(
            titulo_portugues=fake.sentence(nb_words=3),
            genres=fake.random_element(elements=(
                "Comédia",
                "Animação",
                "Musical",
                "Drama",
                "Romance",
                "Ação",
                "Aventura",
                "Ficção científica",
                "Musical",
                "Crime",
                "Documentário",
                "História",
                "Família",
            )),
            ano_lancamento=fake.year(),
            nota=fake.random_number(digits=2),
            quantidade_de_votos=fake.random_number(digits=5),
        )
        db.add(movie)
    db.commit()

# Usage:
# from src.infrastructure.database import SessionLocal
# from src.movies.infrastructure.seeders.movie_seeder import seed_movies

# db = SessionLocal()
# seed_movies(db)
