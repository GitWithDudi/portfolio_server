import psycopg2
from time import sleep
import threading
import os
from dotenv import load_dotenv

load_dotenv()

def keep_alive():
    DB_URL = os.environ.get("NEON_DB_URL")
    while True:
        try:
            conn = psycopg2.connect(DB_URL, connect_timeout=5)
            conn.close()
            print("DB is alive!")
        except Exception as e:
            print("Error:", e)
        sleep(300)

thread = threading.Thread(target=keep_alive)
thread.daemon = True
thread.start()
