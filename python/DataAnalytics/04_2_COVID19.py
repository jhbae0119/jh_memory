# 1. 엑셀 파일 불러오기
# 2. 기준년월 칼럼 추가
# 3. 국적 데이터만 남기기(대륙 데이터 삭제)
# 4. 대륙 칼럼 생성
# 5. 국적별 관광객비율(%) 살펴보기
# 6. 전체 외국인 관광객 대비 국적별 관광객 비율 보기
import pandas as pd 
def create_kto_data(yy,mm):
    # 1. 불러올 엑셀 파일 경로 지정
    file_path = './02_개정판/4_Tourists_Event/files/kto_{}{}.xlsx'.format(yy,mm)

    # 2. 엑셀 파일 불러오기
    df = pd.read_excel(file_path, header=1, skipfooter=4, usecols='A:G')

    # 3. 기준년월 칼럼 추가
    df['기준년월']='{}-{}'.format(yy,mm)

    # 4. "국적"칼럼에서 대륙 제거
    ignore_list = ['아시아주','미주','구주','대양주','아프리카주','기타대륙','교포소계']
    condition =(df['국적'].isin(ignore_list)==False)    #ignore_list에 없는 데이터만 저장
    df_country = df[condition].reset_index(drop=True)

    # 5. 대륙 칼럼 추가
    continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 + ['아프리카']*2 + ['기타대륙'] + ['교포']
    df_country['대륙']= continents

    # 6. 국가별 "관광객비율(%)" 칼럼 추가
    df_country['관광객비율(%)'] = round(df_country.관광/df_country.계*100,1)

    # 7. "전체비율(%)" 칼럼 추가
    tourist_sum = sum(df_country['관광'])
    df_country['전체비율(%)'] = round(df_country['관광']/tourist_sum*100,1)

    # 8. 결과 출력
    return(df_country)

# 여러 엑셀 파일 불러와서 하나로 합치기
# 01. 데이터를 담을 빈 데이터프레임 생성
df = pd.DataFrame()
# 02. 데이터 201001~202012 통합 데이터 생성
for yy in range(2010,2021):
    for mm in range(1,13):
        try:
            temp = create_kto_data(str(yy), str(mm).zfill(2))
            df = df.append(temp, ignore_index=True)
        except:
            pass

# 03. 통합 데이터를 엑셀로 저장
df.to_excel('./DataAnalytics/04_COVID_FILES/kto_total.xlsx', index = False)

# # 04. 국적별 데이터를 엑셀로 저장
# cntry_list=df['국적'].unique()
# for cntry in cntry_list:
#     # 국적으로 필터링
#     condition = (df['국적']==cntry)
#     df_filter=df[condition]
#     # 국적명을 반영한 파일명 만들기
#     file_path ='./DataAnalytics/04_COVID_FILES/[국적별관광객데이터] {}.xlsx'.format(cntry)
#     # 정해놓은 파일명으로 저장하기
#     df_filter.to_excel(file_path, index=False)


# # 예제 4-40 개별 국적별 관광객 데이터 저장하기 
# for cntry in cntry_list: 
#     # 국적으로 필터링 
#     condition = (df['국적'] == cntry)
#     df_filter = df[condition]
    
#     # 국적이름을 반영한 파일명 만들기 
#     file_path = './files/[국적별 관광객 데이터] {}.xlsx'.format(cntry)
    
#     # 정해 놓은 파일명으로 저장하기 
#     df_filter.to_excel(file_path, index = False)