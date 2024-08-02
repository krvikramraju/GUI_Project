import sqlite3


class DataBaseManagement:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()
        self.cur.executescript("""

            CREATE TABLE IF NOT EXISTS Customer (
                CustomerId integer primary key AUTOINCREMENT,
                Name text,
                Email text,
                MobileNumber text,
                Gender text,
                Country text,
                Password text,
                Language text
            );
        """)

    # insert into query
    def insert(self, query):
        self.cur.execute(query)
        self.conn.commit()

    # select from query
    def show(self, query):
        return self.cur.execute(query).fetchall()

    # closing database connection
    def close_connection(self):
        self.conn.close()
