from bs4 import BeautifulSoup

with open("AmazonBestSellers6-10-2025.html") as f:
    soup = BeautifulSoup(f, "html.parser")

categories = []
for section in soup.find_all("div", class_="a-carousel-header-row"):
    # Get category title
    h2 = section.find("h2")
    if not h2:
        continue
    category = h2.get_text(strip=True)

    # Find the carousel's product list (immediately after this header section)
    carousel = section.find_next("ol")
    if not carousel:
        continue

    products = []
    for li in carousel.find_all("li", recursive=False):
        # Product title
        title_tag = li.find("a", class_="a-link-normal aok-block")
        title = title_tag.get_text(strip=True) if title_tag else None

        # Price
        price_tag = li.find("span", class_="p13n-sc-price")
        price = price_tag.get_text(strip=True) if price_tag else None

        # Rating
        rating_tag = li.find("span", class_="a-icon-alt")
        rating = rating_tag.get_text(strip=True) if rating_tag else None

        if title:
            products.append({
                "title": title,
                "price": price,
                "rating": rating,
            })
    categories.append({
        "category": category,
        "products": products
    })

from pprint import pprint
pprint(categories)
pprint(products)
