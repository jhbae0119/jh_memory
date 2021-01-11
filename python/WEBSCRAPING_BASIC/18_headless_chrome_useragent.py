# headless chrome : 브라우저(chrome)를 굳이 안띄워도 되는 웹스크랩핑에서 사용
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

### headless chrome 설정하기
options = webdriver.ChromeOptions()
options.headless = True     # headless chrome 설정
options.add_argument("window-size=1920x1080")   # 눈에 띄진 않지만 백그라운드에서 도는 브라우저 크기를 지정
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
    # 결과:
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) 
    # HeadlessChrome/87.0.4280.141 Safari/537.36  ==> headlessChrome 사용시 tag가 붙음, 차단당할 수 있음

    # options.add_argument("user-agent=") 에 user-agent값 별도로 입력해줌
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
    # headlessChrome tag 사라짐
browser.quit()