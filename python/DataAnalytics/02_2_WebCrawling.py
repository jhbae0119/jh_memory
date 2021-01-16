from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()

url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# songs = soup.select('table > tbody > tr')
# # print(len(songs))
# # print(songs[0])

songs = driver.find_elements_by_css_selector('table > tbody > tr')
for song in songs:
    title = song.find_elements_by_css_selector('div.ellipsis.rank01 > span > a')[0].text
    singer = song.find_elements_by_css_selector('div.ellipsis.rank02 > a')[0].text
    print(title, singer, sep ="|")
# title = songs[0].text
# singers = driver.find_elements_by_xpath("//*[@id='frm']/div/table/tbody/tr[1]/td[4]/div/div/div[2]")
# singer = singers[0].text
# print(title)
# print(singer)

# for song in songs:
#     title 