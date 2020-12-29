# 5-1. list

subway=["jhbae","ssong","park"]
print(subway)

#ssong은 몇번째 칸에 타고 있나?
print(subway.index("ssong"))

#탑승객 추가
subway.append("하하")
print(subway)

#원하는 위치에 추가
subway.insert(1,"호호")
print(subway)

#뒤에서 하나씩 빼냄
print(subway.pop())

#정렬
num_list=[5,2,4,3,1]
num_list.sort()
print(num_list)

#거꾸로 정렬
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용 가능
num_list=[5,4,2,1,3]
mix_list=["jojo", 20, True]

#리스트확장
num_list.extend(mix_list)
print(num_list)

# 5-2. 사전
#key에 대한 중복 허용하지 않음

cabinet={3:"유재석", 100:"조세호"}
print(cabinet[3])       #index
print(cabinet.get(3))   #get사용

#오류상황
print(cabinet[5])       #keyError 발생
print(cabinet.get(5))   #none 출력
print(cabinet.get(5,"none대신출력"))    #none 대신 출력하고싶은 text 출력 가능

#값 존재 여부 확인
print(3 in cabinet)     #cabinet에 3이 있는지 확인 #TRUE
print(5 in cabinet)     #cabinet에 5가 있는지 확인 #FALSE

#key값 string도 가능
cabinet = {"A-3": "jhbae", "B-100":"yoo"}
print(cabinet["A-3"])

#사전에 새 항목 추가
print(cabinet)
cabinet["C-100"] = "jojo"

#기존값 변경
print(cabinet)
cabinet["C-100"] = "hyran"  #jojo -> hyran으로 변경

#값 삭제
del cabinet["C-100"]
print(cabinet)

#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key, values 쌍으로 출력
print(cabinet.items())

#전부 삭제(비우기)
cabinet.clear()
print(cab)

# 5-3. tuple
#리스트와 달리 내용 변경, 추가 불가능하지만,
#list보다 처리속도가 빠름
#변경되지 않는 목록을 쓰고 싶을때 사용

menu=("돈까스","치즈까스")
print(menu[0])

#menu.add("생선까스")  #오류발생:'tuple' object has no attribute 'add'

#여러 개의 변수 한번에 선언 가능
(name, age, hobby) =("김종국", 20, "운동")
print(name, age, hobby)

# 5-4. 세트(집합)
# 중복 안됨, 순서 없음

my_set={1,2,3,3,3}
print(my_set)       #{1, 2, 3}

java={"유재석","조세호","박명수"}
python=set(["유재석","양세형"])
#교집합 (java와 python을 모두할 수 있는 개발자)
print(java&python)                      #{'유재석'}
print(java.intersection(python))        #{'유재석'}

#합집합(java or python)
print(java|python)                      #{'박명수', '유재석', '조세호', '양세형'}
print(java.union(python))               #{'박명수', '유재석', '조세호', '양세형'}

#차집합(java는 할 수 있지만 python은 못하는 개발자)
print(java-python)                      #{'조세호', '박명수'}
print(java.difference(python))          #{'조세호', '박명수'}

#집합에 새 값 추가
python.add("김태호")
print(python)                           #{'양세형', '유재석', '김태호'}

#집합의 값 제거
python.remove("김태호")                 
print(python)                           #{'양세형', '유재석'}

# 5-5. 자료구조의 변경

menu={"커피", "우유", "주스"}
print(menu, type(menu))         #{'주스', '커피', '우유'} <class 'set'>

#list로 자료구조 변경
menu = list(menu)
print(menu, type(menu))         #['우유', '커피', '주스'] <class 'list'>

#tuple로 자료구조 변경
menu=tuple(menu)
print(menu, type(menu))         #('커피', '우유', '주스') <class 'tuple'>

# 5-6. 퀴즈 - 추첨 프로그램 작성
# 댓글작성자 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰 증정
# 조건1: 댓글은 20명이 작성하였고, ID는 1~20임
# 조건2: 댓글 내용과 상관없이 무작위로 추첨, 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용

# 출력 예제 
#   -- 당첨자 발표 --
#   치킨 당첨자 : 1
#   커피 당첨자 : {2,3,4}
#   -- 축하합니다 --

# 활용 예제
from random import *
#lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# range활용해서 1-20까지 나열 가능
lst= range(1,21)
lst =list(lst)  #'range' object does not support item assignment #range형태를 list형태로 변경
shuffle(lst)    

#여러번 sample시 중복당첨 가능
winners=sample(lst,4)


print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

# 6-1. IF문

weather = "rain"
if weather == "rain" :
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("준비물 필요없어요")

#입력받기
weather = input("오늘 날씨 어때요?")
if weather == "rain" or weather =="snow":       #조건 추가 = OR 사용
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("준비물 필요없어요")

#날씨
temp = int(input("기온은 어때요?"))
if 30 <= temp :
    print("너무 더워요")
elif 10 <= temp and temp < 30 :
    print("날씨가 좋아요")
elif 0 <= temp < 10:
    print("외투를 챙기세여")
else :
    print("너무 추워요")


# 6-2. for 문

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no)) 

for waiting_no in range(5):     #0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no)) 


