class Unit:
    """
    인스턴스 속성: 이름,체력,방어,공격
    => 객체마다 다른 값을 가지는 속성

    클래스 속성: 전체 유닛 개수
    => 모든 객체가 공유하는 속성

    비공개 속성
    -> 클래스 안에서만 사용가능한 속성
    """
    # 생성자 (constructor)
    # 객체 생성할떄 호출되는 메서드
    count = 0
    def __init__(self, name,hp,shield,demage):
        self.name = name # self는 객체 자기 자신을 의미한다.
        self.__hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1 
        print(f"[{self.name}] (이)가 생성 됨")

    # 객체 출력 할떄 호출 되는 메서드
    def __str__(self):
        return f"[{self.name}] 체력: {self.__hp} 방어막 : {self.shield} 공격력: {self.demage}"

#프로브 객체 생성
probe = Unit("프로브", 20,20,5)

# 질럿 객체 생성
zealot = Unit("질럿", 60,30,10)
#드라군 
dragoon = Unit("드라군", 100,80,20)

# 인스턴스 속성 수정
probe.demage += 2
print(probe)

# 비공개 속성 접근
probe.__hp = 9999
print(probe)

# 네임 맹글링 (name mangling)
probe._Unit__hp = 9999
print(probe)

# 전체 유닛 개수
print(Unit.count)

