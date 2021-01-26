import requests     # OPEN API 호출을 위해 requests 라이브러리 사용
import pandas as pd 

# 서울열린데이터광장 API 호출키
SEOUL_API_AUTH_KEY = '64497367537075703833784a635057'


# OPEN API 호출을 위한 공통 함수 만들기
def seoul_open_api_data(url, service):
    data_list = None
    try:
        # 결과값 json 형태로 변환
        result_dict = requests.get(url).json()

        # 목록 결과 딕셔너리 데이터 값 가져오기
        result_data = result_dict['SdeTlSccoSigW']

        #
        code = result_data['RESULT']['CODE']
        if code == 'INFO-000':
            data_list = result_data['row']
    except:
        pass

    return data_list

# 시군구 목록 데이터 수집 후 엑셀 다운로드
# 시군구 목록을 가져오는 API 호출 URL
sgg_url = 'http://openapi.seoul.go.kr:8088/{}/json/SdeTlSccoSigW/1/25'.format(SEOUL_API_AUTH_KEY)

sgg_data_list = seoul_open_api_data(sgg_url, 'SdeTlSccoSigW')

# 결과값을 데이터프레임으로 변환
columns = ['SIG_CD','SIG_KOR_NM','LAT','LNG']
sgg_df = pd.DataFrame(data = sgg_data_list, columns = columns)

# 컬럼명 변경
sgg_df.columns = ['시군구 코드','시군구 명','위도','경도']

# 데이터 엑셀 저장
sgg_df.to_excel('./DataAnalytics/2_seoul_sgg_list.xlsx', index = False)