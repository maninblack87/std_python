import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
my_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55"}
res = requests.get(url, headers=my_headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", {"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).get_text())

for item in items:

    # 광고제품은 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print(" <광고 상품은 제외합니다>")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()

    # 애플 상품 제외
    if "Apple" in name:
        print(" <Apple 상품은 제외합니다>")
        continue

    price = item.find("strong", attrs={"class": "price-value"}).get_text()

    # 평점 수 100개 이상, 평점 4.5점 이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품은 제외합니다>")
        continue
    rate_cnt = item.find(
        "span", attrs={"class": "rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print(" <평점 수 없는 상품은 제외합니다>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 50:
        print(name, price, rate, rate_cnt)
