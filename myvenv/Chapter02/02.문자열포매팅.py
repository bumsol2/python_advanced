#문자열 포매팅이 없다면?
#기준님 수강기간이 10일 남았습니다.

name = '솔'
duration = 10

message = name + '님 수강기간이 ' + str(duration) + '일 남았습니다.'
print(message)

# 문자열 포매팅 사용시!!!
message_format = f'{name} 수강기간이 {duration}일 남았습니다.'
print(message_format)

# format 메서드 사용
#'{인덱스}'.format(데이터)
# 인덱스 생략 방법
# 'Hello {} {} {}'.format('apple', 'pineapple', 'pen')
# 'Hello apple pineapple pen'

a = 'Hello {2} {1} {0}'.format('apple', 'pineapple', 'pen')
print(a)

b = 'Hello {} {} {}'.format('apple', 'pineapple', 'pen')
print(b)

# f-string 사용
name1 = 'apple'
name2 = 'pinapple'
name3 = 'pen'
c = f'hello {name1} {name2} {name3}'
print(c)

