#위치 매개변수 가장 기본적인 매개변수
# 함수 호출할떄 순서대로 데이터(인자) 를 넘겨줘야 한다
# 다른 매개변수와 함께 쓸 떄는 항상 맨 앞에 써야 한다.
# def my_func(a,b):
# print(a,b)

def morning_tired(a,b):
    print(a,b)

morning_tired(9,10)

#기본 매개변수
# 매개변수의 기본적인 값
# 함수를 정의 할떄 매개변수의 기본 값을 지정할 수 잇다.
# def post_info(title, content = '내용없음'):
#     print('제목:',title)
#     print('내용:', content)

def post_morning(title, content='내용없음'):
    print('제목 :', title)
    print('내용 :', content)

post_morning('출첵')


#키워드 매개 변수
# 함수 호출시 키워드를 붙여 호출한다.
# 매개변수의 순서를 지키지 않아도 된다.
# def post_info(title, content):
#     print('제목:',title)  
#     print('내용:',content)


def post_morning(title, content):
    print('제목 :', title)
    print('내용 :', content)

post_morning(content = '없다', title ='여자친구 만드는 방법')

