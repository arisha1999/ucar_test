import sqlite3
from datetime import datetime

DATABASE = "reviews.db"

class Review:
    @staticmethod
    def init_db():
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def create_review(text: str, sentiment: str) -> dict:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)",
                (text, sentiment, datetime.utcnow().isoformat())
            )
            review_id = cursor.lastrowid

            cursor.execute(
                "SELECT id, text, sentiment, created_at FROM reviews WHERE id = ?",
                (review_id,)
            )
            review_data = cursor.fetchone()

            conn.commit()

            if not review_data:
                raise ValueError("Не удалось создать запись в базе данных")

            return {
                "id": review_data[0],
                "text": review_data[1],
                "sentiment": review_data[2],
                "created_at": review_data[3]
            }
        finally:
            conn.close()
    @staticmethod
    def get_reviews(sentiment=None) -> list:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        if sentiment:
            cursor.execute(
                "SELECT id, text, sentiment, created_at FROM reviews WHERE sentiment = ?",
                (sentiment,)
            )
        else:
            cursor.execute(
                "SELECT id, text, sentiment, created_at FROM reviews"
            )

        reviews = cursor.fetchall()
        conn.close()

        return [
            {
                "id": row[0],
                "text": row[1],
                "sentiment": row[2],
                "created_at": row[3]
            }
            for row in reviews
        ]