#위치 가변 매개변수
# 가변 매개변수 = 개수가 정해지지 않은 매개변수
# 매개변수 앞에 *가 붙는다.(튜플형)
def print_fruits(*args):
    for arg in args:
        print(arg)
print_fruits('apple','orange','mango','grape')

# 키워드 가변 매개변수 = 개수가 정해지지 않은 매개변수
# 매개변수 앞에 ** 가 붙는다(.딕셔너리형)
def comment_info(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
        
comment_info(name='파린이', content='정말 감사합니다!')