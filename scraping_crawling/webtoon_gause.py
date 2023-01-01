import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

cartoons = soup.find_all("td", attrs={"class": "title"})

# # 1 cartoons의 첫번째 배열의 텍스트 출력하기
# title = cartoons[0].a.get_text()
# print(title)

# # 2 cartoons의 첫번째 배열의 링크 출력하기
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print("https://comic.naver.com" + link)

# # 3 cartoon의 모든 배열의 링크 출력하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 4 cartoons의 모든 배열의 평점 출력하기
total_rates = 0

cartoons = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체점수 : ", total_rates)
print("평균점수 : ", total_rates / len(cartoons))
