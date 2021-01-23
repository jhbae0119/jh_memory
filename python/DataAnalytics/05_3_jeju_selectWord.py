import pandas as pd 
raw_total = pd.read_excel('./02_개정판/5_Jeju_Hotplace/files/1_crawling_raw.xlsx')

# 단어 선택
# 원하는 단어를 포함하는 게시글 찾기

select_word = '해돋이'
check_list = []
for content in raw_total['content']:
    if select_word in content:
        check_list.append(True)
    else:
        check_list.append(False)

select_df = raw_total[check_list]

fpath = f'./DataAnalytics/4_select_data_{select_word}.xlsx'
# select_df.to_excel(fpath)

# 단어 여러개 선택/추출/저장
select_word_list = ['해돋이','박물관','힐링','게스트하우스','섭지코지']

for select_word in select_word_list:
    check_list = []
    for content in raw_total['content']:
        if select_word in content:
            check_list.append(True)
        else:
            check_list.append(False)

    select_df = raw_total[check_list]
    fpath = f'./DataAnalytics/4_select_data_{select_word}.xlsx'
    select_df.to_excel(fpath)    
