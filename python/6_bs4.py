import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# 가져온 html문서를(res.text) lxml 파써를 통해 BeautifulSoup 객체로 만듦
# print(soup.title)   #soup을 통해 html에 직접 접근 가능
# print(soup.title.get_text()) 
# print(soup.a)
# print(soup.a.attrs) # a가 가진 속성값
# print(soup.a["href"]) # 원하는 attribute 값 출력

# find 함수 사용
# # 어떤 a 태그를 찾을지 정의 가능
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
#     # ==>  에 해당 + class 속성이 Nbtn_upload 인 것만 찾음
# print(soup.find(attrs={"class":"Nbtn_upload"}))
#     # ==> 어떤 태그에서 찾을지 설정 안해도 됨

# 인기 만화 순위 가져오기
# print(soup.find("li", attrs ={"class":"rank01"}))
rank1 = soup.find("li", attrs ={"class":"rank01"})
print(rank1.a.get_text())

### next_sibling
# print(rank1.next_sibling)  #rank1의 a 엘리먼트 다음 요소로 넘어감
# print(rank1.next_sibling.next_sibling)
rank2= rank1.next_sibling.next_sibling
rank3= rank2.next_sibling.next_sibling
print(rank3.a.get_text())

### previous_sibling
rank2= rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

### Parent 
#print(rank1.parent)

### find_next_sibling(조건)
rank2=rank1.find_next_sibling("li")
print(rank2.a.get_text())