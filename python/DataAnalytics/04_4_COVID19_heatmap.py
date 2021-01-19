import pandas as pd 
df = pd.read_excel('./DataAnalytics/04_COVID_FILES/kto_total.xlsx')

# 데이터 시각화하기
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


# 히트맵 그래프를 그리기 위해 X축엔 월(month), y축엔 연도(year), 그래프내용엔 관광객 수
# str.slice() 사용해 기준년월을 연도와 월로 분리
df['년도']=df['기준년월'].str.slice(0,4)
df['월']=df['기준년월'].str.slice(5,7)
# print(df.head())

# 데이터를 매트릭스 형태로 변경
condition =(df['국적']=='중국')
df_filter = df[condition]
df_pivot = df_filter.pivot_table(values='관광', index ='년도', columns ='월')
# print(df_pivot)

# 필요한 라이브러리 IMPORT
import matplotlib.pyplot as plt
import seaborn as sns

# 그래프 크기 설정
plt.figure(figsize=(16,10))
# 히트맵 데이터 그리기
sns.heatmap(df_pivot,annot=True, fmt='.0f', cmap='rocket_r')
    # annot=True    : 히트맵 그래프에서 각 칸에 실제 값 표시
    # fmt='.0f'     : 숫자 형태를 소수점이 없는 실수 형태로 표시
    # cmap='rocket_r' : 그래프의 색깔 조합을 지정
# 그래프 타이틀 달기
plt.title('중국인 관광객 히트맵')
plt.show()

# 상위 5개국에 대한 히트맵 그리기
cntry_list = ['중국','일본','대만','미국','홍콩']
for cntry in cntry_list:
    condition =(df['국적']==cntry)
    df_filter = df[condition]
    df_pivot = df_filter.pivot_table(values='관광', index ='년도', columns ='월')
    plt.figure(figsize=(16,10))
    sns.heatmap(df_pivot,annot=True, fmt='.0f', cmap='rocket_r')
    plt.title(cntry + ' 관광객 히트맵')
    plt.show()