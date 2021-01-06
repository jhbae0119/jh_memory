# 9-7. 연산자 오버로딩
# 클래스에서 정의한 메소드 말고 자식 클래스에서 정의한 메소드를 쓰고 싶을떄,
# 메소드를 새롭게 정의해서 사용하는 것

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("지상 유닛 이동")
        print("{0}:{1} 방향으로 이동합니다.[속도 {2}]"\
            .format(self.name,location,self.speed))

# 공격 유닛 : 일반 유닛의 속성을 상속받아 생성할 수 있다.
class AttackUnit(Unit):     # 괄호 속에 상속 받고 싶은 클래스명 입력
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # 상속받을 클래스 호출
        self.damage = damage
    def attack(self, location):
        print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
            .format(self.name,location,self.damage))
    def damaged(self, damage):
        print("{0}:{1} 데미지를 받았습니다.".format(self.name,self.hp))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0}:{1} 방향으로 날아갑니다.[속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  #지상 speed는 0
        Flyable.__init__(self, flying_speed)
    ############ 연산자 오버로딩 ###############
    # move 함수 재정의 = Unit.move가 호출되는 것이 아닌, FlyableAttackUnit의 move 함수 사용
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌처: 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌처", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력 좋고, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")

# 연산자 오버로딩이 없다면:
# battlecruiser.fly(battlecruiser.name,"9시")
# 연산자 오버로딩을 한다면:
battlecruiser.move("9시")



# 9-8. Pass

class BulidingUnit(Unit):
    def __init__(self, name, hp, location):
        pass        # pass = 아무것도 안하고 일단은 넘어간다

# 건물생성 : 1개 건물 마다 8개의 unit 생성
supply_depot = BulidingUnit("서플라이디폿", 500, "7시")

# pass 예제
def game_start():
    print("[알림] 게임을 시작합니다.")
def game_over():
    pass

game_start()
game_over()


# 9-9. super

class BulidingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, speed)
        super().__init__(name, hp, 0)   # super 사용시 괄호를 붙이고, self.사용하지 않음 # 다중상속 불가능
        self.location = location

# 9-9. 스타크래프트 프로젝트
from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다".format(self.name))

    def move(self, location):
        print("지상 유닛 이동")
        print("{0}:{1} 방향으로 이동합니다.[속도 {2}]"\
            .format(self.name,location,self.speed))

    def damaged(self, damage):
        print("{0}:{1} 데미지를 받았습니다.".format(self.name,self.hp))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛 : 일반 유닛의 속성을 상속받아 생성할 수 있다.
class AttackUnit(Unit):     # 괄호 속에 상속 받고 싶은 클래스명 입력
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # 상속받을 클래스 호출
        self.damage = damage
    def attack(self, location):
        print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
            .format(self.name,location,self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩: 일정 시간동안 이동 및 공격 속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp >= 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. HP 10 감소".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 땅에 고정시켜, 더 강한 파워로 공격 가능, 이동 불가
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False: 
            return 
        
        # 현재 시즈모드가 아닐 때 -> 시즈 모드 ON
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈 모드 OFF
        else: 
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode = False

# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0}:{1} 방향으로 날아갑니다.[속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  #지상 speed는 0
        Flyable.__init__(self, flying_speed)
    ############ 연산자 오버로딩 ###############
    # move 함수 재정의 = Unit.move가 호출되는 것이 아닌, FlyableAttackUnit의 move 함수 사용
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스: 공중공격 유닛 생성
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 해제 상태
    
    def clocking(self):
        if self.clocked == True :   # 클로킹 모드 -> 모드해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else :  # 클로킹 모드 해제 -> 클로킹 모드
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True

# 게임 시작 함수 생성
def game_start():
    print("새로운 게임을 시작합니다.")

def game_over():
    print("Player : GG ")
    print("[Player]님이 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

# 마린 3개 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
T1 = Tank()
T2 = Tank()

# 레이스 1기 생성
W1 = Wraith()

# 생성된 모든 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(T1)
attack_units.append(T2)
attack_units.append(W1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료 되었습니다.")

# 공격 모드 준비(탱크 : 시즈모드, 레이스: 클로킹 모드, 마린: 스팀팩)
for unit in attack_units:
    if isinstance(unit, Marine):     #지금 만들어진 객체가 어떤 클래스의 인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21))     # 5-20 사이의 공격을 랜덤으로 받음

# 게임 종료
game_over()


# 9-12. 퀴즈 8 : 부동산 프로그램 개발
# 출력 예제: 
# 총 3개의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location= location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
h1 = House("강남","아파트","매매","10억","2010년")
h2 = House("마포", "오피스텔", "전세","5억","2007년")
h3 = House("송파","빌라","월세","500/50","2000년")

houses.append(h1)
houses.append(h2)
houses.append(h3)

print("총 {0}개의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()