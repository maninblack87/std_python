import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekdayList"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

rank1 = soup.find("li", attrs={"class": "rank01"})
