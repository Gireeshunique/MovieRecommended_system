import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "gireesh@143"),
    database=os.getenv("DB_NAME", "movie_app")
)

cursor = db.cursor(buffered=True)