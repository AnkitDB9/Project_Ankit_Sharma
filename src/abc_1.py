import sqlite3
import random
from datetime import datetime, timedelta

# Establish SQLite connection
conn = sqlite3.connect('product_ratings.db')
cursor = conn.cursor()

# Create Ratings table
cursor.execute('''
    CREATE TABLE Ratings (
        timestamp TEXT,
        user_id INTEGER,
        product_id INTEGER,
        rating INTEGER
    )
''')

# Generate random ratings data
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = (end_date - start_date).days

ratings = [
    (
        (start_date + timedelta(days=random.randint(0, date_range))).strftime('%Y-%m-%d'),
        random.randint(1, 1000),
        random.randint(1, 1000),
        random.randint(1, 5)
    )
    for _ in range(100000)
]

cursor.executemany('INSERT INTO Ratings (timestamp, user_id, product_id, rating) VALUES (?, ?, ?, ?)', ratings)
conn.commit()
