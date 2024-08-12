import sqlite3
from dataclasses import dataclass

@dataclass
class Database_Users:
    connect: sqlite3.Connection = None
    cursor: sqlite3.Cursor = None

    def __post_init__(self):
        self.connect = sqlite3.connect('users.db')
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            user_nikname VARCHAR(255),
            user_xatm_number VARCHAR(255) NOT NULL
            )
        """)
        self.connect.commit()

    def add_users(self, user_id, user_nikname, user_xatm_number):
        self.cursor.execute("INSERT INTO users (user_id, user_nikname, user_xatm_number) VALUES (?, ?, ?)", 
                            (user_id, user_nikname, user_xatm_number))
        self.connect.commit()

    def select_users(self):
        self.cursor.execute("SELECT * FROM users") 
        return self.cursor.fetchall()

    def update_user(self, user_id, user_nikname, user_xatm_number, id):
        self.cursor.execute("""UPDATE users 
                               SET user_id = ?, user_nikname = ?, user_xatm_number = ?
                               WHERE id = ?""",
                            (user_id, user_nikname, user_xatm_number, id))
        self.connect.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connect:
            self.connect.close()
