from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd 

# browser = webdriver.Chrome()
# url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
# browser.get(url)

# html = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')

# # 여러 페이지에서 데이터 받기
# page = 1
# results = []
# for page in range(1,11):
#     url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
#     browser.get(url)
#     time.sleep(2)
#     html = browser.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     channel_list = soup.select('form > table > tbody > tr')
#     for channel in channel_list:
#         title = channel.select('h1 > a')[0].text.strip()
#         category = channel.select('p.category')[0].text.strip()
#         subscriber = channel.select('.subscriber_cnt')[0].text
#         view = channel.select('.view_cnt')[0].text
#         video = channel.select('.video_cnt')[0].text
#         data = [title, category, subscriber, view, video]
#         results.append(data)
# # 데이터 엑셀로 저장하기
# df = pd.DataFrame(results)
# df.columns = ["title", "category", "subscriber", "view", "video"]
# df.to_excel('./youtube_rank.xlsx', index = False)

# 랭킹 데이터 시각화하기
import matplotlib.pyplot as plt 

# matplotlib를 사용할때 한글깨짐을 방지하기 위해 글꼴 변경이 필요
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path ='C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check your OS system')

# 데이터 파일 불러오기
df = pd.read_excel('./youtube_rank.xlsx')

# str.replace : 특정 문자를 다른 문자로 변경
df['replaced_subscriber'] = df['subscriber'].str.replace('만','0000')
# print(df.head())

# astype() : 데이터 타입 변경
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
# print(df.info())

# 카테고리별 구독자 수, 채널 수 피봇테이블 생성하기
pivot_df = df.pivot_table(index='category',values = 'replaced_subscriber', aggfunc=['sum','count'])
# print(pivot_df.head())

# 칼럼명 변경
pivot_df.columns =['subscriber_sum', 'category_count']

# 인덱스 초기화
pivot_df = pivot_df.reset_index()

# 데이터 프레임 내림차순 정렬
pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)
print(pivot_df.head())

# 카테고리별 구독자 수 시각화
plt.figure(figsize=(30,10))     # figure() = 차트 크기 설정
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()

# 카테고리별 채널 수 시각화
pivot_df = pivot_df.sort_values(by='category_count', ascending=False)
plt.figure(figsize=(30,10))     # figure() = 차트 크기 설정
plt.pie(pivot_df['category_count'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()
