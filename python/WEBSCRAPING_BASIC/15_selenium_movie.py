# 구글 무비 페이지에서 할인하고 있는 영화 리스트만 추출하기
import requests
from bs4 import BeautifulSoup

url ="https://play.google.com/store/movies/top"
# header 정보 입력: 한국에서 접속하는 것을 보여줌
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
    ### Accept-Language : 기본 언어 설정-> 한국어로 된 페이지가 있으면 한국어페이지 리턴, 없다면 기본 페이지 리턴

res = requests.get(url, headers=headers) # url 에서 
res.raise_for_status()  # 에러 체크
soup = BeautifulSoup(res.text, 'lxml')

# 영화 목록 추출
movies = soup.find_all("div", attrs= {"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html", "w", encoding="utf-8") as f:
#     # f.write(res.text)     # 너무 보기 복잡함
#     f.write(soup.prettify())    # html 파일을 보기 좋게 출력
#     ### ==> 열리는 html 페이지가 기존에 우리가 원한 페이지가 아님
#     ### ==> 이유: 구글 무비에서 접속하는 header 정보를 통해서 서로 다른 페이지를 리턴함
#     ### ==> 한국에서 접속하면 한국 영화 순위 페이지로, 미국에서 접속하면 미국 영화 순위 페이지로 리턴받음

# 영화 제목 추출
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)