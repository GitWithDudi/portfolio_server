import psycopg2
from time import sleep
import threading
import os

DB_URL = os.environ.get("NEON_DB_URL")

def keep_alive():
    while True:
        try:
            conn = psycopg2.connect(DB_URL)
            conn.close()
            print("DB is alive!")
        except Exception as e:
            print("Error:", e)
        sleep(300)

thread = threading.Thread(target=keep_alive)
thread.daemon = True
thread.start()
