# 정규화
import re

p = re.compile("ca.e") 
# . = 하나의 문자를 의미    (ca.e) = care, cake, cave ,,,
# ^ = 문자열의 시작         (^de) = desk, destination ,,,
# $ = 문자열의 끝           (se$) = case, base ,,,

# m= p.match("case")
# print(m.group())

# m= p.match("caffe")     # ff 두글자여서 매칭되지 않음, 에러발생
# # 매칭되면 출력
# if m:
#     print(m.group())
# else:
#     print("매칭되지 않음")

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")