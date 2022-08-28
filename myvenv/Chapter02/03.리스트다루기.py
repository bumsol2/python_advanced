#리스트
fruits = ['apple', 'orange']
fruits.append('grape')
print(fruits)
#리스트에 리스트 추가하는 방법
fruits = ['apple', 'orange']
fruits.append(['grape','mango'])
print(fruits)

#리스트 데이터 삭제하는 방법   
fruits = ['apple', 'orange', 'mango']
fruits.pop(0) #0 이니까 첫번쨰
print(fruits)
# 리스트 데이터삭제(데이터이용)
fruits = ['apple', 'orange', 'mango']
fruits.remove('orange') #orange만 삭제
print(fruits)
#인텍스 구하기
fruits = ['apple', 'orange', 'mango']
print(fruits.index('orange'))
# 특정 값의 개수 구하는 방법
fruits = ['apple', 'orange', 'mango', 'apple', 'apple']
print(fruits.count('apple')) #3개
# 모든 요소 삭제
fruits = ['apple', 'orange', 'mango', 'apple', 'apple']
fruits.clear()
print(fruits)
# 리스트 정렬하기
numbers = [10,2,6,7,15,8,20]
numbers.sort() #오름차순 정렬
print(numbers)
#enumerate
#for in 사용시 인덱스 같이 출력
numbers = [2,5,6,7,8,9,10]
for index, number in enumerate(numbers):
    print(index,number)

# 리스트 데이터 삭제
fruits = ['apple', 'orange', 'mango']
del fruits[1]
print(fruits)

# 리스트 정렬
numbers = [5, 1, 2, 8, 3]
numbers.sort()
print(numbers)

# # enumerate
titles = ['오늘','날씨','어디인가']

for index, title in enumerate(titles, 1):
    print(f'{index} 번쨰 글입니다. 제목 : {title}')
 
    
# titles = ['출석!!', '출석인증합니다!', '출석이요!!']

# for index, title in enumerate(titles, 1):
#     print(f'{index} 번째 글입니다. 제목 : {title}')