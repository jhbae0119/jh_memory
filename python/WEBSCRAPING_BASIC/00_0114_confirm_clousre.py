from selenium import webdriver
import pandas as pd
import time 

df = pd.read_csv("tmp_data.csv")
df
def confirm_closure(df):
    driver = webdriver.Chrome()
    url = "https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml"
    driver.get(url)
    time.sleep(3)

    result_list = []
    for reg_no in df['가맹점 번호']:
        driver.find_element_by_id('bsno').send_keys(reg_no)
        driver.find_element_by_id('trigger5').click()
        time.sleep(2)
        result = driver.find_element_by_id("grid2_cell_0_1").text
        #print(result)
        rst = None
        if '폐업자' in result:
            rst = '폐업/' + result.split("폐업일자:")[1].split(")")[0]
        elif '일반과세자' in result:
            rst ="일반"
        else:
            rst ="미등록"
        result_list.append(rst)
        time.sleep(5)
    driver.close()
    return pd.Series(result_list)

df['결과'] = confirm_closure(df)
print(df)