# # 사람들이 제주도에서 어떤 장소를 많이 방문하는지

import pandas as pd 
# raw_total = pd.read_excel("./02_개정판/5_Jeju_Hotplace/files/1_crawling_raw.xlsx")

# # 위치별 빈도수 집계
# location_counts = raw_total['place'].value_counts()

# # 빈도수 데이터를 데이터프레임 형태로 변환 후 엑셀 저장
# location_counts_df = pd.DataFrame(location_counts)
# # location_counts_df.to_excel("./DataAnalytics./3_3_location_counts.xlsx")

# # 위치정보의 종류 확인
# locations = list(location_counts.index)

# # 카카오 로컬 API를 활용한 장소검색
# import requests

# def find_places(searching):
#     # ① 접속URL 만들기
#     url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
#     # ② headers 입력하기
#     headers = {
#     "Authorization": "KakaoAK 0cba6af09bfc5ff8c3a0566113014ad7"
#     }
#     # ③ API 요청&정보 받기
#     places = requests.get(url, headers = headers).json()['documents']
#     # ④ 필요한 정보 선택하기
#     place = places[0] 
#     name = place['place_name']
#     x=place['x']
#     y=place['y']
#     data = [name, x, y, searching] 

#     return data

# # 인스타그램 위치명에 대한 위치 정보 검색
# import time
# # from tqdm.notebook import tqdm  #  반복작업 진행시 진행바 표시하기위한 라이브러리 tqdm
# locations_inform = []
# for location in locations:
#     try:
#         data = find_places(location)
#         locations_inform.append(data)
#         time.sleep(3)
#     except:
#         pass

# 위치 정보별 인스타 게시량 정리
# 예제 5-34 인스타 게시량 및 위치정보 데이터 불러오기
location_counts_df = pd.read_excel('./02_개정판/5_Jeju_Hotplace/files/3_location_counts.xlsx', index_col = 0)
locations_inform_df = pd.read_excel('./02_개정판/5_Jeju_Hotplace/files/3_location_inform.xlsx')
# print(location_counts_df.head())
# print("=================================")
# print(locations_inform_df.head())

# 위치 데이터 병합
location_data = pd.merge(locations_inform_df, location_counts_df, how = 'inner', left_on = 'name_official', right_index=True)

print(location_data.head())

# # 장소 이름 기준 병합
# location_data = location_data.pivot_table(index = ['name_official','경도','위도'], values = 'place', aggfunc='sum')
#     # ['name_official','경도','위도']를 통해 값이 모두 동일한 경우 place 값을 병합함
