# 10-1. 예외처리
try:
    print("나누기 전용 계산기")
    nums=[]
    nums.append(int(input("숫자입력: ")))
    nums.append(int(input("숫자입력: ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1}={2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값이 입력되었습니다.")
except ZeroDivisionError as err:
    print(err)
except:
    print("알 수 없는 에러가 발생했습니다.")


# 10-2. 에러 발생 시키기
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("숫자입력:"))
    num2 = int(input("숫자입력:"))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("두자리 이상은 계산할 수 없습니다.")

# 사용자가 정의한 에러명 사용
class BigNumberError(Exception):
    # 방법 1
    # pass
    # 방법 2: 정의한 메시지 출력
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("숫자입력:"))
    num2 = int(input("숫자입력:"))
    if num1 >= 10 or num2 >= 10:
        # 방법 1
        # raise BigNumberError
        # 방법 2: 정의한 메시지 출력
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except BigNumberError as err:
    print("BigNumberError: 두자리 이상은 계산할 수 없습니다.")
    print(err)
# 10-4. finally 
# 예외처리 구분에서 정상수행 여부와 상관없이 항상 실행되는 구문
finally:
    print("계산기를 사용해주셔서 감사합니다.")

# 10-5. 퀴즈 9 : 자동 주문 시스템 만들기
# 치킨 자동 주문 시스템 제작, 적절한 예외처리 구문 넣기

# 조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올땐 ValueError 처리
#     출력 메시지: "잘못된 값을 입력하였습니다."
# 조건2: 대기 손님이 주문할 수 있는 치킨 수량은 총 10마리.
#     치킨 소진시, 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#     출력 메시지: "재고가 소진되어 주문을 받지 않습니다."

class SoldOutError(Exception):
    pass

chicken = 10
waiting =1
while(True):
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = int(input("치킨 주문 수량: "))
        if order > chicken : #남은 치킨보다 수량이 더 많을 때
            print("재고가 부족합니다.")
        elif order > 10:
            raise ValueError
        else:
            print("[대기번호 {0}번 손님, {1}마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting +=1
            chicken -= order

        if chicken ==0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 주문을 받지 않습니다.")
        break
