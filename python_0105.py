# 11-4. 모듈 직접 실행
# thailand 모듈 수정
# class ThailandPackage:
#     def detail(self):
#         print("thailand package")

# if __name__=="__main__":
#     print("Thailand 모듈을 직접 실행")
#     print("이 문장은 모듈이 직접 실행됨을 의미합니다.")
#     trip_to =ThailandPackage()
#     trip_to.detail()
# else:
#     print("Thailand 모듈외부에서 호출")

# 11-5. 패키지 및 모듈 위치
# 패키지와 모듈 위치 확인하는 방법
import inspect
import random
print(inspect.getfile(random))      # 결과: C:\Python39\lib\random.p
#print(inspect.getfile(thailand))

# 11-6. pip install
# 파이썬은 잘 만들어진 패키지를 쉽게 쓸 수 있게 함
# pypi 싸이트 활용

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 패키지 설치하기
pip install <package name>

# 설치된 pip list 확인
pip list

# 특정 패키지의 정보 보기
pip show <package name>

# 설치한 패키지 업그레이드
pip install --upgrade <package name>

# 설치한 패키지 삭제하기
pip uninstall <package name>

# 11-7. 내장 함수

# input: 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
    #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
import random
print(dir())
    #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'random']
import pickle
print(dir())
    #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pickle', 'random']

lst=[1,2,3]
print(dir(lst))
    # lst에서 쓸 수 있는 내용들 출력
    #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pickle', 'random']

# 11-8. 외장 함수
# 직접 import 해서 사용해야함

# glob: 경로 내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py"))    #확장자가 py인 모든 파일
                            #['python_practice.py']


# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder ="sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)    # 폴더 삭제
    print("폴더를 삭제하였습니다.")
else:   
    os.makedirs(folder) # 폴더 생성
    print(folder,"폴더를 생성하였습니다.")

# 11-8. 외장 함수
# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))   #2021-01-05 22:13:05

import datetime
print(datetime.date.today())        #2021-01-05

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()   # 오늘 날짜 저장
td= datetime.timedelta(days=100)    # 100일 저장
print("우리가 만난지 100일 되는 날", today+td)  #우리가 만난지 100일 되는 날 2021-04-15

# 11-9. 퀴즈 9
# 프로젝트에 나만의 시그니처를 남기는 모듈 만들기
# 조건: 모든 파일명은 byme.py로 작성
# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도 코딩에 의해 만들어졌습니다.
# 유튜브: xxx.youtube.com 
# 이메일: xxx@mail.com 

import byme
byme.sign()