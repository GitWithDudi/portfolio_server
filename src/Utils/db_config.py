import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

def get_db_connection():
    # Use NEON_DB_URL connection string if available, otherwise fall back to individual env vars
    database_url = os.getenv("NEON_DB_URL")

    if database_url:
        return psycopg2.connect(database_url)
    else:
        # Fallback to individual environment variables
        DB_CONFIG = {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),
            "sslmode": "require"
        }
        return psycopg2.connect(**DB_CONFIG)


