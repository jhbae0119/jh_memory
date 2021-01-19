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

# 전체 관광객 중 중국 국적의 관광객 수 추출
condition = (df['국적']=='중국')
df_filter = df[condition]
# print(df_filter.head())
plt.figure(figsize=(12,4))  # 그래프 크기 지정
plt.plot(df_filter['기준년월'], df_filter['관광'])  # plt.plot(X축칼럼,Y축칼럼)
plt.title('중국 관광객 추이')
plt.xlabel('기준년월')
plt.ylabel('관광객수')
plt.xticks(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', '2015-01', '2016-01', '2017-01', '2018-01', '2019-01', '2020-01'])
plt.show()

# 국적별 외국인 관광객 추이
cntry_list = ['중국','일본','대만','미국','홍콩']
for cntry in cntry_list:
    condition = (df['국적']==cntry)
    df_filter = df[condition]
    plt.figure(figsize=(12,4))
    plt.plot(df_filter['기준년월'], df_filter['관광'])
    plt.title(cntry + ' 관광객 추이')
    plt.xlabel('기준년월')
    plt.ylabel('관광객수')
    plt.xticks(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', '2015-01', '2016-01', '2017-01', '2018-01', '2019-01', '2020-01'])
    plt.show()