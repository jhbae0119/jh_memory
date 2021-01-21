import pandas as pd 
raw_total = pd.read_excel('./02_개정판/5_Jeju_Hotplace/files/1_crawling_raw.xlsx')
# print(raw_total['tags'][:3])

# 해시태그를 통합 저장
tags_total = []
for tags in raw_total['tags']:
    tags_list = tags[2:-2].split("', '")
    for tag in tags_list:
        tags_total.append(tag)

# 빈도수 집계 
from collections import Counter
tag_counts = Counter(tags_total)
# print(tag_counts.most_common(50))

# 정제할 단어
# STOPWORDS = ['#제주도','#제주','#제주도여행', '#서귀포','#jeju','#일상','#성산일출봉','#맞팔', \
# '#제주도그램', '#선팔','#제주살이','#여행스타그램','#제주눈썹문신','#서귀포눈썹문신', '#여행','#제주시','#반영구','#눈썹문신','#제주자연눈썹','#제주속눈썹']
STOPWORDS = ['#일상', '#선팔', '#제주도', '#jeju', '#반영구', '#제주자연눈썹',
'#서귀포눈썹문신', '#제주눈썹문신', '#소통', '#맞팔']

tag_total_selected =[]
for tag in tags_total:
    if tag not in STOPWORDS:
        tag_total_selected.append(tag)

tag_counts_selected=Counter(tag_total_selected)
# print(tag_total_selected)
# print(tag_counts_selected.most_common(50))

# 막대차트로 해시태그 살펴보기
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import sys

if sys.platform in ["win32", "win64"]:
    font_name = "malgun gothic"
elif sys.platform == "darwin":
    font_name = "AppleGothic"

rc('font',family=font_name)

# 데이터 준비
tag_counts_df = pd.DataFrame(tag_counts_selected.most_common(30))
tag_counts_df.columns = ['tags', 'counts']    # 칼럼명 추가

# 막대차트 그리기
plt.figure(figsize =(30,10))
sns.barplot(x = 'counts', y = 'tags', data = tag_counts_df)
plt.show()

# 워드 클라우드 그리기
from wordcloud.pyplot import WordCloud  #wordcloud 설치 실패
import platform

if platform.system() == 'Windows':   #윈도우의 경우
    font_path = "c:/Windows/Fonts/malgun.ttf"
elif platform.system() == "Darwin":   #Mac 의 경우
    font_path = "/Users/$USER/Library/Fonts/AppleGothic.ttf"

# 1. 워드 클라우드 만들기
wordcloud = WordCloud(font_path= font_path, background_color = 'white', max_words = 100, \
    relative_scaling = 0.3, width = 800, height = 400).generate_from_frequencies(tag_counts_selected)
plt.figure(figsize =(30,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./jeju_wordcloud.png')
plt.show()