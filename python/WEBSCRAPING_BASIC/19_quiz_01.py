# Quiz 부동산 매물 정보 스크래핑 프로그램

# [조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ============매물 1=============
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# ============매물 2=============
# ...

### 필요한 library
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# # 1. 다음으로 이동
# browser = webdriver.Chrome("./chromedriver.exe")
# browser.maximize_window()

# url = "http://daum.net"
# browser.get(url)        # url로 이동

# # 검색창 선택
# browser.find_element_by_xpath("//*[@id='q']").click()

# # 송파 헬리오시티 입력
# browser.find_element_by_xpath("//*[@id='q']").send_keys("송파 헬리오시티")

# # 검색버튼 선택
# browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()

# url
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")
    print("============매물 {}=============".format(index+1))
    print("거래 : ", columns[0].get_text().strip())
    print("면적 : ", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 : ", columns[2].get_text().strip(), "(만원)")
    print("동 : ", columns[3].get_text().strip())
    print("층 : ", columns[4].get_text().strip())

    #.strip() 불필요한 빈칸 삭제
