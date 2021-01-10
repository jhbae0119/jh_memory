import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")


### 네이버 로그인 하기 ###
# 1. 네이버 이동 
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_elements_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_elements_by_id("id").send_keys("naver_id")
browser.find_elements_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)   # 바로 새로운 아이디 입력할 수 없음: 3초 지연 걸기

# 5. 이전에 입력된 값 삭제
browser.find_element_by_id("id").clear())

# 6. id 새로 입력
browser.find_element_by_id("id").send_keys("my id")

# 7. html 정보 출력
print(browser.page_source)  # 지금 페이지의 모든 html 문서 출력

# 8. 브라우저 종료
browser.close()     # 현재 탭만 종료
browser.quit()      # 전체 브라우저 종료