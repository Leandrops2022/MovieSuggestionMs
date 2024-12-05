from src.movies.domain.movie import Movie
from src.movies.infrastructure.data_sources import engine

def upgrade():
    # Create movies table
    Movie.__table__.create(bind=engine)

def downgrade():
    # Drop movies table
    Movie.__table__.drop(bind=engine)