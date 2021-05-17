import sqlite3
import time
import datetime

class ConnectDB:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS data(topic TEXT, datestamp TEXT, value TEXT)")

    def data_entry(self, feed_id, date, payload):
        self.c.execute("INSERT INTO data (topic, datestamp, value) VALUES(?, ?, ?)",
                        (feed_id, date, payload))
        self.conn.commit()
    
    def read_led(self):
        self.c.execute("""
                        SELECT *
                        FROM data
                        WHERE topic = 'led'
                        ORDER BY datestamp DESC
                        """)
                        
        try:
            data = self.c.fetchone()[1:]
        except TypeError as err:
            data = None
            print(err)

        return data
    
    def read_temperature(self):
        self.c.execute("""
                        SELECT *
                        FROM data
                        WHERE topic = 'temperature'
                        ORDER BY datestamp DESC
                        """)
                        
        try:
            data = self.c.fetchone()[1:]
        except TypeError as err:
            data = None
            print(err)

        return data

    def read_sound(self):
        self.c.execute("""
                        SELECT *
                        FROM data
                        WHERE topic = 'sound'
                        ORDER BY datestamp DESC
                        """)

        try:
            data = self.c.fetchone()[1:]
        except TypeError as err:
            data = None
            print(err)

        return data

    def read_light(self):
        self.c.execute("""
                        SELECT *
                        FROM data
                        WHERE topic = 'light'
                        ORDER BY datestamp DESC
                        """)
                        
        try:
            data = self.c.fetchone()[1:]
        except TypeError as err:
            data = None
            print(err)

        return data
    
    def read_infrared(self):
        self.c.execute("""
                        SELECT *
                        FROM data
                        WHERE topic = 'infrared'
                        ORDER BY datestamp DESC
                        """)
                        
        try:
            data = self.c.fetchone()[1:]
        except TypeError as err:
            data = None
            print(err)

        return data
    
    def read_time(self):
        self.c.execute("""
                        SELECT *
                        FROM data
                        WHERE topic = 'time'
                        ORDER BY datestamp DESC
                        """)
                        
        try:
            data = self.c.fetchone()[1:]
        except TypeError as err:
            data = None
            print(err)

        return data

    def log_led(self):
        print("2-color single LED log")
        self.c.execute("SELECT * FROM data WHERE topic = 'led'")
        for row in self.c.fetchall():
            print(row)
        
    def log_temperature(self):
        print("Temperature sensor log")
        self.c.execute("SELECT * FROM data WHERE topic = 'temperature'")
        for row in self.c.fetchall():
            print(row)

    def log_sound(self):
        print("Sound sensor log")
        self.c.execute("SELECT * FROM data WHERE topic = 'sound'")
        for row in self.c.fetchall():
            print(row)

    def log_light(self):
        print("Light sensor log:")
        self.c.execute("SELECT * FROM data WHERE topic = 'light'")
        for row in self.c.fetchall():
            print(row)

    def log_infrared(self):
        print("Infrared sensor log")
        self.c.execute("SELECT * FROM data WHERE topic = 'infrared'")
        for row in self.c.fetchall():
            print(row)

    def log_time(self):
        print("Real-time Clock log")
        self.c.execute("SELECT * FROM data WHERE topic = 'time'")
        for row in self.c.fetchall():
            print(row)