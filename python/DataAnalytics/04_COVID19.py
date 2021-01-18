# 01. 데이터 불러오기
import pandas as pd 
kto_201901 = pd.read_excel('./02_개정판/4_Tourists_Event/files/kto_201901.xlsx',\
    header =1, usecols='A:G', skipfooter=4)

# 02. 데이터 전처리
# 02-1. 데이터 파악하기
# print(kto_201901.info())
# print(kto_201901.describe())

# 각 칼럼에서 0인 부분 필터링
condition =(kto_201901['관광']==0) | (kto_201901['상용']==0) | (kto_201901['공용']==0) | (kto_201901['유학/연수']==0)
# print(kto_201901[condition])

# 02-2. 데이터프레임에 기준년월 추가
kto_201901['기준년월'] ='201901'
# print(kto_201901.head())

# # 02-3. 국적 데이터만 남기기
# print(kto_201901['국적'].unique())  #unique() = 칼럼 내 중복을 제거한 값을 보여주는 함수

# 02-4. 필요 없는 요소 제거
continents_list = ['아시아주','미주','구주','대양주','아프리카주','기타대륙','교포소계']
condition =(kto_201901.국적.isin(continents_list)==False)
kto_201901_contry = kto_201901[condition]
# print(kto_201901_contry['국적'].unique)

# 02-5. 인덱스값 재설정
kto_201901_contry_newindex=kto_201901_contry.reset_index(drop=True)
    # .reset_index() = 인덱스값을 0부터 순차적으로 초기화
    # drop=True 사용하지 않을 경우, 기존 인덱스 값이 새로운 칼럼으로 생성됨
# print(kto_201901_contry_newindex.head())

# 02-6. 국적별 대륙명 설정
continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 \
+ ['아프리카']*2 + ['기타대륙'] + ['교포']
# print(continents)

# 02-7. 대륙 칼럼 생성
kto_201901_contry_newindex['대륙']=continents
# print(kto_201901_contry_newindex.head())

# 02-8. 국가별 관광객 비율 살펴보기
kto_201901_contry_newindex['관광객비율(%)'] = round(kto_201901_contry_newindex['관광']/kto_201901_contry_newindex['계']*100,1)
# print(kto_201901_contry_newindex.head())

# 02-9. 관광객 비율이 높고/낮은 5개국
# print(kto_201901_contry_newindex.sort_values(by='관광객비율(%)', ascending=False).head())
# print(kto_201901_contry_newindex.sort_values(by='관광객비율(%)', ascending=True).head())

# 02-10. 대륙별 관광객 비율의 평균
# print(kto_201901_contry_newindex.pivot_table(values ='관광객비율(%)', index ='대륙', aggfunc='mean'))

# 02-11. 중국국적만 필터링
condition =(kto_201901_contry_newindex['국적']=='중국')
# print(kto_201901_contry_newindex[condition])

# 02-12. 기준년월별로 전체 외국인 관광객 대비 국적별 관광객 비율
tourist_sum = sum(kto_201901_contry_newindex['관광'])
# print(tourist_sum) 
# 결과 : 884293 => 2019년 1월에 한국을 방문한 외국인 관광객 수
# 국적별 외국인 관광객수/884293 => 국가별 전체 외국인 관광객 대비 차지하는 비율
kto_201901_contry_newindex['전체비율(%)']= round(kto_201901_contry_newindex['관광']/tourist_sum*100,1)
# print(kto_201901_contry_newindex.head())
# 내림차순 정렬
print(kto_201901_contry_newindex.sort_values('전체비율(%)', ascending =False))

