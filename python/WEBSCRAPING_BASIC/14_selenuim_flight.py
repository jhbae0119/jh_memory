### 네이버 항공권 예약하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1. 네이버 항공권 예약 페이지로 이동
browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)        # url로 이동

# 가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] 이번 달
# browser.find_elements_by_link_text("28")[0].click() # [0] 이번 달

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] 다음 달
# browser.find_elements_by_link_text("28")[1].click() # [1] 다음 달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] 이번 달
browser.find_elements_by_link_text("28")[1].click() # [1] 다음 달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 로딩 처리하기
try: 
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
        # WebDriverWait를 통해서 browser를 10초동안 대기시키는데,
        # XPATH 조건에 맞는 element가 나오면 대기 종료
        # By.XPATH 외에도 ID, CLASS_NAME, LINK_TEXT 등 사용 가능
    print(elem.text)    # 첫번째 결과 출력
finally:
    browser.quit()