starbucks=["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

# 6-3. while문
# 손님 이름을 다섯번 호명시에도 나타나지 않으면 커피를 버리는 시스템

customer ="thor"
index =5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -=1
    if index == 0 :
        print("커피가 폐기처리 되었습니다.")

# 손님이 커피를 찾으러 온다면 while문 종료
customer ="아이언맨"
person="Unknown"

while person != customer : 
    print("{0}님, 커피가 준비되었습니다. ".format(customer))
    person = input("이름이 어떻게 되세요?")

# 6-4. continue와 break
# 반복문 내에서 사용

absent =[2,5]   #결석
no_book=[7]
for student in rnage(1,11) :        #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue                    #반복 계속 수행
    elif student in no_book:
        print("{0}은 교무실로 따라와".format(no_book))
        break                       #뒤의 값 여부와 상관없이 반복문 종료
    print("{0}, 책을 읽어봐".format(student))

# 6-5. 한줄 for
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

student =[1,2,3,4,5]
print(student)

student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
student=["Iron man", "thor","groot"]
student=[len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
student=["Iron man", "thor","groot"]
student=[i.upper() for i in student]
print(student)


# 6-6. 퀴즈 : 총 탑승객 수를 구하는 프로그램
# 50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램 작성
# 조건1: 승객별 운행 소요시간은 5분~50분 사이의 난수로 정해짐
# 조건2: 당신은 소요시간 5분~15분 사이의 승객만 매칭

# 출력문 예제
# [0] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [0] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간: 18분)
# 총 탑승 승객 : 2 명

from random import *
cnt = 0

for i in range(1,51) :
    time = randrange(5,51)
    if 5 <= time <=15:
        print("[0] {0}번째 손님 (소요시간: {1}분)".format(i,time))
        cnt +=1
    else :
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i,time))
print("총 탑승 승객 : {0} 명".format(cnt))   


# 7-1. 함수
def open_account():
    print("계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance

def withdraw_night(balance, money):
    commission  = 100 #수수료 100원
    return commission, balance - money - commission

#입금 예시
balance = 0
balance = deposit(balance, 3000)

#출금 예시
balance = 0
balance = deposit(balance, 3000)
balance = withdraw(balance, 2000)

#야간 출금 예시
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원입니다. 잔액은 {1}원입니다.".format(commission,balance))

# 7-3. 기본값
def profile(name, age, main_lan):
    print("이름 : {0}\t나이 : {1}\t주 사용언어: {2}"\
        .format(name, age, main_lan))

profile("유재석", 20, "python")
profile("jojo", 25, "java")

def profile_default(name, age=17, main_lan="python"):
    print("이름 : {0}\t나이 : {1}\t주 사용언어: {2}"\
        .format(name, age, main_lan))

profile_default("유재석")
profile_default("jojo")

# 7-4. 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

#키워드인 name, age, main_lang에 값 지정가능 
profile(name="jhbae", main_lang="python", age=17)       #순서 상관없음


# 7-5. 가변인자

def profile(name, age, lang1,lang2,lang3, lang4,lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #end =print문이 끝나도 줄바꿈을 하지 않고 띄어쓰기 후, 이어서 다음 print문 출력
    print(lang1,lang2,lang3,lang4,lang5)

profile("jhbae",20,"python","java","C","C++","GO")
profile("jjjj",17,"python","java","","","")         

#만약, 할줄 아는 언어가 늘어난다면? => 매번 함수를 수정해야 하는가?
#만약, 할줄 아는 언어가 5개가 안된다면? => 매번 빈칸을 입력해줘야 하는가?
#가변 인자 사용해야함!

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #end =print문이 끝나도 줄바꿈을 하지 않고 띄어쓰기 후, 이어서 다음 print문 출력
    for lang in language:
        print(lang, end=" ")
    print()

print("------가변인자 사용-----")
profile("jhbae",20,"python","java","C","C++","GO","6666","777")
profile("jjjj",17,"python","java222") 


# 7-6. 지역변수와 전역변수
# 지역변수 : 함수 내에서 사용하는 변수, 함수호출이 종료되면 사라지는 변수
# 전역변수 : 프로그램 내에서 모든 곳에서 사용할 수 있는 변수

print("------지역변수와 전역변수의 차이점------")
gun = 10        # gun = 전역변수        
def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("함수 내 지역변수 gun의 남은 수: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)   #2명이 총을 들고 경계근무를 나감
print("전체 총 : {0}".format(gun))          # 함수 외부의 전역변수 gun의 개수 반환

##해결방법##
print("------global 변수 지정------")
gun = 10        # gun = 전역변수        
def checkpoint2(soldiers):
    global gun      #전역공간에 있는 gun 사용
    gun = gun - soldiers
    print("함수 내 지역변수 gun의 남은 수: {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint2(2)   #2명이 총을 들고 경계근무를 나감
print("전체 총 : {0}".format(gun))          # 함수 외부의 전역변수 gun의 개수 반환

## 일반적으로 global 변수가 많아지면 관리하기가 어려워짐
## 가급적 함수의 파라미터로 사용하는걸 권장
print("------함수의 파라미터 사용------")
gun = 10        # gun = 전역변수        
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("함수 내 지역변수 gun의 남은 수: {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun,2)
print("전체 총 : {0}".format(gun))     
