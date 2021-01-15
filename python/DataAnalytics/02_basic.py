import pandas as pd 

sample_1 = pd.read_excel("./02_개정판/2_Data_Analysis_Basic/files/sample_1.xlsx", header=1, skipfooter=2, usecols='A:C')
    # header    = 칼럼명의 위치, 시작숫자가 0임
    # skipfooter = 마지막 로우에서 두줄은 생략
    # usecols   = 사용할 컬럼: A부터 C까지
print(sample_1.head(3)) # head(3) = 처음부터 3번째 로우까지 보여줌
print(sample_1.tail(3)) # tail(3) = 마지막부터 3번째 로우까지 보여줌
print(sample_1.describe())  # describe() = 숫자형 변수에 대한 여러가지 통계량 출력
print(sample_1['입국객수']) # 특정 컬럼만 보고싶을 때 
print(sample_1[['입국객수','입국객수']]) # 특정 컬럼 여러개 보고싶을 때

# 칼럼 생성
sample_1['기준년월'] ='2019-11'
print(sample_1)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 특정 칼럼만 선택
condition = (sample_1['성별']=='남성')
print(condition)
print(sample_1[condition])

condition = (sample_1['입국객수']>=15000)
print(sample_1[condition])

# 두개의 칼럼에 대해 필터링하기= and 조건
conditions = (sample_1['성별']=='남성') & (sample_1['입국객수']>=150000)
print(sample_1[conditions])

# 두개의 칼럼에 대해 필터링하기= or 조건
conditions = (sample_1['국적코드'] == 'A01') | (sample_1['국적코드'] == 'A18'])
print(sample_1[conditions])

# 두개의 칼럼에 대해 필터링하기= isin
conditions = (sample_1['국적코드'].isin(['A01','A18']))
print(conditions)
print(sample_1[conditions])

# 두개의 칼럼에 대해 필터링하기= isin == false
conditions = (sample_1['국적코드'].isin(['A01','A18']))
print(sample_1[conditions==False])

# merge
code_master = pd.read_excel("./02_개정판/2_Data_Analysis_Basic/files/sample_codemaster.xlsx")
print(code_master)

sample_1_code = pd.merge(left = sample_1,\
    right = code_master,\
        how='left',\
            left_on='국적코드',\
                right_on='국적코드'
    )
print(sample_1_code)

# inner 조건
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

sample_1_code = pd.merge(left = sample_1,\
    right = code_master,\
        how='inner',\
            left_on='국적코드',\
                right_on='국적코드'
    )
print(sample_1_code)

# append : 두개 테이블을 아래로 통합하는 방법
sample_2 = pd.read_excel('./02_개정판/2_Data_Analysis_Basic/files/sample_2.xlsx',\
    header=1, skipfooter=2, usecols='A:C')
sample_2['기준년월']='2019-12'
sample_2_code = pd.merge(left=sample_2,\
    right=code_master,\
        how='left',\
            left_on='국적코드',\
                right_on='국적코드')

# print(sample_2_code)

# append
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

sample = sample_1_code.append(sample_2_code, ignore_index=True)

# 엑셀파일로 저장하기
sample.to_excel('./sample.xlsx', index=False)

# pivot table 생성하기
sample_pivot = sample.pivot_table(values = '입국객수', index='국적명', columns ='기준년월', aggfunc = 'mean')
print(sample_pivot)

