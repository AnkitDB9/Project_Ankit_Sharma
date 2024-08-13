from src.database import create_connection
from src.data_generation import generate_ratings
from src.aggregates import compute_monthly_aggregates
from src.top_products import find_top_products

def main():
    conn = create_connection('ratings.db')

    # Step 1: Generate product ratings
    generate_ratings(conn)

    # Step 2: Compute monthly aggregates
    compute_monthly_aggregates(conn)

    # Step 3: Find top-rated products for each month
    top_products = find_top_products(conn)

    # Output the top products
    for month, products in top_products.items():
        print(f"Top products for {month}:")
        for product in products:
            print(f"Product ID: {product[0]}, Average Rating: {product[1]:.2f}")
        print()

    conn.close()

if __name__ == '__main__':
    main()
