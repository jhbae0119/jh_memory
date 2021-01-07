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
        print(m.group())    #.group은 일치하는 문자열 반환
        print(m.string)     #.string: 입력받은 문자, 변수가 아님(괄호없이 사용)
        print(m.start())    #.start: 일치하는 문자열의 시작 index 
        print(m.end())      #.end: 일치하는 문자열의 끝 index
        print(m.span())     #.span: 일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지 않음")

# 정규식 02

#비교 .match 는 주어진 문자열의 처음부터 일치하는지 확인
m = p.search("good care")
print_match(m)
# .search는 주어진 문자열 중에 일치하는게 있는지 확인

lst = p.findall("careless")   #.findall: 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 정규식 쓸 때
# 1) p = re.compile("원하는 형태")
# 2) m = p.match("비교할 문자열"): 주어진 문자열의 처음부터 일치하는지 확인
# 3) m = p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
# 4) lst = p.findall("비교할 문자열"): 일치하는 모든 것을 "리스트 형태"로 반환

# 원하는 형태 = 정규식이 됨
# 1) . = 하나의 문자를 의미    (ca.e) = care, cake, cave ,,,
# 2) ^ = 문자열의 시작         (^de) = desk, destination ,,,
# 3) $ = 문자열의 끝           (se$) = case, base ,,,