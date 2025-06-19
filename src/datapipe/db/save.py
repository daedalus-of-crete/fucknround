import psycopg2
from datetime import datetime

from datapipe.models.AbsProduct import AbsProduct 

def save_abs_to_db(product):
    conn = psycopg2.connect(
        dbname="alexandria",
        user="socrates",           # Change to 'erebus' if that's your user
        password="your_password", # Replace with your real password or use env var
        host="localhost",
        port=5432
    )
    cur = conn.cursor()
    print("🔌 Connected.")
    
    insert_query = """
    INSERT INTO scraper_product
    (title, category, price, description, url, last_updated, rating, position)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (url) DO UPDATE SET
    title = EXCLUDED.title,
    category = EXCLUDED.category,
    price = EXCLUDED.price,
    description = EXCLUDED.description,
    last_updated = EXCLUDED.last_updated,
    rating = EXCLUDED.rating,
    position = EXCLUDED.position;
    """

    cur.execute(insert_query, (
        product.title,
        product.category,
        product.price,
        product.description,
        product.url,
        product.last_updated or datetime.utcnow(),
        product.rating,
        product.position
    ))

    conn.commit()
    cur.close()
    conn.close()
