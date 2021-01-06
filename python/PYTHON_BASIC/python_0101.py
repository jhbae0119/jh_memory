# 9-1. 클래스

# 스타크래프트로 예시

# 마린
name ="마린"
hp = 40
damage = 5

# 탱크
tank_name ="탱크"
tank_hp = 150
tank_damage = 35

def attack(name, location, damage):
    print("{0}:{1} 방향으로 적군을 공격합니다.\n[공격력 {2}]".format(\
        name,location,damage))

attack(name,"1시", damage)
attack(tank_name,"1시", damage)

# 만약 탱크가 여러개라면?? 매번 변수를 설정해줄 순 없다.
# so, 클래스를 사용함
# 클래스란, 서로 연관있는 변수와 함수의 집합

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marinel1 = Unit("마린",40,5)
marinel2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)

# 9-2. init
# init : 생성자, 객체가 만들어질때 자동으로 호출됨

# 9-3. 멤버변수
# 위의 self.name = name / self.hp = hp / self.damage = damage 가 멤버 변수
# 클래스 내에서 정의된 변수

# 멤버 변수 에서 사용하기
lase = Unit("레이스", 50, 10)
print("유닛 이름 : {0}, 공격력 {1}".format(lase.name, lase.damage)) # .name 멤버 변수 사용하기

# 외부에서 멤버 변수 추가해 사용하기(클래스 확장)
lase2 = Unit("레이스222", 50, 10)      # 레이스222 유닛이 생성되었습니다. 체력 50, 공격력 10
lase2.clocking = True

if lase2.clocking == True:
    print("{0}은 현재 클로킹 상태입니다.".format(lase2.name)) #레이스222은 현재 클로킹 상태입니다.

# 클래스 확장은 확장을 한 변수에 대해서만 사용가능
# ==> lase2에만 .clocking으로 정의했기때문에 다른 lase에서는 사용 불가능
# example
# if lase.clocking == True:
#     print("{0}은 현재 클로킹 상태입니다.".format(lase2.name)) 
    # ==> 에러 발생할 것


# 9-4. 메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

# 9-5. 상속
# 일반 유닛
class Unit2:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛 : 일반 유닛의 속성을 상속받아 생성할 수 있다.
class AttackUnit2(Unit2):     # 괄호 속에 상속 받고 싶은 클래스명 입력
    def __init__(self, name, hp, damage):
        #self.name = name   일반유닛을 상속받기 때문에 사용할 필요 없음
        #self.hp = hp       일반유닛을 상속받기 때문에 사용할 필요 없음
        Unit2.__init__(self, name, hp)   # 상속받을 클래스 호출
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

# 9-6. 다중 상속
# 일반 유닛
class Unit3:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛 : 일반 유닛의 속성을 상속받아 생성할 수 있다.
class AttackUnit3(Unit3):     # 괄호 속에 상속 받고 싶은 클래스명 입력
    def __init__(self, name, hp, damage):
        #self.name = name   일반유닛을 상속받기 때문에 사용할 필요 없음
        #self.hp = hp       일반유닛을 상속받기 때문에 사용할 필요 없음
        Unit3.__init__(self, name, hp)   # 상속받을 클래스 호출
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

# 비행 유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0}:{1} 방향으로 날아갑니다.[속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 인스턴스 생성 : 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name,"3시")