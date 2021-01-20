from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")
time.sleep(2)

# 인스타그램 로그인하기
# id 입력
email = 'jjing_8o8'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

# password 입력
password = '**jjing1207!'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(3)

# 인스타그램 검색 결과 URL 만들어 접속하기
def insta_searching(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url

time.sleep(5)

# 검색 결과 페이지 접속하기
word ='제주도맛집'
url = insta_searching(word) 
driver.get(url)

time.sleep(5)

# 검색결과 첫번째 게시글 클릭하기
def select_first(driver):
    first = driver.find_element_by_css_selector("div._9AhH0")
    time.sleep(5)
    first.click()
    time.sleep(3)

select_first(driver)

# 게시글 정보 가져오기
import re
from bs4 import BeautifulSoup
import unicodedata

def get_content(driver):
    # 현재 페이지 HTML 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    # 본문 내용 가져오기
    try:
        content = soup.select('div.C4VMK > span')[0].text
        content = unicodedata.normalize('NFC', content)
    except:
        content = " "
    
    # 본문 내용에서 해시캐드 가져오기
    tags = re.findall(r'#[^\s#,\\]+', content)

    # 작성일자 정보 가져오기
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]

    # 좋아요 수 가져오기
    try:
        like = soup.select('div.Nm9Fw > button')[0].text[4:-1]
    except:
        like = 0
    
    # 위치정보 가져오기
    try:
        place = soup.select('div.M30cS')[0].text
        place = unicodedata.normalize('NFC', place)
    except:
        place = ' '
    
    # 수집한 정보 저장하기
    data = [content, date, like, place, tags]
    print(data)
    return data

get_content(driver)

# 다음 게시글 열기
def move_next(driver):
    right = driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)

move_next(driver)