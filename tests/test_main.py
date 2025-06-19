from datapipe.models.AbsProduct import AbsProduct
from datapipe.db.save import save_abs_to_db

def test_insert_single_product():
    product = AbsProduct(
        title="Sample Tumbler",
        category="Home & Kitchen",
        price=29.99,
        description="Keeps drinks cold for 24 hours.",
        url="https://example.com/sample-product",
        rating=4.6,
        position=1
    )

    save_product_to_db(product)
    print("✅ Product saved to database.")
