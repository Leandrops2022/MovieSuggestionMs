from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("DB_USERNAME", "root")
password = os.getenv("DB_PASSWORD", "root")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_DATABASE", "movies")

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{db_host}/{db_name}"
