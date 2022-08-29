# 실습문제 2.4.2
# ['오메가3', None, '비타민C500', None, '홍삼절편']
# ['오메가3', '', '비타민C500', '', '홍삼절편']

items = ['오메가3', None, '비타민C500', None, '홍삼절편']

# 리스트 내포 사용 전
# item2 = []
# for item in items:
#     if item != None:
#         item2.append(item)
#     else:
#         item2.append('')

# print(item2)

item2 = [i if i != None else '' for i in items] #else를 쓰고 싶으면 for보다 앞에 써야된다.
print(item2)
