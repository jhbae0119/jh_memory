from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import time 

browser= webdriver.Chrome()
url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'
browser.get(url)
time.sleep(4)

# 서울 클릭
seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
browser.find_element_by_css_selector(seoul_btn).click()
time.sleep(4)
# 전체 클릭
all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'
browser.find_element_by_css_selector(all_btn).click()
time.sleep(4)

# 예제 6-5  BeautifulSoup으로 HTML 파서 만들기
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

# 원하는 HTML 태그 모두 찾기
starbucks_soup_list = soup.select('li.quickResultLstCon')

# 스타벅스 매장 목록 데이터 만들기
starbucks_list = []
for item in starbucks_soup_list:
    name = item.select('strong')[0].text.strip()
    lat = item['data-lat'].strip()
    lng = item['data-long'].strip()
    store_type = item.select('i')[0]['class'][0][4:]
    address = str(item.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
    tel = str(item.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
    starbucks_list.append([ name, lat, lng, store_type, address, tel])
    #starbucks_list.append([ name, lat, lng, store_type, address, tel])

# 데이터 프레임으로 변환
columns = ['매장명','위도','경도','매장타입','주소','전화번호']
seoul_starbucks_df = pd.DataFrame(starbucks_list, columns = columns)
# 엑셀로 저장
seoul_starbucks_df.to_excel('./DataAnalytics./1_seoul_starbucks_list.xlsx', index = False)