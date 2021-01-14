from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.get("https://www.google.co.kr/")

elem = driver.find_element_by_name("q")
elem.send_keys("김선호")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_class_name("hide-focus-ring")
elem.click()
# time.sleep(2)

#### 스크롤 내리기 ####
# SCROLL_PAUSE_TIME = 1

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_elements_by_css_selector(".mye4qd")
#         except: 
#             break
#     last_height = new_height

### 이미지 저장 ####
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    image.click()
    time.sleep(3)
    imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, str(count)+"김선호.jpg")
    count = count +1
driver.close()