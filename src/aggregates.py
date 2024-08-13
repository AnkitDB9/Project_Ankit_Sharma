from sqlite3 import Connection

def compute_monthly_aggregates(conn: Connection):
    """Compute monthly average ratings for each product and store them in the RatingsMonthlyAggregates table."""
    cursor = conn.cursor()

    # Create RatingsMonthlyAggregates table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RatingsMonthlyAggregates (
            month TEXT,
            product_id INTEGER,
            average_rating REAL
        )
    ''')

    # Calculate monthly averages and insert them into the table
    cursor.execute('''
        INSERT INTO RatingsMonthlyAggregates (month, product_id, average_rating)
        SELECT 
            strftime('%Y-%m', timestamp) AS month,
            product_id,
            AVG(rating) as average_rating
        FROM Ratings
        GROUP BY month, product_id
    ''')

    conn.commit()
