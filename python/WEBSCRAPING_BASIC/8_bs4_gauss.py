import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

### find_all
# 웹툰의 제목 뿐만 아니라, 페이지 링크도 같이
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# 웹툰의 제목, 페이지 링크
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+cartoon.a["href"]
#     print(title, link)

# 웹툰의 제목, 페이지 링크 + 별점
total_rates = 0
cartoons_rating = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons_rating:
    rate = cartoon.find("strong").get_text()
    #print(rate)
    total_rates += float(rate)
print("전체 점수: " , total_rates)
print("평균 점수: " , total_rates/len(cartoons_rating))
