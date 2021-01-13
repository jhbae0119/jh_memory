# 지점, 현재기온, 체감온도 저장

import re
import requests
from bs4 import BeautifulSoup

url ="http://www.weather.go.kr/weather/observation/currentweather.jsp"
headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# table 중 table_develop3 클래스 저장
table = soup.find("table", attrs ={"class":"table_develop3"})

data = []

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):    # <td> 안에 <a> 태그가 있으면(지점인지 확인)
            # 지점명 
            point = td.find('a').text
            # 현재 온도
            temperature = tds[5].text
            # 체감 온도
            feel_temperature = tds[7].text
            print(point,temperature,feel_temperature)
#             data.append([point,temperature,feel_temperature])
# with open('weather.csv', 'w') as file:
#     file.write('point,temperater,feel_temperature\n')
#     for i in data:
#         file.write('{},{},{}\n'.format(i[0],i[1],i[2]))     
