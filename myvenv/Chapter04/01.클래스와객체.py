#절차지향프로그래밍 1.씻고 => 2. 옷 입고 => 3. 밥 먹는다.
#규모 작을떄
#기능들을 어떤 순서로 처리할 것인가에 초점을 맞춘다.
# 객체 지향 프로그래밍
#객체가 중심이되고, 객체를 정의하고 객체간 상호 작용에 초점을 맞춘다.
# A 사람, B사람 :A가 B에게 돈을 빌려줌 A -10, B +10
# 규모가 클떄

#클래스 
#객체를 만들기 위한 설계도
#객체
#설계도로부터 만들어낸 제품
# 클래스 => 속성 이름,체력,공격
# 메서드 => 공격, 이동하기 
# class 클래스 이름:
# pass
# class Unit:
#     pass
#인스턴스=클래스이름()
# zealot= Unit()
# Unit 클래스
class Unit:
    """
    속성: 이름,체력,방어,공격
    """
    # 생성자 (constructor)
    # 객체 생성할떄 호출되는 메서드
    def __init__(self, name,hp,shield,demage):
        self.name = name # self는 객체 자기 자신을 의미한다.
        self.hp = hp
        self.shield = shield
        self.demage = demage
        print(f"[{self.name}] (이)가 생성 됨")

    # 객체 출력 할떄 호출 되는 메서드
    def __str__(self):
        return f"[{self.name}] 체력: {self.name} 방어막 : {self.shield} 공격력: {self.demage}"

#프로브 객체 생성
probe = Unit("프로브", 20,20,5)

# 질럿 객체 생성
zealot = Unit("질럿", 60,30,10)
#드라군 
dragoon = Unit("드라군", 100,80,20)

print(probe)
print(zealot)
print(dragoon)


