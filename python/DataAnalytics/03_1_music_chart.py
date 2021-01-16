from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()

# 멜론 뮤직 차트 
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1
songs = soup.select('table > tbody > tr')
for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > a')[0].text
    song_data.append(['Melon',rank, title, singer])
    rank = rank +1

# 데이터 엑셀 파일로 저장하기
import pandas as pd 
columns = ['서비스','순위','타이틀','가수']
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.to_excel('./melons.xlsx', index=False)

# 지니 뮤직 차트 
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1
songs = soup.select('table > tbody > tr')
for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    song_data.append(['Genie',rank, title, singer])
    rank = rank +1

# 데이터 엑셀 파일로 저장하기  
import pandas as pd 
columns = ['서비스','순위','타이틀','가수']
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.to_excel('./genie.xlsx', index=False)

# 두개 엑셀 하나로 합치기
import pandas as pd 
excel_names = ['./melons.xlsx','./genie.xlsx']
appended_data = pd.DataFrame()
for name in excel_names:
    pd_data = pd.read_excel(name)
    appended_data = appended_data.append(pd_data)
# 합친 파일 엑셀로 저장
appended_data.to_excel('./musicChart.xlsx', index = False)