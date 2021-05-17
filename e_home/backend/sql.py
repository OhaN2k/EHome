import sqlite3
import time
import datetime

class ConnectDB:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS database(datestamp TEXT, topic TEXT, value INT)")

    def sound_entry(self, payload):
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
        topic = "sound"
        self.c.execute("INSERT INTO database (datestamp, topic, value) VALUES(?, ?, ?)",
                        (date, topic, payload))
        self.conn.commit()
    
    def light_entry(self, payload):
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
        topic = "light"
        self.c.execute("INSERT INTO database (datestamp, topic, value) VALUES(?, ?, ?)",
                        (date, topic, payload))
        self.conn.commit()
    
    def read_sound(self):
        self.c.execute("""
                        SELECT *
                        FROM database
                        WHERE topic = 'sound'
                        ORDER BY datestamp DESC
                        """)
        print(self.c.fetchone())

    def read_light(self):
        self.c.execute("""
                        SELECT *
                        FROM database
                        WHERE topic = 'sound'
                        ORDER BY datestamp DESC
                        """)
        print(self.c.fetchone())

    def log_sound(self):
        print("Sound sensor log")
        self.c.execute("SELECT * FROM database WHERE topic = 'sound'")
        for row in self.c.fetchall():
            print(row)

    def log_light(self):
        print("Light sensor log:")
        self.c.execute("SELECT * FROM database WHERE topic = 'light'")
        for row in self.c.fetchall():
            print(row)

    