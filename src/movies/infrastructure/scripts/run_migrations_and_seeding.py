from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import time
import subprocess
import sys

from src.movies.infrastructure.seeders.movie_seeder import seed_movies

DATABASE_URL = "mysql+pymysql://root:root@localhost:3308"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def start_docker_container():
    """Start the Docker container if not already running."""
    try:
        subprocess.run(["docker", "start", "mss-container"], check=True)
        print("Docker container started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting Docker container: {e}")
        sys.exit(1)


def wait_for_db_connection():
    """Wait for the database to be ready to accept connections."""
    print("Waiting for the database to be ready...")
    retries = 10
    for _ in range(retries):
        try:
            with engine.connect() as conn:
                print("Database is ready.")
                return True
        except OperationalError:
            print("Database not ready yet, retrying...")
            time.sleep(5)
    print("Database did not become ready in time.")
    sys.exit(1)


def run_migrations():
    print("Running migrations...")
    create_db_sql = "CREATE DATABASE IF NOT EXISTS mss_test;"
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS filmes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo_portugues VARCHAR(255) NOT NULL,
            ano_lancamento INT,
            nota FLOAT,
            genres VARCHAR(255),
            quantidade_de_votos INT
        );
    """

    try:
        with engine.connect() as conn:
            print("Executing CREATE DATABASE SQL...")
            conn.execute(text(create_db_sql))  # Create the database
            print("Database created or already exists.")

            # Now connect to the specific database (mss_test) and create the table
            conn.execute(text("USE mss_test;"))  # Switch to the correct database
            print("Switched to mss_test database.")

            print("Executing CREATE TABLE SQL...")
            conn.execute(text(create_table_sql))  # Create the table in the correct database
            print("Table created or already exists.")

            print("Migrations completed successfully.")
    except Exception as e:
        print(f"Error running migrations: {e}")
        sys.exit(1)


def seed_movies_data():
    print("Seeding movies...")
    db = SessionLocal()
    try:
        seed_movies(db)
        print("Movies seeded successfully.")
    finally:
        db.close()


def configure_environment():
    start_docker_container()
    wait_for_db_connection()
    run_migrations()
    seed_movies_data()


if __name__ == "__main__":
    start_docker_container()
    wait_for_db_connection()
    run_migrations()
    seed_movies_data()
