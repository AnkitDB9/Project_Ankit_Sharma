from sqlite3 import Connection

def find_top_products(conn: Connection):
    """Find the top 3 rated products for each month."""
    cursor = conn.cursor()

    cursor.execute('''
        SELECT month, product_id, average_rating
        FROM (
            SELECT month, product_id, average_rating,
            ROW_NUMBER() OVER (PARTITION BY month ORDER BY average_rating DESC) as rank
            FROM RatingsMonthlyAggregates
        )
        WHERE rank <= 3
    ''')

    rows = cursor.fetchall()
    top_products = {}
    
    for row in rows:
        month = row[0]
        if month not in top_products:
            top_products[month] = []
        top_products[month].append((row[1], row[2]))

    return top_products
