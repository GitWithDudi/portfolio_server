import psycopg2
from time import sleep
import threading

DB_URL = "postgresql://neondb_owner:npg_58CjfwRargqm@ep-little-glitter-a5u0h1tl-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"

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
