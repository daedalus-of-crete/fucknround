from bs4 import BeautifulSoup
from datapipe.models.AbsProduct import AbsProduct


# ******** Eventually ill need to edit this file and make a script
# that can crawl the website and find all tags and such
# but this will work for idk a month ***********


def parseABS(data):
    '''
        This function takes in a page of html and parses Amazon Best
        Sellers to spit out clean product info
    '''
    products = []

    # Find all product blocks (Amazon uses this class for items in best sellers)
    for div in soup.find_all("div", class_="p13n-sc-uncoverable-faceout"):
        try:
            title_tag = div.find("div", class_="p13n-sc-truncate")
            price_tag = div.find("span", class_="_cDEzb_p13n-sc-price_3mJ9Z")
            rating_tag = div.find("span", class_="a-icon-alt")
            product = {
                "title": title_tag.get_text(strip=True) if title_tag else "N/A",
                "price": price_tag.get_text(strip=True) if price_tag else "N/A",
                "rating": rating_tag.get_text(strip=True) if rating_tag else "N/A",
            }
            products.append(product)
        except Exception as e:
            print(f"Error parsing product: {e}")

     # Pretty print result
    from pprint import pprint
    pprint(products)


with open("AmazonBestSellers6-10-20251.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

parseABS(soup)
