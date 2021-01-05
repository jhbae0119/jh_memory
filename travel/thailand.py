class ThailandPackage:
    def detail(self):
        print("thailand package")

if __name__=="__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈이 직접 실행됨을 의미합니다.")
    trip_to =ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 모듈외부에서 호출")