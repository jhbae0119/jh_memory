# headless chrome : 브라우저(chrome)를 굳이 안띄워도 되는 웹스크랩핑에서 사용
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


### headless chrome 설정하기
options = webdriver.ChromeOptions()
options.headless = True     # headless chrome 설정
options.add_argument("window-size=1920x1080")   # 눈에 띄진 않지만 백그라운드에서 도는 브라우저 크기를 지정


browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url ="https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기 # scroll을 1080만큼 scroll down = 한페이지 새로고침
browser.execute_script("window.scrollTo(0,1080)")    # 사용하는 pc의 해상도 높이: 1920*1080

# 화면 가장 아래로 스크롤 내리기
# 현재 문서의 총 높이만큼 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval = 2    # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 현재 문서 높이와 이전 문서 높이가 같으면 더이상 페이지가 없는 것이기 때문에 for문 끝냄
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
print("스크롤 완료")

# screenshot 남기기
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, 'lxml')

# 영화 목록 추출
### 가져와야 하는 클래스가 두개 이상일 때 = list로 감싸줌
# movies = soup.find_all("div", attrs= {"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs= {"class":"Vpfmgd"})

# 영화 제목 추출
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else: 
        #print(title, "<할인되지 않는 영화>")
        continue

    # 할인된 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 영화의 링크 정보
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 생성 : https://play.google.com + link
    
    print(f"제목:  {title}")
    print(f"할인 전 금액:  {original_price}")
    print(f"할인 후 금액:  {price}")
    print("링크 : ", "https://play.google.com"+link)
    print("-"*100)

browser.quit()