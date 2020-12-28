#랜덤함수
from random import *
print(random())             #0.0~1.0 미만의 임의의 값 생성
print(random() *10)         #0.0~10.0 미만의 임의의 값 생성
print(int(random() *10))    #0~10 미만의 임의의 값 생성
print(int(random() *10)+1)  #1~10 미만의 임의의 값 생성

#로또
print(int(random() * 45)+1) #1~45 이하의 임의의 값 생성

#다른 방식 randomrange #미만
print(randrange(1,46))      #1~46미만의 임의의 값 생성

#다른 방식 randint #이하
print(randint(1,45))        #1~45 이하의 임의의 값 생성

#Quiz
    #월 4회 스터디 모임: 3번은 온라인, 1번은 오프라인
    #아래 조건에 맞는 오프라인 모임 날자를 정해주는 프로그램 작성

    #조건1: 랜덤으로 날짜 뽑기
    #조건2: 월별 날짜는 다름을 감안하여 최소 일수는 28일 이내로 정함
    #조건3: 매월 1~3일은 스터디 준비를 해야하므로 제외

    #출력문: 오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.


from random import *
Study_date=randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(Study_date) + "일로 선정되었습니다.")
#Study_date는 숫자형이기때문에 문자열로 바꿔줘야 함

#4-1. 문자열
sen = '나는 소년입니다.'
print(sen)
sen2 = "파이썬은 쉬워요"
print(sen2)

#여러개 문장 한번에 출력하기
sen3 = """
나는 소년입니다.
파이썬은 쉬워요
펭펭펭!
"""
print(sen3)

#4-2 슬라이싱
jumin="990101-1234567"
      #01234567890123
print("성별: " + jumin[7])
print("생년: " + jumin[0:2])    #0부터 2직전까지
print("월: " + jumin[2:4])      #2부터 4직전까지
print("일: " + jumin[4:6])      #4부터 6직전까지
print("생년월일: " + jumin[:6])  #처음부터 6 직전까지
print("뒤 7자리: " + jumin[7:])  #7부터 끝까지
print("뒤 7자리(뒤부터): " + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지

#4-3 문자열 처리함수
python="Python is Amazing"
print(python.lower())       #python is amazing
print(python.upper())       #PYTHON IS AMAZING

#대문자인지 확인
print(python[0].isupper())  #True

#문자열 길이 반환
print(len(python))          #17

#문자열 치환
print(python.replace("Python", "java"))     #java is Amazing

#특정 문자 위치 반환
Index=python.index("n")     #n의 위치 반환
print(Index)
Index=python.index("n", Index+1)     #두번째 n 찾기 index(찾을 text, start위치)
print(Index)

#특정 문자열 찾기
print(python.find("Python"))
print(python.find("java"))
print(python.index("Python"))
#print(python.index("java")) # Exception has occurred: ValueError : substring not found

#특정문자열이 몇번 나오는지 count
print(python.count("n"))

#4-4. 문자열 포맷

#방법1
print("나는 %d살 입니다." % 20)                #%d에 %이후에 오는 값을 입력 : d는 정수값
print("나는 %s를 좋아합니다." % "파이썬")       #%s에 %이후에 오는 값을 입력 : s는 문자열
print("Apple은 %c로 시작합니다." % "A")        #%c에 %이후에 오는 값을 입력 : c는 character, 한글자만 받음
print("나는 %s색과 %s색을 좋아합니다." % ("빨간","파란")) #%s에 %이후에 오는 값을 입력: 여러개는 괄호로 묶어

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아합니다.".format("파란","빨간")) #중괄호에 순번을 넣을 수 있음
print("나는 {1}색과 {0}색을 좋아합니다.".format("파란","빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))

#방법4 (ptyhon v3.6이상부터 사용가능)
age = 20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") #f값을 넣으면 실제 변수값을 입력받을 수 있음

#4-5. 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문자열 탈출문자 
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \ 하나로 인식
print("C:\\Users\\Jaehyun\\Desktop\\PythonWork")

# \r : 커서를 맨앞으로 이동
print("Red Apple\rPine")        #Red Apple -> 커서 맨앞으로 이동 -> 'Red '부분에 'Pine' 입력

# \b : 백 스페이스(한글자삭제)
print("Redd\bApple")        #RedApple

# \t : 탭
print("red\tapple")         #red     apple

#Quiz
    #사이트별로 비밀번호를 만들어주는 프로그램 작성

    # 예) http://naver.com
    # 규칙1 : http:// 부분은 제외 => naver.com
    # 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
    # 규칙3: 남은 글자중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1)+ "!"로 구성
    # 최종 생성 비밀번호: nav51!

site ="http://naver.com"
rule1=site[7:]
#print(rule1)
rule2 = rule1[:rule1.index(".")]
#print(rule2)
rule3 = rule2[:3]
#print(rule3) 
password= rule3 + str(len(rule2)) + str(rule2.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(site, password))