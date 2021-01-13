# 지점, 현재기온, 체감온도 저장

import re
import requests
from bs4 import BeautifulSoup

url ="http://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2020&mm=12&obs=1&x=21&y=7"
headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# table 중 table_develop3 클래스 저장
table = soup.find("table", attrs ={"class":"table_develop"})

data = []

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    # print(tds)
    for td in tds[1::2]: 
        print(td.get_text())
    # print(tds[8].text)
    # for td in tds:
    #     if :
    #         print(td)
            # 일자 
            # sunday = tds[0].text
            # monday = tds[1].text
            # tuesday = tds[2].text
            # print(sunday, monday, tuesday)
            # wednesday = tds[3].text
            # thursday = tds[4].text
            # friday = tds[5].text
            # saturday = tds[6].text
            
            # print(monday,tuesday,wednesday)
            # data.append([point,temperature,feel_temperature])
# with open('weather.csv', 'w') as file:
#     file.write('point,temperater,feel_temperature\n')
#     for i in data:
#         file.write('{},{},{}\n'.format(i[0],i[1],i[2]))     
