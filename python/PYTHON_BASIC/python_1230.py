# 8-1. 표준 입출력

# seperation = sep
print("python", "java")                 # python jave
print("python", "java", sep=",")        # python,java
print("python", "java", sep=" vs ")     # python vs java

# end = 줄바꿈 대신 특정 문자로 문장 종료, 뒤의 문장과 연달아 출력
print("python", "java", sep=" vs ", end ="?")
print("무엇이 더 재밌을까요?")            #python vs java?무엇이 더 재밌을까요?

# sys
import sys
print("python", "java", file=sys.stdout)    #표준출력으로 처리
print("python", "java", file=sys.stderr)    #표준에러로 처리 #로그에서 에러 확인 가능하게 함

#시험성적
scores={"math":0,"english":50,"coding":100}
for subject, score in scores.items():   #items:key와 value 쌍으로 tuple로 가져옴
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")  
    # ljst(8)      : 왼쪽 정렬, 8칸
    # rjust(4)     : 오른 정렬, 4칸
    # 결과값
    # math    :   0
    # english :  50
    # coding  : 100

# 은행 대기 순번표
# 001, 002, 003 ...
for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3))     #0값으로 채워줌
    # 출력 결과:
    # 대기번호 :001
    # 대기번호 :002
    # 대기번호 :003 ...
    # 대기번호 :020

# input
answer = input("아무값이나 입력하세요: ")   #사용자 입력을 문자열로 받음
print("입력하신 값은 " + answer + "입니다")


# 8-2. 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:10}".format(500))     #        500

# 양수일 떈 +로 표시, 음수일땐 -로 표시
print("{0:>+10}".format(500))   #       +500
print("{0:>+10}".format(-500))  #       -500

# 왼쪽 정렬을 하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))   # +500______

# 3자리 마다 , 입력
print("{0:,}".format(100000000))   # 100,000,000

# 3자리 마다 , 입력, +- 부호 붙여주기
print("{0:+,}".format(100000000))    # +100,000,000
print("{0:+,}".format(-100000000))   # -100,000,000

# 3자리 마다 , 입력, +- 부호 붙여주기, 자릿수 확보, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(100000000)) # +100,000,000^^^^^^^^^^^^^^^^^^

# 소수점 출력
print("{0:f}".format(5/3))      # 1.666667
# 소수점 출력시: 특정자리수까지만 표시
print("{0:.2f}".format(5/3))    # 1.67


# 8-3. 파일 입출력 = open / write
score_file = open("score.txt", "w", encoding="utf8")
                                # w = 쓰기모드로 열기
                                # encoding = utf8 설정 필요
print("수학 : 0 ", file=score_file)
print("영어 : 0 ", file=score_file)
score_file.close()          # 꼭 close 해줘야 함


# 8-3. 파일 입출력 = open / append
score_file = open("score.txt", "a", encoding="utf8")
                                # a(append) = 추가 입력
                                # encoding = utf8 설정 필요
score_file.write("과학 : 80")
score_file.write("\n코딩 : 80")
score_file.close()          # 꼭 close 해줘야 함

# 8-3. 파일 입출력 = open / read
score_file = open("score.txt", "r", encoding="utf8")
                                # r(read) = 파일 읽기
                                # encoding = utf8 설정 필요
print(score_file.read())
score_file.close()          # 꼭 close 해줘야 함

# 8-3. 파일 입출력 = open / readline
score_file = open("score.txt", "r", encoding="utf8")
                                # r(read) = 파일 읽기
                                # encoding = utf8 설정 필요
print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file.close()          # 꼭 close 해줘야 함

# 파일이 총 몇 줄인지 모를때 1
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line)
score_file.close()          # 꼭 close 해줘야 함


# 파일이 총 몇 줄인지 모를때 2
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 라인 전부 읽어 들여, list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()          # 꼭 close 해줘야 함


# 8-4. pickle
# 프로그램상에서 사용하는 데이터를 파일 형태로 저장하는 것

import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구","야구","배구"]}
print(profile)

pickle.dump(profile, profile_file)  # profile에 있는 정보를 profile_file에 전달
profile_file.close()


import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file의 데이터를 profile에 load
print(profile)
profile_file.close()


# 8-5. with
# with를 쓰면 파일을 열고 읽고 닫는것이 편함

import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# 8-5. with
# with로 파일 작성
import pickle
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부 중")
# with로 파일 읽기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# 8-6. 퀴즈 : 보고서 만들기
# 매주 1회 작성해야하는 보고서가 있습니다.
# - X 주차 주간 보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램 작성
# 조건: 파일명은 '1주차.txt' '2주차.txt' ...와 같이 작성

import pickle
week = input("몇 주차 입니까?")
dept = input("부서: ")
name = input("이름: ")
work = input("업무 요약: ")

with open("{0} 주차 보고서.txt".format(week), "w", encoding="utf8") as report:
    report.write(" - {0} 주차 주간 보고 -".format(week))
    report.write("\n부서 : {0}".format(dept))
    report.write("\n이름 : {0}".format(name))
    report.write("\n업무 요약 : {0}".format(work))


# 선생님 코드
for i in range(1:4):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간 보고 -".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")
