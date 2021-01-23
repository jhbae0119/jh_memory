import pandas as pd

location_data = pd.read_excel("./02_개정판/5_Jeju_Hotplace/files/3_location_inform.xlsx")

# 지도 표시
import folium

Mt_Hanla =[33.362500, 126.533694]
map_jeju = folium.Map(location = Mt_Hanla, zoom_start = 11)

for i in range(len(location_data)):
    name = location_data ['name_official'][i]    # 공식명칭
    count = location_data ['place'][i]           # 게시글 개수
    size = int(count)*2
    long = float(location_data['위도'][i])      
    lat = float(location_data['경도'][i])       
    folium.CircleMarker((long,lat), radius = size, color='red', popup=name).add_to(map_jeju)
    
# 파일로 저장
map_jeju.save("./DataAnalytics/3_jeju.html")