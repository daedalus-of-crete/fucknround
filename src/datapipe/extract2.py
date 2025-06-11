import requests as r
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.amazon.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-GPC": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0, i"
    }

base_url = 'https://www.amazon.in/'
url = 'https://www.amazon.com/Best-Sellers/zgbs'

base_response = r.get(base_url, headers=headers)
print(f"base response: {base_response.status_code}\n")
cookies = base_response.cookies

time.sleep(5)
dataPull = r.get(url, headers=headers, cookies=cookies)

print(f"bestsellers response: {dataPull.status_code}\n")
# print(f"Content type: {dataPull.headers.get("Content-Type")}\n")
# print(f"length: {len(dataPull.text)}")

with open("AmazonBestSellers6-10-2025.html", "w", encoding="utf-8") as f:
    f.write(dataPull.text)

def parseBS(page):
    pass
