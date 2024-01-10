from .conn import Connection
from mysql.connector import connect, Error
import datetime

class Controller:
    # Updates database values
    def __init__(self, bot_id: int) -> None:
        self.conn = Connection()
        try:
            connection = connect(
                host = self.conn.DB_HOST,
                user = self.conn.DB_USER,
                password = self.conn.DB_PASS,
                database="wbot"
            )
            self.connection = connection
        except Error as e:
            print(e)
        self.bot_id = bot_id
    
    def get_bot(self) -> dict:
        sql = f"SELECT * FROM bots WHERE id='{self.bot_id}'"
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result[0]
    
    def set_completed(self, value:int):
        if value == 0 or value == 1:
            sql = f"UPDATE bots SET completed='{value}' WHERE id='{self.bot_id}'"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                self.connection.commit()
        else:
            raise ValueError(f"Invalid parameter {value}. Only 0 or 1.")
    
    def is_completed(self) -> bool:
        bot = self.get_bot()
        completed = bot["completed"]
        if completed == 1:
            return True
        else:
            return False
    
    def get_streak(self) -> int:
        bot = self.get_bot()
        return int(bot["streak_count"])
    
    def update_streak(self):
        strk = self.get_streak()
        strk += 1
        sql = f"UPDATE bots SET streak_count='{strk}' WHERE id='{self.bot_id}'"
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
    
    def reset_streak(self):
        now = datetime.datetime.now()
        sql = f"UPDATE bots SET streak_count='0', streak_start='{now}' WHERE id='{self.bot_id}'"
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()