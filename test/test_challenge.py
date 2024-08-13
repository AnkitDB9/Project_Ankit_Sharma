import unittest
from src.database import create_connection
from src.data_generation import generate_ratings
from src.aggregates import compute_monthly_aggregates
from src.top_products import find_top_products

class TestDataEngineeringChallenge(unittest.TestCase):

    def setUp(self):
        """Set up the test database and connection."""
        self.conn = create_connection(':memory:')  # Using an in-memory database for testing
        generate_ratings(self.conn)

    def test_generate_ratings(self):
        """Test that the Ratings table has been populated."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Ratings')
        count = cursor.fetchone()[0]
        self.assertEqual(count, 100000)

    def test_compute_monthly_aggregates(self):
        """Test that the monthly aggregates are computed correctly."""
        compute_monthly_aggregates(self.conn)
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM RatingsMonthlyAggregates')
        count = cursor.fetchone()[0]
        self.assertGreater(count, 0)

    def test_find_top_products(self):
        """Test that the top-rated products are found correctly."""
        compute_monthly_aggregates(self.conn)
        top_products = find_top_products(self.conn)
        for month, products in top_products.items():
            self.assertEqual(len(products), 3)

    def tearDown(self):
        """Close the database connection after tests."""
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
