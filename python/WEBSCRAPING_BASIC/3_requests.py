import requests
res=requests.get("http://naver.com")
res.raise_for_status()
print("응답코드:" , res.status_code)

# #오류 발생시 출력 방법1
# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제발생: 에러코드 [", res.status_code, "]")

# #오류 발생시 출력 방법2
# res.raise_for_status()
# #정상이라면 print
# print("웹 스크래핑을 진행합니다.")
# #오류발생 시, 오류 출력 및 프로그램 종료

#불러오는 페이지의 크기 확인
print(len(res.text))

#페이지 데이터를 파일로 저장하기
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)